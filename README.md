# Documentation Hub

A static documentation site for quick reference and learning. Browse beautiful, searchable docs for multiple topics — all in one place. Includes a lightweight PyQt6 desktop browser with built-in content management.

## Quick Start

### Desktop app (recommended)

```bash
pip install -r requirements.txt
python run.py
```

Launches a dedicated PyQt6 desktop browser with navigation toolbar, find-in-page, system tray, and an integrated content manager for adding/editing docs.

### Web-only (no desktop app)

```bash
python serve.py
```

Opens the hub at `http://localhost:8000` in your default browser.

## Project Structure

```
├── run.py                    # Desktop app entry point
├── serve.py                  # Standalone dev server (port 8000)
├── requirements.txt          # Python dependencies
├── .manifest.json            # Document registry (metadata, categories)
│
├── app/                      # Application package
│   ├── __init__.py           # Version
│   ├── config.py             # Paths, colour palette, settings keys
│   ├── server.py             # Embedded HTTP server
│   ├── icons.py              # SVG icon library
│   ├── styles.py             # Qt stylesheets
│   ├── site_engine.py        # HTML generation, injection, search registration
│   ├── data.py               # Data layer — manifest CRUD, activity log, trash
│   ├── widgets.py            # Reusable Qt widgets (CodeEditor, FindBar, etc.)
│   ├── dialogs.py            # All dialog windows (AddDocWizard, EditDoc, etc.)
│   ├── views.py              # Dashboard, DocsList, CategoryManager, Editor views
│   ├── content_manager.py    # Side-panel orchestrator (tabs + stacked views)
│   └── browser.py            # Main window (toolbar, WebView, splitter, tray)
│
├── site/                     # Static site — GitHub Pages root
│   ├── .nojekyll             # Disables Jekyll processing on GitHub Pages
│   ├── index.html            # Hub home page
│   ├── css/style.css         # Global styles + per-doc themes
│   ├── js/
│   │   ├── docs-renderer.js  # Markdown renderer, TOC & search engine
│   │   └── global-search.js  # Cross-doc search index
│   ├── pages/                # One HTML shell per doc
│   └── content/              # Markdown source files (fetched at runtime)
│       ├── python-3.14.md
│       ├── customtkinter.md
│       ├── reportlab.md
│       ├── html-complete-reference-practical-guide.md
│       └── css-complete-reference-practical-guide.md
│
└── tools/                    # CLI utilities
    ├── add_doc.py            # CLI wizard — add a new doc to the hub
    ├── check_fences.py       # Markdown code-fence balance checker
    └── generate_icon.py      # App icon generator (SVG + ICO)
```

## How It Works

Each documentation page is a lightweight HTML shell that loads:

- **Markdown content** from `content/*.md` via `fetch()`
- **Rendering** via [marked.js](https://marked.js.org/) (Markdown → HTML)
- **Syntax highlighting** via [highlight.js](https://highlightjs.org/)
- **Shared renderer** (`docs-renderer.js`) — sidebar TOC, search, scroll-spy, code-copy buttons, and theme toggle

## Features

- Dark / light theme toggle (persisted in `localStorage`)
- Collapsible sidebar navigation (h1 → h4 depth)
- Full-text section search with keyboard shortcut (`/`)
- Reading progress bar
- Code block copy buttons
- Mobile-responsive layout
- Per-document colour themes
- Desktop app with integrated content manager
- Split-view live-preview markdown editor
- Category management with drag-reorder
- Activity log & storage stats dashboard

## Adding a New Documentation Page

**Desktop app:** click the **+** button in the toolbar, or open the Content Manager (`Ctrl+M`) and use the Dashboard's "Add Doc" action.

**CLI:**

```bash
python tools/add_doc.py path/to/your-guide.md
```

The wizard prompts for title, category, version, description, tags, and colours, then wires everything up automatically.

## Tools

| Tool | Purpose |
|---|---|
| `add_doc.py` | Interactive CLI wizard to add a new doc to the hub |
| `check_fences.py` | Validate Markdown code-fence balance |
| `generate_icon.py` | Generate app icon (SVG + ICO) |

## Requirements

- **Python 3.10+**
- **PyQt6** + **PyQt6-WebEngine** (desktop app)
- No npm, no build step — the site is pure static HTML/CSS/JS
