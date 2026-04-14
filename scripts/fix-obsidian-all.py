#!/usr/bin/env python3
"""
Master script to fix all Obsidian compatibility issues for a content directory.
Fixes: aliases, links, tags

Usage: python fix-obsidian-all.py <content_dir> [--dry-run]
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Optional

def get_content_dir() -> Path:
    if len(sys.argv) < 2:
        print("Usage: python fix-obsidian-all.py <content_dir> [--dry-run]")
        sys.exit(1)
    return Path(sys.argv[1])

DRY_RUN = "--dry-run" in sys.argv
CONTENT_DIR = get_content_dir()

if not CONTENT_DIR.exists():
    print(f"Error: {CONTENT_DIR} does not exist")
    sys.exit(1)

# === ALIASES ===
def extract_title(content: str) -> Optional[str]:
    match = re.search(r'^title:\s*["\']?([^"\'\n]+)["\']?', content, re.MULTILINE)
    return match.group(1).strip() if match else None

def has_aliases(content: str) -> bool:
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        return 'aliases:' in fm_match.group(1)
    return False

def add_aliases(content: str, title: str) -> str:
    def replacer(match):
        return f'{match.group(0)}\naliases: ["{title}"]'
    return re.sub(r'^(title:\s*["\']?[^"\'\n]+["\']?)$', replacer, content, count=1, flags=re.MULTILINE)

# === LINKS ===
def calculate_relative_path(from_file: Path, to_path: str) -> str:
    to_path = to_path.strip('/')
    from_dir = from_file.parent.relative_to(CONTENT_DIR)
    levels_up = len(from_dir.parts)
    up_path = '../' * levels_up if levels_up > 0 else './'
    target = f"{up_path}{to_path}"
    if not to_path.endswith('.md'):
        target = f"{target}/_index.md"
    return target

def convert_links(content: str, file_path: Path) -> tuple:
    count = 0
    def replacer(match):
        nonlocal count
        text, path = match.group(1), match.group(2)
        if path.startswith(('http', '#', 'mailto:')) or not path.startswith('/'):
            return match.group(0)
        count += 1
        return f'[{text}]({calculate_relative_path(file_path, path)})'
    new_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replacer, content)
    return new_content, count

# === TAGS ===
def extract_keywords(content: str) -> List[str]:
    match = re.search(r'^keywords:\s*\[([^\]]+)\]', content, re.MULTILINE)
    if match:
        items = match.group(1)
        keywords = [k.strip().strip('"\'') for k in items.split(',') if k.strip()]
        return [k for k in keywords if k and not k.startswith('[') and not k.startswith('-')]

    match = re.search(r'^keywords:\s*["\']([^"\']+)["\']', content, re.MULTILINE)
    if match:
        return [k.strip() for k in match.group(1).split(',') if k.strip()]

    match = re.search(r'^keywords:\s*([^\n\[\]]+)$', content, re.MULTILINE)
    if match:
        keywords_str = match.group(1).strip()
        if keywords_str:
            return [k.strip() for k in keywords_str.split(',') if k.strip()]
    return []

def has_tags(content: str) -> bool:
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        return bool(re.search(r'^tags:', fm_match.group(1), re.MULTILINE))
    return False

def add_tags(content: str, tags: List[str]) -> str:
    tags = tags[:10]
    tags_yaml = 'tags: [' + ', '.join(f'"{t}"' for t in tags) + ']'
    def replacer(match):
        return f'{match.group(0)}\n{tags_yaml}'
    return re.sub(r'^(keywords:\s*[^\n]+)$', replacer, content, count=1, flags=re.MULTILINE)

# === MAIN ===
def process_file(filepath: Path) -> dict:
    stats = {'aliases': 0, 'links': 0, 'tags': 0}
    content = filepath.read_text(encoding='utf-8')
    modified = False

    # Fix aliases for _index.md files
    if filepath.name == '_index.md' and not has_aliases(content):
        title = extract_title(content)
        if title:
            content = add_aliases(content, title)
            stats['aliases'] = 1
            modified = True

    # Fix Hugo absolute links
    new_content, link_count = convert_links(content, filepath)
    if link_count > 0:
        content = new_content
        stats['links'] = link_count
        modified = True

    # Add tags from keywords
    if not has_tags(content):
        keywords = extract_keywords(content)
        if keywords:
            content = add_tags(content, keywords)
            stats['tags'] = 1
            modified = True

    if modified and not DRY_RUN:
        filepath.write_text(content, encoding='utf-8')

    return stats

def main():
    if DRY_RUN:
        print("DRY RUN - no files will be modified\n")

    print(f"Processing: {CONTENT_DIR}\n")

    md_files = list(CONTENT_DIR.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files\n")

    totals = {'aliases': 0, 'links': 0, 'tags': 0, 'files': 0}

    for filepath in md_files:
        stats = process_file(filepath)
        if any(stats.values()):
            totals['files'] += 1
            totals['aliases'] += stats['aliases']
            totals['links'] += stats['links']
            totals['tags'] += stats['tags']
            rel = filepath.relative_to(CONTENT_DIR)
            changes = []
            if stats['aliases']: changes.append('alias')
            if stats['links']: changes.append(f"{stats['links']} links")
            if stats['tags']: changes.append('tags')
            print(f"  {', '.join(changes)}: {rel}")

    print(f"\n{'Would modify' if DRY_RUN else 'Modified'}: {totals['files']} files")
    print(f"  - Aliases added: {totals['aliases']}")
    print(f"  - Links converted: {totals['links']}")
    print(f"  - Tags added: {totals['tags']}")

if __name__ == "__main__":
    main()
