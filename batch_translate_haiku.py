#!/usr/bin/env python3
"""HVAC batch translator: English → Russian (metric), single-GPU Ollama + qwen3.5:35b.

Expert-tuned pipeline:
  - Adaptive num_ctx per request (biggest bottleneck in prior run was num_ctx=262144)
  - think=False, flash_attention, keep_alive=-1
  - Line-walker chunker with fence-depth tracking — never splits mid-code/table/math
  - Files ≤ SINGLE_SHOT_BYTES translate in one request; larger files split by H2
  - YAML frontmatter translated once; preserved structural keys (weight, date, slug, draft, url)
  - Deterministic preamble stripping (detect first markdown-structural line)
  - JSONL state file for crash resume, per-chunk retries (3)
  - Serial processing (1 request at a time — MoE + single GPU forbids concurrency)
"""

import os
import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# -------- config --------
ROOT = Path('/Users/evgenygantman/Documents/github/gantmane/hvac')
SRC = ROOT / 'content'
DST = ROOT / 'content-ru'
OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://192.168.2.2:11434/api/generate')
MODEL = os.environ.get('TRANSLATE_MODEL', 'qwen3.5:35b')

SINGLE_SHOT_BYTES = 6000          # files ≤ this size → 1 request (includes YAML)
CHUNK_TARGET_BYTES = 4000         # target size per body chunk for big files
CHUNK_MAX_BYTES = 8000            # hard cap per chunk

# Tuning adopted from production jobs-finder project on same hardware (RTX 5090 + qwen3.5:35b).
# Docs note: "num_ctx=16384 is 5x faster than 262144 on RTX 5090"
NUM_CTX_FIXED = 16384             # fits our max chunk (~10KB prompt + 8KB output ≈ 5100 tok)
NUM_PREDICT = 8192                # matches jobs-finder cap; enough for any single chunk
KEEP_ALIVE = -1
TEMPERATURE = 0.1
TIMEOUT = 600
MAX_RETRIES = 3

LOG = ROOT / 'translate_haiku.log'
STATE = ROOT / 'translate_state.jsonl'

SYSTEM = """HVAC English→Russian translator with imperial→metric conversion.

Output ONLY the translated markdown. No preambles. No wrapping code fences. Preserve all markdown structure (headers, lists, tables, fenced code, $...$ and $$...$$ math, Hugo {{< ... >}} shortcodes). Keep code blocks and LaTeX variable names unchanged. Keep HVAC acronyms in English (HVAC, SEER, AFUE, HSPF, ACH50, ASHRAE, VAV, CFM, ERV, HRV, MMBtu, MWh, kWh, kW, COP, EER, CO2, H2O, PM2.5, LEED, ISO, ANSI, ASME, NFPA, NEC, IECC, AHRI, EPA, OSHA). Convert: BTU→кДж(×1.055), °F→°C((F−32)×5/9), ft→м(×0.3048), ft²→м²(×0.0929), ft³→м³(×0.0283), in→см(×2.54), lb→кг(×0.4536), gal→л(×3.785), psi→кПа(×6.895), CFM keep but append "(м³/ч)"(×1.699), HVAC-ton→kW(×3.517), R→RSI(÷5.678). Use professional Russian HVAC terminology. Preserve all table structure with converted numbers.
"""

YAML_SYSTEM = """Translate Hugo YAML frontmatter values to Russian. Output ONLY valid YAML, no commentary, no code fences. Translate VALUES of: title, description, keywords, summary, subtitle, heading, linkTitle, tags. Do NOT change keys. Do NOT change weight/date/slug/draft/url/aliases/layout/type/menu/categories/author values. Preserve indentation and quoting exactly.
"""


# -------- Ollama client --------

def ollama_generate(prompt: str, system: str) -> str:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "system": system,
        "stream": False,
        "think": False,
        "keep_alive": KEEP_ALIVE,
        "options": {
            "temperature": TEMPERATURE,
            "num_ctx": NUM_CTX_FIXED,
            "num_predict": NUM_PREDICT,
        },
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(OLLAMA_URL, data=data, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        body = json.loads(resp.read().decode('utf-8'))
    return body.get('response', '')


def call_with_retry(prompt: str, system: str, label: str) -> str:
    last = None
    for attempt in range(MAX_RETRIES):
        try:
            out = ollama_generate(prompt, system)
            out = strip_preamble(out).strip()
            if not out:
                raise RuntimeError("empty response")
            return out
        except Exception as e:
            last = e
            log(f"  retry {attempt+1}/{MAX_RETRIES} on {label}: {str(e)[:120]}")
            time.sleep(2 ** attempt)
    raise RuntimeError(f"failed after {MAX_RETRIES}: {last}")


# -------- preamble stripping --------

_STRUCT_PREFIXES = ('#', '-', '*', '+', '|', '`', '$', '>', '{{', '```', '~~~', '---', '...')


def strip_preamble(text: str) -> str:
    """Drop 'Here is the translation:' style preambles by finding first structural line."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        # first line that looks like markdown content or prose → start here
        if (s.startswith(_STRUCT_PREFIXES)
                or s[0].isalpha() and not s.lower().startswith(('here is', 'here\'s', 'translation:', 'translated:', 'sure', 'certainly', 'of course', 'below is'))):
            return '\n'.join(lines[i:])
    return text


# -------- frontmatter & chunker --------

def split_frontmatter(content: str) -> tuple[str, str]:
    """Return (yaml_block_without_dashes, body). Empty yaml if no frontmatter."""
    if not content.startswith('---'):
        return '', content
    # find closing ---
    lines = content.split('\n')
    if lines[0].strip() != '---':
        return '', content
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end = i
            break
    if end is None:
        return '', content
    yaml_block = '\n'.join(lines[1:end])
    body = '\n'.join(lines[end + 1:])
    return yaml_block, body


class FenceTracker:
    """Tracks whether the current line is inside a code/math/HTML/shortcode fence."""
    def __init__(self):
        self.code_fence = None       # None, '```', '~~~'
        self.math_display = False    # inside $$ ... $$
        self.html_depth = 0          # <div> etc nesting
        self.shortcode_depth = 0     # {{< ... >}} nesting

    @property
    def inside(self) -> bool:
        return (self.code_fence is not None
                or self.math_display
                or self.html_depth > 0
                or self.shortcode_depth > 0)

    def feed(self, line: str) -> None:
        stripped = line.strip()
        # code fence
        if self.code_fence is None and self.math_display is False:
            if stripped.startswith('```'):
                self.code_fence = '```'
                return
            if stripped.startswith('~~~'):
                self.code_fence = '~~~'
                return
        elif self.code_fence is not None:
            if stripped.startswith(self.code_fence):
                self.code_fence = None
            return
        # standalone $$ toggles math
        if stripped == '$$':
            self.math_display = not self.math_display
            return
        # shortcode open/close — rudimentary counting
        opens = stripped.count('{{<') - stripped.count('{{< /')
        closes = stripped.count('{{< /') + stripped.count('{{</')
        self.shortcode_depth = max(0, self.shortcode_depth + opens - closes)


def chunk_body(body: str, target: int = CHUNK_TARGET_BYTES, hard_max: int = CHUNK_MAX_BYTES) -> list[str]:
    """Split markdown body into chunks, respecting fences. Prefer H2 boundaries."""
    lines = body.splitlines(keepends=True)
    tracker = FenceTracker()
    chunks: list[str] = []
    buf: list[str] = []
    buf_size = 0

    def flush():
        nonlocal buf, buf_size
        if buf:
            chunks.append(''.join(buf))
            buf = []
            buf_size = 0

    for i, line in enumerate(lines):
        is_blank = line.strip() == ''
        is_h2 = line.startswith('## ') and not tracker.inside
        # decide BEFORE feeding (the line will be part of next chunk if we split here)
        if buf_size >= target and not tracker.inside and (is_blank or is_h2):
            flush()
        # hard cap safeguard
        if buf_size >= hard_max and not tracker.inside and is_blank:
            flush()
        buf.append(line)
        buf_size += len(line)
        tracker.feed(line)

    flush()
    # merge tiny tail chunk into previous
    if len(chunks) >= 2 and len(chunks[-1]) < target // 3:
        chunks[-2] = chunks[-2] + chunks[-1]
        chunks.pop()
    return chunks


# -------- translation orchestration --------

def log(msg: str):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}\n"
    with LOG.open('a', encoding='utf-8') as f:
        f.write(line)
    print(msg, flush=True)


def translate_yaml(yaml_block: str) -> str:
    if not yaml_block.strip():
        return yaml_block
    return call_with_retry(
        prompt=f"Translate to Russian:\n\n{yaml_block}",
        system=YAML_SYSTEM,
        label="yaml",
    )


def translate_body_chunk(chunk: str, idx: int, total: int) -> str:
    return call_with_retry(
        prompt=f"Translate to Russian with metric units:\n\n{chunk}",
        system=SYSTEM,
        label=f"chunk {idx}/{total}",
    )


def translate_single_shot(content: str) -> str:
    return call_with_retry(
        prompt=f"Translate full markdown file (with YAML frontmatter) to Russian with metric units:\n\n{content}",
        system=SYSTEM,
        label="single",
    )


def assemble_file(yaml_rus: str, body_chunks_rus: list[str]) -> str:
    out = ''
    if yaml_rus.strip():
        out += '---\n' + yaml_rus.strip() + '\n---\n\n'
    out += '\n'.join(c.rstrip() + '\n' for c in body_chunks_rus)
    return out.rstrip() + '\n'


def translate_file(src_path: Path, dst_path: Path) -> tuple[bool, str, float]:
    t0 = time.time()
    try:
        content = src_path.read_text(encoding='utf-8')
        if not content.strip():
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            dst_path.write_text(content, encoding='utf-8')
            return True, "empty", 0.0

        size = len(content)
        if size <= SINGLE_SHOT_BYTES:
            out = translate_single_shot(content)
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            dst_path.write_text(out.rstrip() + '\n', encoding='utf-8')
            return True, f"single({size}B)", time.time() - t0

        # big: split frontmatter + chunk body
        yaml_block, body = split_frontmatter(content)
        yaml_rus = translate_yaml(yaml_block) if yaml_block else ''
        chunks = chunk_body(body)
        log(f"  chunked {size}B → {len(chunks)} chunks (sizes: {[len(c) for c in chunks]})")
        translated = []
        for i, ch in enumerate(chunks, 1):
            translated.append(translate_body_chunk(ch, i, len(chunks)))
        out = assemble_file(yaml_rus, translated)
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        dst_path.write_text(out, encoding='utf-8')
        return True, f"chunked({size}B,{len(chunks)})", time.time() - t0
    except Exception as e:
        return False, str(e)[:180], time.time() - t0


# -------- state file --------

def load_state() -> dict:
    if not STATE.exists():
        return {}
    state = {}
    for line in STATE.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        state[rec['file']] = rec
    return state


def append_state(rec: dict):
    with STATE.open('a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')


# -------- main --------

def main():
    src_files = {p.relative_to(SRC) for p in SRC.rglob('*.md')}
    dst_files = {p.relative_to(DST) for p in DST.rglob('*.md')}
    missing = sorted(src_files - dst_files, key=lambda p: (SRC / p).stat().st_size)
    total = len(missing)

    state = load_state()

    log(f"START: {total} files, model={MODEL}, single_shot≤{SINGLE_SHOT_BYTES}B, chunk_target={CHUNK_TARGET_BYTES}B")

    done = 0
    failed = 0
    skipped = 0
    t0 = time.time()

    for idx, rel in enumerate(missing, 1):
        rel_str = str(rel)
        if rel_str in state and state[rel_str].get('status') == 'ok':
            skipped += 1
            continue
        src_p = SRC / rel
        dst_p = DST / rel
        if dst_p.exists():
            skipped += 1
            continue

        size = src_p.stat().st_size
        log(f"[{idx}/{total}] {rel} ({size}B)")
        ok, status, dt = translate_file(src_p, dst_p)
        if ok:
            done += 1
            log(f"  ✓ {status} in {dt:.1f}s")
            append_state({"file": rel_str, "status": "ok", "size": size, "duration": round(dt, 1)})
        else:
            failed += 1
            log(f"  ✗ FAIL: {status}")
            append_state({"file": rel_str, "status": "fail", "size": size, "error": status})

        elapsed = time.time() - t0
        if done > 0:
            rate = done / elapsed
            eta_min = (total - idx) / rate / 60 if rate else 0
            if idx % 5 == 0 or size > 20000:
                log(f"  progress: {done} ok, {failed} fail, {skipped} skip | {rate*60:.1f} files/min | ETA {eta_min:.0f} min")

    log(f"DONE: {done} ok, {failed} failed, {skipped} skipped in {(time.time()-t0)/60:.1f} min")


if __name__ == '__main__':
    main()
