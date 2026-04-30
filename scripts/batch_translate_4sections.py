#!/usr/bin/env python3
"""
HVAC batch translator for 4 critical sections: English → Russian (metric only).
Sections:
  1. sustainability-emerging-tech-economics (78 missing)
  2. international-perspectives (69 missing)
  3. professional-development-training (49 missing)
  4. codes-standards-regulations-safety (47 missing)

Uses Ollama qwen3.5:35b (serial, single GPU).
Resumes from translate_state_4sec.jsonl on restart.
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

SECTIONS = [
    'sustainability-emerging-tech-economics',
    'international-perspectives',
    'professional-development-training',
    'codes-standards-regulations-safety',
]

SINGLE_SHOT_BYTES = 6000       # files <= this → 1 request
CHUNK_TARGET_BYTES = 4000      # target per body chunk
CHUNK_MAX_BYTES = 8000         # hard cap per chunk

NUM_CTX_FIXED = 16384
NUM_PREDICT = 8192
KEEP_ALIVE = -1
TEMPERATURE = 0.1
TIMEOUT = 600
MAX_RETRIES = 3

LOG = ROOT / 'translate_4sec.log'
STATE = ROOT / 'translate_state_4sec.jsonl'

# -------- system prompts --------
# Unit conversions required by task brief:
#   Btu/h → W (×0.293) or kW
#   °F → °C ((F-32)×5/9)
#   CFM → m³/s (×0.000471947)
#   psi → Pa (×6895)
#   in.w.c./w.g. → Pa (×249)
#   inches → mm (×25.4)
#   feet → m (×0.3048)
#   ft² → m² (×0.0929)
#   hp → kW (×0.746)
#   BTU (energy) → kJ (×1.055)
#   lb → kg (×0.4536)
#   gal → L (×3.785)
#   ton (cooling) → kW (×3.517)
#   R-value → RSI (÷5.678)

SYSTEM = """HVAC English→Russian translator. Output ONLY the translated markdown. No preambles, no commentary.

RULES:
- Translate all content to Russian
- Preserve all markdown structure: headers, lists, tables, fenced code blocks, $...$ and $$...$$ math, Hugo {{< ... >}} shortcodes
- Keep code blocks and LaTeX variable names UNCHANGED
- Keep these acronyms in English: HVAC, SEER, SEER2, AFUE, HSPF, HSPF2, ACH50, EUI, CDD, HDD, ASHRAE, RECS, EIA, DOE, VAV, CFM, ERV, HRV, MMBtu, MWh, kWh, kW, MW, COP, EER, CO2, H2O, PM2.5, LEED, ISO, ANSI, ASME, NFPA, NEC, IECC, AHRI, EPA, OSHA, SMACNA, IESNA, USGBC, WELL, MERV, HEPA, UL, CE, UPC, IMC

UNIT CONVERSIONS — replace ALL imperial units with metric equivalents only (no dual units):
- Btu/h → W (multiply by 0.293) or kW for large values
- BTU (energy) → кДж (multiply by 1.055)
- °F → °C using (°F − 32) × 5/9, round to 1 decimal
- CFM → м³/с (multiply by 0.000471947); for larger values use м³/ч (multiply by 1.699)
- psi → Па (multiply by 6895) or кПа (multiply by 6.895)
- in. w.c. or in. w.g. → Па (multiply by 249)
- inches (in.) → мм (multiply by 25.4)
- feet (ft) → м (multiply by 0.3048)
- ft² → м² (multiply by 0.0929)
- ft³ → м³ (multiply by 0.0283)
- hp → кВт (multiply by 0.746)
- lb → кг (multiply by 0.4536)
- gal → л (multiply by 3.785)
- ton (cooling) → кВт (multiply by 3.517)
- R-value → RSI (divide by 5.678)
- miles → км (multiply by 1.609)

Use professional Russian HVAC terminology. Preserve all table structure with converted numbers.
"""

YAML_SYSTEM = """Translate Hugo YAML frontmatter values to Russian. Output ONLY valid YAML, no commentary, no code fences.
Translate VALUES of: title, description, keywords, summary, subtitle, heading, linkTitle, tags.
Do NOT change keys. Do NOT change weight/date/slug/draft/url/aliases/layout/type/menu/categories/author values.
Preserve indentation and quoting exactly.
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
    """Drop 'Here is the translation:' style preambles."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        if (s.startswith(_STRUCT_PREFIXES)
                or (s[0].isalpha() and not s.lower().startswith(
                    ('here is', "here's", 'translation:', 'translated:', 'sure',
                     'certainly', 'of course', 'below is', 'вот')))):
            return '\n'.join(lines[i:])
    return text


# -------- frontmatter & chunker --------

def split_frontmatter(content: str) -> tuple[str, str]:
    """Return (yaml_block_without_dashes, body)."""
    if not content.startswith('---'):
        return '', content
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
    """Tracks whether current line is inside a code/math/shortcode fence."""
    def __init__(self):
        self.code_fence = None
        self.math_display = False
        self.shortcode_depth = 0

    @property
    def inside(self) -> bool:
        return (self.code_fence is not None
                or self.math_display
                or self.shortcode_depth > 0)

    def feed(self, line: str) -> None:
        stripped = line.strip()
        if self.code_fence is None and not self.math_display:
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
        if stripped == '$$':
            self.math_display = not self.math_display
            return
        opens = stripped.count('{{<') - stripped.count('{{< /')
        closes = stripped.count('{{< /') + stripped.count('{{</')
        self.shortcode_depth = max(0, self.shortcode_depth + opens - closes)


def chunk_body(body: str, target: int = CHUNK_TARGET_BYTES, hard_max: int = CHUNK_MAX_BYTES) -> list[str]:
    """Split markdown body at H2/blank boundaries, respecting fences."""
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

    for line in lines:
        is_blank = line.strip() == ''
        is_h2 = line.startswith('## ') and not tracker.inside
        if buf_size >= target and not tracker.inside and (is_blank or is_h2):
            flush()
        if buf_size >= hard_max and not tracker.inside and is_blank:
            flush()
        buf.append(line)
        buf_size += len(line)
        tracker.feed(line)

    flush()
    # merge tiny tail into previous
    if len(chunks) >= 2 and len(chunks[-1]) < target // 3:
        chunks[-2] = chunks[-2] + chunks[-1]
        chunks.pop()
    return chunks


# -------- translation --------

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
        prompt=f"Translate to Russian with metric units only:\n\n{chunk}",
        system=SYSTEM,
        label=f"chunk {idx}/{total}",
    )


def translate_single_shot(content: str) -> str:
    return call_with_retry(
        prompt=f"Translate full markdown file (with YAML frontmatter) to Russian with metric units only:\n\n{content}",
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
        try:
            rec = json.loads(line)
            state[rec['file']] = rec
        except Exception:
            pass
    return state


def append_state(rec: dict):
    with STATE.open('a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')


# -------- logging --------

def log(msg: str):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}\n"
    with LOG.open('a', encoding='utf-8') as f:
        f.write(line)
    print(msg, flush=True)


# -------- main --------

def collect_missing() -> list[Path]:
    """Return sorted list of src paths that have no matching dst file."""
    missing = []
    for section in SECTIONS:
        src_dir = SRC / section
        dst_dir = DST / section
        if not src_dir.exists():
            log(f"WARNING: source section not found: {src_dir}")
            continue
        dst_files = set()
        if dst_dir.exists():
            dst_files = {p.relative_to(DST) for p in dst_dir.rglob('*.md')}
        for sf in sorted(src_dir.rglob('*.md')):
            rel = sf.relative_to(SRC)
            if rel not in dst_files:
                missing.append(sf)
    return missing


def main():
    missing = collect_missing()
    total = len(missing)
    state = load_state()

    log(f"START: {total} missing files across {len(SECTIONS)} sections")
    log(f"Model: {MODEL}, Ollama: {OLLAMA_URL}")
    log(f"single_shot <= {SINGLE_SHOT_BYTES}B, chunk_target = {CHUNK_TARGET_BYTES}B")

    # Section counters
    sec_counts: dict[str, dict] = {s: {'done': 0, 'fail': 0, 'skip': 0} for s in SECTIONS}

    done = failed = skipped = 0
    t0 = time.time()

    for idx, src_p in enumerate(missing, 1):
        rel = src_p.relative_to(SRC)
        rel_str = str(rel)
        section = rel.parts[0]

        # skip already done
        if rel_str in state and state[rel_str].get('status') == 'ok':
            skipped += 1
            sec_counts[section]['skip'] += 1
            continue
        dst_p = DST / rel
        if dst_p.exists():
            skipped += 1
            sec_counts[section]['skip'] += 1
            continue

        size = src_p.stat().st_size
        log(f"[{idx}/{total}] {rel} ({size}B)")
        ok, status, dt = translate_file(src_p, dst_p)

        if ok:
            done += 1
            sec_counts[section]['done'] += 1
            log(f"  OK {status} in {dt:.1f}s")
            append_state({"file": rel_str, "status": "ok", "size": size,
                          "duration": round(dt, 1), "section": section})
        else:
            failed += 1
            sec_counts[section]['fail'] += 1
            log(f"  FAIL: {status}")
            append_state({"file": rel_str, "status": "fail", "size": size,
                          "error": status, "section": section})

        elapsed = time.time() - t0
        if done > 0:
            rate = done / elapsed
            eta_min = (total - idx) / rate / 60 if rate else 0
            if idx % 10 == 0 or size > 20000:
                log(f"  progress: {done} ok, {failed} fail, {skipped} skip "
                    f"| {rate*60:.1f} files/min | ETA {eta_min:.0f} min")

    elapsed_total = (time.time() - t0) / 60
    log(f"DONE: {done} ok, {failed} failed, {skipped} skipped in {elapsed_total:.1f} min")
    log("Section breakdown:")
    for sec, counts in sec_counts.items():
        log(f"  {sec}: {counts['done']} done, {counts['fail']} fail, {counts['skip']} skip")


if __name__ == '__main__':
    main()
