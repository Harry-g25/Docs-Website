#!/usr/bin/env python3
"""
Check Fences — Markdown code-fence balance checker.

Scans a Markdown file for unclosed fenced code blocks (``` ... ```).
Useful for catching formatting errors before publishing.

Usage:
    python tools/check_fences.py <markdown-file>
    python tools/check_fences.py site/content/python-3.14.md
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check_fences(filepath: str) -> list[tuple[int, str]]:
    """Return list of (line_number, fence_text) for unclosed fences."""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_code = False
    opens: list[tuple[int, str]] = []
    tick3 = "```"

    for i, line in enumerate(lines):
        stripped = line.strip()
        if in_code:
            if stripped == tick3:
                in_code = False
                opens.pop()
        else:
            if stripped.startswith(tick3):
                in_code = True
                opens.append((i + 1, stripped[:40]))

    return opens


def main():
    if len(sys.argv) < 2:
        # Default: check all .md files in the docs content directory.
        # Historical layouts used ROOT/content; current layout uses ROOT/site/content.
        content_dir = os.path.join(ROOT, "content")
        if not os.path.isdir(content_dir):
            content_dir = os.path.join(ROOT, "site", "content")
        if not os.path.isdir(content_dir):
            print(
                "Could not find a docs content directory. Expected either 'content/' or 'site/content/' at repo root.",
                file=sys.stderr,
            )
            sys.exit(1)
        files = sorted(
            os.path.join(content_dir, f)
            for f in os.listdir(content_dir)
            if f.endswith(".md")
        )
    else:
        files = [sys.argv[1]]

    all_ok = True
    for filepath in files:
        name = os.path.relpath(filepath, ROOT)
        unclosed = check_fences(filepath)
        if unclosed:
            all_ok = False
            print(f"  FAIL  {name} — {len(unclosed)} unclosed fence(s):")
            for ln, txt in unclosed:
                print(f"        line {ln}: {txt}")
        else:
            print(f"  OK    {name}")

    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
