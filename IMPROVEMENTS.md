# Docs Website — Improvement Plan (Prioritized)

This file is the “what next” list for the docs site and the Python guide.

## ✅ Completed

- Fixed heading anchor injection order so “copy link to section” works reliably.
- Improved global search indexing by skipping fenced code blocks (less noise, better performance).
- Improved Python 3.14 guide accuracy + navigation (metadata header, corrected release wording/examples, clickable TOC).
- Added a Projects & Case Studies section with many standard-library-only projects + full solutions.
- Added a runnable Tkinter heat-loss calculator reference project: `examples/heat_loss_app/`.
- Added “Tutorial vs Reference” usage guidance + an Exercises section (with solutions) to support a learn→practice loop.
- Added track mini-index tables (Beginner/Intermediate/Advanced) with stable jump links.
- Added in-track Tutorial vs Reference signposting (mode markers + end-of-track checkpoints).
- Expanded exercises coverage with end-of-section drills + inline solutions for key chapters.
- Completed a standard-library-only sweep of the Python mega-page (removed remaining `requests` examples, removed pytest-heavy content in favor of `unittest`, replaced the `aiohttp` async demo with a stdlib approach).
- Deepened the heat-loss capstone app (summary screen, validated edit forms, text report export).
- Polished the heat-loss capstone app (room list shows per-room totals; report includes assumptions/units notes).

## 🔥 Next (High impact)

1. **Heat-loss capstone depth**
  - Optional further polish: add project-level unit assumptions (design temperatures, external conditions) and/or a simple “print preview” style report view.

## 🧹 Quality / Polish

- Reduce markdownlint noise in `site/content/python-3.14.md` (bare URLs, fence spacing, etc.).
  - Not required for runtime, but makes editing and reviewing easier.

## 🧪 Verification checklist

- `python tools/check_fences.py site/content/python-3.14.md`
- `python -m unittest examples.heat_loss_app.tests.test_calc`
- Smoke test the site renderer for:
  - TOC jump links
  - copy-link anchors
  - global search relevance
