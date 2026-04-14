#!/usr/bin/env python3
"""
Convert Hugo absolute links to Obsidian-compatible relative links.
Example: [text](/path/to/page/) -> [text](../../../path/to/page/_index.md)
"""

import os
import re
import sys
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"

def calculate_relative_path(from_file: Path, to_path: str) -> str:
    """Convert Hugo absolute path to relative path from current file."""
    # Remove leading slash and trailing slash
    to_path = to_path.strip('/')

    # Get the directory of the source file relative to content
    from_dir = from_file.parent.relative_to(CONTENT_DIR)

    # Calculate how many levels up we need to go
    levels_up = len(from_dir.parts)

    # Build relative path
    up_path = '../' * levels_up if levels_up > 0 else './'

    # Target path - check if it's a section (ends with /) or a file
    target = f"{up_path}{to_path}"

    # If it looks like a section, add _index.md
    if not to_path.endswith('.md'):
        target = f"{target}/_index.md"

    return target

def convert_links(content: str, file_path: Path) -> tuple[str, int]:
    """Convert Hugo absolute links to relative. Returns (new_content, count)."""
    count = 0

    def replacer(match):
        nonlocal count
        text = match.group(1)
        path = match.group(2)

        # Skip external links, anchors, mailto
        if path.startswith(('http', '#', 'mailto:')):
            return match.group(0)

        # Only convert absolute paths starting with /
        if not path.startswith('/'):
            return match.group(0)

        count += 1
        relative = calculate_relative_path(file_path, path)
        return f'[{text}]({relative})'

    # Match markdown links: [text](path)
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    new_content = re.sub(pattern, replacer, content)

    return new_content, count

def process_file(filepath: Path, dry_run: bool = False) -> int:
    """Process a single file. Returns count of links converted."""
    content = filepath.read_text(encoding='utf-8')
    new_content, count = convert_links(content, filepath)

    if count > 0:
        rel_path = filepath.relative_to(CONTENT_DIR)
        if dry_run:
            print(f"  WOULD CONVERT {count} links in {rel_path}")
        else:
            filepath.write_text(new_content, encoding='utf-8')
            print(f"  CONVERTED {count} links in {rel_path}")

    return count

def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN - no files will be modified\n")

    md_files = list(CONTENT_DIR.rglob("*.md"))
    print(f"Scanning {len(md_files)} markdown files...\n")

    total_converted = 0
    files_modified = 0

    for filepath in md_files:
        count = process_file(filepath, dry_run)
        if count > 0:
            total_converted += count
            files_modified += 1

    print(f"\n{'Would convert' if dry_run else 'Converted'}: {total_converted} links in {files_modified} files")

    if dry_run and total_converted > 0:
        print("\nRun without --dry-run to apply changes.")

if __name__ == "__main__":
    main()
