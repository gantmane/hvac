#!/usr/bin/env python3
"""
Wave 1 script fix:
  - For each directory under content-ru/, renumber `weight:` in _index.md and sibling
    .md files sequentially (1, 2, 3, ...) when duplicates exist.
  - Leave files with unique weights alone.
  - Fill missing `weight:` fields.
Does NOT touch title, description, or body.
"""
import os, re, sys
from pathlib import Path

ROOT = Path("/Users/evgenygantman/Documents/github/gantmane/hvac/content-ru")
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WEIGHT_RE = re.compile(r"^(\s*)weight:\s*(\d+)\s*$", re.MULTILINE)

changed_files = 0
renumbered_dirs = 0

def parse_fm(text):
    m = FM_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end():]

def set_weight(fm_text, new_weight):
    if WEIGHT_RE.search(fm_text):
        return WEIGHT_RE.sub(f"weight: {new_weight}", fm_text, count=1)
    # insert weight line after title if present, else at end
    lines = fm_text.split("\n")
    inserted = False
    for i, ln in enumerate(lines):
        if ln.startswith("title:"):
            lines.insert(i + 1, f"weight: {new_weight}")
            inserted = True
            break
    if not inserted:
        lines.append(f"weight: {new_weight}")
    return "\n".join(lines)

def get_weight(fm_text):
    m = WEIGHT_RE.search(fm_text)
    return int(m.group(2)) if m else None

def process_dir(d: Path):
    global changed_files, renumbered_dirs
    siblings = sorted([p for p in d.iterdir() if p.is_dir() and (p / "_index.md").exists()])
    if not siblings:
        return
    entries = []
    for child in siblings:
        idx = child / "_index.md"
        text = idx.read_text(encoding="utf-8")
        fm, body = parse_fm(text)
        if fm is None:
            continue
        entries.append((idx, fm, body, get_weight(fm)))
    if not entries:
        return
    weights = [e[3] for e in entries if e[3] is not None]
    has_dupes = len(weights) != len(set(weights))
    has_missing = any(e[3] is None for e in entries)
    if not has_dupes and not has_missing:
        return
    # renumber 1..N preserving order
    for i, (idx, fm, body, _w) in enumerate(entries, start=1):
        new_fm = set_weight(fm, i)
        if new_fm != fm:
            new_text = f"---\n{new_fm}\n---\n{body}"
            idx.write_text(new_text, encoding="utf-8")
            changed_files += 1
    renumbered_dirs += 1

def main():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        process_dir(Path(dirpath))
    print(f"renumbered_dirs={renumbered_dirs} changed_files={changed_files}")

if __name__ == "__main__":
    main()
