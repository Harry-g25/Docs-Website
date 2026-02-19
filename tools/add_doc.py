#!/usr/bin/env python3
"""
Add-Doc CLI Wizard
==================
Interactive tool to add a new markdown doc to the Documentation Hub.

Usage:
    python tools/add_doc.py <path-to-markdown-file>
    python tools/add_doc.py                          # prompts for path

All heavy-lifting (HTML generation, injection, search registration)
lives in ``app.site_engine``.  This file is just a thin CLI wrapper.
"""

import os
import re
import shutil
import sys

# Ensure the project root is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import CONTENT_DIR, INDEX_HTML, PAGES_DIR
from app.icons import CARD_ICONS, SECTION_ICONS
from app.site_engine import (
    count_cards_in_category,
    generate_card_html,
    generate_doc_page,
    generate_new_section_html,
    get_existing_categories,
    inject_card_into_existing_section,
    inject_new_section,
    register_in_search,
    slugify,
    update_hub_stats,
    validate_hex,
)


def _prompt(msg: str, default: str | None = None) -> str:
    suffix = f" [{default}]" if default else ""
    ans = input(f"  {msg}{suffix}: ").strip()
    return ans or default or ""


def _prompt_hex(msg: str) -> str:
    while True:
        val = _prompt(msg)
        if not val.startswith("#"):
            val = "#" + val
        if validate_hex(val):
            return val
        print("    \u26a0  Enter a valid hex colour (e.g. #6366f1)")


def main():
    print()
    print("  \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557")
    print("  \u2551      \U0001f4da Add Doc \u2014 CLI Wizard         \u2551")
    print("  \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d")
    print()

    # Step 0 â€” Markdown file
    md_path = sys.argv[1] if len(sys.argv) > 1 else _prompt("Path to markdown file")
    md_path = os.path.abspath(md_path)
    if not os.path.isfile(md_path):
        print(f"\n  \u2717 File not found: {md_path}")
        sys.exit(1)
    if not md_path.endswith(".md"):
        print(f"\n  \u2717 Expected a .md file, got: {md_path}")
        sys.exit(1)
    print(f"\n  \u2713 Found: {os.path.basename(md_path)}\n")

    # Step 1 â€” Title
    with open(md_path, "r", encoding="utf-8") as f:
        head = f.readlines()[:20]
    auto_title = None
    for line in head:
        m = re.match(r"^#\s+(.+)", line.strip())
        if m:
            auto_title = m.group(1).strip()
            break
    title = _prompt("Doc title", default=auto_title)
    slug = slugify(title)
    doc_id = slug.replace("-", "")

    if os.path.exists(os.path.join(PAGES_DIR, f"{slug}.html")):
        print(f"\n  \u26a0  site/pages/{slug}.html already exists")
        if _prompt("Overwrite? (y/n)", "n").lower() != "y":
            print("  Aborted.")
            sys.exit(0)

    # Step 2 â€” Category
    print()
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        index_html = f.read()
    cats = get_existing_categories(index_html)
    cat_keys = list(cats.keys())

    print("  Existing categories:")
    for i, (cid, cname) in enumerate(cats.items(), 1):
        cnt = count_cards_in_category(index_html, cid)
        print(f"    {i}. {cname} ({cnt} docs)")
    print(f"    {len(cat_keys) + 1}. \u2795 Create new category")

    while True:
        try:
            idx = int(input("\n  Pick a category number: ").strip()) - 1
            if 0 <= idx < len(cat_keys):
                cat_id, cat_title, is_new = cat_keys[idx], cats[cat_keys[idx]], False
                break
            if idx == len(cat_keys):
                is_new = True
                break
        except ValueError:
            pass
        print(f"    \u26a0  Enter 1\u2013{len(cat_keys) + 1}")

    section_icon_svg = ""
    if is_new:
        cat_title = _prompt("New category name")
        cat_id = slugify(cat_title)
        cat_desc = _prompt("Description", f"{cat_title} documentation and guides")
        sec_keys = list(SECTION_ICONS.keys())
        print("\n  Section header icon:")
        for i, k in enumerate(sec_keys, 1):
            print(f"    {i}. {k}")
        while True:
            try:
                si = int(input("  Icon number: ").strip()) - 1
                if 0 <= si < len(sec_keys):
                    section_icon_svg = SECTION_ICONS[sec_keys[si]]
                    break
            except ValueError:
                pass

    # Steps 3-7 â€” Version, description, tags, colours, icon
    version = _prompt("Version", "v1.0")
    if not version.startswith("v"):
        version = "v" + version
    print()
    description = _prompt("Short description (1-2 sentences)")
    tags = [t.strip() for t in _prompt("Tags (comma-separated)").split(",") if t.strip()]
    print()
    color1 = _prompt_hex("Gradient start colour (e.g. #6366f1)")
    color2 = _prompt_hex("Gradient end colour   (e.g. #818cf8)")

    icon_keys = list(CARD_ICONS.keys())
    print("\n  Card icon:")
    for i, k in enumerate(icon_keys, 1):
        print(f"    {i:2}. {k}")
    while True:
        try:
            ii = int(input("  Icon number: ").strip()) - 1
            if 0 <= ii < len(icon_keys):
                icon_svg = CARD_ICONS[icon_keys[ii]]
                break
        except ValueError:
            pass

    # Confirm
    print(f"\n  Title:    {title}  ({slug})")
    print(f"  Category: {cat_title}")
    print(f"  Colours:  {color1} \u2192 {color2}")
    if _prompt("\n  Proceed? (y/n)", "y").lower() != "y":
        print("  Aborted.")
        sys.exit(0)

    # Execute
    print()
    dest_md = os.path.join(CONTENT_DIR, f"{slug}.md")
    shutil.copy2(md_path, dest_md)
    print(f"  \u2713 Copied markdown \u2192 content/{slug}.md")

    page_html = generate_doc_page(slug, title, version, doc_id, color1)
    with open(os.path.join(PAGES_DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"  \u2713 Created page \u2192 site/pages/{slug}.html")

    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        index_html = f.read()

    card_html = generate_card_html(
        slug, title, version, description, tags, color1, color2, icon_svg,
    )

    if is_new:
        section_html = generate_new_section_html(
            cat_id, cat_title, cat_desc, color1, color2,
            section_icon_svg, card_html,
        )
        index_html, _ = inject_new_section(index_html, section_html)
    else:
        index_html, _ = inject_card_into_existing_section(
            index_html, cat_id, card_html,
        )

    index_html = update_hub_stats(index_html)
    with open(INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(index_html)
    print("  \u2713 Updated index.html")

    register_in_search(slug, title, color1)
    print("  \u2713 Registered in global search")
    print(f"\n  Done! View: http://localhost:8000/site/pages/{slug}.html\n")


if __name__ == "__main__":
    main()
