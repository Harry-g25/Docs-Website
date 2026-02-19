"""
Shared paths, constants, and color palette for the Documentation Hub.
"""

import os

# ── Directory layout ─────────────────────────────────────────────

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(BASE_DIR, "site")
CONTENT_DIR = os.path.join(SITE_DIR, "content")
PAGES_DIR = os.path.join(SITE_DIR, "pages")
INDEX_HTML = os.path.join(SITE_DIR, "index.html")
SEARCH_JS = os.path.join(SITE_DIR, "js", "global-search.js")
MANIFEST_FILE = os.path.join(BASE_DIR, ".manifest.json")
ACTIVITY_LOG = os.path.join(BASE_DIR, ".activity_log.json")
TRASH_DIR = os.path.join(BASE_DIR, ".trash")

# ── Qt application metadata ──────────────────────────────────────

SETTINGS_ORG = "DocsHub"
SETTINGS_APP = "DocsBrowser"

# ── Color palette (dark theme) ───────────────────────────────────

BG_DARK = "#0f172a"
BG_PANEL = "#111827"
BG_CARD = "#1e293b"
BG_HOVER = "#334155"
BORDER = "rgba(255,255,255,0.06)"
TEXT = "#e2e8f0"
TEXT_DIM = "#94a3b8"
TEXT_FAINT = "#64748b"
ACCENT = "#6366f1"
ACCENT_L = "#818cf8"
RED = "#f87171"
GREEN = "#34d399"
YELLOW = "#fbbf24"
