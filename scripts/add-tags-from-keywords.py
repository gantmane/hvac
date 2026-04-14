#!/usr/bin/env python3
"""
Add tags from keywords in frontmatter for Obsidian Tag Pane compatibility.
Converts: keywords: "a, b, c" -> adds tags: ["a", "b", "c"]
"""

import re
import sys
from pathlib import Path
from typing import List

CONTENT_DIR = Path(__file__).parent.parent / "content"

def extract_keywords(content: str) -> List[str]:
    """Extract keywords from frontmatter."""
    # First try array format: keywords: ["a", "b", "c"]
    match = re.search(r'^keywords:\s*\[([^\]]+)\]', content, re.MULTILINE)
    if match:
        items = match.group(1)
        keywords = [k.strip().strip('"\'') for k in items.split(',') if k.strip()]
        # Filter out malformed entries
        return [k for k in keywords if k and not k.startswith('[') and not k.startswith('-')]

    # Try string format: keywords: "a, b, c"
    match = re.search(r'^keywords:\s*["\']([^"\']+)["\']', content, re.MULTILINE)
    if match:
        keywords_str = match.group(1)
        return [k.strip() for k in keywords_str.split(',') if k.strip()]

    # Try unquoted format: keywords: a, b, c
    match = re.search(r'^keywords:\s*([^\n\[\]]+)$', content, re.MULTILINE)
    if match:
        keywords_str = match.group(1).strip()
        if keywords_str:
            return [k.strip() for k in keywords_str.split(',') if k.strip()]

    return []

def has_tags(content: str) -> bool:
    """Check if frontmatter already has tags."""
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        return bool(re.search(r'^tags:', fm_match.group(1), re.MULTILINE))
    return False

def add_tags(content: str, tags: List[str]) -> str:
    """Add tags field after keywords in frontmatter."""
    # Limit to 10 most relevant tags to avoid clutter
    tags = tags[:10]

    # Format tags as YAML array
    tags_yaml = 'tags: [' + ', '.join(f'"{t}"' for t in tags) + ']'

    # Insert after keywords line
    def replacer(match):
        return f'{match.group(0)}\n{tags_yaml}'

    return re.sub(
        r'^(keywords:\s*[^\n]+)$',
        replacer,
        content,
        count=1,
        flags=re.MULTILINE
    )

def process_file(filepath: Path, dry_run: bool = False) -> bool:
    """Process a single file. Returns True if modified."""
    content = filepath.read_text(encoding='utf-8')

    if has_tags(content):
        return False

    keywords = extract_keywords(content)
    if not keywords:
        return False

    new_content = add_tags(content, keywords)

    rel_path = filepath.relative_to(CONTENT_DIR)
    if dry_run:
        print(f"  WOULD ADD tags: {keywords[:5]}{'...' if len(keywords) > 5 else ''} to {rel_path}")
    else:
        filepath.write_text(new_content, encoding='utf-8')
        print(f"  ADDED {len(keywords)} tags to {rel_path}")

    return True

def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN - no files will be modified\n")

    md_files = list(CONTENT_DIR.rglob("*.md"))
    print(f"Scanning {len(md_files)} markdown files...\n")

    modified = 0
    for filepath in md_files:
        if process_file(filepath, dry_run):
            modified += 1

    print(f"\n{'Would modify' if dry_run else 'Modified'}: {modified} files")

    if dry_run and modified > 0:
        print("\nRun without --dry-run to apply changes.")

if __name__ == "__main__":
    main()
