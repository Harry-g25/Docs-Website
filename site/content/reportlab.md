# ReportLab — Complete Documentation & Reference Guide

**Version:** 4.2 (Latest)  
**Last Updated:** February 2026  
**Official Website:** <https://www.reportlab.com/>  
**PyPI:** <https://pypi.org/project/reportlab/>

---

## Table of Contents

<details open>
<summary><strong>Table of Contents — click to expand/collapse</strong></summary>

<nav aria-label="Table of contents">
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li>
            <a href="#installation--setup">Installation &amp; Setup</a>
            <ul>
                <li><a href="#basic-installation">Basic Installation</a></li>
                <li><a href="#verify-installation">Verify Installation</a></li>
                <li><a href="#optional-dependencies">Optional Dependencies</a></li>
                <li><a href="#platform-notes">Platform Notes</a></li>
            </ul>
        </li>
        <li>
            <a href="#quick-start--your-first-pdf">Quick Start — Your First PDF</a>
            <ul>
                <li><a href="#hello-world-pdf">Hello World PDF</a></li>
                <li><a href="#understanding-the-coordinate-system">Understanding the Coordinate System</a></li>
            </ul>
        </li>
        <li>
            <a href="#core-concepts">Core Concepts</a>
            <ul>
                <li><a href="#the-canvas">The Canvas</a></li>
                <li><a href="#units-of-measurement">Units of Measurement</a></li>
                <li><a href="#page-sizes">Page Sizes</a></li>
                <li><a href="#the-graphics-state">The Graphics State</a></li>
                <li><a href="#canvas-vs-platypus">Canvas vs Platypus</a></li>
            </ul>
        </li>
        <li>
            <a href="#canvas-operations">Canvas Operations</a>
            <ul>
                <li><a href="#drawing-text">Drawing Text</a></li>
                <li><a href="#drawing-lines--shapes">Drawing Lines &amp; Shapes</a></li>
                <li><a href="#drawing-rectangles--rounded-rectangles">Drawing Rectangles &amp; Rounded Rectangles</a></li>
                <li><a href="#drawing-circles--ellipses">Drawing Circles &amp; Ellipses</a></li>
                <li><a href="#drawing-paths">Drawing Paths</a></li>
                <li><a href="#fill--stroke-colors">Fill &amp; Stroke Colors</a></li>
                <li><a href="#line-styles--dash-patterns">Line Styles &amp; Dash Patterns</a></li>
                <li><a href="#canvas-transformations">Canvas Transformations</a></li>
                <li><a href="#clipping">Clipping</a></li>
                <li><a href="#multiple-pages">Multiple Pages</a></li>
            </ul>
        </li>
        <li>
            <a href="#working-with-text">Working with Text</a>
            <ul>
                <li><a href="#basic-text-drawing">Basic Text Drawing</a></li>
                <li><a href="#text-alignment">Text Alignment</a></li>
                <li><a href="#text-wrapping-with-textobject">Text Wrapping with textobject</a></li>
                <li><a href="#fonts--font-management">Fonts &amp; Font Management</a></li>
                <li><a href="#registering-truetype-fonts">Registering TrueType Fonts</a></li>
                <li><a href="#font-families--bold--italic">Font Families — Bold &amp; Italic</a></li>
                <li><a href="#unicode--international-text">Unicode &amp; International Text</a></li>
            </ul>
        </li>
        <li>
            <a href="#platypus-framework">Platypus Framework</a>
            <ul>
                <li><a href="#what-is-platypus">What is Platypus?</a></li>
                <li><a href="#simpledoctemplate">SimpleDocTemplate</a></li>
                <li><a href="#flowables">Flowables</a></li>
                <li><a href="#paragraph">Paragraph</a></li>
                <li><a href="#spacer">Spacer</a></li>
                <li><a href="#page-break">Page Break</a></li>
                <li><a href="#keep-together">Keep Together</a></li>
                <li><a href="#conditional-page-break">Conditional Page Break</a></li>
                <li><a href="#horizontal-rule-flowable">Horizontal Rule Flowable</a></li>
            </ul>
        </li>
        <li>
            <a href="#paragraph-styles">Paragraph Styles</a>
            <ul>
                <li><a href="#paragraphstyle-reference">ParagraphStyle Reference</a></li>
                <li><a href="#using-the-default-stylesheet">Using the Default Stylesheet</a></li>
                <li><a href="#custom-paragraph-styles">Custom Paragraph Styles</a></li>
                <li><a href="#inline-markup-in-paragraphs">Inline Markup in Paragraphs</a></li>
            </ul>
        </li>
        <li>
            <a href="#tables">Tables</a>
            <ul>
                <li><a href="#basic-table">Basic Table</a></li>
                <li><a href="#tablestyle-commands">TableStyle Commands</a></li>
                <li><a href="#spanning-cells">Spanning Cells</a></li>
                <li><a href="#alternating-row-colors">Alternating Row Colors</a></li>
                <li><a href="#tables-with-paragraphs">Tables with Paragraphs</a></li>
                <li><a href="#long-tables-across-pages">Long Tables Across Pages</a></li>
                <li><a href="#dynamic-tables-from-data">Dynamic Tables from Data</a></li>
            </ul>
        </li>
        <li>
            <a href="#images">Images</a>
            <ul>
                <li><a href="#inserting-images">Inserting Images</a></li>
                <li><a href="#image-sizing--aspect-ratio">Image Sizing &amp; Aspect Ratio</a></li>
                <li><a href="#images-in-platypus">Images in Platypus</a></li>
                <li><a href="#images-from-urls--bytes">Images from URLs &amp; Bytes</a></li>
            </ul>
        </li>
        <li>
            <a href="#page-layout--templates">Page Layout &amp; Templates</a>
            <ul>
                <li><a href="#headers--footers">Headers &amp; Footers</a></li>
                <li><a href="#page-numbers">Page Numbers</a></li>
                <li><a href="#multi-column-layouts">Multi-Column Layouts</a></li>
                <li><a href="#basedoctemplate--pagetemplate">BaseDocTemplate &amp; PageTemplate</a></li>
                <li><a href="#frame-objects">Frame Objects</a></li>
                <li><a href="#watermarks--backgrounds">Watermarks &amp; Backgrounds</a></li>
            </ul>
        </li>
        <li>
            <a href="#colors--drawing">Colors &amp; Drawing</a>
            <ul>
                <li><a href="#named-colors">Named Colors</a></li>
                <li><a href="#hex-colors">Hex Colors</a></li>
                <li><a href="#rgb--cmyk-colors">RGB &amp; CMYK Colors</a></li>
                <li><a href="#transparency--alpha">Transparency &amp; Alpha</a></li>
                <li><a href="#gradients">Gradients</a></li>
            </ul>
        </li>
        <li>
            <a href="#charts--graphs">Charts &amp; Graphs</a>
            <ul>
                <li><a href="#pie-charts">Pie Charts</a></li>
                <li><a href="#bar-charts">Bar Charts</a></li>
                <li><a href="#line-charts">Line Charts</a></li>
                <li><a href="#chart-legends">Chart Legends</a></li>
                <li><a href="#chart-customization">Chart Customization</a></li>
            </ul>
        </li>
        <li>
            <a href="#barcodes--qr-codes">Barcodes &amp; QR Codes</a>
            <ul>
                <li><a href="#code128-barcode">Code128 Barcode</a></li>
                <li><a href="#qr-codes">QR Codes</a></li>
                <li><a href="#barcodes-in-platypus">Barcodes in Platypus</a></li>
            </ul>
        </li>
        <li>
            <a href="#pdf-metadata--security">PDF Metadata &amp; Security</a>
            <ul>
                <li><a href="#setting-metadata">Setting Metadata</a></li>
                <li><a href="#pdf-encryption--passwords">PDF Encryption &amp; Passwords</a></li>
                <li><a href="#bookmarks--outlines">Bookmarks &amp; Outlines</a></li>
                <li><a href="#hyperlinks">Hyperlinks</a></li>
            </ul>
        </li>
        <li>
            <a href="#common-recipes">Common Recipes</a>
            <ul>
                <li><a href="#invoice-pdf">Invoice PDF</a></li>
                <li><a href="#multi-page-report-from-csv">Multi-Page Report from CSV</a></li>
                <li><a href="#certificate-generator">Certificate Generator</a></li>
                <li><a href="#letter--letterhead">Letter &amp; Letterhead</a></li>
            </ul>
        </li>
        <li>
            <a href="#best-practices--patterns">Best Practices &amp; Patterns</a>
            <ul>
                <li><a href="#project-structure">Project Structure</a></li>
                <li><a href="#reusable-styles">Reusable Styles</a></li>
                <li><a href="#performance-tips">Performance Tips</a></li>
                <li><a href="#memory-management">Memory Management</a></li>
            </ul>
        </li>
        <li>
            <a href="#troubleshooting--faq">Troubleshooting &amp; FAQ</a>
            <ul>
                <li><a href="#common-errors">Common Errors</a></li>
                <li><a href="#font-issues">Font Issues</a></li>
                <li><a href="#layout-debugging">Layout Debugging</a></li>
                <li><a href="#platform-specific-issues">Platform-Specific Issues</a></li>
                <li><a href="#frequently-asked-questions">Frequently Asked Questions</a></li>
            </ul>
        </li>
        <li><a href="#api-quick-reference">API Quick Reference</a></li>
        <li><a href="#summary">Summary</a></li>
    </ul>
</nav>

</details>

---

## Introduction

ReportLab is the **industry-standard open-source PDF generation library** for Python. It allows you to create complex, pixel-perfect PDF documents programmatically — from simple one-page letters to data-driven reports with hundreds of pages containing tables, charts, images, and custom graphics.

**Key Features:**

| Feature | Description |
| --- | --- |
| Canvas API | Low-level drawing: text, lines, shapes, images at exact coordinates |
| Platypus Framework | High-level "Page Layout and Typography Using Scripts" — automatic page flow |
| Tables & Grids | Powerful table generation with styling, spanning, and multi-page support |
| Charts & Graphs | Built-in pie, bar, line, scatter charts via `reportlab.graphics` |
| Fonts & Unicode | Full TrueType/OpenType font support, Unicode, and international text |
| Images | JPEG, PNG, GIF, SVG support with automatic sizing |
| Barcodes & QR Codes | Code128, Code39, EAN, QR codes built in |
| PDF Features | Encryption, bookmarks, hyperlinks, metadata, form fields |
| Cross-Platform | Works on Windows, macOS, Linux — pure Python with C extensions for speed |

**When to use ReportLab:**

- Generating invoices, receipts, or financial statements
- Creating data-driven reports from databases or APIs
- Building certificates, letters, or form-filled documents
- Producing catalogs, brochures, or documentation PDFs
- Any scenario where you need precise control over PDF output

---

## How to Use This Guide

This guide mixes two kinds of code blocks:

- **Runnable examples** (full scripts) — these have an **Output** section underneath, including an embedded PDF preview when the code generates a PDF.
- **Snippets** (API fragments) — these illustrate one concept and may omit setup (e.g. `c = canvas.Canvas(...)`). Snippets usually won’t have an output preview.

> **About the previews:** the PDFs you see embedded in this page are **pre-generated** from the runnable examples, so you can learn visually without running anything.

### Debugging Toolkit (Read This When Something Looks “Wrong”)

If your generated PDF is blank / missing content / misaligned, check these first:

- **Did you call `save()` / `build()`?** Canvas requires `c.save()`. Platypus requires `doc.build(story)`.
- **Are you drawing off-page?** PDF origin is bottom-left; `y` increases upward.
- **Units:** coordinates are in points (1 inch = 72 points). Mixing `cm`/`inch` with raw numbers is a common source of layout drift.
- **Paths & state:** if you use `saveState()`, always pair it with `restoreState()`.
- **Platypus layout:** enable `showBoundary=1` to see frames and margins when debugging.

---

## Installation & Setup

### Basic Installation

Install ReportLab via pip:

```bash
pip install reportlab
```

For the latest development version:

```bash
pip install reportlab --upgrade
```

To install with all optional extras:

```bash
pip install reportlab[accel]
```

### Verify Installation

```python
import reportlab
print(reportlab.Version)
# Output: 4.2
```

Output:
```output
4.2
```

Test that PDF generation works:

```python
from reportlab.pdfgen import canvas

c = canvas.Canvas("test.pdf")
c.drawString(100, 750, "ReportLab is working!")
c.save()
print("✓ test.pdf created successfully")
```

Output:
```output
✓ test.pdf created successfully
```

- Download: [test.pdf](../assets/reportlab/test.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/test.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/test.pdf">test.pdf</a></p>
</object>

</details>

### Optional Dependencies

| Package | Purpose | Install |
|---------|---------|---------|
| `Pillow` | Advanced image handling (PNG, TIFF, etc.) | `pip install Pillow` |
| `rlPyCairo` | Improved rendering for SVG/graphics | `pip install rlPyCairo` |
| `preppy` | ReportLab's templating system | `pip install preppy` |
| `pyRXP` | Fast XML parsing for RML | `pip install pyRXP` |
| `matplotlib` | Integration for matplotlib charts | `pip install matplotlib` |

### Platform Notes

**Windows:**
- Installs cleanly with pip. Pre-built wheels are available.
- TrueType fonts in `C:\Windows\Fonts` are auto-discovered.

**macOS:**
- Use `pip install reportlab`. Xcode command line tools may be needed for C extensions.
- Fonts in `/Library/Fonts` and `~/Library/Fonts` are accessible.

**Linux:**
- May need `python3-dev` and build tools: `sudo apt install python3-dev build-essential`
- Install FreeType headers: `sudo apt install libfreetype6-dev`

---

## Quick Start — Your First PDF

### Hello World PDF

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Create a canvas — this is the PDF document
c = canvas.Canvas("hello.pdf", pagesize=A4)
width, height = A4  # 595.27, 841.89 points

# Draw text at position (x=100, y=750) from bottom-left
c.setFont("Helvetica", 24)
c.drawString(100, 750, "Hello, ReportLab!")

# Draw a sub-heading
c.setFont("Helvetica", 14)
c.drawString(100, 710, "This is your first PDF document.")

# Draw a line
c.setStrokeColorRGB(0.2, 0.3, 0.7)
c.setLineWidth(2)
c.line(100, 700, 495, 700)

# Draw a rectangle
c.setFillColorRGB(0.9, 0.95, 1.0)
c.setStrokeColorRGB(0.2, 0.3, 0.7)
c.roundRect(100, 600, 395, 80, 10, fill=1)

# Draw text inside the rectangle
c.setFillColorRGB(0, 0, 0)
c.setFont("Helvetica", 12)
c.drawString(120, 655, "ReportLab gives you complete control over")
c.drawString(120, 638, "every pixel of your PDF output.")
c.drawString(120, 618, "Coordinates start from the bottom-left corner.")

# Save the PDF
c.save()
print("hello.pdf created!")
```

Output:
```output
hello.pdf created!
```

- Download: [hello.pdf](../assets/reportlab/hello.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/hello.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/hello.pdf">hello.pdf</a></p>
</object>

</details>

<details>
<summary>Try it (quick exercise)</summary>

- Change the page size to `LETTER` and notice how the available drawing area changes.
- Add a second page with `c.showPage()` and draw a different heading on page 2.
- Move the rectangle to the top of the page by using `height - y` style calculations.

</details>

### Understanding the Coordinate System

ReportLab uses a **bottom-left origin** coordinate system, just like PostScript and PDF natively:

```
(0, height) ─────────────────── (width, height)
     │                                │
     │          PDF Page              │
     │                                │
     │    ● (100, 600)                │
     │                                │
(0, 0) ───────────────────────── (width, 0)
```

- **x** increases left → right
- **y** increases bottom → top
- Units are in **points** (1 point = 1/72 inch)

> **Tip:** If you're used to top-left coordinate systems (like HTML), you'll need to flip your y-thinking. Use `height - y` to convert from top-down coordinates.

---

## Core Concepts

### The Canvas

The `Canvas` is the fundamental object for drawing PDF content. Think of it as a blank sheet of paper with an invisible pen:

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("output.pdf", pagesize=A4)

# Draw things...
c.drawString(100, 700, "Text on page 1")

# Move to next page
c.showPage()
c.drawString(100, 700, "Text on page 2")

# Finalize and save
c.save()
```

- Download: [output.pdf](../assets/reportlab/output.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/output.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/output.pdf">output.pdf</a></p>
</object>

</details>

**Canvas Constructor Arguments:**

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `filename` | str | (required) | Output file path or file-like object |
| `pagesize` | tuple | `A4` | `(width, height)` in points |
| `bottomup` | int | `1` | 1 = origin at bottom-left; 0 = top-left |
| `pageCompression` | int | `0` | 1 = compress page streams |
| `invariant` | int | `None` | For reproducible output (testing) |
| `verbosity` | int | `0` | Logging verbosity level |
| `encrypt` | obj | `None` | Encryption object for password protection |
| `cropMarks` | bool | `None` | Show crop marks for printing |
| `pdfVersion` | str | `None` | Force specific PDF version |

### Units of Measurement

ReportLab works in **points** by default. Use the `units` module for convenience:

```python
from reportlab.lib.units import inch, cm, mm, pica

# All of these are in points:
print(1*inch)    # 72.0
print(1*cm)      # 28.346...
print(1*mm)      # 2.834...
print(1*pica)    # 12.0

# Usage example:
c.drawString(1*inch, 10*inch, "One inch from left, 10 inches from bottom")
c.rect(2*cm, 15*cm, 5*cm, 3*cm)  # Rectangle at 2cm, 15cm — 5cm wide, 3cm tall
```

**Conversion table:**

| Unit | Points | Inches | cm |
|------|--------|--------|-------|
| 1 point | 1 | 0.01389 | 0.03528 |
| 1 inch | 72 | 1 | 2.54 |
| 1 cm | 28.35 | 0.3937 | 1 |
| 1 mm | 2.835 | 0.03937 | 0.1 |

### Page Sizes

Common page sizes are provided in `reportlab.lib.pagesizes`:

```python
from reportlab.lib.pagesizes import (
    A4, A3, A5, A6,
    LETTER, LEGAL, TABLOID,
    landscape, portrait
)

# A4 portrait (default)
width, height = A4  # (595.27, 841.89)

# A4 landscape
width, height = landscape(A4)  # (841.89, 595.27)

# Letter size (US)
width, height = LETTER  # (612, 792)

# Custom page size: 6 x 4 inches
from reportlab.lib.units import inch
custom_size = (6*inch, 4*inch)
c = canvas.Canvas("custom.pdf", pagesize=custom_size)
```

### The Graphics State

The Canvas maintains a **graphics state** — settings like current font, colors, line width, and transformations. You can save and restore it:

```python
c = canvas.Canvas("state_demo.pdf")

# Save current state
c.saveState()

# Modify state
c.setFont("Helvetica-Bold", 20)
c.setFillColorRGB(1, 0, 0)
c.drawString(100, 700, "Bold Red Text")

# Restore previous state (font and color revert)
c.restoreState()
c.drawString(100, 670, "Back to defaults")

c.save()
```

- Download: [state_demo.pdf](../assets/reportlab/state_demo.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/state_demo.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/state_demo.pdf">state_demo.pdf</a></p>
</object>

</details>

> **Important:** Always pair `saveState()` with `restoreState()`. Unmatched calls will cause errors.

### Canvas vs Platypus

| Feature | Canvas | Platypus |
|---------|--------|----------|
| **Level** | Low-level | High-level |
| **Control** | Pixel-perfect positioning | Automatic flow layout |
| **Page breaks** | Manual (`showPage()`) | Automatic |
| **Best for** | Custom graphics, forms | Reports, documents, articles |
| **Learning curve** | Lower | Higher |
| **Flexibility** | Maximum | Constrained by framework |

> **Recommendation:** Use **Platypus** for most document generation. Use **Canvas** for custom graphics, backgrounds, or when you need pixel-perfect control.

---

## Canvas Operations

### Drawing Text

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("text_demo.pdf", pagesize=A4)
w, h = A4

# Basic text
c.setFont("Helvetica", 16)
c.drawString(72, h - 72, "drawString: Left-aligned text")

# Centered text
c.drawCentredString(w/2, h - 110, "drawCentredString: Centered on page")

# Right-aligned text
c.drawRightString(w - 72, h - 148, "drawRightString: Right-aligned")

# Rotated text
c.saveState()
c.translate(72, h - 250)
c.rotate(45)
c.drawString(0, 0, "Rotated 45 degrees!")
c.restoreState()

# Text with different fonts
fonts = ["Helvetica", "Helvetica-Bold", "Helvetica-Oblique",
         "Times-Roman", "Times-Bold", "Courier", "Courier-Bold"]

y = h - 320
for font in fonts:
    c.setFont(font, 14)
    c.drawString(72, y, f"{font}: The quick brown fox jumps over the lazy dog")
    y -= 24

c.save()
```

- Download: [text_demo.pdf](../assets/reportlab/text_demo.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/text_demo.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/text_demo.pdf">text_demo.pdf</a></p>
</object>

</details>

### Drawing Lines & Shapes

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

c = canvas.Canvas("shapes_demo.pdf", pagesize=A4)
w, h = A4

# Simple line
c.setStrokeColorRGB(0, 0, 0)
c.setLineWidth(1)
c.line(2*cm, h - 3*cm, 19*cm, h - 3*cm)

# Thick colored line
c.setStrokeColorRGB(0.2, 0.4, 0.8)
c.setLineWidth(4)
c.line(2*cm, h - 4*cm, 19*cm, h - 4*cm)

# Dashed line
c.setDash(6, 3)  # 6pt dash, 3pt gap
c.line(2*cm, h - 5*cm, 19*cm, h - 5*cm)
c.setDash()  # Reset to solid

# Polyline (connected lines)
c.setStrokeColorRGB(0.8, 0.2, 0.2)
c.setLineWidth(2)
path = c.beginPath()
path.moveTo(2*cm, h - 8*cm)
path.lineTo(6*cm, h - 6*cm)
path.lineTo(10*cm, h - 8*cm)
path.lineTo(14*cm, h - 6*cm)
path.lineTo(18*cm, h - 8*cm)
c.drawPath(path)

c.save()
```

- Download: [shapes_demo.pdf](../assets/reportlab/shapes_demo.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/shapes_demo.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/shapes_demo.pdf">shapes_demo.pdf</a></p>
</object>

</details>

### Drawing Rectangles & Rounded Rectangles

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

c = canvas.Canvas("rectangles.pdf", pagesize=A4)
w, h = A4

# Simple rectangle (stroke only)
c.rect(2*cm, h - 5*cm, 8*cm, 3*cm)

# Filled rectangle
c.setFillColorRGB(0.85, 0.92, 1.0)
c.setStrokeColorRGB(0.2, 0.4, 0.8)
c.rect(12*cm, h - 5*cm, 6*cm, 3*cm, fill=1)

# Rounded rectangle
c.setFillColorRGB(1.0, 0.95, 0.85)
c.setStrokeColorRGB(0.8, 0.5, 0.1)
c.roundRect(2*cm, h - 10*cm, 8*cm, 3*cm, radius=10, fill=1)

# Rectangle with no stroke
c.setFillColorRGB(0.9, 0.85, 1.0)
c.setStrokeColorRGB(0.9, 0.85, 1.0)
c.roundRect(12*cm, h - 10*cm, 6*cm, 3*cm, radius=15, fill=1, stroke=0)

c.save()
```

- Download: [rectangles.pdf](../assets/reportlab/rectangles.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/rectangles.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/rectangles.pdf">rectangles.pdf</a></p>
</object>

</details>

### Drawing Circles & Ellipses

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

c = canvas.Canvas("circles.pdf", pagesize=A4)
w, h = A4

# Circle (using ellipse with equal width/height)
c.setStrokeColorRGB(0.2, 0.6, 0.3)
c.setFillColorRGB(0.85, 1.0, 0.9)
c.circle(6*cm, h - 5*cm, 2*cm, fill=1)

# Ellipse
c.setStrokeColorRGB(0.6, 0.2, 0.6)
c.setFillColorRGB(0.95, 0.85, 1.0)
c.ellipse(11*cm, h - 7*cm, 18*cm, h - 3*cm, fill=1)

# Wedge (pie slice) — part of a circle
c.setFillColorRGB(1.0, 0.9, 0.8)
c.setStrokeColorRGB(0.8, 0.4, 0.1)
c.wedge(3*cm, h - 14*cm, 9*cm, h - 8*cm, startAng=0, extent=120, fill=1)

c.save()
```

- Download: [circles.pdf](../assets/reportlab/circles.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/circles.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/circles.pdf">circles.pdf</a></p>
</object>

</details>

### Drawing Paths

Paths let you create complex custom shapes:

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

c = canvas.Canvas("paths.pdf", pagesize=A4)
w, h = A4

# Custom shape — a star
p = c.beginPath()
import math
cx, cy, r = 10*cm, h - 8*cm, 3*cm
for i in range(5):
    angle = math.radians(90 + i * 144)
    x = cx + r * math.cos(angle)
    y = cy + r * math.sin(angle)
    if i == 0:
        p.moveTo(x, y)
    else:
        p.lineTo(x, y)
p.close()

c.setFillColorRGB(1.0, 0.85, 0.0)
c.setStrokeColorRGB(0.8, 0.5, 0.0)
c.setLineWidth(2)
c.drawPath(p, fill=1)

# Triangle
p2 = c.beginPath()
p2.moveTo(3*cm, h - 16*cm)
p2.lineTo(6*cm, h - 12*cm)
p2.lineTo(9*cm, h - 16*cm)
p2.close()

c.setFillColorRGB(0.8, 0.9, 1.0)
c.setStrokeColorRGB(0.2, 0.4, 0.8)
c.drawPath(p2, fill=1)

# Bezier curve
p3 = c.beginPath()
p3.moveTo(12*cm, h - 16*cm)
p3.curveTo(13*cm, h - 12*cm, 16*cm, h - 12*cm, 18*cm, h - 16*cm)
c.setStrokeColorRGB(0.8, 0.2, 0.2)
c.setLineWidth(3)
c.drawPath(p3)

c.save()
```

- Download: [paths.pdf](../assets/reportlab/paths.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/paths.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/paths.pdf">paths.pdf</a></p>
</object>

</details>

### Fill & Stroke Colors

```python
from reportlab.pdfgen import canvas
from reportlab.lib.colors import (
    red, blue, green, black, white, gray,
    HexColor, CMYKColor, Color
)
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("colors_demo.pdf", pagesize=A4)
w, h = A4

# Named colors
c.setFillColor(red)
c.rect(72, h - 100, 60, 40, fill=1)

c.setFillColor(blue)
c.rect(142, h - 100, 60, 40, fill=1)

c.setFillColor(green)
c.rect(212, h - 100, 60, 40, fill=1)

# RGB (values 0.0 to 1.0)
c.setFillColorRGB(0.95, 0.3, 0.1)
c.rect(72, h - 160, 60, 40, fill=1)

# Hex color
c.setFillColor(HexColor("#6366f1"))
c.rect(142, h - 160, 60, 40, fill=1)

# CMYK color
cmyk = CMYKColor(0.1, 0.8, 0.9, 0.0)
c.setFillColor(cmyk)
c.rect(212, h - 160, 60, 40, fill=1)

# Transparency (alpha)
c.setFillColor(Color(0, 0, 1, alpha=0.3))
c.rect(72, h - 220, 200, 40, fill=1)

c.save()
```

- Download: [colors_demo.pdf](../assets/reportlab/colors_demo.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/colors_demo.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/colors_demo.pdf">colors_demo.pdf</a></p>
</object>

</details>

### Line Styles & Dash Patterns

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("line_styles.pdf", pagesize=A4)
w, h = A4
x1, x2 = 72, 500

# Solid line
c.setLineWidth(1)
c.line(x1, h - 80, x2, h - 80)
c.drawString(x1, h - 75, "Solid (default)")

# Thick line
c.setLineWidth(4)
c.line(x1, h - 120, x2, h - 120)
c.drawString(x1, h - 115, "Thick (4pt)")

# Dashed
c.setLineWidth(1)
c.setDash(6, 3)
c.line(x1, h - 160, x2, h - 160)
c.drawString(x1, h - 155, "Dashed (6, 3)")

# Dot-dash
c.setDash([1, 2, 6, 2])
c.line(x1, h - 200, x2, h - 200)
c.drawString(x1, h - 195, "Dot-dash pattern")

# Reset dash
c.setDash()

# Line cap styles
c.setLineWidth(8)

# Butt cap (default)
c.setLineCap(0)
c.line(x1, h - 260, x2, h - 260)
c.setFont("Helvetica", 10)
c.drawString(x1, h - 248, "Butt cap (0)")

# Round cap
c.setLineCap(1)
c.line(x1, h - 300, x2, h - 300)
c.drawString(x1, h - 288, "Round cap (1)")

# Square cap
c.setLineCap(2)
c.line(x1, h - 340, x2, h - 340)
c.drawString(x1, h - 328, "Square cap (2)")

# Line join styles
c.setLineWidth(6)
c.setLineCap(0)

# Miter join (default)
c.setLineJoin(0)
p = c.beginPath()
p.moveTo(x1, h - 400); p.lineTo(200, h - 370); p.lineTo(300, h - 400)
c.drawPath(p)
c.setFont("Helvetica", 10)
c.drawString(x1, h - 415, "Miter join (0)")

# Round join
c.setLineJoin(1)
p = c.beginPath()
p.moveTo(x1, h - 460); p.lineTo(200, h - 430); p.lineTo(300, h - 460)
c.drawPath(p)
c.drawString(x1, h - 475, "Round join (1)")

# Bevel join
c.setLineJoin(2)
p = c.beginPath()
p.moveTo(x1, h - 520); p.lineTo(200, h - 490); p.lineTo(300, h - 520)
c.drawPath(p)
c.drawString(x1, h - 535, "Bevel join (2)")

c.save()
```

- Download: [line_styles.pdf](../assets/reportlab/line_styles.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/line_styles.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/line_styles.pdf">line_styles.pdf</a></p>
</object>

</details>

### Canvas Transformations

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

c = canvas.Canvas("transforms.pdf", pagesize=A4)
w, h = A4

# translate() — move the origin
c.saveState()
c.translate(5*cm, h - 6*cm)
c.rect(0, 0, 3*cm, 2*cm, fill=0)
c.drawString(5, 10, "Translated")
c.restoreState()

# rotate() — rotate around origin
c.saveState()
c.translate(12*cm, h - 6*cm)
c.rotate(30)
c.rect(0, 0, 3*cm, 2*cm, fill=0)
c.drawString(5, 10, "Rotated 30°")
c.restoreState()

# scale() — resize
c.saveState()
c.translate(5*cm, h - 12*cm)
c.scale(1.5, 1.5)
c.rect(0, 0, 2*cm, 1.5*cm, fill=0)
c.drawString(5, 10, "Scaled 1.5x")
c.restoreState()

# skew() — shear transformation
c.saveState()
c.translate(12*cm, h - 12*cm)
c.skew(15, 0)
c.rect(0, 0, 3*cm, 2*cm, fill=0)
c.drawString(5, 10, "Skewed")
c.restoreState()

c.save()
```

- Download: [transforms.pdf](../assets/reportlab/transforms.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/transforms.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/transforms.pdf">transforms.pdf</a></p>
</object>

</details>

### Clipping

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

c = canvas.Canvas("clipping.pdf", pagesize=A4)
w, h = A4

# Circular clipping region
c.saveState()
p = c.beginPath()
p.circle(10*cm, h - 8*cm, 3*cm)
c.clipPath(p, stroke=0)

# Draw a grid that will be clipped to the circle
c.setStrokeColorRGB(0.2, 0.4, 0.8)
for i in range(0, 25):
    x = (5 + i * 0.5) * cm
    c.line(x, h - 14*cm, x, h - 2*cm)
    y = (h - 14*cm) + i * 0.5 * cm
    c.line(5*cm, y, 15*cm, y)

c.restoreState()

c.save()
```

- Download: [clipping.pdf](../assets/reportlab/clipping.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/clipping.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/clipping.pdf">clipping.pdf</a></p>
</object>

</details>

### Multiple Pages

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("multipage.pdf", pagesize=A4)
w, h = A4

for page_num in range(1, 6):
    c.setFont("Helvetica-Bold", 24)
    c.drawString(72, h - 72, f"Page {page_num} of 5")

    c.setFont("Helvetica", 12)
    c.drawString(72, h - 110, f"This is the content for page {page_num}.")

    # Page number at bottom
    c.setFont("Helvetica", 9)
    c.drawCentredString(w/2, 30, f"— {page_num} —")

    if page_num < 5:
        c.showPage()  # Start a new page

c.save()
print("multipage.pdf created with 5 pages")
```

```output
multipage.pdf created with 5 pages
```

- Download: [multipage.pdf](../assets/reportlab/multipage.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/multipage.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/multipage.pdf">multipage.pdf</a></p>
</object>

</details>

---

## Working with Text

### Basic Text Drawing

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("text_basics.pdf", pagesize=A4)
w, h = A4

# drawString — anchored at baseline-left
c.setFont("Helvetica", 14)
c.drawString(72, h - 72, "This is drawString (left-aligned)")

# drawCentredString — anchored at baseline-center
c.drawCentredString(w/2, h - 110, "This is drawCentredString (centered)")

# drawRightString — anchored at baseline-right
c.drawRightString(w - 72, h - 148, "This is drawRightString (right)")

c.save()
```

- Download: [text_basics.pdf](../assets/reportlab/text_basics.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/text_basics.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/text_basics.pdf">text_basics.pdf</a></p>
</object>

</details>

### Text Alignment

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("text_align.pdf", pagesize=A4)
w, h = A4

# Draw a reference line at center
c.setDash(2, 2)
c.setStrokeColorRGB(0.7, 0.7, 0.7)
c.line(w/2, h, w/2, 0)
c.setDash()

c.setFont("Helvetica", 14)

# Left aligned at center
c.drawString(w/2, h - 100, "← Left from center")

# Centered at center
c.drawCentredString(w/2, h - 140, "Centered on center")

# Right aligned at center
c.drawRightString(w/2, h - 180, "Right to center →")

c.save()
```

- Download: [text_align.pdf](../assets/reportlab/text_align.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/text_align.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/text_align.pdf">text_align.pdf</a></p>
</object>

</details>

### Text Wrapping with textobject

For multi-line text, use `beginText()`:

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("textobject.pdf", pagesize=A4)
w, h = A4

# Create a text object
text = c.beginText(72, h - 72)
text.setFont("Helvetica", 12)
text.setFillColorRGB(0, 0, 0)

# Set leading (line spacing) — default is 1.2x font size
text.setLeading(18)

# Add lines of text
paragraphs = [
    "ReportLab's TextObject is ideal for multi-line text blocks.",
    "Each call to textLine() advances to the next line automatically.",
    "",
    "You can change fonts and colors mid-stream:",
]

for line in paragraphs:
    text.textLine(line)

# Change font mid-text
text.setFont("Helvetica-Bold", 12)
text.setFillColorRGB(0.2, 0.4, 0.8)
text.textLine("This line is bold and blue.")

text.setFont("Courier", 11)
text.setFillColorRGB(0.4, 0.4, 0.4)
text.textLine("And this is in Courier.")

# Draw the text object onto the canvas
c.drawText(text)
c.save()
```

- Download: [textobject.pdf](../assets/reportlab/textobject.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/textobject.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/textobject.pdf">textobject.pdf</a></p>
</object>

</details>

### Fonts & Font Management

ReportLab includes 14 built-in PDF fonts (the "PDF Base 14"):

```python
# The 14 standard PDF fonts (always available, no embedding needed):
standard_fonts = [
    "Courier",
    "Courier-Bold",
    "Courier-Oblique",
    "Courier-BoldOblique",
    "Helvetica",
    "Helvetica-Bold",
    "Helvetica-Oblique",
    "Helvetica-BoldOblique",
    "Times-Roman",
    "Times-Bold",
    "Times-Italic",
    "Times-BoldItalic",
    "Symbol",
    "ZapfDingbats",
]
```

List all available fonts:

```python
from reportlab.pdfgen import canvas

c = canvas.Canvas("font_list.pdf")
c.setFont("Helvetica-Bold", 16)
c.drawString(72, 750, "Available Standard Fonts")

y = 710
for font_name in standard_fonts:
    c.setFont(font_name, 12)
    c.drawString(72, y, f"{font_name}: The quick brown fox jumps over the lazy dog")
    y -= 20

c.save()
```

- Download: [font_list.pdf](../assets/reportlab/font_list.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/font_list.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/font_list.pdf">font_list.pdf</a></p>
</object>

</details>

### Registering TrueType Fonts

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register a single TTF font
pdfmetrics.registerFont(TTFont("MyFont", "path/to/MyFont-Regular.ttf"))

# Now use it
from reportlab.pdfgen import canvas
c = canvas.Canvas("custom_font.pdf")
c.setFont("MyFont", 16)
c.drawString(72, 700, "This text uses MyFont!")
c.save()
```

### Font Families — Bold & Italic

Register a complete font family so ReportLab can find bold/italic variants:

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register each variant
pdfmetrics.registerFont(TTFont("Roboto", "Roboto-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Roboto-Bold", "Roboto-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Roboto-Italic", "Roboto-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Roboto-BoldItalic", "Roboto-BoldItalic.ttf"))

# Register the family mapping
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily(
    "Roboto",
    normal="Roboto",
    bold="Roboto-Bold",
    italic="Roboto-Italic",
    boldItalic="Roboto-BoldItalic"
)
```

### Unicode & International Text

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Register a Unicode-capable font
pdfmetrics.registerFont(TTFont("NotoSans", "NotoSans-Regular.ttf"))

c = canvas.Canvas("unicode.pdf")
c.setFont("NotoSans", 14)

# Various languages
c.drawString(72, 700, "English: Hello, World!")
c.drawString(72, 670, "Chinese: 你好世界")
c.drawString(72, 640, "Japanese: こんにちは世界")
c.drawString(72, 610, "Korean: 안녕하세요 세계")
c.drawString(72, 580, "Arabic: مرحبا بالعالم")
c.drawString(72, 550, "Russian: Привет мир")
c.drawString(72, 520, "Emoji: 🎉 📄 ✅ ❤️")

c.save()
```

> **Note:** Emoji and complex scripts require a font that includes those glyphs. Noto Sans or Noto Emoji are good choices.

---

## Platypus Framework

### What is Platypus?

**Platypus** (Page Layout and Typography Using Scripts) is ReportLab's high-level layout engine. Instead of specifying exact pixel positions, you build a list of **Flowables** (paragraphs, tables, images, spacers) and Platypus automatically flows them across pages.

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Create the document
doc = SimpleDocTemplate("platypus_intro.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []  # List of flowables

# Add content
story.append(Paragraph("My First Platypus Document", styles["Title"]))
story.append(Spacer(1, 20))
story.append(Paragraph(
    "Platypus automatically handles page breaks, text wrapping, "
    "and layout for you. Just add flowable objects to the story "
    "and call build().",
    styles["BodyText"]
))
story.append(Spacer(1, 12))
story.append(Paragraph(
    "This is a second paragraph. It will wrap naturally within "
    "the page margins and overflow to the next page if needed.",
    styles["BodyText"]
))

# Build the PDF
doc.build(story)
print("platypus_intro.pdf created!")
```

```output
platypus_intro.pdf created!
```

- Download: [platypus_intro.pdf](../assets/reportlab/platypus_intro.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/platypus_intro.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/platypus_intro.pdf">platypus_intro.pdf</a></p>
</object>

</details>

### SimpleDocTemplate

`SimpleDocTemplate` is the easiest way to create a Platypus document:

```python
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm

# Basic usage
doc = SimpleDocTemplate("output.pdf", pagesize=A4)

# With custom margins
doc = SimpleDocTemplate(
    "output.pdf",
    pagesize=A4,
    leftMargin=2*cm,
    rightMargin=2*cm,
    topMargin=2.5*cm,
    bottomMargin=2.5*cm,
    title="My Report",
    author="John Doe",
    subject="Monthly Report",
)

# Landscape
doc = SimpleDocTemplate("landscape.pdf", pagesize=landscape(A4))
```

**SimpleDocTemplate Arguments:**

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `filename` | str | (required) | Output file path |
| `pagesize` | tuple | `A4` | Page dimensions (width, height) |
| `leftMargin` | float | 72 (1 inch) | Left margin in points |
| `rightMargin` | float | 72 | Right margin |
| `topMargin` | float | 72 | Top margin |
| `bottomMargin` | float | 72 | Bottom margin |
| `title` | str | `None` | PDF title metadata |
| `author` | str | `None` | PDF author metadata |
| `subject` | str | `None` | PDF subject metadata |
| `showBoundary` | int | 0 | 1 = show frame boundaries (debugging) |

### Flowables

Flowables are objects that "flow" into a document. Key flowables:

| Flowable | Description |
|----------|-------------|
| `Paragraph` | Styled text with inline markup |
| `Spacer` | Vertical whitespace |
| `Table` | Data tables with styling |
| `Image` | Images (JPEG, PNG, etc.) |
| `PageBreak` | Force a new page |
| `KeepTogether` | Prevent page break inside a group |
| `CondPageBreak` | Break only if not enough space |
| `HRFlowable` | Horizontal rule line |
| `ListFlowable` | Ordered/unordered lists |
| `Preformatted` | Preformatted monospace text |
| `XPreformatted` | Preformatted with inline markup |

### Paragraph

The most common flowable. Supports inline HTML-like markup:

```python
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

# Basic paragraph
p1 = Paragraph("This is a simple paragraph.", styles["BodyText"])

# With inline markup
p2 = Paragraph(
    "Text can be <b>bold</b>, <i>italic</i>, <u>underlined</u>, "
    "or <font color='red'>colored</font>.",
    styles["BodyText"]
)

# With links
p3 = Paragraph(
    'Visit <a href="https://www.reportlab.com/" color="blue">ReportLab</a> for more.',
    styles["BodyText"]
)

# With inline code
p4 = Paragraph(
    'Use <font face="Courier" size="10" color="#6366f1">canvas.drawString()</font> '
    'for low-level text drawing.',
    styles["BodyText"]
)

# Bullet point
p5 = Paragraph(
    "This is a bullet point",
    styles["Bullet"]
)
```

**Supported Paragraph Markup Tags:**

| Tag | Description | Example |
|-----|-------------|---------|
| `<b>` | Bold | `<b>bold text</b>` |
| `<i>` | Italic | `<i>italic text</i>` |
| `<u>` | Underline | `<u>underlined</u>` |
| `<strike>` | Strikethrough | `<strike>deleted</strike>` |
| `<super>` | Superscript | `x<super>2</super>` |
| `<sub>` | Subscript | `H<sub>2</sub>O` |
| `<font>` | Font properties | `<font face="Courier" size="10" color="red">text</font>` |
| `<a>` | Hyperlink | `<a href="https://example.com">link</a>` |
| `<br/>` | Line break | `line1<br/>line2` |
| `<img>` | Inline image | `<img src="icon.png" width="16" height="16"/>` |
| `<seq>` | Auto-numbering | `<seq id="items"/>. Item` |

### Spacer

Add vertical whitespace between flowables:

```python
from reportlab.platypus import Spacer
from reportlab.lib.units import cm

# 1cm of vertical space
story.append(Spacer(1, 1*cm))

# 20 points of space
story.append(Spacer(1, 20))
```

### Page Break

```python
from reportlab.platypus import PageBreak

story.append(PageBreak())  # Force new page
```

### Keep Together

Prevent a group of flowables from being split across pages:

```python
from reportlab.platypus import KeepTogether, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

# These elements will stay on the same page
group = KeepTogether([
    Paragraph("Section Title", styles["Heading2"]),
    Spacer(1, 6),
    Paragraph("This paragraph will appear on the same page as the title above.", styles["BodyText"]),
    Spacer(1, 6),
    Paragraph("And so will this one.", styles["BodyText"]),
])

story.append(group)
```

### Conditional Page Break

Break to a new page only if there isn't enough space remaining:

```python
from reportlab.platypus import CondPageBreak
from reportlab.lib.units import cm

# Start a new page only if less than 5cm of space remains
story.append(CondPageBreak(5*cm))
```

### Horizontal Rule Flowable

```python
from reportlab.platypus import HRFlowable
from reportlab.lib.colors import HexColor

# Simple horizontal rule
story.append(HRFlowable(
    width="100%",
    thickness=1,
    color=HexColor("#e2e8f0"),
    spaceBefore=12,
    spaceAfter=12,
))

# Thicker colored rule
story.append(HRFlowable(
    width="60%",
    thickness=3,
    color=HexColor("#6366f1"),
    hAlign="CENTER",
    spaceBefore=20,
    spaceAfter=20,
))
```

---

## Paragraph Styles

### ParagraphStyle Reference

```python
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

style = ParagraphStyle(
    name="CustomBody",
    fontName="Helvetica",
    fontSize=11,
    leading=15,           # Line spacing (usually fontSize * 1.2–1.5)
    alignment=TA_JUSTIFY, # TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
    textColor=HexColor("#1e293b"),
    leftIndent=0,
    rightIndent=0,
    firstLineIndent=0,    # Indent the first line of each paragraph
    spaceBefore=6,        # Space above the paragraph
    spaceAfter=12,        # Space below the paragraph
    bulletIndent=0,
    bulletFontName="Helvetica",
    bulletFontSize=10,
    bulletColor=HexColor("#000000"),
    backColor=None,       # Background color
    borderWidth=0,
    borderColor=None,
    borderPadding=0,
    borderRadius=None,
    wordWrap="CJK",       # Word wrap mode
    allowWidows=1,        # Minimum lines at top of page
    allowOrphans=0,       # Minimum lines at bottom of page
)
```

### Using the Default Stylesheet

```python
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

# Available built-in styles:
# styles["Title"]       — Large bold title
# styles["Heading1"]    — H1 heading
# styles["Heading2"]    — H2 heading
# styles["Heading3"]    — H3 heading
# styles["Heading4"]    — H4 heading
# styles["Normal"]      — Normal body text
# styles["BodyText"]    — Body text with extra spacing
# styles["Italic"]      — Italic text
# styles["Bullet"]      — Bullet list item
# styles["Definition"]  — Definition list style
# styles["Code"]        — Monospaced code style

# Example: Use Title style
from reportlab.platypus import Paragraph
title = Paragraph("Document Title", styles["Title"])
```

### Custom Paragraph Styles

```python
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.colors import HexColor

styles = getSampleStyleSheet()

# Add a custom style based on an existing one
styles.add(ParagraphStyle(
    name="CustomTitle",
    parent=styles["Title"],
    fontSize=28,
    textColor=HexColor("#6366f1"),
    spaceAfter=20,
    alignment=TA_CENTER,
))

styles.add(ParagraphStyle(
    name="CustomBody",
    parent=styles["BodyText"],
    fontSize=11,
    leading=16,
    alignment=TA_JUSTIFY,
    textColor=HexColor("#334155"),
    spaceBefore=4,
    spaceAfter=10,
))

styles.add(ParagraphStyle(
    name="CodeBlock",
    parent=styles["Code"],
    fontSize=9,
    fontName="Courier",
    backColor=HexColor("#f1f5f9"),
    borderWidth=1,
    borderColor=HexColor("#e2e8f0"),
    borderPadding=8,
    borderRadius=4,
    leftIndent=12,
    rightIndent=12,
    spaceBefore=8,
    spaceAfter=8,
))

# Create a highlighted callout style
styles.add(ParagraphStyle(
    name="Callout",
    parent=styles["BodyText"],
    fontSize=11,
    leading=15,
    backColor=HexColor("#eff6ff"),
    borderWidth=0,
    borderPadding=12,
    leftIndent=20,
    textColor=HexColor("#1e40af"),
    spaceBefore=12,
    spaceAfter=12,
))
```

### Inline Markup in Paragraphs

```python
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

# Mix formatting within a paragraph
p = Paragraph(
    """
    <b>ReportLab</b> is a <i>powerful</i> library for creating
    <font color="#6366f1">professional PDF documents</font>.
    It supports <u>underlined text</u>, <super>superscript</super>,
    <sub>subscript</sub>, and even <strike>strikethrough</strike>.
    <br/><br/>
    You can include <font face="Courier" size="9" 
    color="#dc2626">inline code</font> and
    <a href="https://www.reportlab.com" color="blue">hyperlinks</a>.
    """,
    styles["BodyText"]
)
```

---

## Tables

### Basic Table

```python
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.units import cm

doc = SimpleDocTemplate("basic_table.pdf", pagesize=A4)
story = []

# Data: first row is header
data = [
    ["Name", "Role", "Department", "Salary"],
    ["Alice Johnson", "Engineer", "Engineering", "£55,000"],
    ["Bob Smith", "Designer", "Design", "£48,000"],
    ["Carol White", "Manager", "Engineering", "£65,000"],
    ["David Brown", "Analyst", "Finance", "£52,000"],
    ["Eve Davis", "Developer", "Engineering", "£58,000"],
]

# Create the table
table = Table(data, colWidths=[5*cm, 3.5*cm, 4*cm, 3*cm])

# Style the table
table.setStyle(TableStyle([
    # Header row
    ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
    ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 11),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ("TOPPADDING", (0, 0), (-1, 0), 10),

    # Body rows
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 1), (-1, -1), 10),
    ("TOPPADDING", (0, 1), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),

    # Grid lines
    ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),

    # Right-align salary column
    ("ALIGN", (-1, 1), (-1, -1), "RIGHT"),
]))

story.append(table)
doc.build(story)
```

- Download: [basic_table.pdf](../assets/reportlab/basic_table.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/basic_table.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/basic_table.pdf">basic_table.pdf</a></p>
</object>

</details>

<details>
<summary>Try it (table exercises)</summary>

- Add a **Total** row at the bottom and style it with bold text.
- Make the **header row** taller by increasing top/bottom padding.
- Highlight rows where Department is `Engineering` using conditional styling.

</details>

### TableStyle Commands

Complete reference for `TableStyle` commands:

| Command | Arguments | Description |
|---------|-----------|-------------|
| `BACKGROUND` | `(col, row), (col, row), color` | Cell background color |
| `TEXTCOLOR` | `(col, row), (col, row), color` | Text color |
| `FONTNAME` | `(col, row), (col, row), name` | Font name |
| `FONTSIZE` | `(col, row), (col, row), size` | Font size in points |
| `LEADING` | `(col, row), (col, row), leading` | Line spacing |
| `ALIGNMENT` / `ALIGN` | `(col, row), (col, row), align` | LEFT, CENTER, RIGHT, DECIMAL |
| `VALIGN` | `(col, row), (col, row), align` | TOP, MIDDLE, BOTTOM |
| `LEFTPADDING` | `(col, row), (col, row), pts` | Left cell padding |
| `RIGHTPADDING` | `(col, row), (col, row), pts` | Right cell padding |
| `TOPPADDING` | `(col, row), (col, row), pts` | Top cell padding |
| `BOTTOMPADDING` | `(col, row), (col, row), pts` | Bottom cell padding |
| `GRID` | `(col, row), (col, row), width, color` | All cell borders |
| `BOX` | `(col, row), (col, row), width, color` | Outer border |
| `INNERGRID` | `(col, row), (col, row), width, color` | Inner grid lines |
| `LINEBELOW` | `(col, row), (col, row), width, color` | Line below cells |
| `LINEABOVE` | `(col, row), (col, row), width, color` | Line above cells |
| `LINEBEFORE` | `(col, row), (col, row), width, color` | Line before cells |
| `LINEAFTER` | `(col, row), (col, row), width, color` | Line after cells |
| `SPAN` | `(col, row), (col, row)` | Merge cells |
| `ROWBACKGROUNDS` | `(col, row), (col, row), [colors]` | Alternating row colors |
| `COLBACKGROUNDS` | `(col, row), (col, row), [colors]` | Alternating col colors |

**Cell coordinates:** `(column, row)` where `(0, 0)` is top-left. Use `-1` for last column/row.

### Spanning Cells

```python
from reportlab.platypus import Table, TableStyle
from reportlab.lib.colors import HexColor, white

data = [
    ["Q1 2026 Sales Report", "", "", ""],
    ["Region", "Jan", "Feb", "Mar"],
    ["North", "£12,000", "£14,500", "£13,200"],
    ["South", "£9,800", "£11,200", "£10,500"],
    ["East", "£15,300", "£16,100", "£14,800"],
    ["Totals", "£37,100", "£41,800", "£38,500"],
]

table = Table(data)
table.setStyle(TableStyle([
    # Span the title row across all columns
    ("SPAN", (0, 0), (-1, 0)),
    ("BACKGROUND", (0, 0), (-1, 0), HexColor("#1e293b")),
    ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 14),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ("TOPPADDING", (0, 0), (-1, 0), 12),

    # Header row
    ("BACKGROUND", (0, 1), (-1, 1), HexColor("#6366f1")),
    ("TEXTCOLOR", (0, 1), (-1, 1), white),
    ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),

    # Totals row
    ("BACKGROUND", (0, -1), (-1, -1), HexColor("#f1f5f9")),
    ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),

    # Grid
    ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),
    ("ALIGN", (1, 2), (-1, -1), "RIGHT"),
]))
```

### Alternating Row Colors

```python
from reportlab.platypus import Table, TableStyle
from reportlab.lib.colors import HexColor, white

data = [
    ["ID", "Product", "Price", "Stock"],
    ["001", "Widget A", "£9.99", "150"],
    ["002", "Widget B", "£14.99", "89"],
    ["003", "Gadget C", "£24.99", "200"],
    ["004", "Gadget D", "£19.99", "45"],
    ["005", "Widget E", "£7.99", "300"],
    ["006", "Gadget F", "£29.99", "67"],
]

table = Table(data)
table.setStyle(TableStyle([
    # Header
    ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
    ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

    # Alternating row colors
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [
        HexColor("#ffffff"),
        HexColor("#f8fafc")
    ]),

    # Grid and padding
    ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("ALIGN", (2, 1), (3, -1), "RIGHT"),
]))
```

### Tables with Paragraphs

Embed `Paragraph` objects inside table cells for rich text:

```python
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import cm

doc = SimpleDocTemplate("rich_table.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Rich-text cells using Paragraphs
data = [
    [
        Paragraph("<b>Feature</b>", styles["BodyText"]),
        Paragraph("<b>Description</b>", styles["BodyText"]),
        Paragraph("<b>Status</b>", styles["BodyText"]),
    ],
    [
        Paragraph("PDF Generation", styles["BodyText"]),
        Paragraph(
            "Create <b>professional PDF</b> documents with "
            "<font color='#6366f1'>tables</font>, charts, and images.",
            styles["BodyText"]
        ),
        Paragraph("<font color='green'>✓ Complete</font>", styles["BodyText"]),
    ],
    [
        Paragraph("Multi-page Support", styles["BodyText"]),
        Paragraph(
            "Automatic page breaks with <i>headers and footers</i> "
            "on every page.",
            styles["BodyText"]
        ),
        Paragraph("<font color='green'>✓ Complete</font>", styles["BodyText"]),
    ],
    [
        Paragraph("Chart Integration", styles["BodyText"]),
        Paragraph(
            "Built-in <b>pie</b>, <b>bar</b>, and <b>line</b> charts "
            "with customizable legends and colors.",
            styles["BodyText"]
        ),
        Paragraph("<font color='orange'>⏳ In Progress</font>", styles["BodyText"]),
    ],
]

table = Table(data, colWidths=[4*cm, 8*cm, 3.5*cm])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
    ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#ffffff"), HexColor("#f8fafc")]),
]))

story.append(table)
doc.build(story)
```

- Download: [rich_table.pdf](../assets/reportlab/rich_table.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/rich_table.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/rich_table.pdf">rich_table.pdf</a></p>
</object>

</details>

### Long Tables Across Pages

For tables that span multiple pages with repeated headers:

```python
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import cm

doc = SimpleDocTemplate("long_table.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Generate a large dataset
header = ["ID", "Name", "Email", "Amount"]
data = [header]
for i in range(1, 101):
    data.append([
        str(i).zfill(3),
        f"Person {i}",
        f"person{i}@example.com",
        f"£{(i * 13.5):.2f}",
    ])

# Create table with repeatRows=1 to repeat header on each page
table = Table(data, colWidths=[2*cm, 4*cm, 6*cm, 3*cm], repeatRows=1)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
    ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 10),
    ("FONTSIZE", (0, 1), (-1, -1), 9),
    ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#ffffff"), HexColor("#f8fafc")]),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ("ALIGN", (-1, 1), (-1, -1), "RIGHT"),
]))

story.append(table)
doc.build(story)
```

- Download: [long_table.pdf](../assets/reportlab/long_table.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/long_table.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/long_table.pdf">long_table.pdf</a></p>
</object>

</details>

### Dynamic Tables from Data

Build tables from CSV, database queries, or API responses:

```python
import csv
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import cm

def csv_to_table(csv_filepath):
    """Read a CSV file and return a ReportLab Table."""
    with open(csv_filepath, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    if not data:
        return None

    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 1), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [
            HexColor("#ffffff"), HexColor("#f8fafc")
        ]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))

    return table

# Usage:
# doc = SimpleDocTemplate("csv_report.pdf", pagesize=A4)
# story = [csv_to_table("data.csv")]
# doc.build(story)
```

---

## Images

### Inserting Images

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

c = canvas.Canvas("images_canvas.pdf", pagesize=A4)
w, h = A4

# Draw an image at a specific position
c.drawImage("photo.jpg", 2*cm, h - 10*cm, width=8*cm, height=6*cm)

# Draw with aspect ratio preserved
c.drawImage(
    "logo.png",
    2*cm, h - 14*cm,
    width=4*cm, height=4*cm,
    preserveAspectRatio=True,
    anchor="sw"  # south-west = bottom-left
)

# Draw with a border mask (transparency)
c.drawImage(
    "icon.png",
    10*cm, h - 14*cm,
    width=3*cm, height=3*cm,
    mask="auto"  # Automatic transparency
)

c.save()
```

### Image Sizing & Aspect Ratio

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

c = canvas.Canvas("image_sizing.pdf", pagesize=A4)
w, h = A4

# Original size (image's native resolution at 72 DPI)
c.drawImage("photo.jpg", 2*cm, h - 8*cm)

# Scaled to exact dimensions (may distort)
c.drawImage("photo.jpg", 2*cm, h - 16*cm, width=6*cm, height=4*cm)

# Scaled preserving aspect ratio (fits within bounds)
c.drawImage(
    "photo.jpg",
    10*cm, h - 16*cm,
    width=6*cm, height=4*cm,
    preserveAspectRatio=True,
    anchor="c"  # center the image within the bounds
)

c.save()
```

**Anchor values for `preserveAspectRatio`:**

| Anchor | Position |
|--------|----------|
| `"sw"` | Bottom-left (default) |
| `"s"` | Bottom-center |
| `"se"` | Bottom-right |
| `"w"` | Middle-left |
| `"c"` | Center |
| `"e"` | Middle-right |
| `"nw"` | Top-left |
| `"n"` | Top-center |
| `"ne"` | Top-right |

### Images in Platypus

```python
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

doc = SimpleDocTemplate("images_platypus.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("Images in Platypus", styles["Title"]))
story.append(Spacer(1, 12))

# Basic image (specify at least width or height)
img = Image("photo.jpg", width=12*cm, height=8*cm)
story.append(img)
story.append(Spacer(1, 12))

# Image with preserved aspect ratio
img2 = Image("photo.jpg", width=8*cm, height=6*cm, kind="proportional")
story.append(img2)
story.append(Spacer(1, 12))

# Centered image
img3 = Image("logo.png", width=4*cm, height=4*cm)
img3.hAlign = "CENTER"
story.append(img3)

doc.build(story)
```

> **Note:** This example requires local image files (`photo.jpg`, `logo.png`). No embedded preview is provided.

### Images from URLs & Bytes

```python
from reportlab.platypus import Image
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
import io
import urllib.request

# From a URL
url = "https://www.reportlab.com/static/cms/img/logo.png"
img_data = urllib.request.urlopen(url).read()
img_reader = ImageReader(io.BytesIO(img_data))

# In Canvas:
# c.drawImage(img_reader, x, y, width, height)

# In Platypus:
img = Image(io.BytesIO(img_data), width=6*cm, height=3*cm)
```

---

## Page Layout & Templates

### Headers & Footers

Add consistent headers and footers using callback functions:

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor

def header_footer(canvas, doc):
    """Called on every page to draw header and footer."""
    canvas.saveState()
    width, height = A4

    # ─── Header ───
    canvas.setStrokeColor(HexColor("#6366f1"))
    canvas.setLineWidth(2)
    canvas.line(2*cm, height - 2*cm, width - 2*cm, height - 2*cm)

    canvas.setFont("Helvetica-Bold", 10)
    canvas.setFillColor(HexColor("#6366f1"))
    canvas.drawString(2*cm, height - 1.7*cm, "My Company Report")

    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(HexColor("#64748b"))
    canvas.drawRightString(width - 2*cm, height - 1.7*cm, "Confidential")

    # ─── Footer ───
    canvas.setStrokeColor(HexColor("#e2e8f0"))
    canvas.setLineWidth(0.5)
    canvas.line(2*cm, 2*cm, width - 2*cm, 2*cm)

    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(HexColor("#94a3b8"))
    canvas.drawString(2*cm, 1.2*cm, "Generated with ReportLab")
    canvas.drawRightString(
        width - 2*cm, 1.2*cm,
        f"Page {canvas.getPageNumber()}"
    )

    canvas.restoreState()

# Build the document
doc = SimpleDocTemplate(
    "header_footer.pdf",
    pagesize=A4,
    topMargin=3*cm,      # Extra space for header
    bottomMargin=3*cm,   # Extra space for footer
)

styles = getSampleStyleSheet()
story = []

for i in range(1, 6):
    story.append(Paragraph(f"Chapter {i}", styles["Heading1"]))
    story.append(Spacer(1, 12))
    for j in range(8):
        story.append(Paragraph(
            f"This is paragraph {j+1} of chapter {i}. "
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            styles["BodyText"]
        ))
    if i < 5:
        story.append(PageBreak())

# Pass the callback via onFirstPage and onLaterPages
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
```

- Download: [header_footer.pdf](../assets/reportlab/header_footer.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/header_footer.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/header_footer.pdf">header_footer.pdf</a></p>
</object>

</details>

### Page Numbers

Several ways to add page numbers:

```python
# Method 1: In a header/footer callback (shown above)
canvas.drawRightString(width - 2*cm, 1.2*cm, f"Page {canvas.getPageNumber()}")

# Method 2: "Page X of Y" using PageTemplate and afterFlowable
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

class NumberedDocTemplate(SimpleDocTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_count = 0

    def afterFlowable(self, flowable):
        pass  # Can track TOC entries here

    def afterPage(self):
        self.page_count += 1

def page_number_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.drawCentredString(
        A4[0] / 2, 1.5*cm,
        f"Page {canvas.getPageNumber()}"
    )
    canvas.restoreState()
```

### Multi-Column Layouts

```python
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

styles = getSampleStyleSheet()

# Create frames for two columns
frame_left = Frame(
    2*cm, 2*cm,         # x, y
    8.5*cm, 25*cm,      # width, height
    id="left"
)
frame_right = Frame(
    11.5*cm, 2*cm,
    8.5*cm, 25*cm,
    id="right"
)

# Create page template with both frames
template = PageTemplate(
    id="two_col",
    frames=[frame_left, frame_right]
)

doc = BaseDocTemplate("two_columns.pdf", pagesize=A4)
doc.addPageTemplates([template])

story = []
for i in range(20):
    story.append(Paragraph(f"<b>Section {i+1}</b>", styles["Heading3"]))
    story.append(Paragraph(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation.",
        styles["BodyText"]
    ))
    story.append(Spacer(1, 8))

doc.build(story)
```

- Download: [two_columns.pdf](../assets/reportlab/two_columns.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/two_columns.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/two_columns.pdf">two_columns.pdf</a></p>
</object>

</details>

### BaseDocTemplate & PageTemplate

For complex layouts, use `BaseDocTemplate` with custom `PageTemplate`s:

```python
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate,
    Paragraph, Spacer, NextPageTemplate, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor

styles = getSampleStyleSheet()

def cover_page_draw(canvas, doc):
    """Draw the cover page background."""
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(HexColor("#1e293b"))
    canvas.rect(0, 0, w, h, fill=1)
    canvas.setFillColor(HexColor("#ffffff"))
    canvas.setFont("Helvetica-Bold", 36)
    canvas.drawCentredString(w/2, h/2 + 40, "Annual Report")
    canvas.setFont("Helvetica", 16)
    canvas.drawCentredString(w/2, h/2 - 10, "2026 Edition")
    canvas.restoreState()

def normal_page_draw(canvas, doc):
    """Standard page with header/footer."""
    canvas.saveState()
    w, h = A4
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(HexColor("#94a3b8"))
    canvas.drawCentredString(w/2, 1.5*cm, f"Page {canvas.getPageNumber()}")
    canvas.restoreState()

# Define frames
cover_frame = Frame(2*cm, 2*cm, A4[0] - 4*cm, A4[1] - 4*cm, id="cover")
normal_frame = Frame(2*cm, 3*cm, A4[0] - 4*cm, A4[1] - 5*cm, id="normal")

# Define page templates
cover_template = PageTemplate(id="cover", frames=[cover_frame], onPage=cover_page_draw)
normal_template = PageTemplate(id="normal", frames=[normal_frame], onPage=normal_page_draw)

doc = BaseDocTemplate("complex_layout.pdf", pagesize=A4)
doc.addPageTemplates([cover_template, normal_template])

story = []

# Cover page (empty — drawing is done in cover_page_draw)
story.append(Spacer(1, 1))
story.append(NextPageTemplate("normal"))
story.append(PageBreak())

# Content pages
for i in range(1, 4):
    story.append(Paragraph(f"Chapter {i}", styles["Heading1"]))
    story.append(Spacer(1, 12))
    for j in range(6):
        story.append(Paragraph(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Vivamus lacinia odio vitae vestibulum vestibulum.",
            styles["BodyText"]
        ))

doc.build(story)
```

- Download: [complex_layout.pdf](../assets/reportlab/complex_layout.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/complex_layout.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/complex_layout.pdf">complex_layout.pdf</a></p>
</object>

</details>

### Frame Objects

Frame controls where content flows on a page:

```python
from reportlab.platypus import Frame
from reportlab.lib.units import cm

# Frame(x, y, width, height, ...)
frame = Frame(
    x1=2*cm,            # Left edge (from page left)
    y1=3*cm,            # Bottom edge (from page bottom)
    width=17*cm,        # Frame width
    height=23*cm,       # Frame height
    leftPadding=6,      # Internal padding
    rightPadding=6,
    topPadding=6,
    bottomPadding=6,
    showBoundary=0,     # 1 = show frame border (debugging)
    id="main_frame"
)
```

### Watermarks & Backgrounds

```python
from reportlab.pdfgen import canvas as canvas_module
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import Color, HexColor

def add_watermark(canvas, doc):
    """Add a diagonal watermark on every page."""
    canvas.saveState()
    w, h = A4

    # Semi-transparent text
    canvas.setFillColor(Color(0, 0, 0, alpha=0.06))
    canvas.setFont("Helvetica-Bold", 60)

    # Rotate and draw at center
    canvas.translate(w/2, h/2)
    canvas.rotate(45)
    canvas.drawCentredString(0, 0, "DRAFT")

    canvas.restoreState()

    # Also add a page number
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(HexColor("#94a3b8"))
    canvas.drawCentredString(w/2, 1.5*cm, f"Page {canvas.getPageNumber()}")
    canvas.restoreState()

doc = SimpleDocTemplate("watermark.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

for i in range(5):
    story.append(Paragraph(f"Section {i+1}", styles["Heading1"]))
    story.append(Paragraph(
        "This document has a diagonal DRAFT watermark on every page. "
        "The watermark is drawn using canvas operations in a callback.",
        styles["BodyText"]
    ))
    story.append(Spacer(1, 200))

doc.build(story, onFirstPage=add_watermark, onLaterPages=add_watermark)
```

- Download: [watermark.pdf](../assets/reportlab/watermark.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/watermark.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/watermark.pdf">watermark.pdf</a></p>
</object>

</details>

---

## Colors & Drawing

### Named Colors

```python
from reportlab.lib.colors import (
    red, green, blue, black, white, gray,
    darkred, darkgreen, darkblue,
    lightgrey, darkgrey,
    pink, yellow, cyan, magenta, orange, purple,
    brown, navy, olive, teal, maroon,
    transparent
)

# Use in canvas
c.setFillColor(red)
c.setStrokeColor(blue)

# Use in TableStyle
("BACKGROUND", (0, 0), (-1, 0), navy)
```

### Hex Colors

```python
from reportlab.lib.colors import HexColor

# Standard hex
color1 = HexColor("#6366f1")
color2 = HexColor("#1e293b")

# With alpha (transparency)
color3 = HexColor("#6366f180")  # 50% transparent

# Short hex
color4 = HexColor("#f00")  # Red
```

### RGB & CMYK Colors

```python
from reportlab.lib.colors import Color, CMYKColor

# RGB (values 0.0 to 1.0)
rgb_color = Color(0.39, 0.40, 0.95)  # Indigo-ish

# RGB with alpha
transparent_blue = Color(0, 0, 1, alpha=0.3)

# CMYK (values 0.0 to 1.0)
cmyk_red = CMYKColor(0, 1, 1, 0)    # Pure red in CMYK
cmyk_custom = CMYKColor(0.1, 0.8, 0.9, 0.05)
```

### Transparency & Alpha

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color

c = canvas.Canvas("transparency.pdf", pagesize=A4)
w, h = A4

# Draw overlapping circles with transparency
colors = [
    Color(1, 0, 0, alpha=0.4),   # Red
    Color(0, 1, 0, alpha=0.4),   # Green
    Color(0, 0, 1, alpha=0.4),   # Blue
]

positions = [(250, 500), (320, 500), (285, 560)]

for color, (x, y) in zip(colors, positions):
    c.setFillColor(color)
    c.circle(x, y, 80, fill=1, stroke=0)

c.save()
```

    - Download: [transparency.pdf](../assets/reportlab/transparency.pdf)

    <details>
    <summary>Preview (PDF)</summary>

    <object data="../assets/reportlab/transparency.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
        <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/transparency.pdf">transparency.pdf</a></p>
    </object>

    </details>

### Gradients

ReportLab doesn't have native gradient fills, but you can simulate them:

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color

c = canvas.Canvas("gradient.pdf", pagesize=A4)
w, h = A4

# Simulate a vertical gradient with thin rectangles
x, y, gw, gh = 72, 400, 400, 200
steps = 100

for i in range(steps):
    t = i / steps
    r = 0.39 + t * 0.2   # From indigo to lighter
    g = 0.40 + t * 0.35
    b = 0.95 - t * 0.1

    c.setFillColor(Color(r, g, b))
    stripe_h = gh / steps
    c.rect(x, y + i * stripe_h, gw, stripe_h + 1, fill=1, stroke=0)

c.save()
```

    - Download: [gradient.pdf](../assets/reportlab/gradient.pdf)

    <details>
    <summary>Preview (PDF)</summary>

    <object data="../assets/reportlab/gradient.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
        <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/gradient.pdf">gradient.pdf</a></p>
    </object>

    </details>

---

## Charts & Graphs

ReportLab includes a charting library in `reportlab.graphics.charts`.

### Pie Charts

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.colors import HexColor

doc = SimpleDocTemplate("pie_chart.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("Sales by Region", styles["Title"]))
story.append(Spacer(1, 20))

# Create a Drawing to hold the chart
drawing = Drawing(400, 250)

# Configure the pie chart
pie = Pie()
pie.x = 100
pie.y = 25
pie.width = 180
pie.height = 180
pie.data = [35, 25, 20, 15, 5]
pie.labels = ["North", "South", "East", "West", "Other"]

# Colors
pie.slices[0].fillColor = HexColor("#6366f1")
pie.slices[1].fillColor = HexColor("#ec4899")
pie.slices[2].fillColor = HexColor("#f59e0b")
pie.slices[3].fillColor = HexColor("#10b981")
pie.slices[4].fillColor = HexColor("#94a3b8")

# Style
pie.slices.strokeWidth = 0.5
pie.slices.strokeColor = HexColor("#ffffff")
pie.sideLabels = True
pie.simpleLabels = False
pie.slices.fontName = "Helvetica"
pie.slices.fontSize = 10

drawing.add(pie)
story.append(drawing)

doc.build(story)
```

- Download: [pie_chart.pdf](../assets/reportlab/pie_chart.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/pie_chart.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/pie_chart.pdf">pie_chart.pdf</a></p>
</object>

</details>

<details>
<summary>Try it (chart exercises)</summary>

- Change the data so one slice dominates (e.g. `[60, 15, 10, 10, 5]`) and see how label placement changes.
- Turn off side labels with `pie.sideLabels = False` and compare readability.
- Experiment with slice colors to match your brand palette.

</details>

### Bar Charts

```python
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib.colors import HexColor

drawing = Drawing(450, 250)

chart = VerticalBarChart()
chart.x = 60
chart.y = 50
chart.width = 350
chart.height = 170

# Data: each sub-list is a series
chart.data = [
    [45, 52, 61, 58, 72],    # 2024
    [50, 58, 68, 65, 80],    # 2025
]

# X-axis labels
chart.categoryAxis.categoryNames = ["Q1", "Q2", "Q3", "Q4", "Q5"]
chart.categoryAxis.labels.fontName = "Helvetica"
chart.categoryAxis.labels.fontSize = 10

# Y-axis
chart.valueAxis.valueMin = 0
chart.valueAxis.valueMax = 100
chart.valueAxis.valueStep = 20
chart.valueAxis.labels.fontName = "Helvetica"
chart.valueAxis.labels.fontSize = 9

# Series colors
chart.bars[0].fillColor = HexColor("#6366f1")
chart.bars[1].fillColor = HexColor("#10b981")

# Bar styling
chart.barWidth = 12
chart.groupSpacing = 15

drawing.add(chart)

# Add title
title = String(225, 235, "Quarterly Revenue (£k)", fontSize=14,
               fontName="Helvetica-Bold", textAnchor="middle")
drawing.add(title)

# Use in story:
# story.append(drawing)
```

### Line Charts

```python
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.lib.colors import HexColor

drawing = Drawing(450, 250)

chart = HorizontalLineChart()
chart.x = 60
chart.y = 50
chart.width = 350
chart.height = 170

chart.data = [
    [10, 15, 22, 30, 28, 35, 42, 50, 48, 55, 62, 70],  # Revenue
    [5, 8, 12, 18, 15, 20, 25, 30, 28, 32, 38, 45],     # Profit
]

# X-axis
chart.categoryAxis.categoryNames = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]
chart.categoryAxis.labels.fontName = "Helvetica"
chart.categoryAxis.labels.fontSize = 8
chart.categoryAxis.labels.angle = 45

# Y-axis
chart.valueAxis.valueMin = 0
chart.valueAxis.valueMax = 80
chart.valueAxis.valueStep = 10

# Line styles
chart.lines[0].strokeColor = HexColor("#6366f1")
chart.lines[0].strokeWidth = 2
chart.lines[1].strokeColor = HexColor("#10b981")
chart.lines[1].strokeWidth = 2

# Markers
chart.lines[0].symbol = makeMarker("Circle")
chart.lines[1].symbol = makeMarker("Square")

drawing.add(chart)
```

> **Note:** Import `from reportlab.graphics.widgets.markers import makeMarker` for line markers.

### Chart Legends

```python
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.colors import HexColor

drawing = Drawing(450, 300)

# ... (add your chart first) ...

# Add a legend
legend = Legend()
legend.x = 60
legend.y = 10
legend.dx = 8
legend.dy = 8
legend.fontName = "Helvetica"
legend.fontSize = 10
legend.boxAnchor = "sw"
legend.columnMaximum = 1
legend.strokeWidth = 0.5
legend.strokeColor = HexColor("#e2e8f0")
legend.deltax = 75
legend.deltay = 10
legend.autoXPadding = 5
legend.yGap = 0
legend.dxTextSpace = 5
legend.alignment = "right"
legend.dividerLines = 1 | 2 | 4
legend.subCols.rpad = 15

legend.colorNamePairs = [
    (HexColor("#6366f1"), "2024 Revenue"),
    (HexColor("#10b981"), "2025 Revenue"),
]

drawing.add(legend)
```

### Chart Customization

```python
# Grid lines
chart.valueAxis.visibleGrid = True
chart.valueAxis.gridStrokeColor = HexColor("#e2e8f0")
chart.valueAxis.gridStrokeWidth = 0.5

# Axis styling
chart.categoryAxis.strokeColor = HexColor("#94a3b8")
chart.valueAxis.strokeColor = HexColor("#94a3b8")

# Labels
chart.categoryAxis.labels.fontName = "Helvetica"
chart.categoryAxis.labels.fontSize = 9
chart.categoryAxis.labels.fillColor = HexColor("#64748b")

# Bar labels (showing values on bars)
chart.barLabelFormat = "%.0f"
chart.barLabels.fontName = "Helvetica"
chart.barLabels.fontSize = 8
chart.barLabels.fillColor = HexColor("#334155")
```

---

## Barcodes & QR Codes

### Code128 Barcode

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.graphics.barcode import code128

c = canvas.Canvas("barcode.pdf", pagesize=A4)
w, h = A4

# Draw a Code128 barcode
barcode = code128.Code128(
    "ABC-12345-XYZ",
    barWidth=0.5*cm/10,
    barHeight=1.5*cm,
    humanReadable=True
)

barcode.drawOn(c, 2*cm, h - 5*cm)

c.save()
```

- Download: [barcode.pdf](../assets/reportlab/barcode.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/barcode.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/barcode.pdf">barcode.pdf</a></p>
</object>

</details>

### QR Codes

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing

c = canvas.Canvas("qrcode.pdf", pagesize=A4)
w, h = A4

# Create a QR code
qr = QrCodeWidget("https://www.reportlab.com")
qr.barWidth = 4*cm
qr.barHeight = 4*cm
qr.qrVersion = 1

# Wrap in a Drawing
d = Drawing(4*cm, 4*cm)
d.add(qr)
d.drawOn(c, 2*cm, h - 7*cm)

# QR code with more data
qr2 = QrCodeWidget("Name: John Doe\nEmail: john@example.com\nPhone: +44 123 456 7890")
qr2.barWidth = 5*cm
qr2.barHeight = 5*cm

d2 = Drawing(5*cm, 5*cm)
d2.add(qr2)
d2.drawOn(c, 10*cm, h - 8*cm)

c.save()
```

- Download: [qrcode.pdf](../assets/reportlab/qrcode.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/qrcode.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/qrcode.pdf">qrcode.pdf</a></p>
</object>

</details>

### Barcodes in Platypus

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.barcode import code128
from reportlab.graphics.shapes import Drawing

doc = SimpleDocTemplate("barcodes_platypus.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("Barcode Examples", styles["Title"]))
story.append(Spacer(1, 20))

# Code128 barcode as a flowable
story.append(Paragraph("Code128 Barcode:", styles["Heading2"]))
barcode = code128.Code128(
    "ITEM-2026-001",
    barWidth=1.2,
    barHeight=40,
    humanReadable=True,
)
story.append(barcode)
story.append(Spacer(1, 20))

# QR code as a flowable
story.append(Paragraph("QR Code:", styles["Heading2"]))
qr = QrCodeWidget("https://www.reportlab.com")
qr.barWidth = 100
qr.barHeight = 100

d2 = Drawing(120, 120)
d2.add(qr)
story.append(d2)

doc.build(story)
```

- Download: [barcodes_platypus.pdf](../assets/reportlab/barcodes_platypus.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/barcodes_platypus.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/barcodes_platypus.pdf">barcodes_platypus.pdf</a></p>
</object>

</details>

**Available Barcode Types:**

| Type | Module | Example Value |
|------|--------|---------------|
| Code128 | `reportlab.graphics.barcode.code128` | `"ABC-123"` |
| Code39 | `reportlab.graphics.barcode.code39` | `"HELLO"` |
| EAN13 | `reportlab.graphics.barcode.eanbc` | `"5012345678900"` |
| EAN8 | `reportlab.graphics.barcode.eanbc` | `"12345670"` |
| UPCA | `reportlab.graphics.barcode.usps` | `"012345678905"` |
| QR | `reportlab.graphics.barcode.qr` | Any string |

---

## PDF Metadata & Security

### Setting Metadata

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("metadata.pdf", pagesize=A4)

# Set PDF metadata
c.setTitle("My Report Title")
c.setAuthor("John Doe")
c.setSubject("Monthly Sales Report - January 2026")
c.setCreator("ReportLab PDF Generator")
c.setKeywords(["report", "sales", "2026", "pdf"])

c.drawString(100, 700, "Check File > Properties in your PDF viewer!")
c.save()
```

- Download: [metadata.pdf](../assets/reportlab/metadata.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/metadata.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/metadata.pdf">metadata.pdf</a></p>
</object>

</details>

With Platypus:

```python
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4

doc = SimpleDocTemplate(
    "metadata_platypus.pdf",
    pagesize=A4,
    title="My Report",
    author="John Doe",
    subject="Monthly Report",
    creator="ReportLab",
    keywords=["report", "monthly"],
)
```

### PDF Encryption & Passwords

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pdfencrypt import StandardEncryption

# Password protection
enc = StandardEncryption(
    userPassword="reader123",     # Required to open
    ownerPassword="admin456",     # Required to change permissions
    canPrint=True,
    canModify=False,
    canCopy=False,
    canAnnotate=False,
    strength=128                  # 40 or 128 bit
)

c = canvas.Canvas("encrypted.pdf", pagesize=A4, encrypt=enc)
c.drawString(100, 700, "This PDF is password-protected!")
c.save()
```

```output
Creates a password-protected PDF.
```

- Download: [encrypted.pdf](../assets/reportlab/encrypted.pdf) (password: `reader123`)

### Bookmarks & Outlines

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("bookmarks.pdf", pagesize=A4)
w, h = A4

# Page 1
c.bookmarkPage("page1")
c.addOutlineEntry("Chapter 1 — Introduction", "page1", level=0)
c.setFont("Helvetica-Bold", 20)
c.drawString(72, h - 72, "Chapter 1: Introduction")
c.setFont("Helvetica", 12)
c.drawString(72, h - 110, "Welcome to the document.")

c.showPage()

# Page 2
c.bookmarkPage("page2")
c.addOutlineEntry("Chapter 2 — Details", "page2", level=0)
c.setFont("Helvetica-Bold", 20)
c.drawString(72, h - 72, "Chapter 2: Details")

# Sub-section
c.bookmarkPage("page2_sect1")
c.addOutlineEntry("Section 2.1 — Data", "page2_sect1", level=1)
c.setFont("Helvetica-Bold", 16)
c.drawString(72, h - 130, "Section 2.1: Data")

c.showPage()

# Page 3
c.bookmarkPage("page3")
c.addOutlineEntry("Chapter 3 — Conclusion", "page3", level=0)
c.setFont("Helvetica-Bold", 20)
c.drawString(72, h - 72, "Chapter 3: Conclusion")

c.save()
```

- Download: [bookmarks.pdf](../assets/reportlab/bookmarks.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/bookmarks.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/bookmarks.pdf">bookmarks.pdf</a></p>
</object>

</details>

### Hyperlinks

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor

c = canvas.Canvas("hyperlinks.pdf", pagesize=A4)
w, h = A4

# External link (URL)
c.setFont("Helvetica", 14)
c.setFillColor(HexColor("#6366f1"))
c.drawString(72, h - 72, "Click here to visit ReportLab")

# Make the text area clickable
c.linkURL(
    "https://www.reportlab.com/",
    (72, h - 78, 340, h - 58),   # (x1, y1, x2, y2) bounding box
    relative=0
)

# Internal link (to a bookmark on another page)
c.setFont("Helvetica", 14)
c.drawString(72, h - 120, "Go to Chapter 2")
c.linkRect(
    "Go to Chapter 2",
    "chapter2",
    (72, h - 126, 240, h - 106),
    relative=0
)

c.showPage()

# Page 2 with bookmark target
c.bookmarkPage("chapter2")
c.setFont("Helvetica-Bold", 20)
c.drawString(72, h - 72, "Chapter 2")

c.save()
```

- Download: [hyperlinks.pdf](../assets/reportlab/hyperlinks.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/hyperlinks.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/hyperlinks.pdf">hyperlinks.pdf</a></p>
</object>

</details>

---

## Common Recipes

### Invoice PDF

```python
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from datetime import date

def generate_invoice(filename, invoice_data):
    """Generate a professional invoice PDF."""

    doc = SimpleDocTemplate(
        filename, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm,
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        "InvoiceTitle", parent=styles["Title"],
        fontSize=28, textColor=HexColor("#1e293b"),
    ))
    styles.add(ParagraphStyle(
        "RightAligned", parent=styles["Normal"],
        alignment=TA_RIGHT,
    ))

    story = []

    # ─── Header ───
    header_data = [
        [
            Paragraph("<b>ACME Corp</b><br/>123 Business St<br/>London, EC1A 1BB<br/>accounts@acme.com", styles["Normal"]),
            Paragraph(
                f"<b>INVOICE</b><br/>"
                f"Invoice #: {invoice_data['number']}<br/>"
                f"Date: {invoice_data['date']}<br/>"
                f"Due: {invoice_data['due_date']}",
                styles["RightAligned"]
            ),
        ]
    ]
    header_table = Table(header_data, colWidths=[9*cm, 8*cm])
    header_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 20))

    # ─── Bill To ───
    story.append(Paragraph("<b>Bill To:</b>", styles["Normal"]))
    story.append(Paragraph(invoice_data["client_name"], styles["Normal"]))
    story.append(Paragraph(invoice_data["client_address"], styles["Normal"]))
    story.append(Spacer(1, 20))

    # ─── Items Table ───
    items_header = ["Description", "Qty", "Unit Price", "Total"]
    items_data = [items_header]

    subtotal = 0
    for item in invoice_data["items"]:
        total = item["qty"] * item["price"]
        subtotal += total
        items_data.append([
            item["description"],
            str(item["qty"]),
            f"£{item['price']:.2f}",
            f"£{total:.2f}",
        ])

    vat = subtotal * 0.20
    grand_total = subtotal + vat

    # Add totals rows
    items_data.append(["", "", "Subtotal:", f"£{subtotal:.2f}"])
    items_data.append(["", "", "VAT (20%):", f"£{vat:.2f}"])
    items_data.append(["", "", "TOTAL:", f"£{grand_total:.2f}"])

    items_table = Table(items_data, colWidths=[8*cm, 2*cm, 3.5*cm, 3.5*cm])
    items_table.setStyle(TableStyle([
        # Header
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (1, 0), (-1, 0), "CENTER"),

        # Body
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("GRID", (0, 0), (-1, -4), 0.5, HexColor("#e2e8f0")),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),

        # Totals
        ("FONTNAME", (2, -3), (-1, -1), "Helvetica-Bold"),
        ("LINEABOVE", (2, -3), (-1, -3), 1, HexColor("#e2e8f0")),
        ("FONTNAME", (2, -1), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (2, -1), (-1, -1), 12),
        ("BACKGROUND", (2, -1), (-1, -1), HexColor("#f1f5f9")),
    ]))
    story.append(items_table)
    story.append(Spacer(1, 30))

    # ─── Notes ───
    story.append(Paragraph("<b>Notes:</b>", styles["Normal"]))
    story.append(Paragraph(
        "Payment due within 30 days. Please reference the invoice number "
        "when making payment. Bank details: Sort Code 12-34-56, Account 12345678.",
        styles["BodyText"]
    ))

    doc.build(story)

# Usage:
invoice = {
    "number": "INV-2026-001",
    "date": "2026-02-16",
    "due_date": "2026-03-18",
    "client_name": "Widget Co Ltd",
    "client_address": "456 Client Road, Manchester, M1 2AB",
    "items": [
        {"description": "Web Development - Homepage", "qty": 1, "price": 2500.00},
        {"description": "Web Development - API Integration", "qty": 1, "price": 1800.00},
        {"description": "UI/UX Design - Mockups", "qty": 3, "price": 450.00},
        {"description": "Hosting Setup (Annual)", "qty": 1, "price": 350.00},
    ],
}

generate_invoice("invoice.pdf", invoice)
```

- Download: [invoice.pdf](../assets/reportlab/invoice.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/invoice.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/invoice.pdf">invoice.pdf</a></p>
</object>

</details>

### Multi-Page Report from CSV

```python
import csv
from datetime import date
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white

def generate_csv_report(csv_path, output_path, title="Data Report"):
    """Generate a multi-page PDF report from a CSV file."""
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Title page
    story.append(Spacer(1, 200))
    story.append(Paragraph(title, styles["Title"]))
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        f"Generated on {date.today().strftime('%d %B %Y')}",
        styles["Normal"]
    ))
    story.append(PageBreak())

    # Read CSV
    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)

    # Summary section
    story.append(Paragraph("Summary", styles["Heading1"]))
    story.append(Paragraph(f"Total records: <b>{len(rows)}</b>", styles["BodyText"]))
    story.append(Paragraph(f"Columns: <b>{', '.join(headers)}</b>", styles["BodyText"]))
    story.append(Spacer(1, 20))

    # Data table
    story.append(Paragraph("Data", styles["Heading1"]))
    story.append(Spacer(1, 10))

    data = [headers] + rows
    num_cols = len(headers)
    col_width = (A4[0] - 4*cm) / num_cols

    table = Table(data, colWidths=[col_width] * num_cols, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#fff"), HexColor("#f8fafc")]),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(table)

    doc.build(story)

# Usage:
sample_csv = "sales_data.csv"
with open(sample_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Region", "Product", "Units", "Revenue"])
    writer.writerow(["2026-01-05", "North", "Widget", "12", "£599.88"])
    writer.writerow(["2026-01-08", "South", "Gadget", "7", "£419.93"])
    writer.writerow(["2026-01-14", "East", "Service", "1", "£1200.00"])
    writer.writerow(["2026-01-22", "West", "Widget", "4", "£199.96"])

generate_csv_report(sample_csv, "sales_report.pdf", "Q1 Sales Report")
```

- Download: [sales_report.pdf](../assets/reportlab/sales_report.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/sales_report.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/sales_report.pdf">sales_report.pdf</a></p>
</object>

</details>

### Certificate Generator

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor

def generate_certificate(filename, name, course, date_str, cert_id):
    """Generate a professional certificate."""
    page = landscape(A4)
    c = canvas.Canvas(filename, pagesize=page)
    w, h = page

    # ─── Border ───
    c.setStrokeColor(HexColor("#6366f1"))
    c.setLineWidth(3)
    c.rect(1.5*cm, 1.5*cm, w - 3*cm, h - 3*cm)
    c.setLineWidth(1)
    c.rect(2*cm, 2*cm, w - 4*cm, h - 4*cm)

    # ─── Decorative corners ───
    corner_size = 30
    for x, y in [(2.5*cm, h - 2.5*cm), (w - 2.5*cm, h - 2.5*cm),
                 (2.5*cm, 2.5*cm), (w - 2.5*cm, 2.5*cm)]:
        c.setFillColor(HexColor("#6366f1"))
        c.circle(x, y, 4, fill=1)

    # ─── Title ───
    c.setFont("Times-Bold", 36)
    c.setFillColor(HexColor("#1e293b"))
    c.drawCentredString(w/2, h - 5*cm, "Certificate of Completion")

    # ─── Decorative line ───
    c.setStrokeColor(HexColor("#6366f1"))
    c.setLineWidth(1.5)
    c.line(w/2 - 8*cm, h - 5.8*cm, w/2 + 8*cm, h - 5.8*cm)

    # ─── "This certifies that" ───
    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#64748b"))
    c.drawCentredString(w/2, h - 7.5*cm, "This certifies that")

    # ─── Name ───
    c.setFont("Times-BoldItalic", 32)
    c.setFillColor(HexColor("#1e293b"))
    c.drawCentredString(w/2, h - 9.5*cm, name)

    # ─── Line under name ───
    c.setStrokeColor(HexColor("#e2e8f0"))
    c.line(w/2 - 6*cm, h - 10*cm, w/2 + 6*cm, h - 10*cm)

    # ─── Course ───
    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#64748b"))
    c.drawCentredString(w/2, h - 11.5*cm, "has successfully completed the course")

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(HexColor("#6366f1"))
    c.drawCentredString(w/2, h - 13*cm, course)

    # ─── Date ───
    c.setFont("Helvetica", 12)
    c.setFillColor(HexColor("#64748b"))
    c.drawCentredString(w/2, h - 15*cm, f"Date: {date_str}")

    # ─── Certificate ID ───
    c.setFont("Helvetica", 9)
    c.setFillColor(HexColor("#94a3b8"))
    c.drawCentredString(w/2, 2.5*cm, f"Certificate ID: {cert_id}")

    c.save()

# Usage:
generate_certificate(
    "certificate.pdf",
    "Alice Johnson",
    "Advanced Python Programming",
    "16 February 2026",
    "CERT-2026-00142"
)
```

- Download: [certificate.pdf](../assets/reportlab/certificate.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/certificate.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/certificate.pdf">certificate.pdf</a></p>
</object>

</details>

### Letter & Letterhead

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_RIGHT

def generate_letter(filename, sender, recipient, subject, body_paragraphs, date_str):
    """Generate a formal letter with letterhead."""

    def letterhead(canvas, doc):
        canvas.saveState()
        w, h = A4

        # Company name
        canvas.setFont("Helvetica-Bold", 18)
        canvas.setFillColor(HexColor("#6366f1"))
        canvas.drawString(2*cm, h - 2*cm, sender["company"])

        # Address line
        canvas.setFont("Helvetica", 9)
        canvas.setFillColor(HexColor("#64748b"))
        canvas.drawString(2*cm, h - 2.6*cm, sender["address"])

        # Accent line
        canvas.setStrokeColor(HexColor("#6366f1"))
        canvas.setLineWidth(2)
        canvas.line(2*cm, h - 3*cm, w - 2*cm, h - 3*cm)

        # Footer
        canvas.setStrokeColor(HexColor("#e2e8f0"))
        canvas.setLineWidth(0.5)
        canvas.line(2*cm, 2*cm, w - 2*cm, 2*cm)

        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(HexColor("#94a3b8"))
        canvas.drawCentredString(w/2, 1.3*cm, f"{sender['company']} | {sender['address']} | {sender['email']}")

        canvas.restoreState()

    doc = SimpleDocTemplate(
        filename, pagesize=A4,
        topMargin=4*cm, bottomMargin=3*cm,
        leftMargin=2*cm, rightMargin=2*cm,
    )

    styles = getSampleStyleSheet()
    story = []

    # Date
    story.append(Paragraph(date_str, styles["Normal"]))
    story.append(Spacer(1, 30))

    # Recipient
    story.append(Paragraph(f"<b>{recipient['name']}</b>", styles["Normal"]))
    story.append(Paragraph(recipient["address"], styles["Normal"]))
    story.append(Spacer(1, 20))

    # Subject
    story.append(Paragraph(f"<b>Re: {subject}</b>", styles["Normal"]))
    story.append(Spacer(1, 15))

    # Greeting
    story.append(Paragraph(f"Dear {recipient['name']},", styles["Normal"]))
    story.append(Spacer(1, 12))

    # Body paragraphs
    for para in body_paragraphs:
        story.append(Paragraph(para, styles["BodyText"]))

    # Closing
    story.append(Spacer(1, 25))
    story.append(Paragraph("Kind regards,", styles["Normal"]))
    story.append(Spacer(1, 30))
    story.append(Paragraph(f"<b>{sender['name']}</b>", styles["Normal"]))
    story.append(Paragraph(sender["title"], styles["Normal"]))

    doc.build(story, onFirstPage=letterhead, onLaterPages=letterhead)

# Usage:
generate_letter(
    "letter.pdf",
    sender={
        "company": "ACME Corp",
        "name": "John Smith",
        "title": "Managing Director",
        "address": "123 Business St, London, EC1A 1BB",
        "email": "john@acme.com"
    },
    recipient={
        "name": "Jane Wilson",
        "address": "456 Client Road\nManchester, M1 2AB",
    },
    subject="Partnership Proposal",
    body_paragraphs=[
        "Thank you for your interest in partnering with ACME Corp. "
        "We are delighted to present this proposal for your consideration.",

        "Our team has extensive experience in delivering high-quality "
        "solutions that drive business value. We believe a partnership "
        "would be mutually beneficial.",

        "Please find the detailed terms and conditions enclosed with "
        "this letter. We look forward to your response.",
    ],
    date_str="16 February 2026",
)
```

- Download: [letter.pdf](../assets/reportlab/letter.pdf)

<details>
<summary>Preview (PDF)</summary>

<object data="../assets/reportlab/letter.pdf" type="application/pdf" style="width:100%;height:600px;border:1px solid var(--border);border-radius:10px;background:var(--code-bg)">
    <p>Your browser can’t preview PDFs here. Download instead: <a href="../assets/reportlab/letter.pdf">letter.pdf</a></p>
</object>

</details>

---

## Best Practices & Patterns

### Project Structure

Organize your ReportLab project for maintainability:

```
my_reports/
├── main.py                # Entry point
├── templates/
│   ├── __init__.py
│   ├── base.py            # Base document template with headers/footers
│   ├── invoice.py         # Invoice generator
│   └── report.py          # Report generator
├── styles/
│   ├── __init__.py
│   └── custom_styles.py   # Reusable ParagraphStyle definitions
├── utils/
│   ├── __init__.py
│   ├── colors.py          # Brand colors
│   ├── fonts.py           # Font registration
│   └── helpers.py         # Common helpers
├── assets/
│   ├── fonts/             # TTF font files
│   ├── images/            # Logos, icons
│   └── data/              # CSV, JSON data files
├── output/                # Generated PDFs
└── requirements.txt
```

### Reusable Styles

Create a central style module:

```python
# styles/custom_styles.py

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.colors import HexColor

# Brand colors
BRAND_PRIMARY = HexColor("#6366f1")
BRAND_DARK = HexColor("#1e293b")
BRAND_MUTED = HexColor("#64748b")
BRAND_LIGHT = HexColor("#f1f5f9")
BRAND_BORDER = HexColor("#e2e8f0")

def get_custom_styles():
    """Return reusable stylesheet with brand styles."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        "BrandTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=24,
        textColor=BRAND_DARK,
        spaceAfter=16,
    ))

    styles.add(ParagraphStyle(
        "BrandBody",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=BRAND_DARK,
        alignment=TA_JUSTIFY,
        spaceBefore=4,
        spaceAfter=8,
    ))

    styles.add(ParagraphStyle(
        "BrandCaption",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=9,
        textColor=BRAND_MUTED,
        alignment=TA_CENTER,
        spaceBefore=4,
        spaceAfter=12,
    ))

    return styles
```

### Performance Tips

```python
# 1. Use pageCompression for smaller file sizes
c = canvas.Canvas("output.pdf", pageCompression=1)

# 2. Reuse Image objects for repeated images (logos, icons)
from reportlab.platypus import Image
logo = Image("logo.png", width=100, height=50)
# Use `logo` in multiple places instead of re-reading the file

# 3. For very large tables, build data incrementally
def generate_large_table(data_generator, output_path):
    doc = SimpleDocTemplate(output_path)
    story = []

    # Process data in chunks
    chunk = []
    for i, row in enumerate(data_generator()):
        chunk.append(row)
        if len(chunk) >= 50:  # Flush every 50 rows
            table = Table(chunk)
            story.append(table)
            chunk = []

    if chunk:
        table = Table(chunk)
        story.append(table)

    doc.build(story)

# 4. Use StringIO for in-memory PDF generation
from io import BytesIO

buffer = BytesIO()
c = canvas.Canvas(buffer)
c.drawString(100, 700, "In-memory PDF")
c.save()

pdf_bytes = buffer.getvalue()  # Get the PDF as bytes
buffer.close()
```

### Memory Management

```python
# For very large documents, use afterFlowable to track progress
class ProgressDoc(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        """Called after each flowable is rendered."""
        if hasattr(flowable, 'text'):
            # Track which flowable was just rendered
            pass

    def afterPage(self):
        """Called after each page is completed."""
        print(f"Page {self.page} rendered")

# Tip: Release large data structures after building tables
import gc

data = load_massive_dataset()
table = Table(data)
story.append(table)

del data  # Free memory
gc.collect()
```

---

## Troubleshooting & FAQ

### Common Errors

**`reportlab.lib.utils.ImageReaderError: Unable to read image`**

```python
# Problem: Image file not found or unsupported format
# Solution: Verify the path and install Pillow
# pip install Pillow

import os
image_path = "logo.png"
assert os.path.exists(image_path), f"Image not found: {image_path}"
```

**`KeyError: 'fontName'` or `Can't map font`**

```python
# Problem: Using a font that isn't registered
# Solution: Register the font first

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register before using
pdfmetrics.registerFont(TTFont("MyFont", "MyFont.ttf"))
```

**`LayoutError: Flowable too large on page`**

```python
# Problem: A table or image is larger than the available frame
# Solution 1: Reduce size
table = Table(data, colWidths=[3*cm, 3*cm, 3*cm])  # Smaller columns

# Solution 2: Use splitInRow or splitByRow for tables
table = Table(data, repeatRows=1, splitByRow=True)

# Solution 3: Increase page size or reduce margins
doc = SimpleDocTemplate("out.pdf", pagesize=A4,
                        leftMargin=1*cm, rightMargin=1*cm)
```

**`Canvas instance has no attribute 'xxx'`**

```python
# Problem: Calling c.save() before drawing, or typo in method name
# Common typos:
# c.drawstring()  → c.drawString()
# c.setfont()     → c.setFont()
# c.showpage()    → c.showPage()
```

### Font Issues

**Font not rendering correctly:**

```python
# 1. Verify the font is registered
from reportlab.pdfbase import pdfmetrics
print(pdfmetrics.getRegisteredFontNames())

# 2. Verify the font file exists
import os
print(os.path.exists("MyFont.ttf"))

# 3. Use absolute paths
import os
font_dir = os.path.join(os.path.dirname(__file__), "assets", "fonts")
pdfmetrics.registerFont(TTFont("MyFont", os.path.join(font_dir, "MyFont.ttf")))
```

**Font embedding — ensuring fonts are included in the PDF:**

```python
# TrueType fonts registered with pdfmetrics.registerFont() are
# automatically embedded. The 14 standard fonts are NOT embedded
# (they're expected to exist in every PDF reader).

# To ensure a specific look, always use registered TTF fonts
# rather than the standard 14.
```

### Layout Debugging

```python
# 1. Show frame boundaries
doc = SimpleDocTemplate("debug.pdf", showBoundary=1)

# 2. Draw coordinate guides on canvas
def draw_grid(canvas, page_size):
    """Draw a coordinate grid for debugging."""
    w, h = page_size
    canvas.saveState()
    canvas.setStrokeColorRGB(0.9, 0.9, 0.9)
    canvas.setFont("Helvetica", 6)

    # Vertical lines every cm
    for x in range(0, int(w), 28):  # ~1cm
        canvas.line(x, 0, x, h)
        canvas.drawString(x + 2, 5, str(x))

    # Horizontal lines every cm
    for y in range(0, int(h), 28):
        canvas.line(0, y, w, y)
        canvas.drawString(2, y + 2, str(y))

    canvas.restoreState()

# 3. Print flowable dimensions
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()

p = Paragraph("Test", styles["BodyText"])
pw, ph = p.wrap(400, 800)  # available width, height
print(f"Paragraph: {pw}w x {ph}h points")
```

### Platform-Specific Issues

**Windows:**
- Paths with spaces: Use raw strings `r"C:\My Folder\file.pdf"` or forward slashes
- Long filenames: Keep paths under 260 characters or use `\\?\` prefix

**macOS:**
- `libfreetype` warnings: Install via `brew install freetype` if C extensions need it
- Permission errors: Check write permissions in the output directory

**Linux:**
- Missing C extensions: `sudo apt install python3-dev build-essential libfreetype6-dev`
- Font discovery: Place fonts in `~/.local/share/fonts/` or register with full path

### Frequently Asked Questions

**Q: How do I add a table of contents?**

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

styles = getSampleStyleSheet()

# Create TOC styles
toc = TableOfContents()
toc.levelStyles = [
    ParagraphStyle(name="TOC1", fontName="Helvetica-Bold", fontSize=12,
                   leftIndent=20, spaceBefore=5),
    ParagraphStyle(name="TOC2", fontName="Helvetica", fontSize=10,
                   leftIndent=40, spaceBefore=3),
]

# Custom doc template that notifies TOC of headings
class MyDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            style = flowable.style.name
            if style == "Heading1":
                level = 0
                text = flowable.getPlainText()
                self.notify("TOCEntry", (level, text, self.page))
            elif style == "Heading2":
                level = 1
                text = flowable.getPlainText()
                self.notify("TOCEntry", (level, text, self.page))

doc = MyDocTemplate("toc_example.pdf")
story = [toc, PageBreak()]
# ... add your content with Heading1 and Heading2 styles ...
# Build TWICE for TOC page numbers to resolve:
doc.multiBuild(story)
```

**Q: Can I merge or append existing PDFs?**

```python
# ReportLab focuses on creation, not manipulation.
# Use PyPDF2 or pypdf for merging:
# pip install pypdf

from pypdf import PdfMerger

merger = PdfMerger()
merger.append("first.pdf")
merger.append("second.pdf")
merger.write("merged.pdf")
merger.close()
```

**Q: How do I generate PDFs in a web framework (Flask/Django)?**

```python
# Flask example:
from flask import Flask, send_file
from io import BytesIO
from reportlab.pdfgen import canvas

app = Flask(__name__)

@app.route("/generate-pdf")
def generate_pdf():
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.drawString(100, 700, "PDF from Flask!")
    c.save()
    buffer.seek(0)
    return send_file(buffer, mimetype="application/pdf",
                     download_name="report.pdf")
```

**Q: How do I add page numbers like "Page 1 of 5"?**

```python
# Use a two-pass approach or a custom canvas:
from reportlab.pdfgen import canvas as canvas_module
from reportlab.lib.pagesizes import A4

class PageNumCanvas(canvas_module.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        super().showPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.setFont("Helvetica", 9)
        w, h = A4
        self.drawCentredString(
            w / 2, 30,
            f"Page {self._pageNumber} of {page_count}"
        )

# Use with Platypus:
doc = SimpleDocTemplate("output.pdf")
doc.build(story, canvasmaker=PageNumCanvas)
```

---

## API Quick Reference

### Canvas Methods

| Method | Description |
|--------|-------------|
| `drawString(x, y, text)` | Draw text at (x, y) left-aligned |
| `drawCentredString(x, y, text)` | Draw centered text |
| `drawRightString(x, y, text)` | Draw right-aligned text |
| `setFont(name, size)` | Set current font |
| `setFillColor(color)` | Set fill color |
| `setFillColorRGB(r, g, b)` | Set fill color by RGB |
| `setStrokeColor(color)` | Set stroke color |
| `setStrokeColorRGB(r, g, b)` | Set stroke color by RGB |
| `setLineWidth(width)` | Set line width |
| `setLineCap(mode)` | Line cap: 0=butt, 1=round, 2=square |
| `setLineJoin(mode)` | Line join: 0=miter, 1=round, 2=bevel |
| `setDash(array, phase)` | Set dash pattern |
| `line(x1, y1, x2, y2)` | Draw a line |
| `rect(x, y, w, h, fill, stroke)` | Draw rectangle |
| `roundRect(x, y, w, h, r, fill, stroke)` | Draw rounded rectangle |
| `circle(x, y, r, fill, stroke)` | Draw circle |
| `ellipse(x1, y1, x2, y2, fill, stroke)` | Draw ellipse |
| `wedge(x1, y1, x2, y2, startAng, extent, fill)` | Draw wedge |
| `drawImage(image, x, y, w, h, ...)` | Draw image |
| `beginPath()` | Start a new path |
| `drawPath(path, fill, stroke)` | Draw a path |
| `clipPath(path, stroke, fill)` | Set clipping region |
| `beginText(x, y)` | Start a text object |
| `drawText(textObj)` | Render a text object |
| `saveState()` | Push graphics state |
| `restoreState()` | Pop graphics state |
| `translate(dx, dy)` | Move origin |
| `rotate(degrees)` | Rotate canvas |
| `scale(sx, sy)` | Scale canvas |
| `skew(ax, ay)` | Skew canvas |
| `showPage()` | Finish page, start new one |
| `save()` | Finalize and write PDF |
| `setTitle(title)` | Set PDF title metadata |
| `setAuthor(author)` | Set PDF author metadata |
| `setSubject(subject)` | Set PDF subject metadata |
| `bookmarkPage(key)` | Create bookmark at current page |
| `addOutlineEntry(title, key, level)` | Add outline/bookmark entry |
| `linkURL(url, rect, relative)` | Add hyperlink |
| `getPageNumber()` | Get current page number |

### Platypus Flowables

| Flowable | Usage |
|----------|-------|
| `Paragraph(text, style)` | Styled paragraph |
| `Spacer(width, height)` | Blank space |
| `Table(data, colWidths, rowHeights, repeatRows)` | Data table |
| `Image(filename, width, height)` | Image |
| `PageBreak()` | Force page break |
| `CondPageBreak(height)` | Conditional page break |
| `KeepTogether(flowables)` | Keep group together |
| `HRFlowable(width, thickness, color)` | Horizontal rule |
| `ListFlowable(items, bulletType)` | List (ordered/unordered) |
| `Preformatted(text, style)` | Preformatted text |
| `XPreformatted(text, style)` | Preformatted with markup |
| `NextPageTemplate(name)` | Switch page template |
| `TableOfContents()` | Auto-generated TOC |

### Common Imports Cheat Sheet

```python
# Canvas and page sizes
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A3, LETTER, landscape, portrait

# Units
from reportlab.lib.units import inch, cm, mm, pica

# Colors
from reportlab.lib.colors import (
    HexColor, Color, CMYKColor,
    red, blue, green, black, white, gray
)

# Platypus (high-level layout)
from reportlab.platypus import (
    SimpleDocTemplate, BaseDocTemplate,
    Paragraph, Spacer, Table, TableStyle,
    Image, PageBreak, KeepTogether, CondPageBreak,
    HRFlowable, ListFlowable, Frame, PageTemplate,
    NextPageTemplate
)

# Styles
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

# Fonts
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Charts
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.legends import Legend

# Barcodes
from reportlab.graphics.barcode.code128 import Code128
from reportlab.graphics.barcode.qr import QrCodeWidget

# Encryption
from reportlab.lib.pdfencrypt import StandardEncryption
```

---

## Summary

ReportLab is a comprehensive PDF generation toolkit for Python, offering:

- **Canvas API** — Low-level drawing with precise control over every coordinate, shape, and text placement
- **Platypus Framework** — High-level document layout engine with automatic page flow, styles, and templates
- **Tables** — Full-featured table generation with styling, spanning, alternating colors, and multi-page support
- **Charts** — Built-in pie, bar, and line charts with customizable colors, legends, and labels
- **Images** — JPEG, PNG with automatic sizing, aspect ratio preservation, and URL support
- **Fonts** — TrueType font embedding, Unicode support, and font family registration
- **Barcodes & QR** — Code128, Code39, EAN, and QR code generation
- **Security** — PDF encryption, password protection, and permission control
- **Metadata** — Title, author, bookmarks, outlines, and hyperlinks

**Key tips:**

1. Use **Platypus** (`SimpleDocTemplate` + flowables) for most document generation tasks
2. Use **Canvas** for custom graphics, backgrounds, and pixel-perfect positioning
3. Always use `saveState()` / `restoreState()` when modifying canvas state
4. Use `repeatRows=1` for tables that span multiple pages
5. Register TrueType fonts for consistent rendering across all PDF readers
6. Use `BytesIO` for in-memory PDF generation in web frameworks
7. Test with `showBoundary=1` to debug frame and layout issues

**Resources:**

- [Official Docs](https://docs.reportlab.com/)
- [User Guide PDF](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- [PyPI Package](https://pypi.org/project/reportlab/)
- [GitHub Repository](https://github.com/MrBitBucket/reportlab-mirror)
