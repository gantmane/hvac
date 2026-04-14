#!/usr/bin/env python3
"""Ollama throughput benchmark — HVAC EN→RU translation, 7 configs × 3 runs."""

import json, math, statistics, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

OLLAMA_URL = "http://192.168.2.2:11434/api/generate"
MODEL      = "qwen3.5:35b"
TIMEOUT_S  = 300
REPEATS    = 3
CHUNK_PATH = (
    "/Users/evgenygantman/Documents/github/gantmane/hvac/content/"
    "hvac-fundamentals/building-envelope-moisture/"
    "hygrothermal-material-properties/hygroscopic-moisture-content/_index.md"
)

SYSTEM_FULL = """\
You are an expert HVAC technical translator specializing in translating English \
technical documentation to Russian with metric system conversion.

CRITICAL RULES:
1. Translate ALL content to Russian (except abbreviations listed below)
2. Keep UNCHANGED in English: HVAC, SEER, SEER2, AFUE, HSPF, HSPF2, ACH50, EUI, \
CDD, HDD, ASHRAE, RECS, EIA, DOE, VAV, CFM, ERV, HRV, ECB, MMBtu, MWh, kWh, kW, \
MW, CO2, H2O
3. Keep all LaTeX formulas and variable notation UNCHANGED
4. Keep all markdown formatting intact (headers, lists, tables, code blocks, mermaid)
5. Convert units to METRIC: BTU→kJ (×1.055), °F→°C ((F-32)×5/9), ft→m (×0.3048), \
ft²→m² (×0.0929), lb→kg (×0.4536), gal→L (×3.785), R-value÷5.678
6. Use professional Russian HVAC terminology
7. Preserve all table structures with converted values
8. Translate YAML front matter (title, description, keywords); keep weight unchanged
9. Show conversions inline e.g. "45-55°F" becomes "7-13°C"
"""

SYSTEM_SHORT = "Translate to Russian. Use metric units. Keep all markdown formatting."

with open(CHUNK_PATH, encoding="utf-8") as _f:
    CHUNK = _f.read()

def round_up_ctx(prompt: str) -> int:
    raw = int((len(prompt) / 3.5 + 2000) * 1.2)
    return math.ceil(raw / 1024) * 1024

def make_payload(system: str, num_batch: int = 512,
                 flash_attention: bool = True, context=None) -> bytes:
    ctx = round_up_ctx(system + CHUNK)
    p = {"model": MODEL, "prompt": CHUNK, "system": system, "stream": False,
         "options": {"temperature": 0.1, "num_ctx": ctx,
                     "num_batch": num_batch, "flash_attention": flash_attention},
         "think": False, "keep_alive": -1}
    if context is not None:
        p["context"] = context
    return json.dumps(p).encode()

def call_ollama(data: bytes, retry: bool = True) -> dict:
    req = urllib.request.Request(
        OLLAMA_URL, data=data,
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
            return json.loads(resp.read())
    except (urllib.error.URLError, ConnectionResetError) as exc:
        if retry:
            time.sleep(2); return call_ollama(data, retry=False)
        raise RuntimeError(f"Ollama error: {exc}") from exc

def timed(data: bytes) -> dict:
    t0 = time.perf_counter()
    r  = call_ollama(data)
    r["_wall"] = time.perf_counter() - t0
    return r

def tok_s(count: int, ns: int) -> float:
    return count / (ns / 1e9) if ns > 0 else 0.0

# ── Fixed input info ────────────────────────────────────────────────────────
print(f"Chunk: {len(CHUNK):,} bytes  |  Model: {MODEL}  |  Runs: {REPEATS}\n")

# ── Standard 5 configs ──────────────────────────────────────────────────────
CONFIGS = [
    ("baseline",        lambda: make_payload(SYSTEM_FULL,  512,  True)),
    ("num_batch=2048",  lambda: make_payload(SYSTEM_FULL,  2048, True)),
    ("num_batch=1024",  lambda: make_payload(SYSTEM_FULL,  1024, True)),
    ("short_sysprompt", lambda: make_payload(SYSTEM_SHORT, 512,  True)),
    ("no_flash_attn",   lambda: make_payload(SYSTEM_FULL,  512,  False)),
]

results: dict = {}

for name, fn in CONFIGS:
    print(f"--- {name} ---")
    walls, gen_ts, ptok_ts, obytes = [], [], [], []
    for i in range(1, REPEATS + 1):
        try:
            r = timed(fn())
            walls.append(r["_wall"])
            gen_ts.append(tok_s(r.get("eval_count", 0),        r.get("eval_duration", 0)))
            ptok_ts.append(tok_s(r.get("prompt_eval_count", 0), r.get("prompt_eval_duration", 0)))
            obytes.append(len(r.get("response", "").encode()))
            print(f"  run {i}: {r['_wall']:.1f}s  gen={gen_ts[-1]:.1f} tok/s")
        except Exception as e:
            print(f"  run {i}: FAILED — {e}")
    if walls:
        results[name] = {"median_wall": statistics.median(walls),
                         "gen_tok_s":   statistics.median(gen_ts),
                         "prompt_tok_s": statistics.median(ptok_ts),
                         "out_bytes":   statistics.median(obytes)}

# ── Config 6: KV-cache reuse ─────────────────────────────────────────────────
print("--- kv_cache_reuse ---")
kv_walls, saved_ctx = [], []
try:
    r0 = timed(make_payload(SYSTEM_FULL, 512, True))
    saved_ctx = r0.get("context", [])
    kv_walls.append(r0["_wall"])
    print(f"  warmup: {r0['_wall']:.1f}s  (ctx tokens={len(saved_ctx)})")
    for i in range(2, REPEATS + 1):
        r = timed(make_payload(SYSTEM_FULL, 512, True, context=saved_ctx or None))
        kv_walls.append(r["_wall"])
        print(f"  run {i}: {r['_wall']:.1f}s  delta={r['_wall']-kv_walls[0]:+.1f}s")
except Exception as e:
    print(f"  FAILED — {e}")
if kv_walls:
    results["kv_cache_reuse"] = {"median_wall": statistics.median(kv_walls),
                                 "gen_tok_s": 0.0, "prompt_tok_s": 0.0, "out_bytes": 0}

# ── Config 7: 2 concurrent vs 2 sequential ───────────────────────────────────
def _call(_=None) -> float:
    return timed(make_payload(SYSTEM_FULL, 512, True))["_wall"]

print("--- concurrent_2x vs sequential_2x ---")
conc_walls, seq_walls = [], []
for trial in range(REPEATS):
    try:
        t0 = time.perf_counter()
        with ThreadPoolExecutor(max_workers=2) as ex:
            list(as_completed([ex.submit(_call) for _ in range(2)]))
        conc_walls.append(time.perf_counter() - t0)

        t1 = time.perf_counter()
        _call(); _call()
        seq_walls.append(time.perf_counter() - t1)

        print(f"  trial {trial+1}: concurrent={conc_walls[-1]:.1f}s  sequential={seq_walls[-1]:.1f}s")
    except Exception as e:
        print(f"  trial {trial+1}: FAILED — {e}")

if conc_walls:
    results["concurrent_2x"]  = {"median_wall": statistics.median(conc_walls),
                                  "gen_tok_s": 0.0, "prompt_tok_s": 0.0, "out_bytes": 0}
if seq_walls:
    results["sequential_2x"]  = {"median_wall": statistics.median(seq_walls),
                                  "gen_tok_s": 0.0, "prompt_tok_s": 0.0, "out_bytes": 0}

# ── Results table ─────────────────────────────────────────────────────────────
W = [20, 15, 12, 16, 12]
HDR = ["config", "median_wall_s", "gen_tok_s", "prompt_eval_tok_s", "output_bytes"]
SEP = "-" * (sum(W) + 2 * (len(W) - 1))

def row(cells):
    return "  ".join(str(c).ljust(w) for c, w in zip(cells, W))

print(f"\n{'='*len(SEP)}")
print("BENCHMARK RESULTS — sorted fastest first")
print(f"{'='*len(SEP)}")
print(row(HDR))
print(SEP)
for name, m in sorted(results.items(), key=lambda kv: kv[1]["median_wall"]):
    print(row([
        name,
        f"{m['median_wall']:.2f}",
        f"{m['gen_tok_s']:.1f}"    if m["gen_tok_s"]    else "n/a",
        f"{m['prompt_tok_s']:.1f}" if m["prompt_tok_s"] else "n/a",
        f"{int(m['out_bytes'])}"   if m["out_bytes"]     else "n/a",
    ]))
print(SEP)
print()
print("Notes:")
print("  gen_tok_s         — eval_count / eval_duration  (generation speed)")
print("  prompt_eval_tok_s — prompt_eval_count / prompt_eval_duration  (prefill speed)")
print("  concurrent_2x     — aggregate wall time for 2 simultaneous requests")
print("  sequential_2x     — wall time for 2 sequential requests")
print("  kv_cache_reuse    — median incl. warmup; see per-run delta printed above")
