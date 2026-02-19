"""
Site engine — HTML generation, parsing, and injection for the Documentation Hub.

This module contains all functions for:
  • Generating doc-page HTML and card HTML
  • Parsing index.html to extract categories and cards
  • Injecting cards and sections into index.html
  • Updating hub stats and global-search.js registration

Used by the data layer, CLI wizard, and GUI dialogs.
"""

import re
import textwrap
from datetime import datetime

from app.config import INDEX_HTML, SEARCH_JS, CONTENT_DIR, PAGES_DIR
from app.icons import CARD_ICONS, SECTION_ICONS


# ── Utilities ────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Convert text to a URL/file-friendly slug."""
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def validate_hex(color: str) -> bool:
    """Check if a string is a valid hex color (#rrggbb)."""
    return bool(re.match(r"^#[0-9a-fA-F]{6}$", color))


# ── Index.html parsing ──────────────────────────────────────

def get_existing_categories(html: str) -> dict[str, str]:
    """Parse index.html to find existing category sections.

    Returns {category_id: category_title}.
    """
    categories = {}
    for m in re.finditer(
        r'<section class="hub-section" data-category="([^"]+)">', html
    ):
        cat_id = m.group(1)
        after = html[m.start() : m.start() + 500]
        title_m = re.search(r'<h2 class="hub-section-title">([^<]+)</h2>', after)
        title = title_m.group(1).replace("&amp;", "&") if title_m else cat_id.title()
        categories[cat_id] = title
    return categories


def count_cards_in_category(html: str, cat_id: str) -> int:
    """Count how many hub-card links exist in a category section."""
    pattern = rf'<section class="hub-section" data-category="{re.escape(cat_id)}">'
    m = re.search(pattern, html)
    if not m:
        return 0
    section_start = m.start()
    end_m = html.find("</section>", section_start)
    section_html = html[section_start:end_m] if end_m != -1 else html[section_start:]
    return len(re.findall(r'<a href="[^"]*" class="hub-card">', section_html))


# ── HTML generation ──────────────────────────────────────────

def generate_card_html(
    slug: str,
    title: str,
    version: str,
    description: str,
    tags: list[str],
    color1: str,
    color2: str,
    icon_svg: str,
) -> str:
    """Generate a hub-card <a> block."""
    tags_html = "\n".join(
        f'            <span class="hub-tag">{t}</span>' for t in tags
    )
    return textwrap.dedent(f"""\
          <!-- {title} Card -->
          <a href="pages/{slug}.html" class="hub-card">
            <div class="hub-card-icon" style="background: linear-gradient(135deg, {color1}, {color2});">
              {icon_svg}
            </div>
            <div class="hub-card-body">
              <div class="hub-card-title-row">
                <h2>{title}</h2>
                <span class="hub-card-badge hub-badge-new">New</span>
              </div>
              <span class="hub-card-version">{version}</span>
              <p>{description}</p>
              <div class="hub-card-tags">
    {tags_html}
              </div>
            </div>
            <div class="hub-card-arrow">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </div>
          </a>""")


def generate_new_section_html(
    cat_id: str,
    cat_title: str,
    cat_desc: str,
    color1: str,
    color2: str,
    section_icon_svg: str,
    card_html: str,
) -> str:
    """Generate a full new category section with one card."""
    return textwrap.dedent(f"""\

      <!-- ═══════════ {cat_title.upper()} SECTION ═══════════ -->
      <section class="hub-section" data-category="{cat_id}">
        <div class="hub-section-header">
          <div class="hub-section-icon" style="background: linear-gradient(135deg, {color1}, {color2});">
            {section_icon_svg}
          </div>
          <div class="hub-section-title-group">
            <h2 class="hub-section-title">{cat_title}</h2>
            <p class="hub-section-desc">{cat_desc}</p>
          </div>
          <span class="hub-section-count">1 doc</span>
        </div>

        <div class="hub-grid">
{textwrap.indent(card_html, '    ')}
        </div>
      </section>""")


def generate_doc_page(
    slug: str, title: str, version: str, doc_id: str, color1: str
) -> str:
    """Generate a full doc HTML page from template."""
    return textwrap.dedent(f"""\
<!doctype html>
<html lang="en" data-theme="dark" data-doc="{doc_id}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{title} — Documentation</title>

  <!-- Highlight.js for code blocks (local) -->
  <link id="hljs-theme" rel="stylesheet" href="../css/highlight-github-dark.min.css">
  <script src="../js/highlight.min.js"></script>
  <script src="../js/highlight-python.min.js"></script>
  <script src="../js/highlight-bash.min.js"></script>
  <script src="../js/highlight-json.min.js"></script>

  <!-- Marked (local) -->
  <script src="../js/marked.min.js"></script>

  <link rel="stylesheet" href="../css/style.css">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="../icon.svg">
  <link rel="icon" type="image/x-icon" href="../icon.ico">

  <!-- prevent FOUC: apply saved theme instantly -->
  <script>
    (function(){{
      var t = localStorage.getItem('ctk-theme') || 'dark';
      document.documentElement.setAttribute('data-theme', t);
    }})();
  </script>
</head>
<body>

  <!-- Reading progress bar -->
  <div id="progress-bar"></div>

  <!-- Mobile top-bar -->
  <header id="mobile-bar">
    <button id="menu-btn" aria-label="Toggle sidebar">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
    </button>
    <span class="mobile-title">{title} Docs</span>
    <button id="theme-btn-mobile" aria-label="Toggle theme">
      <svg id="sun-mobile" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
      <svg id="moon-mobile" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3a7 7 0 009.79 9.79z"/></svg>
    </button>
  </header>

  <div id="overlay"></div>

  <div id="container">
    <!-- Sidebar -->
    <aside id="sidebar">
      <div id="sidebar-header">
        <div id="logo">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{color1}" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/></svg>
          <span>{title}</span>
        </div>
        <div style="display:flex;align-items:center;gap:8px">
          <a href="../index.html" class="sidebar-home-btn" title="Back to Documentation Hub">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>
          </a>
          <button id="theme-btn" aria-label="Toggle theme" title="Toggle light / dark mode">
            <svg id="sun-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
            <svg id="moon-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3a7 7 0 009.79 9.79z"/></svg>
          </button>
        </div>
      </div>

      <!-- Search -->
      <div id="search-wrap">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        <input id="toc-search" type="text" placeholder="Search sections… ( / )" autocomplete="off">
        <kbd class="search-kbd">/</kbd>
      </div>

      <nav id="toc"></nav>

      <div id="sidebar-footer">
        <span class="version-badge">{version}</span>
        <div id="footer-links">
          <a href="../index.html">← Back to Hub</a>
          <span class="kbd-hint" title="Keyboard shortcuts: / = search, T = toggle theme, Esc = close">⌨ Shortcuts</span>
        </div>
      </div>
    </aside>

    <!-- Main content -->
    <main id="main">
      <div id="content">
        <div class="loader">
          <div class="spinner"></div>
          <p>Loading documentation…</p>
        </div>
      </div>

      <!-- Back to top -->
      <button id="back-to-top" aria-label="Back to top" title="Back to top">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 15l-6-6-6 6"/></svg>
      </button>
    </main>
  </div>

  <script>
    window.__DOC_CONFIG = {{
      mdPath: '../content/{slug}.md',
      title: '{title} Docs'
    }};
  </script>
  <script src="../js/docs-renderer.js"></script>
</body>
</html>
""")


# ── Index.html manipulation ──────────────────────────────────

def inject_card_into_existing_section(
    html: str, cat_id: str, card_html: str
) -> tuple[str, bool]:
    """Add a card into an existing category section's .hub-grid."""
    section_pattern = (
        rf'(<section class="hub-section" data-category="{re.escape(cat_id)}">)'
    )
    m = re.search(section_pattern, html)
    if not m:
        return html, False

    section_start = m.start()
    section_end = html.find("</section>", section_start)
    section_block = html[section_start:section_end]

    if '<div class="hub-empty-section">' in section_block:
        empty_start = html.find('<div class="hub-empty-section">', section_start)
        empty_end = html.find("</div>", empty_start) + len("</div>")
        replacement = f'<div class="hub-grid">\n{card_html}\n        </div>'
        html = html[:empty_start] + replacement + html[empty_end:]
    else:
        grid_start = html.find('<div class="hub-grid">', section_start)
        if grid_start == -1:
            return html, False
        grid_section = html[grid_start:section_end]
        last_card_end = grid_section.rfind("</a>")
        if last_card_end == -1:
            return html, False
        insert_pos = grid_start + last_card_end + len("</a>")
        html = html[:insert_pos] + "\n\n" + card_html + html[insert_pos:]

    count = count_cards_in_category(html, cat_id)
    html = update_section_count(html, cat_id, count)
    return html, True


def inject_new_section(html: str, section_html: str) -> tuple[str, bool]:
    """Add a new category section before the closing </div> of hub-sections."""
    marker = "</div><!-- /hub-sections -->"
    if marker in html:
        html = html.replace(marker, section_html + "\n\n    " + marker)
        return html, True

    alt_marker = "    </div><!-- /hub-sections -->"
    if alt_marker in html:
        html = html.replace(alt_marker, section_html + "\n\n" + alt_marker)
        return html, True

    return html, False


def update_section_count(html: str, cat_id: str, count: int) -> str:
    """Update the 'N docs' badge in a section header."""
    pattern = (
        rf'(<section class="hub-section" data-category="{re.escape(cat_id)}">'
        r'.*?<span class="hub-section-count">)(.*?)(</span>)'
    )
    label = f"{count} doc{'s' if count != 1 else ''}"
    return re.sub(pattern, rf"\g<1>{label}\3", html, count=1, flags=re.DOTALL)


def update_hub_stats(html: str) -> str:
    """Recount total docs and categories, update the stats bar."""
    total = len(re.findall(r'<a href="[^"]*" class="hub-card">', html))
    cats = get_existing_categories(html)
    cats_with_docs = sum(
        1 for cid in cats if count_cards_in_category(html, cid) > 0
    )

    html = re.sub(
        r'(<strong id="stat-docs">)\d+(</strong>)',
        rf"\g<1>{total}\2",
        html,
    )
    html = re.sub(
        r'(<strong id="stat-categories">)\d+(</strong>)',
        rf"\g<1>{cats_with_docs}\2",
        html,
    )
    month = datetime.now().strftime("%b %Y")
    html = re.sub(
        r'(Updated <strong>)[^<]+(</strong>)',
        rf"\g<1>{month}\2",
        html,
    )
    return html


# ── global-search.js manipulation ────────────────────────────

def register_in_search(slug: str, title: str, color1: str) -> bool:
    """Add a new entry to the DOCS array in global-search.js."""
    try:
        with open(SEARCH_JS, "r", encoding="utf-8") as f:
            js = f.read()
    except OSError:
        return False

    doc_id = slug.replace("-", "")
    new_entry = textwrap.dedent(f"""\
    {{
      id: '{doc_id}',
      title: '{title}',
      mdPath: 'content/{slug}.md',
      htmlPage: 'pages/{slug}.html',
      color: '{color1}',
    }}""")

    docs_end = js.find("];", js.find("const DOCS"))
    if docs_end == -1:
        return False

    js = js[:docs_end] + "    " + new_entry + ",\n  " + js[docs_end:]

    with open(SEARCH_JS, "w", encoding="utf-8") as f:
        f.write(js)
    return True


def remove_from_search(slug: str) -> None:
    """Remove a doc entry from global-search.js."""
    try:
        with open(SEARCH_JS, "r", encoding="utf-8") as f:
            js = f.read()
        entry_pat = re.compile(
            r",?\s*\{\s*\n\s*id:\s*'[^']*',\s*\n\s*title:\s*'[^']*',\s*\n"
            r"\s*mdPath:\s*'content/"
            + re.escape(slug)
            + r"\.md'.*?\}",
            re.DOTALL,
        )
        js = entry_pat.sub("", js, count=1)
        js = re.sub(r"\[\s*,", "[", js)
        with open(SEARCH_JS, "w", encoding="utf-8") as f:
            f.write(js)
    except Exception:
        pass
