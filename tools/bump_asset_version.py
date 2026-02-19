"""Bump the static site's cache-busting version.

Version scheme: YYYYMMDD-N (increments N each bump on the same day).

This updates:
- window.__ASSET_VERSION in site/index.html and site/pages/*.html
- all occurrences of ?v=... / &v=... inside those HTML files

Usage:
  python tools/bump_asset_version.py
  python tools/bump_asset_version.py --dry-run
  python tools/bump_asset_version.py --set 20260219-3
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


_RE_ASSET_VERSION = re.compile(
    r"(window\.__ASSET_VERSION\s*=\s*['\"])([^'\"]+)(['\"]\s*;)",
    re.IGNORECASE,
)
_RE_QUERY_V = re.compile(r"([?&]v=)[^&#\"']+", re.IGNORECASE)

# Repair patterns for a previous buggy replacement that could turn
#   ?v=20260219-2  ->  P260219-2
# and
#   window.__ASSET_VERSION = '20260219-2';  ->  P260219-2';
_RE_BROKEN_VERSION_LINE = re.compile(r"(^[ \t]*)P\d{6}-\d+';", re.MULTILINE)
_RE_BROKEN_SUFFIX = re.compile(r"(\.(?:css|js|html))P\d{6}-\d+", re.IGNORECASE)


@dataclass(frozen=True)
class UpdateResult:
    path: Path
    changed: bool


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def _extract_current_version(index_html: str) -> str:
    m = _RE_ASSET_VERSION.search(index_html)
    return m.group(2).strip() if m else ""


def _compute_next_version(current: str, now: datetime) -> str:
    today = now.strftime("%Y%m%d")
    m = re.fullmatch(r"(\d{8})-(\d+)", (current or "").strip())
    if m and m.group(1) == today:
        return f"{today}-{int(m.group(2)) + 1}"
    return f"{today}-1"


def _apply_version_updates(content: str, new_version: str) -> str:
    # Repair previously corrupted content first.
    content = _RE_BROKEN_VERSION_LINE.sub(
        lambda m: f"{m.group(1)}window.__ASSET_VERSION = '{new_version}';",
        content,
    )
    content = _RE_BROKEN_SUFFIX.sub(
        lambda m: f"{m.group(1)}?v={new_version}",
        content,
    )

    # Update JS global.
    content = _RE_ASSET_VERSION.sub(
        lambda m: f"{m.group(1)}{new_version}{m.group(3)}",
        content,
    )

    # Update cache-busting query params.
    content = _RE_QUERY_V.sub(
        lambda m: f"{m.group(1)}{new_version}",
        content,
    )

    return content


def _update_file(path: Path, new_version: str, dry_run: bool) -> UpdateResult:
    before = _read_text(path)
    after = _apply_version_updates(before, new_version)

    changed = after != before
    if changed and not dry_run:
        _write_text(path, after)

    return UpdateResult(path=path, changed=changed)


def main() -> int:
    parser = argparse.ArgumentParser(description="Bump the site's asset version (cache-busting ?v=).")
    parser.add_argument(
        "--set",
        dest="set_version",
        default="",
        help="Set an explicit version string (e.g. 20260219-3).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files.",
    )

    args = parser.parse_args()

    root = _repo_root()
    site_dir = root / "site"
    index_path = site_dir / "index.html"
    pages_dir = site_dir / "pages"

    if not index_path.is_file():
        raise SystemExit(f"Expected {index_path} to exist")

    index_html = _read_text(index_path)
    current = _extract_current_version(index_html)

    now = datetime.now()
    new_version = args.set_version.strip() or _compute_next_version(current, now)

    targets: list[Path] = [index_path]
    if pages_dir.is_dir():
        targets.extend(sorted(pages_dir.glob("*.html")))

    results = [_update_file(p, new_version, args.dry_run) for p in targets]
    changed = [r for r in results if r.changed]

    mode = "DRY RUN" if args.dry_run else "UPDATED"
    print(f"{mode}: {current or '(missing)'} -> {new_version}")
    print(f"Files scanned: {len(results)}")
    print(f"Files changed: {len(changed)}")
    for r in changed:
        rel = r.path.relative_to(root)
        print(f" - {rel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
