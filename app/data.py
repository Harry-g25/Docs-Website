"""
Data layer — manifest cache, activity log, CRUD operations, file helpers.

All index.html reads/writes and doc-level mutations are centralised here
so the UI never touches the filesystem directly.
"""

import html as html_module
import json
import os
import re
import shutil
import tempfile
import time
from datetime import datetime, timezone

from app.config import (
    ACTIVITY_LOG, BASE_DIR, CONTENT_DIR, INDEX_HTML, MANIFEST_FILE,
    PAGES_DIR, SEARCH_JS, SITE_DIR, TRASH_DIR,
)
from app.icons import SECTION_ICONS
from app.site_engine import (
    count_cards_in_category,
    generate_card_html,
    generate_doc_page,
    get_existing_categories,
    inject_card_into_existing_section,
    inject_new_section,
    register_in_search,
    remove_from_search,
    slugify,
    update_hub_stats,
    update_section_count,
)


# ═════════════════════════════════════════════════════════════
#  Atomic write
# ═════════════════════════════════════════════════════════════

def atomic_write(path: str, content: str, encoding: str = "utf-8") -> None:
    """Write via temp file + os.replace for crash safety."""
    dir_name = os.path.dirname(path)
    os.makedirs(dir_name, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=dir_name, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding=encoding) as f:
            f.write(content)
        os.replace(tmp, path)
    except Exception:
        try:
            os.remove(tmp)
        except OSError:
            pass
        raise


# ═════════════════════════════════════════════════════════════
#  Activity log
# ═════════════════════════════════════════════════════════════

ACTION_LABELS = {
    "deleted": "\U0001f5d1 Deleted",
    "edited": "\u270f Edited",
    "moved": "\U0001f4e6 Moved",
    "renamed": "\u270f Renamed",
    "added_category": "\u2795 Category",
    "deleted_category": "\U0001f5d1 Category",
    "reordered": "\u2195 Reordered",
    "added": "\u2795 Added",
}


def log_activity(action: str, target: str, detail: str = "") -> None:
    entry = {
        "time": time.time(),
        "action": action,
        "target": target,
        "detail": detail,
    }
    try:
        entries: list = []
        if os.path.isfile(ACTIVITY_LOG):
            with open(ACTIVITY_LOG, "r", encoding="utf-8") as f:
                entries = json.load(f)
        entries.insert(0, entry)
        atomic_write(ACTIVITY_LOG, json.dumps(entries[:100], indent=2))
    except Exception:
        pass


def get_recent_activity(limit: int = 10) -> list[dict]:
    try:
        if os.path.isfile(ACTIVITY_LOG):
            with open(ACTIVITY_LOG, "r", encoding="utf-8") as f:
                return json.load(f)[:limit]
    except Exception:
        pass
    return []


# ═════════════════════════════════════════════════════════════
#  Trash / backup
# ═════════════════════════════════════════════════════════════

def _ensure_trash() -> None:
    os.makedirs(TRASH_DIR, exist_ok=True)


def _backup_index() -> None:
    _ensure_trash()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy2(INDEX_HTML, os.path.join(TRASH_DIR, f"index_{ts}.html"))
    backups = sorted(
        [f for f in os.listdir(TRASH_DIR) if f.startswith("index_")],
        reverse=True,
    )
    for old in backups[20:]:
        try:
            os.remove(os.path.join(TRASH_DIR, old))
        except OSError:
            pass


def _trash_file(path: str) -> None:
    if not os.path.exists(path):
        return
    _ensure_trash()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.move(path, os.path.join(TRASH_DIR, f"{ts}_{os.path.basename(path)}"))


# ═════════════════════════════════════════════════════════════
#  Manifest cache
# ═════════════════════════════════════════════════════════════

_cache: dict = {"docs": None, "cats": None, "mtime": 0}


def _invalidate_cache() -> None:
    _cache["docs"] = None
    _cache["cats"] = None


def _ensure_cache() -> None:
    try:
        mtime = os.path.getmtime(INDEX_HTML)
    except OSError:
        return
    if _cache["docs"] is not None and mtime == _cache["mtime"]:
        return
    html = _read_index()
    _cache["docs"] = parse_docs(html)
    _cache["cats"] = parse_categories(html)
    _cache["mtime"] = mtime
    try:
        atomic_write(
            MANIFEST_FILE,
            json.dumps(
                {
                    "docs": _cache["docs"],
                    "categories": _cache["cats"],
                    "synced": datetime.now(timezone.utc).isoformat(),
                },
                indent=2,
            ),
        )
    except Exception:
        pass


def cached_docs() -> list[dict]:
    _ensure_cache()
    return list(_cache["docs"] or [])


def cached_categories() -> list[dict]:
    _ensure_cache()
    return list(_cache["cats"] or [])


# ═════════════════════════════════════════════════════════════
#  Index.html read/write
# ═════════════════════════════════════════════════════════════

def _read_index() -> str:
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        return f.read()


def _write_index(html: str) -> None:
    atomic_write(INDEX_HTML, html)
    _invalidate_cache()


# ═════════════════════════════════════════════════════════════
#  HTML parsing
# ═════════════════════════════════════════════════════════════

def parse_docs(html: str | None = None) -> list[dict]:
    if html is None:
        html = _read_index()
    docs = []
    categories = get_existing_categories(html)
    for cat_id, cat_name in categories.items():
        pat = rf'<section class="hub-section" data-category="{re.escape(cat_id)}">'
        m = re.search(pat, html)
        if not m:
            continue
        sec_start = m.start()
        sec_end = html.find("</section>", sec_start)
        sec = html[sec_start:sec_end] if sec_end != -1 else html[sec_start:]
        card_pat = re.compile(
            r'<a\s+href="pages/([^"]+)\.html"\s+class="hub-card"[^>]*>'
            r".*?"
            r'style="background:\s*linear-gradient\(135deg,\s*([^,]+),\s*([^)]+)\)'
            r".*?"
            r"<h2>([^<]+)</h2>"
            r".*?"
            r'<span class="hub-card-version">([^<]+)</span>'
            r".*?"
            r"<p>([^<]+)</p>"
            r".*?</a>",
            re.DOTALL,
        )
        for cm in card_pat.finditer(sec):
            card_block = cm.group(0)
            tags = re.findall(
                r'<span class="hub-tag">([^<]+)</span>', card_block
            )
            docs.append(
                {
                    "slug": cm.group(1),
                    "title": cm.group(4).strip(),
                    "version": cm.group(5).strip(),
                    "description": cm.group(6).strip(),
                    "color1": cm.group(2).strip(),
                    "color2": cm.group(3).strip(),
                    "tags": tags,
                    "category_id": cat_id,
                    "category_name": cat_name,
                }
            )
    return docs


def parse_categories(html: str | None = None) -> list[dict]:
    if html is None:
        html = _read_index()
    cats = []
    for m in re.finditer(
        r'<section class="hub-section" data-category="([^"]+)">.*?'
        r'style="background:\s*linear-gradient\(135deg,\s*([^,]+),\s*([^)]+)\)[^"]*".*?'
        r'<h2 class="hub-section-title">([^<]+)</h2>.*?'
        r'<p class="hub-section-desc">([^<]*)</p>',
        html,
        re.DOTALL,
    ):
        cid = m.group(1)
        cats.append(
            {
                "id": cid,
                "name": m.group(4).replace("&amp;", "&"),
                "description": m.group(5).replace("&amp;", "&"),
                "color1": m.group(2).strip(),
                "color2": m.group(3).strip(),
                "doc_count": count_cards_in_category(html, cid),
            }
        )
    return cats


# ═════════════════════════════════════════════════════════════
#  File-system helpers
# ═════════════════════════════════════════════════════════════

def dir_size_bytes(path: str) -> int:
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            try:
                total += os.path.getsize(os.path.join(dirpath, f))
            except OSError:
                pass
    return total


def format_bytes(b: int) -> str:
    if b < 1024:
        return f"{b} B"
    if b < 1024 * 1024:
        return f"{b / 1024:.1f} KB"
    return f"{b / (1024 * 1024):.1f} MB"


def recent_content_files(limit: int = 8) -> list[tuple[str, float]]:
    files = []
    if os.path.isdir(CONTENT_DIR):
        for fn in os.listdir(CONTENT_DIR):
            if fn.endswith(".md"):
                fp = os.path.join(CONTENT_DIR, fn)
                files.append((fn, os.path.getmtime(fp)))
    files.sort(key=lambda x: x[1], reverse=True)
    return files[:limit]


def relative_time(ts: float) -> str:
    diff = time.time() - ts
    if diff < 60:
        return "just now"
    if diff < 3600:
        m = int(diff // 60)
        return f"{m} min{'s' if m > 1 else ''} ago"
    if diff < 86400:
        h = int(diff // 3600)
        return f"{h} hour{'s' if h > 1 else ''} ago"
    d = int(diff // 86400)
    if d == 1:
        return "yesterday"
    if d < 30:
        return f"{d} days ago"
    return datetime.fromtimestamp(ts).strftime("%b %d, %Y")


# ═════════════════════════════════════════════════════════════
#  CRUD operations
# ═════════════════════════════════════════════════════════════

def delete_doc(slug: str) -> None:
    _backup_index()
    html = _read_index()
    card_pat = re.compile(
        r"[ \t]*(?:<!-- [^>]+ -->\n)?[ \t]*<a\s+href=\"pages/"
        + re.escape(slug)
        + r'\.html"\s+class="hub-card"[^>]*>.*?</a>\s*',
        re.DOTALL,
    )
    html, n = card_pat.subn("", html, count=1)
    if n > 0:
        cats = get_existing_categories(html)
        for cid in cats:
            html = update_section_count(
                html, cid, count_cards_in_category(html, cid)
            )
        html = update_hub_stats(html)
        _write_index(html)
    remove_from_search(slug)
    _trash_file(os.path.join(CONTENT_DIR, f"{slug}.md"))
    _trash_file(os.path.join(PAGES_DIR, f"{slug}.html"))
    log_activity("deleted", slug, f"Deleted doc: {slug}")


def update_doc_metadata(
    slug: str,
    title: str | None = None,
    version: str | None = None,
    description: str | None = None,
    tags: list[str] | None = None,
    color1: str | None = None,
    color2: str | None = None,
) -> bool:
    """Update a doc card's metadata in index.html and regenerate page."""
    from app.icons import CARD_ICONS

    _backup_index()
    html = _read_index()
    docs = parse_docs(html)
    doc = next((d for d in docs if d["slug"] == slug), None)
    if not doc:
        return False

    new_title = title if title is not None else doc["title"]
    new_ver = version if version is not None else doc["version"]
    new_desc = description if description is not None else doc["description"]
    new_tags = tags if tags is not None else doc["tags"]
    new_c1 = color1 if color1 is not None else doc["color1"]
    new_c2 = color2 if color2 is not None else doc["color2"]

    # Extract icon SVG from old card
    card_pat = re.compile(
        r'([ \t]*(?:<!-- [^>]+ -->\n)?[ \t]*<a\s+href="pages/'
        + re.escape(slug)
        + r'\.html"\s+class="hub-card"[^>]*>.*?</a>)',
        re.DOTALL,
    )
    m = card_pat.search(html)
    if not m:
        return False
    old_card = m.group(1)
    icon_m = re.search(
        r'<div class="hub-card-icon"[^>]*>\s*(<svg.*?</svg>)',
        old_card,
        re.DOTALL,
    )
    icon_svg = icon_m.group(1) if icon_m else CARD_ICONS.get("book", "")

    new_card = generate_card_html(
        slug, new_title, new_ver, new_desc, new_tags, new_c1, new_c2, icon_svg
    )
    html = html[: m.start()] + new_card + html[m.end() :]
    _write_index(html)

    # Regenerate doc page
    doc_id = slug.replace("-", "")
    atomic_write(
        os.path.join(PAGES_DIR, f"{slug}.html"),
        generate_doc_page(slug, new_title, new_ver, doc_id, new_c1),
    )

    # Update search JS title
    try:
        with open(SEARCH_JS, "r", encoding="utf-8") as f:
            js = f.read()
        js = re.sub(
            r"(id:\s*'" + re.escape(doc_id) + r"',\s*\n\s*title:\s*')[^']*(')",
            rf"\g<1>{new_title}\2",
            js,
            count=1,
        )
        atomic_write(SEARCH_JS, js)
    except Exception:
        pass

    log_activity("edited", slug, f"Updated: {new_title}")
    return True


def rename_category(
    cat_id: str, new_name: str, new_desc: str | None = None
) -> None:
    _backup_index()
    html = _read_index()
    pat = re.compile(
        r'(<section class="hub-section" data-category="'
        + re.escape(cat_id)
        + r'">'
        r'.*?<h2 class="hub-section-title">)([^<]+)(</h2>)',
        re.DOTALL,
    )
    html = pat.sub(rf"\g<1>{html_module.escape(new_name)}\3", html, count=1)
    if new_desc is not None:
        desc_pat = re.compile(
            r'(<section class="hub-section" data-category="'
            + re.escape(cat_id)
            + r'">'
            r'.*?<p class="hub-section-desc">)([^<]*)(</p>)',
            re.DOTALL,
        )
        html = desc_pat.sub(
            rf"\g<1>{html_module.escape(new_desc)}\3", html, count=1
        )
    _write_index(html)
    log_activity("renamed", cat_id, f"Renamed to {new_name}")


def delete_category(cat_id: str) -> None:
    """Remove category section and trash all its docs."""
    _backup_index()
    html = _read_index()
    pat = rf'<section class="hub-section" data-category="{re.escape(cat_id)}">'
    m = re.search(pat, html)
    if not m:
        return
    sec_start = m.start()
    sec_end_pos = html.find("</section>", sec_start)
    sec = html[sec_start:sec_end_pos] if sec_end_pos != -1 else ""
    slugs = re.findall(r'href="pages/([^"]+)\.html"', sec)
    if sec_end_pos != -1:
        removal_end = sec_end_pos + len("</section>")
        while removal_end < len(html) and html[removal_end] in "\n\r":
            removal_end += 1
        html = html[:sec_start] + html[removal_end:]
    html = update_hub_stats(html)
    _write_index(html)
    for s in slugs:
        _trash_file(os.path.join(CONTENT_DIR, f"{s}.md"))
        _trash_file(os.path.join(PAGES_DIR, f"{s}.html"))
        remove_from_search(s)
    log_activity(
        "deleted_category", cat_id, f"Deleted category ({len(slugs)} docs trashed)"
    )


def move_doc_to_category(slug: str, new_cat_id: str) -> bool:
    _backup_index()
    html = _read_index()
    card_pat = re.compile(
        r'([ \t]*(?:<!-- [^>]+ -->\n)?[ \t]*<a\s+href="pages/'
        + re.escape(slug)
        + r'\.html"\s+class="hub-card"[^>]*>.*?</a>)',
        re.DOTALL,
    )
    m = card_pat.search(html)
    if not m:
        return False
    card_html = m.group(1).strip()
    html = card_pat.sub("", html, count=1)
    html, ok = inject_card_into_existing_section(html, new_cat_id, card_html)
    if ok:
        cats = get_existing_categories(html)
        for cid in cats:
            html = update_section_count(
                html, cid, count_cards_in_category(html, cid)
            )
        html = update_hub_stats(html)
        _write_index(html)
        log_activity("moved", slug, f"Moved to {new_cat_id}")
    return ok


def add_category(
    name: str,
    description: str,
    color1: str,
    color2: str,
    icon_key: str = "book",
) -> tuple[bool, str]:
    """Add a new empty category section to index.html."""
    _backup_index()
    html = _read_index()
    cat_id = slugify(name)
    if cat_id in get_existing_categories(html):
        return False, "Category already exists"
    section_icon = SECTION_ICONS.get(icon_key, SECTION_ICONS["book"])
    safe_name = html_module.escape(name)
    safe_desc = html_module.escape(description)
    section_html = (
        f'\n      <!-- ═══════════ {safe_name.upper()} SECTION ═══════════ -->\n'
        f'      <section class="hub-section" data-category="{cat_id}">\n'
        f"        <div class=\"hub-section-header\">\n"
        f'          <div class="hub-section-icon" style="background: linear-gradient(135deg, {color1}, {color2});">\n'
        f"            {section_icon}\n"
        f"          </div>\n"
        f'          <div class="hub-section-title-group">\n'
        f'            <h2 class="hub-section-title">{safe_name}</h2>\n'
        f'            <p class="hub-section-desc">{safe_desc}</p>\n'
        f"          </div>\n"
        f'          <span class="hub-section-count">0 docs</span>\n'
        f"        </div>\n\n"
        f'        <div class="hub-grid">\n'
        f"        </div>\n"
        f"      </section>"
    )
    html, ok = inject_new_section(html, section_html)
    if ok:
        html = update_hub_stats(html)
        _write_index(html)
        log_activity("added_category", cat_id, f"Created: {name}")
    return ok, "" if ok else "Failed to inject section"


def swap_categories(cat_id_a: str, cat_id_b: str) -> bool:
    """Swap positions of two category sections in index.html."""
    _backup_index()
    html = _read_index()

    def _find_block(h: str, cid: str):
        tag = f'<section class="hub-section" data-category="{cid}">'
        idx = h.find(tag)
        if idx == -1:
            return None
        line_start = h.rfind("\n", 0, idx) + 1
        prefix = h[line_start:idx].strip()
        if prefix.startswith("<!--"):
            prev_nl = h.rfind("\n", 0, line_start - 1)
            start = (prev_nl + 1) if prev_nl != -1 else 0
        else:
            start = line_start
        end = h.find("</section>", idx)
        if end == -1:
            return None
        end += len("</section>")
        while end < len(h) and h[end] in "\n\r":
            end += 1
        return start, end

    a = _find_block(html, cat_id_a)
    b = _find_block(html, cat_id_b)
    if not a or not b:
        return False
    if a[0] > b[0]:
        a, b = b, a
    a_text = html[a[0] : a[1]]
    b_text = html[b[0] : b[1]]
    html = html[: b[0]] + a_text + html[b[1] :]
    html = html[: a[0]] + b_text + html[a[1] :]
    _write_index(html)
    log_activity("reordered", cat_id_a, f"Swapped with {cat_id_b}")
    return True
