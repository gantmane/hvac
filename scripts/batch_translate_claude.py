#!/usr/bin/env python3
"""HVAC batch translator: English → Russian (metric) via Claude Haiku 4.5.

- Uses Anthropic API via Claude Code OAuth token (from macOS keychain)
- Haiku 4.5's 200K context → no chunking needed, send whole file
- 20 parallel workers (ThreadPoolExecutor)
- JSONL state file for resume
"""

import os
import json
import time
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# -------- config --------
ROOT = Path('/Users/evgenygantman/Documents/github/gantmane/hvac')
SRC = ROOT / 'content'
DST = ROOT / 'content-ru'
MODEL = 'claude-haiku-4-5-20251001'
MAX_WORKERS = 20
MAX_TOKENS = 50000
MAX_RETRIES = 3
LOG = ROOT / 'translate_claude.log'
STATE = ROOT / 'translate_state_claude.jsonl'

SYSTEM = """You are an expert HVAC technical translator. Translate English HVAC documentation to Russian using the METRIC system.

OUTPUT RULES:
- Output ONLY the translated markdown. No preamble. No wrapping code fences.
- Preserve all markdown structure exactly: YAML frontmatter, headers, lists, tables, fenced code blocks, mermaid diagrams, LaTeX math $...$ and $$...$$, links, images, Hugo shortcodes {{< ... >}}.
- Keep LaTeX variables unchanged (e.g. $Q_{heating}$).
- Keep code blocks unchanged (only translate comments inside if present).

TRANSLATION RULES:
1. Translate all prose and narrative content to Russian.
2. Keep these acronyms in English: HVAC, SEER, SEER2, AFUE, HSPF, HSPF2, ACH50, EUI, CDD, HDD, ASHRAE, RECS, EIA, DOE, VAV, CFM, ERV, HRV, ECB, MMBtu, MWh, kWh, kW, MW, CO2, H2O, COP, EER, IEER, PM2.5, VOC, LEED, BREEAM, ISO, ANSI, ASME, NFPA, NEC, IECC, IBC, IMC, IPC, UL, AHRI, EPA, NIOSH, OSHA.

3. Convert imperial units to METRIC:
   - BTU → кДж (1 BTU = 1.055 kJ); MMBtu → ГДж
   - °F → °C via (°F − 32) × 5/9
   - ft → м (×0.3048); ft² → м² (×0.0929); ft³ → м³ (×0.0283)
   - in → см (×2.54); mi → км (×1.609)
   - lb → кг (×0.4536); short ton → т (×0.9072)
   - HVAC ton of cooling → kW (1 ton = 3.517 kW)
   - gal → л (×3.785); psi → кПа (×6.895)
   - CFM → keep "CFM" and append "(м³/ч)" using 1 CFM = 1.699 m³/ч
   - R-value (imperial) → RSI (÷5.678)

4. YAML frontmatter rules:
   - Translate VALUES of: title, description, keywords, summary, subtitle, heading, linkTitle.
   - Keep VALUES of: weight, date, slug, draft, url, aliases, layout, type, author.
   - Keep all keys unchanged.

5. Use professional Russian HVAC terminology. Preserve tables exactly with converted numeric values.
"""


def get_oauth_token() -> str:
    out = subprocess.check_output(
        ['security', 'find-generic-password', '-s', 'Claude Code-credentials', '-w'],
        stderr=subprocess.DEVNULL,
    ).decode().strip()
    return json.loads(out)['claudeAiOauth']['accessToken']


# -------- Anthropic client (one per thread via thread-local) --------
import threading
_tls = threading.local()


def get_client():
    if not hasattr(_tls, 'client'):
        # Clear base URL so we don't hit the Ollama proxy
        for var in ('ANTHROPIC_BASE_URL', 'ANTHROPIC_API_KEY'):
            os.environ.pop(var, None)
        import anthropic
        _tls.client = anthropic.Anthropic(
            auth_token=get_oauth_token(),
            default_headers={'anthropic-beta': 'oauth-2025-04-20'},
            max_retries=0,  # we do our own retry
        )
    return _tls.client


_STRUCT_PREFIXES = ('#', '-', '*', '+', '|', '`', '$', '>', '{{', '```', '~~~', '---', '...')


def strip_preamble(text: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        if (s.startswith(_STRUCT_PREFIXES)
                or (s[0].isalpha() and not s.lower().startswith(
                    ('here is', "here's", 'translation:', 'translated:', 'sure', 'certainly', 'of course', 'below is')))):
            return '\n'.join(lines[i:])
    return text


def translate_content(content: str) -> str:
    client = get_client()
    last = None
    for attempt in range(MAX_RETRIES):
        try:
            text_parts = []
            with client.messages.stream(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=SYSTEM,
                messages=[{
                    "role": "user",
                    "content": f"Translate this HVAC markdown file to Russian with metric units. Output only the translated markdown:\n\n{content}",
                }],
            ) as stream:
                for chunk in stream.text_stream:
                    text_parts.append(chunk)
            text = strip_preamble(''.join(text_parts)).strip()
            if not text:
                raise RuntimeError("empty response")
            return text
        except Exception as e:
            last = e
            msg = str(e)
            if '429' in msg or 'rate_limit' in msg:
                time.sleep(60 + 30 * attempt)
            else:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"failed after {MAX_RETRIES}: {last}")


def process_file(rel: Path) -> tuple[Path, bool, str, float]:
    t0 = time.time()
    src = SRC / rel
    dst = DST / rel
    if dst.exists():
        return rel, True, "skip", 0.0
    try:
        content = src.read_text(encoding='utf-8')
        if not content.strip():
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(content, encoding='utf-8')
            return rel, True, "empty", 0.0
        out = translate_content(content)
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(out.rstrip() + '\n', encoding='utf-8')
        return rel, True, f"ok({len(content)}→{len(out)}B)", time.time() - t0
    except Exception as e:
        return rel, False, str(e)[:200], time.time() - t0


def log(msg: str):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    with LOG.open('a', encoding='utf-8') as f:
        f.write(line + '\n')
    print(line, flush=True)


def load_done() -> set:
    if not STATE.exists():
        return set()
    done = set()
    for line in STATE.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
            if rec.get('status') == 'ok':
                done.add(rec['file'])
        except Exception:
            pass
    return done


_state_lock = threading.Lock()


def append_state(rec: dict):
    with _state_lock:
        with STATE.open('a', encoding='utf-8') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')


def main():
    src_files = {p.relative_to(SRC) for p in SRC.rglob('*.md')}
    dst_files = {p.relative_to(DST) for p in DST.rglob('*.md')}
    done = load_done()
    missing = sorted(
        (p for p in src_files - dst_files if str(p) not in done),
        key=lambda p: (SRC / p).stat().st_size,
    )
    total = len(missing)
    log(f"START: {total} files, model={MODEL}, workers={MAX_WORKERS}")

    t0 = time.time()
    done_count = 0
    fail_count = 0
    lock = threading.Lock()

    def log_progress():
        elapsed = time.time() - t0
        rate = done_count / elapsed if elapsed > 0 else 0
        eta_min = (total - done_count - fail_count) / rate / 60 if rate > 0 else 0
        log(f"progress: {done_count} ok, {fail_count} fail, {rate*60:.1f} files/min, ETA {eta_min:.0f} min")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(process_file, rel): rel for rel in missing}
        for fut in as_completed(futures):
            rel, ok, status, dt = fut.result()
            rel_str = str(rel)
            with lock:
                if ok:
                    done_count += 1
                    append_state({"file": rel_str, "status": "ok", "duration": round(dt, 1)})
                    n = done_count + fail_count
                    if n % 20 == 0 or dt > 30:
                        log(f"[{n}/{total}] ✓ {rel} {status} ({dt:.1f}s)")
                else:
                    fail_count += 1
                    append_state({"file": rel_str, "status": "fail", "error": status})
                    log(f"[{done_count+fail_count}/{total}] ✗ FAIL {rel}: {status}")
                if (done_count + fail_count) % 50 == 0:
                    log_progress()

    log(f"DONE: {done_count} ok, {fail_count} failed in {(time.time()-t0)/60:.1f} min")


if __name__ == '__main__':
    main()
