#!/usr/bin/env python3
"""Dump raw chunks from Ollama stream to understand response shape."""
import json, urllib.request, time

# use a SMALL file first to confirm the pipeline works end-to-end
SRC = 'content/ventilation-indoor-air-quality/ventilation-rates.md'
src = open(SRC).read()[:2000]  # only first 2KB to keep prompt-eval fast

payload = {
    "model": "qwen3.5:35b",
    "prompt": f"Translate to Russian (metric units). Output only markdown:\n\n{src}",
    "system": "/no_think\nHVAC translator. English to Russian with metric system.",
    "stream": True,
    "options": {"temperature": 0.1, "num_ctx": 8192, "num_predict": 4096},
}
req = urllib.request.Request("http://192.168.2.2:11434/api/generate",
                              data=json.dumps(payload).encode(),
                              headers={"Content-Type": "application/json"})

t0 = time.time()
n = 0
with urllib.request.urlopen(req, timeout=600) as r:
    for line in r:
        if not line.strip():
            continue
        obj = json.loads(line.decode())
        n += 1
        if n <= 5 or n % 50 == 0:
            dt = time.time() - t0
            print(f"[{dt:6.1f}s] chunk#{n} keys={list(obj.keys())} response_len={len(obj.get('response',''))} done={obj.get('done',False)}", flush=True)
            if 'response' in obj and obj['response']:
                print(f"         response[:80]={obj['response'][:80]!r}", flush=True)
            if 'thinking' in obj:
                print(f"         thinking[:80]={str(obj.get('thinking',''))[:80]!r}", flush=True)
        if obj.get("done"):
            print(f"\nDONE at {time.time()-t0:.1f}s: reason={obj.get('done_reason')} eval={obj.get('eval_count')} prompt_eval={obj.get('prompt_eval_count')}", flush=True)
            print(f"total_duration={obj.get('total_duration',0)/1e9:.1f}s load_duration={obj.get('load_duration',0)/1e9:.1f}s", flush=True)
            break
print(f"\ntotal chunks: {n}, elapsed: {time.time()-t0:.1f}s", flush=True)
