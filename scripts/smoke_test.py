#!/usr/bin/env python3
"""Smoke-test the translator on one small + the biggest file."""
import sys, time
sys.path.insert(0, '.')
import batch_translate_haiku as bt
from pathlib import Path

TESTS = [
    ('small', Path('content/about/_index.md')),
    ('big',   Path('content/ventilation-indoor-air-quality/ventilation-rates.md')),
]

for label, src in TESTS:
    if not src.exists():
        print(f"[{label}] SKIP: {src} not found", flush=True)
        continue
    dst = Path(f'/tmp/smoke_{label}.md')
    size = src.stat().st_size
    print(f"\n=== [{label}] {src} ({size}B) ===", flush=True)
    t0 = time.time()
    ok, status, dt = bt.translate_file(src, dst)
    tag = "OK" if ok else "FAIL"
    print(f"[{label}] {tag} in {dt:.1f}s: {status}", flush=True)
    if ok:
        out = dst.read_text(encoding='utf-8')
        print(f"[{label}] output: {len(out)}B", flush=True)
        print(f"[{label}] head:\n{out[:400]}", flush=True)
        print(f"[{label}] tail:\n{out[-300:]}", flush=True)
