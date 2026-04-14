#!/usr/bin/env python3
"""Test 2-chunk batching: send 2 chunks in one request with XML delimiters,
parse back, compare vs 2 serial requests. Uses the real chunker from batch_translate_haiku."""
import sys, time, re, json, urllib.request
sys.path.insert(0, '.')
import batch_translate_haiku as bt
from pathlib import Path

URL = 'http://192.168.2.2:11434/api/generate'
MODEL = 'qwen3.5:35b'
NUM_CTX = 16384
NUM_PREDICT = 8192

BATCH_SYSTEM = bt.SYSTEM + """

When given multiple sections wrapped in <chunk id="N">...</chunk>, translate each section independently and return the translations in the SAME format with the SAME ids. Never merge sections. Never omit a chunk. Output exactly:
<chunk id="1">...translated section 1...</chunk>
<chunk id="2">...translated section 2...</chunk>
"""

def ollama_raw(prompt: str, system: str) -> dict:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "system": system,
        "stream": False,
        "think": False,
        "keep_alive": -1,
        "options": {"temperature": 0.1, "num_ctx": NUM_CTX, "num_predict": NUM_PREDICT},
    }
    req = urllib.request.Request(URL, data=json.dumps(payload).encode(), headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read().decode())

def serial_2(chunk_a: str, chunk_b: str) -> tuple[str, str, float]:
    t0 = time.time()
    out_a = bt.call_with_retry(
        prompt=f"Translate to Russian with metric units:\n\n{chunk_a}",
        system=bt.SYSTEM, label="chunk A")
    out_b = bt.call_with_retry(
        prompt=f"Translate to Russian with metric units:\n\n{chunk_b}",
        system=bt.SYSTEM, label="chunk B")
    return out_a, out_b, time.time() - t0

def batch_2(chunk_a: str, chunk_b: str) -> tuple[str, str, float, dict]:
    prompt = (
        "Translate the following 2 markdown sections to Russian with metric units. "
        "Return EXACTLY 2 chunks with the same ids:\n\n"
        f'<chunk id="1">\n{chunk_a}\n</chunk>\n\n'
        f'<chunk id="2">\n{chunk_b}\n</chunk>\n'
    )
    t0 = time.time()
    resp = ollama_raw(prompt, BATCH_SYSTEM)
    dt = time.time() - t0
    raw = resp.get('response', '')
    # parse chunks
    m1 = re.search(r'<chunk id="1">\s*(.*?)\s*</chunk>', raw, re.DOTALL)
    m2 = re.search(r'<chunk id="2">\s*(.*?)\s*</chunk>', raw, re.DOTALL)
    out_a = m1.group(1) if m1 else ''
    out_b = m2.group(1) if m2 else ''
    meta = {
        'wall': dt,
        'eval_count': resp.get('eval_count', 0),
        'prompt_eval_count': resp.get('prompt_eval_count', 0),
        'response_len': len(raw),
        'parsed_a': bool(m1), 'parsed_b': bool(m2),
        'raw_head': raw[:300],
    }
    return out_a, out_b, dt, meta

def main():
    # get 2 real chunks from ventilation-rates.md
    content = Path('content/ventilation-indoor-air-quality/ventilation-rates.md').read_text()
    yaml_block, body = bt.split_frontmatter(content)
    chunks = bt.chunk_body(body)
    print(f"Source has {len(chunks)} chunks")
    chunk_a, chunk_b = chunks[0], chunks[1]
    print(f"chunk A: {len(chunk_a)} bytes")
    print(f"chunk B: {len(chunk_b)} bytes")

    print("\n=== SERIAL (2 separate requests) ===")
    try:
        a1, b1, t_serial = serial_2(chunk_a, chunk_b)
        print(f"serial time: {t_serial:.1f}s  out_a={len(a1)}B  out_b={len(b1)}B")
    except Exception as e:
        print(f"serial FAILED: {e}")
        return

    print("\n=== BATCHED (1 request, 2 chunks in XML) ===")
    try:
        a2, b2, t_batch, meta = batch_2(chunk_a, chunk_b)
        print(f"batch time: {t_batch:.1f}s  out_a={len(a2)}B  out_b={len(b2)}B")
        print(f"parsed_a={meta['parsed_a']}  parsed_b={meta['parsed_b']}")
        print(f"eval_count={meta['eval_count']}  prompt_eval_count={meta['prompt_eval_count']}")
        if not meta['parsed_a'] or not meta['parsed_b']:
            print(f"raw head: {meta['raw_head']!r}")
    except Exception as e:
        print(f"batch FAILED: {e}")
        return

    print("\n=== RESULT ===")
    speedup = (t_serial - t_batch) / t_serial * 100
    print(f"serial: {t_serial:.1f}s  batch: {t_batch:.1f}s  speedup: {speedup:+.0f}%")
    if meta['parsed_a'] and meta['parsed_b'] and t_batch < t_serial:
        print("BATCHING WINS — consider using it")
    else:
        print("BATCHING LOSES or broke — keep serial chunking")

    # save outputs for manual inspection
    Path('/tmp/serial_a.md').write_text(a1)
    Path('/tmp/serial_b.md').write_text(b1)
    Path('/tmp/batch_a.md').write_text(a2)
    Path('/tmp/batch_b.md').write_text(b2)
    print("saved: /tmp/{serial,batch}_{a,b}.md")

if __name__ == '__main__':
    main()
