#!/usr/bin/env python3
"""Wave 3: Re-translate specific files from content/ → content-ru/ (force overwrite).
Uses existing batch_translate_claude.py machinery but on an explicit file list."""
import sys, time, threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, '/Users/evgenygantman/Documents/github/gantmane/hvac')
from batch_translate_claude import translate_content, SRC, DST, log, append_state

import os
LIST = Path(os.environ.get('WAVE_LIST', '/Users/evgenygantman/Documents/github/gantmane/hvac/__in/wave3-final.txt'))
MAX_WORKERS = 10

def process(rel_str: str):
    rel = Path(rel_str)
    t0 = time.time()
    src = SRC / rel
    dst = DST / rel
    if not src.exists():
        return rel_str, False, "source missing", 0.0
    try:
        content = src.read_text(encoding='utf-8')
        out = translate_content(content)
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(out.rstrip() + '\n', encoding='utf-8')
        return rel_str, True, f"ok({len(content)}→{len(out)}B)", time.time()-t0
    except Exception as e:
        return rel_str, False, str(e)[:200], time.time()-t0

def main():
    files = [l.strip() for l in LIST.read_text().splitlines() if l.strip()]
    log(f"WAVE3 START: {len(files)} files, workers={MAX_WORKERS}")
    t0 = time.time()
    ok = fail = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {ex.submit(process, f): f for f in files}
        for fut in as_completed(futs):
            rel, success, status, dt = fut.result()
            if success:
                ok += 1
                log(f"[{ok+fail}/{len(files)}] ok {rel} {status} ({dt:.1f}s)")
            else:
                fail += 1
                log(f"[{ok+fail}/{len(files)}] FAIL {rel}: {status}")
            append_state({"wave": 3, "file": rel, "status": "ok" if success else "fail",
                          "info": status, "duration": round(dt,1)})
    log(f"WAVE3 DONE: {ok} ok, {fail} fail in {(time.time()-t0)/60:.1f} min")

if __name__ == '__main__':
    main()
