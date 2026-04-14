#!/usr/bin/env python3
"""
Wave Protocol: Fix broken links in markdown content.
Removes link markup from broken links, keeping the text.
Example: [Topic](../broken/_index.md) -> Topic
"""

import os
import re
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_content_dir():
    if len(sys.argv) < 2:
        print("Usage: python fix-broken-links.py <content_dir> [--dry-run]")
        sys.exit(1)
    return Path(sys.argv[1])

DRY_RUN = "--dry-run" in sys.argv
CONTENT_DIR = get_content_dir()

def is_link_broken(file_path: Path, link: str) -> bool:
    """Check if a relative link is broken."""
    # Skip external links, anchors, mailto
    if link.startswith(('http', '#', 'mailto:', '/')):
        return False

    # Only check relative links
    if not link.startswith('..'):
        return False

    # Remove anchor from link
    link_path = link.split('#')[0]
    if not link_path:
        return False

    # Resolve the target path
    file_dir = file_path.parent
    try:
        target = (file_dir / link_path).resolve()
        # Check if target exists
        if target.exists():
            return False
        # Check without .md extension
        if target.with_suffix('').exists():
            return False
        # Check as directory with _index.md
        if (target.parent / '_index.md').exists():
            return False
        return True
    except:
        return True

def fix_broken_links(content: str, file_path: Path) -> tuple:
    """Remove broken links, keep text. Returns (new_content, count)."""
    count = 0

    def replacer(match):
        nonlocal count
        full_match = match.group(0)
        text = match.group(1)
        link = match.group(2)

        if is_link_broken(file_path, link):
            count += 1
            return text  # Return just the text, removing link markup
        return full_match

    # Match markdown links: [text](path)
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    new_content = re.sub(pattern, replacer, content)

    return new_content, count

def process_file(filepath: Path) -> dict:
    """Process a single file. Returns stats."""
    try:
        content = filepath.read_text(encoding='utf-8')
        new_content, count = fix_broken_links(content, filepath)

        if count > 0 and not DRY_RUN:
            filepath.write_text(new_content, encoding='utf-8')

        return {'path': filepath, 'fixed': count}
    except Exception as e:
        return {'path': filepath, 'fixed': 0, 'error': str(e)}

def main():
    if DRY_RUN:
        print("DRY RUN - no files will be modified\n")

    if not CONTENT_DIR.exists():
        print(f"Error: {CONTENT_DIR} does not exist")
        sys.exit(1)

    print(f"Processing: {CONTENT_DIR}\n")

    md_files = list(CONTENT_DIR.rglob("*.md"))
    print(f"Scanning {len(md_files)} files...\n")

    total_fixed = 0
    files_modified = 0

    # Process files in parallel for speed
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(process_file, f): f for f in md_files}

        for future in as_completed(futures):
            result = future.result()
            if result['fixed'] > 0:
                files_modified += 1
                total_fixed += result['fixed']
                rel_path = result['path'].relative_to(CONTENT_DIR)
                print(f"  Fixed {result['fixed']} links: {rel_path}")

    print(f"\n{'Would fix' if DRY_RUN else 'Fixed'}: {total_fixed} broken links in {files_modified} files")

if __name__ == "__main__":
    main()
