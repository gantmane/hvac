#!/usr/bin/env python3
"""
HVAC Energy Resources Batch Translator: English to Russian with Metric Conversion
"""

import os
import re
from pathlib import Path
from typing import Tuple, List
import sys
sys.path.insert(0, '/Users/evgenygantman/Documents/github/gantmane/hvac/.venv/lib/python3.12/site-packages')

from anthropic import Anthropic

client = Anthropic()

def read_file(filepath: str) -> Tuple[str, str]:
    """Read markdown file and extract YAML front matter and content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_matter = parts[1].strip()
            markdown_content = parts[2].strip()
            return yaml_matter, markdown_content

    return '', content

def translate_with_anthropic(markdown_content: str, yaml_matter: str = '') -> str:
    """Use Anthropic API to translate text to Russian with metric units."""

    system_prompt = """You are an expert HVAC technical translator specializing in translating English technical documentation to Russian with metric system conversion.

CRITICAL RULES:
1. Translate ALL content to Russian (except abbreviations listed below)
2. Keep these abbreviations UNCHANGED in English: HVAC, SEER, SEER2, AFUE, HSPF, HSPF2, ACH50, EUI, CDD, HDD, ASHRAE, RECS, EIA, DOE, VAV, CFM, ERV, HRV, ECB, MMBtu, MWh, kWh, kW, MW, CO2, H2O
3. Keep all LaTeX formulas and variable notation UNCHANGED (e.g., $E_{annual}$, $Q_{heating}$, etc.)
4. Keep all markdown formatting intact (headers, lists, tables, code blocks, mermaid diagrams)
5. Convert units to METRIC ONLY:
   - BTU → кДж (Kilo Joules) - use 1 BTU = 1.055 kJ
   - Btu/ft³ → kJ/m³
   - Btu/gal → kJ/L
   - °F → °C (use (°F - 32) × 5/9 = °C for conversions)
   - ft → m (1 ft = 0.3048 m)
   - ft² → m² (1 ft² = 0.0929 m²)
   - lb → kg (1 lb = 0.453592 kg)
   - hr → hr (keep same)
   - gal → L (1 gal = 3.785 L)
   - ton → тонна (metric ton)
   - R-value conversions: Divide by 5.678 (R-19 becomes R-3.3, etc.)
6. Use professional Russian HVAC terminology
7. Preserve all table structures exactly with converted values
8. Keep external references and citations
9. Maintain scientific notation and technical units
10. For percentages and efficiency metrics (SEER, AFUE, etc.), convert the underlying energy values but keep the metric names

YAML front matter (if present) should be translated too:
- title: translate to Russian
- description: translate to Russian
- keywords: translate to Russian
- weight: keep unchanged

When converting imperial values, show conversions clearly (e.g., "45-55°F (7-13°C)" becomes "7-13°C").

Translate the following content:

"""

    message = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=8000,
        messages=[
            {
                "role": "user",
                "content": system_prompt + markdown_content
            }
        ]
    )

    return message.content[0].text

def create_output_directory(output_path: str) -> None:
    """Create output directory structure if it doesn't exist."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

def translate_file(input_file: str, output_file: str) -> Tuple[bool, str]:
    """Translate a single markdown file."""
    try:
        yaml_matter, markdown_content = read_file(input_file)

        # Translate the markdown content
        translated_content = translate_with_anthropic(markdown_content, yaml_matter)

        # Create output directory
        create_output_directory(output_file)

        # Write translated file with YAML front matter
        with open(output_file, 'w', encoding='utf-8') as f:
            if yaml_matter:
                # Translate YAML front matter
                translated_yaml = translate_with_anthropic(yaml_matter)
                f.write('---\n')
                f.write(translated_yaml)
                f.write('\n---\n\n')
            f.write(translated_content)

        return True, "Success"
    except Exception as e:
        return False, str(e)

def main():
    """Main translation process."""
    source_base = '/Users/evgenygantman/Documents/github/gantmane/hvac/content/hvac-fundamentals/energy-resources'
    target_base = '/Users/evgenygantman/Documents/github/gantmane/hvac/content-ru/hvac-fundamentals/energy-resources'

    source_path = Path(source_base)
    markdown_files = sorted(list(source_path.rglob('*.md')))

    print(f"Found {len(markdown_files)} markdown files to translate")
    print(f"Source: {source_base}")
    print(f"Target: {target_base}")
    print(f"\n{'='*70}")

    translated_files = []
    failed_files = []

    for idx, source_file in enumerate(markdown_files, 1):
        relative_path = source_file.relative_to(source_base)
        output_file = Path(target_base) / relative_path

        print(f"[{idx:3d}/{len(markdown_files)}] {relative_path}")

        success, message = translate_file(str(source_file), str(output_file))

        if success:
            translated_files.append(str(relative_path))
            print(f"         ✓ Translated")
        else:
            failed_files.append((str(relative_path), message))
            print(f"         ✗ Failed: {message[:50]}")

    # Summary
    print(f"\n{'='*70}")
    print(f"TRANSLATION COMPLETE")
    print(f"{'='*70}")
    print(f"Successfully translated: {len(translated_files)}/{len(markdown_files)}")

    if failed_files:
        print(f"Failed: {len(failed_files)}")
        for file, err in failed_files:
            print(f"  - {file}")

    # Write summary
    summary_path = Path(target_base) / "TRANSLATION_SUMMARY.txt"
    summary_path.parent.mkdir(parents=True, exist_ok=True)

    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(f"HVAC Energy Resources Translation Summary\n")
        f.write(f"{'='*70}\n")
        f.write(f"Date: 2026-04-14\n")
        f.write(f"Source: English\n")
        f.write(f"Target: Russian (Metric System)\n")
        f.write(f"\nTotal Files: {len(markdown_files)}\n")
        f.write(f"Translated: {len(translated_files)}\n")
        f.write(f"Failed: {len(failed_files)}\n\n")

        f.write(f"Translated Files:\n")
        for file in translated_files:
            f.write(f"  {file}\n")

        if failed_files:
            f.write(f"\nFailed Files:\n")
            for file, err in failed_files:
                f.write(f"  {file}: {err}\n")

    print(f"\nSummary: {summary_path}")

if __name__ == '__main__':
    main()
