#!/usr/bin/env python3
"""Register an existing Markdown doc in the Documentation Hub.

This is a non-interactive alternative to tools/add_doc.py.

It:
  - Ensures the markdown file exists in site/content/<slug>.md
  - Generates/overwrites site/pages/<slug>.html
  - Injects a hub card into an existing category (default: web)
  - Updates hub stats
  - Registers the doc in global search (idempotent)

Usage:
  python tools/register_doc.py --slug markdown-language --title "Markdown Language"

Optional:
  --md-path path/to/source.md   (copied into site/content/<slug>.md)
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys

# Ensure the project root is importable
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from app.config import CONTENT_DIR, INDEX_HTML, PAGES_DIR
from app.icons import CARD_ICONS
from app.site_engine import (
    generate_card_html,
    generate_doc_page,
    get_existing_categories,
    inject_card_into_existing_section,
    register_in_search,
    slugify,
    update_hub_stats,
)


def _read_first_h1(md_path: str) -> str | None:
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            for _ in range(60):
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                if line.startswith("# "):
                    return line[2:].strip()
    except OSError:
        return None
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Register existing doc in hub")
    parser.add_argument("--slug", help="Doc slug (used for filenames)")
    parser.add_argument(
        "--md-path",
        help="Optional source markdown path to copy from",
        default=None,
    )
    parser.add_argument("--title", help="Card/page title", default=None)
    parser.add_argument("--version", help="Card/page version string", default="v2026.02")
    parser.add_argument(
        "--category",
        help="Existing category id in site/index.html",
        default="web",
    )
    parser.add_argument(
        "--description",
        help="Card description (1-2 sentences)",
        default=(
            "Exhaustive Markdown study manual and reference: CommonMark core + GFM extensions, "
            "with security, testing, and dialect-compatibility guidance."
        ),
    )
    parser.add_argument(
        "--tags",
        help="Comma-separated card tags",
        default="Markdown,CommonMark,GFM,Reference,Security,Testing",
    )
    parser.add_argument("--color1", default="#06b6d4")
    parser.add_argument("--color2", default="#3b82f6")
    parser.add_argument(
        "--icon",
        choices=sorted(CARD_ICONS.keys()),
        default="book",
        help="Card icon key",
    )
    parser.add_argument(
        "--overwrite-page",
        action="store_true",
        help="Overwrite the generated HTML page if it exists",
    )

    args = parser.parse_args()

    # Determine markdown source and slug.
    md_source = os.path.abspath(args.md_path) if args.md_path else None

    if not args.slug:
        if md_source:
            args.slug = slugify(os.path.splitext(os.path.basename(md_source))[0])
        else:
            print("✗ --slug is required if --md-path is not provided")
            return 2

    slug = args.slug
    dest_md = os.path.join(CONTENT_DIR, f"{slug}.md")

    if md_source:
        if not os.path.isfile(md_source):
            print(f"✗ Markdown source not found: {md_source}")
            return 2
        os.makedirs(CONTENT_DIR, exist_ok=True)
        if os.path.abspath(md_source) != os.path.abspath(dest_md):
            shutil.copy2(md_source, dest_md)
            print(f"✓ Copied markdown → site/content/{slug}.md")
        else:
            print(f"✓ Markdown already at site/content/{slug}.md")
    else:
        if not os.path.isfile(dest_md):
            print(f"✗ Expected existing markdown at: {dest_md}")
            print("  Provide --md-path to copy it in.")
            return 2
        print(f"✓ Found markdown: site/content/{slug}.md")

    # Title
    title = args.title or _read_first_h1(dest_md) or slug.replace("-", " ").title()

    # Ensure category exists
    try:
        with open(INDEX_HTML, "r", encoding="utf-8") as f:
            index_html = f.read()
    except OSError as e:
        print(f"✗ Could not read index.html: {e}")
        return 2

    categories = get_existing_categories(index_html)
    if args.category not in categories:
        print(f"✗ Category '{args.category}' not found in site/index.html")
        print("  Existing categories:")
        for cid, cname in categories.items():
            print(f"  - {cid}: {cname}")
        return 2

    # Generate/overwrite doc page
    os.makedirs(PAGES_DIR, exist_ok=True)
    page_path = os.path.join(PAGES_DIR, f"{slug}.html")
    if os.path.exists(page_path) and not args.overwrite_page:
        # Still safe to regenerate to keep asset version etc, but default is conservative.
        print(f"✓ Page exists (skipped): site/pages/{slug}.html")
    else:
        doc_id = slug.replace("-", "")
        page_html = generate_doc_page(slug, title, args.version, doc_id, args.color1)
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"✓ Wrote page → site/pages/{slug}.html")

    # Inject card (idempotent)
    if f"pages/{slug}.html" in index_html:
        print("✓ Hub card already present in index.html")
    else:
        icon_svg = CARD_ICONS[args.icon]
        tags = [t.strip() for t in args.tags.split(",") if t.strip()]
        card_html = generate_card_html(
            slug=slug,
            title=title,
            version=args.version,
            description=args.description,
            tags=tags,
            color1=args.color1,
            color2=args.color2,
            icon_svg=icon_svg,
        )
        index_html, ok = inject_card_into_existing_section(index_html, args.category, card_html)
        if not ok:
            print(f"✗ Failed to inject card into category '{args.category}'")
            return 1

        index_html = update_hub_stats(index_html)
        with open(INDEX_HTML, "w", encoding="utf-8") as f:
            f.write(index_html)
        print(f"✓ Injected hub card into category '{args.category}' and updated stats")

    # Search registration (idempotent)
    if register_in_search(slug, title, args.color1):
        print("✓ Registered in global search")
    else:
        print("✗ Failed to register in global search")
        return 1

    print(f"\nDone. Open: site/pages/{slug}.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
