#!/usr/bin/env python3
"""
Fix malformed tags that were incorrectly inserted into YAML list keywords.
Removes bad tags lines like: tags: ["- keyword"]
"""

import re
import sys
from pathlib import Path

def get_content_dir():
    if len(sys.argv) < 2:
        print("Usage: python fix-malformed-tags.py <content_dir> [--dry-run]")
        sys.exit(1)
    return Path(sys.argv[1])

DRY_RUN = "--dry-run" in sys.argv
CONTENT_DIR = get_content_dir()

def fix_malformed_tags(content: str) -> tuple:
    """Remove malformed tags lines. Returns (new_content, was_fixed)."""
    # Pattern to match malformed tags like: tags: ["- something"]
    pattern = r'^tags: \["- [^\]]*"\]\n'

    if re.search(pattern, content, re.MULTILINE):
        new_content = re.sub(pattern, '', content, flags=re.MULTILINE)
        return new_content, True
    return content, False

def process_file(filepath: Path) -> bool:
    """Process a single file. Returns True if fixed."""
    try:
        content = filepath.read_text(encoding='utf-8')
        new_content, was_fixed = fix_malformed_tags(content)

        if was_fixed and not DRY_RUN:
            filepath.write_text(new_content, encoding='utf-8')

        return was_fixed
    except Exception as e:
        print(f"  ERROR: {filepath}: {e}")
        return False

def main():
    if DRY_RUN:
        print("DRY RUN - no files will be modified\n")

    if not CONTENT_DIR.exists():
        print(f"Error: {CONTENT_DIR} does not exist")
        sys.exit(1)

    print(f"Processing: {CONTENT_DIR}\n")

    md_files = list(CONTENT_DIR.rglob("*.md"))
    fixed_count = 0

    for filepath in md_files:
        if process_file(filepath):
            fixed_count += 1
            rel_path = filepath.relative_to(CONTENT_DIR)
            print(f"  Fixed: {rel_path}")

    print(f"\n{'Would fix' if DRY_RUN else 'Fixed'}: {fixed_count} files")

if __name__ == "__main__":
    main()
