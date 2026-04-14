#!/usr/bin/env python3
"""
HVAC batch translator — Wave 2 (high-priority foundational sections).
English → Russian, metric units only.

Sections:
  1. refrigeration-systems         (~381 missing)
  2. heating-systems                (~120 missing)
  3. hvac-fundamentals              (~120 missing)
  4. air-conditioning-cooling       (~55 missing)
  5. ventilation-indoor-air-quality (~40 missing)
  6. controls-automation-building   (~36 missing)
Total: ~750 files

Uses Ollama qwen3.5:35b at http://192.168.2.2:11434 (serial, single GPU).
Resumes from translate_state_wave2.jsonl on restart.
Logs to translate_wave2.log.
"""

import json
import os
import time
from pathlib import Path

# -------- config --------
ROOT = Path('/Users/evgenygantman/Documents/github/gantmane/hvac')
SRC  = ROOT / 'content'
DST  = ROOT / 'content-ru'

OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://192.168.2.2:11434/api/generate')
MODEL      = os.environ.get('TRANSLATE_MODEL', 'qwen3.5:35b')

SECTIONS = [
    'refrigeration-systems',
    'heating-systems',
    'hvac-fundamentals',
    'air-conditioning-cooling',
    'ventilation-indoor-air-quality',
    'controls-automation-building',
]

# Chunking thresholds (bytes)
SINGLE_SHOT_BYTES = 6000   # files at or below this size → 1 Ollama call
CHUNK_TARGET_BYTES = 4000  # preferred chunk size
CHUNK_MAX_BYTES    = 8000  # hard cap per chunk

# Ollama request options
NUM_CTX_FIXED = 16384
NUM_PREDICT   = 8192
KEEP_ALIVE    = -1          # keep model loaded between calls
TEMPERATURE   = 0.1
TIMEOUT       = 600         # seconds per HTTP call
MAX_RETRIES   = 3

LOG   = ROOT / 'translate_wave2.log'
STATE = ROOT / 'translate_state_wave2.jsonl'

# -------- system prompts --------
# Unit conversions (same as Wave 1b):
#   Btu/h → W (×0.293) or kW for large values
#   BTU (energy) → кДж (×1.055)
#   °F → °C  ((F-32)×5/9)
#   CFM → м³/с (×0.000471947); larger → м³/ч (×1.699)
#   psi → Па (×6895) or кПа (×6.895)
#   in. w.c./w.g. → Па (×249)
#   inches → мм (×25.4)
#   feet → м (×0.3048)
#   ft² → м² (×0.0929)
#   ft³ → м³ (×0.0283)
#   hp → кВт (×0.746)
#   lb → кг (×0.4536)
#   gal → л (×3.785)
#   ton (cooling) → кВт (×3.517)
#   R-value → RSI (÷5.678)
#   miles → км (×1.609)

SYSTEM = """HVAC English→Russian translator. Output ONLY the translated markdown. No preambles, no commentary.

RULES:
- Translate all content to Russian
- Preserve all markdown structure: headers, lists, tables, fenced code blocks, $...$ and $$...$$ math, Hugo {{< ... >}} shortcodes
- Keep code blocks and LaTeX variable names UNCHANGED
- Keep these acronyms in English: HVAC, SEER, SEER2, AFUE, HSPF, HSPF2, ACH50, EUI, CDD, HDD, ASHRAE, RECS, EIA, DOE, VAV, CFM, ERV, HRV, MMBtu, MWh, kWh, kW, MW, COP, EER, CO2, H2O, PM2.5, LEED, ISO, ANSI, ASME, NFPA, NEC, IECC, AHRI, EPA, OSHA, SMACNA, IESNA, USGBC, WELL, MERV, HEPA, UL, CE, UPC, IMC, R-410A, R-32, R-134a, R-22, R-404A, R-407C, R-507A, R-290, R-600a, R-717, R-744

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
- oz → г (multiply by 28.35)
- lb/ft³ → кг/м³ (multiply by 16.018)
- Btu/(h·ft²·°F) → Вт/(м²·°C) (multiply by 5.678)

Use professional Russian HVAC and refrigeration terminology. Preserve all table structure with converted numbers.
"""

YAML_SYSTEM = """Translate Hugo YAML frontmatter values to Russian. Output ONLY valid YAML, no commentary, no code fences.
Translate VALUES of: title, description, keywords, summary, subtitle, heading, linkTitle, tags.
Do NOT change keys. Do NOT change weight/date/slug/draft/url/aliases/layout/type/menu/categories/author values.
Preserve indentation and quoting exactly.
"""


# -------- Ollama client --------

def ollama_generate(prompt: str, system: str) -> str:
    import urllib.request
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
    req = urllib.request.Request(
        OLLAMA_URL, data=data,
        headers={'Content-Type': 'application/json'},
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        body = json.loads(resp.read().decode('utf-8'))
    return body.get('response', '')


def call_with_retry(prompt: str, system: str, label: str) -> str:
    last: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            out = ollama_generate(prompt, system)
            out = strip_preamble(out).strip()
            if not out:
                raise RuntimeError("empty response from model")
            return out
        except Exception as exc:
            last = exc
            log(f"  retry {attempt + 1}/{MAX_RETRIES} on {label}: {str(exc)[:120]}")
            time.sleep(2 ** attempt)
    raise RuntimeError(f"failed after {MAX_RETRIES} attempts: {last}")


# -------- preamble stripping --------

_STRUCT_PREFIXES = ('#', '-', '*', '+', '|', '`', '$', '>', '{{', '```', '~~~', '---', '...')


def strip_preamble(text: str) -> str:
    """Drop 'Here is the translation:' style preambles before the real content."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        if s.startswith(_STRUCT_PREFIXES) or (
            s[0].isalpha()
            and not s.lower().startswith(
                ('here is', "here's", 'translation:', 'translated:', 'sure',
                 'certainly', 'of course', 'below is', 'вот')
            )
        ):
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
    end: int | None = None
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
    """Track whether the current line is inside a code/math/shortcode fence."""

    def __init__(self) -> None:
        self.code_fence: str | None = None
        self.math_display: bool = False
        self.shortcode_depth: int = 0

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
        opens  = stripped.count('{{<') - stripped.count('{{< /')
        closes = stripped.count('{{< /') + stripped.count('{{</')
        self.shortcode_depth = max(0, self.shortcode_depth + opens - closes)


def chunk_body(body: str,
               target: int = CHUNK_TARGET_BYTES,
               hard_max: int = CHUNK_MAX_BYTES) -> list[str]:
    """Split markdown body at H2/blank boundaries, respecting fences."""
    lines = body.splitlines(keepends=True)
    tracker = FenceTracker()
    chunks: list[str] = []
    buf: list[str] = []
    buf_size = 0

    def flush() -> None:
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
    # Merge tiny trailing chunk into the previous one
    if len(chunks) >= 2 and len(chunks[-1]) < target // 3:
        chunks[-2] = chunks[-2] + chunks[-1]
        chunks.pop()
    return chunks


# -------- translation helpers --------

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
        log(f"  chunked {size}B → {len(chunks)} chunks "
            f"(sizes: {[len(c) for c in chunks]})")
        translated: list[str] = []
        for i, ch in enumerate(chunks, 1):
            translated.append(translate_body_chunk(ch, i, len(chunks)))
        out = assemble_file(yaml_rus, translated)
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        dst_path.write_text(out, encoding='utf-8')
        return True, f"chunked({size}B,{len(chunks)})", time.time() - t0

    except Exception as exc:
        return False, str(exc)[:180], time.time() - t0


# -------- state file --------

def load_state() -> dict[str, dict]:
    if not STATE.exists():
        return {}
    state: dict[str, dict] = {}
    for line in STATE.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
            state[rec['file']] = rec
        except Exception:
            pass
    return state


def append_state(rec: dict) -> None:
    with STATE.open('a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')


# -------- logging --------

def log(msg: str) -> None:
    line = f"[{time.strftime('%H:%M:%S')}] {msg}\n"
    with LOG.open('a', encoding='utf-8') as f:
        f.write(line)
    print(msg, flush=True)


# -------- file collection --------

def collect_missing() -> list[Path]:
    """Return sorted list of src paths that have no matching dst file."""
    missing: list[Path] = []
    for section in SECTIONS:
        src_dir = SRC / section
        dst_dir = DST / section
        if not src_dir.exists():
            log(f"WARNING: source section not found: {src_dir}")
            continue
        dst_files: set[Path] = set()
        if dst_dir.exists():
            dst_files = {p.relative_to(DST) for p in dst_dir.rglob('*.md')}
        for sf in sorted(src_dir.rglob('*.md')):
            rel = sf.relative_to(SRC)
            if rel not in dst_files:
                missing.append(sf)
    return missing


# -------- smoke test helpers --------

def check_ollama_connectivity() -> bool:
    """Verify the Ollama server responds before starting the batch."""
    import urllib.request
    import urllib.error
    health_url = OLLAMA_URL.replace('/api/generate', '/api/tags')
    try:
        with urllib.request.urlopen(health_url, timeout=10) as resp:
            body = json.loads(resp.read().decode('utf-8'))
        models = [m['name'] for m in body.get('models', [])]
        log(f"Ollama reachable. Available models: {models}")
        if not any(MODEL in m for m in models):
            log(f"WARNING: model '{MODEL}' not found in available models.")
        return True
    except Exception as exc:
        log(f"ERROR: cannot reach Ollama at {health_url}: {exc}")
        return False


def smoke_test_translation(src_path: Path) -> None:
    """Translate the first ~300 chars of the first missing file as a sanity check."""
    content = src_path.read_text(encoding='utf-8')
    snippet = content[:300]
    log(f"Smoke test: translating 300-char snippet from {src_path.name} ...")
    try:
        result = call_with_retry(
            prompt=f"Translate to Russian with metric units only:\n\n{snippet}",
            system=SYSTEM,
            label="smoke_test",
        )
        log(f"Smoke test OK. Sample output (first 200 chars):\n  {result[:200]}")
    except Exception as exc:
        log(f"Smoke test FAILED: {exc}")
        raise


# -------- main --------

def main() -> None:
    missing = collect_missing()
    total   = len(missing)
    state   = load_state()

    log("=" * 70)
    log(f"Wave 2 batch translator — {total} missing files across {len(SECTIONS)} sections")
    log(f"Model: {MODEL}  Ollama: {OLLAMA_URL}")
    log(f"State: {STATE}")
    log(f"Log:   {LOG}")
    log(f"single_shot <= {SINGLE_SHOT_BYTES}B  |  chunk_target = {CHUNK_TARGET_BYTES}B")
    log("=" * 70)

    # Section file counts for reference
    for section in SECTIONS:
        count = sum(1 for p in missing if p.relative_to(SRC).parts[0] == section)
        log(f"  {section}: {count} files to translate")

    # Pre-flight: verify Ollama is reachable
    if not check_ollama_connectivity():
        log("Aborting: Ollama server not reachable. Start it and retry.")
        return

    # Smoke test on the first uncompleted file
    for sf in missing:
        rel_str = str(sf.relative_to(SRC))
        if rel_str not in state or state[rel_str].get('status') != 'ok':
            if not (DST / sf.relative_to(SRC)).exists():
                smoke_test_translation(sf)
                break

    # Per-section counters
    sec_counts: dict[str, dict[str, int]] = {
        s: {'done': 0, 'fail': 0, 'skip': 0} for s in SECTIONS
    }

    done = failed = skipped = 0
    t0 = time.time()

    for idx, src_p in enumerate(missing, 1):
        rel     = src_p.relative_to(SRC)
        rel_str = str(rel)
        section = rel.parts[0]

        # Skip files already recorded as successful
        if state.get(rel_str, {}).get('status') == 'ok':
            skipped += 1
            sec_counts[section]['skip'] += 1
            continue

        dst_p = DST / rel
        if dst_p.exists():
            skipped += 1
            sec_counts[section]['skip'] += 1
            continue

        size = src_p.stat().st_size
        log(f"[{idx}/{total}] {rel}  ({size}B)")

        ok, status, dt = translate_file(src_p, dst_p)

        if ok:
            done += 1
            sec_counts[section]['done'] += 1
            log(f"  OK {status} in {dt:.1f}s")
            append_state({
                "file": rel_str, "status": "ok",
                "size": size, "duration": round(dt, 1), "section": section,
            })
        else:
            failed += 1
            sec_counts[section]['fail'] += 1
            log(f"  FAIL: {status}")
            append_state({
                "file": rel_str, "status": "fail",
                "size": size, "error": status, "section": section,
            })

        elapsed = time.time() - t0
        if done > 0 and (idx % 10 == 0 or size > 20_000):
            rate    = done / elapsed              # files per second
            eta_min = (total - idx) / rate / 60 if rate else 0
            log(f"  progress: {done} ok, {failed} fail, {skipped} skip"
                f" | {rate * 60:.1f} files/min | ETA {eta_min:.0f} min")

    elapsed_total = (time.time() - t0) / 60
    log("=" * 70)
    log(f"DONE: {done} ok, {failed} failed, {skipped} skipped"
        f" in {elapsed_total:.1f} min")
    log("Section breakdown:")
    for sec, counts in sec_counts.items():
        log(f"  {sec}: {counts['done']} done, {counts['fail']} fail,"
            f" {counts['skip']} skip")


if __name__ == '__main__':
    main()
