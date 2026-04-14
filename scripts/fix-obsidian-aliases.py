#!/usr/bin/env python3
"""
Add 'aliases' to _index.md frontmatter so Obsidian displays title instead of '_index'
"""

import os
import re
import sys
from pathlib import Path
from typing import Optional

CONTENT_DIR = Path(__file__).parent.parent / "content"

def extract_title(content: str) -> Optional[str]:
    """Extract title from YAML frontmatter."""
    match = re.search(r'^title:\s*["\']?([^"\'\n]+)["\']?', content, re.MULTILINE)
    return match.group(1).strip() if match else None

def has_aliases(content: str) -> bool:
    """Check if frontmatter already has aliases."""
    # Check within frontmatter block
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        return 'aliases:' in fm_match.group(1)
    return False

def add_aliases(content: str, title: str) -> str:
    """Add aliases field after title in frontmatter."""
    # Find the title line and add aliases after it
    def replacer(match):
        return f'{match.group(0)}\naliases: ["{title}"]'

    # Match title line in frontmatter
    return re.sub(
        r'^(title:\s*["\']?[^"\'\n]+["\']?)$',
        replacer,
        content,
        count=1,
        flags=re.MULTILINE
    )

def process_file(filepath: Path, dry_run: bool = False) -> bool:
    """Process a single _index.md file. Returns True if modified."""
    content = filepath.read_text(encoding='utf-8')

    if has_aliases(content):
        return False

    title = extract_title(content)
    if not title:
        print(f"  SKIP (no title): {filepath}")
        return False

    new_content = add_aliases(content, title)

    if dry_run:
        print(f"  WOULD ADD: aliases: [\"{title}\"] to {filepath.relative_to(CONTENT_DIR)}")
    else:
        filepath.write_text(new_content, encoding='utf-8')
        print(f"  ADDED: aliases: [\"{title}\"] to {filepath.relative_to(CONTENT_DIR)}")

    return True

def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN - no files will be modified\n")

    index_files = list(CONTENT_DIR.rglob("_index.md"))
    print(f"Found {len(index_files)} _index.md files\n")

    modified = 0
    for filepath in index_files:
        if process_file(filepath, dry_run):
            modified += 1

    print(f"\n{'Would modify' if dry_run else 'Modified'}: {modified} files")

    if dry_run and modified > 0:
        print("\nRun without --dry-run to apply changes.")

if __name__ == "__main__":
    main()
