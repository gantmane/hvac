#!/usr/bin/env python3
"""Diagnostic: stream-translate the biggest HVAC file, print progress every 5s."""
import json, urllib.request, time, re, sys

SRC = 'content/ventilation-indoor-air-quality/ventilation-rates.md'
URL = 'http://192.168.2.2:11434/api/generate'
MODEL = 'qwen3.5:35b'

src = open(SRC).read()
print(f"input: {len(src)} bytes", flush=True)

payload = {
    "model": MODEL,
    "prompt": f"Translate this markdown file to Russian with metric units. Output only translated markdown, no commentary:\n\n{src}",
    "system": "/no_think\n\nYou are an HVAC translator. Translate English to Russian using the metric system. Output only the translated markdown.",
    "stream": True,
    "options": {"temperature": 0.1, "num_ctx": 262144, "num_predict": 32768},
}
req = urllib.request.Request(URL, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})

t0 = time.time()
chunks = []
tok_count = 0
last_print = t0

with urllib.request.urlopen(req, timeout=3600) as r:
    for line in r:
        if not line.strip():
            continue
        obj = json.loads(line.decode())
        piece = obj.get("response", "")
        if piece:
            chunks.append(piece)
            tok_count += 1
        now = time.time()
        if now - last_print >= 5:
            bytes_so_far = sum(len(c) for c in chunks)
            rate = tok_count / (now - t0) if now > t0 else 0
            print(f"  [{now-t0:6.0f}s] tokens={tok_count:6d}  bytes={bytes_so_far:7d}  rate={rate:.1f} tok/s", flush=True)
            last_print = now
        if obj.get("done"):
            print(f"\nDONE: reason={obj.get('done_reason')} eval_count={obj.get('eval_count')} prompt_eval={obj.get('prompt_eval_count')}", flush=True)
            break

out = "".join(chunks)
print(f"\nTOTAL: {len(out)} bytes in {time.time()-t0:.1f}s", flush=True)
print("--- head (first 500) ---", flush=True)
print(out[:500], flush=True)
print("--- tail (last 500) ---", flush=True)
print(out[-500:], flush=True)
stripped = re.sub(r'<think>[\s\S]*?</think>', '', out, flags=re.I).strip()
print(f"\nafter <think> strip: {len(stripped)} bytes", flush=True)

# save full output for inspection
with open('test_big_out.md', 'w') as f:
    f.write(stripped)
print("saved: test_big_out.md", flush=True)
