#!/usr/bin/env python3
"""Generate static PDF assets for the ReportLab documentation page.

This creates PDFs under: site/assets/reportlab/

Notes:
- Uses only built-in fonts and no external image/font files.
- Intended for maintainers to refresh embedded previews in reportlab.md.
"""

from __future__ import annotations

from pathlib import Path


ASSETS_DIR = Path(__file__).resolve().parents[1] / "site" / "assets" / "reportlab"


def _ensure_dir() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)


def _p(name: str) -> str:
    return str(ASSETS_DIR / name)


def make_test_pdf() -> None:
    from reportlab.pdfgen import canvas

    c = canvas.Canvas(_p("test.pdf"))
    c.drawString(100, 750, "ReportLab is working!")
    c.save()


def make_hello_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("hello.pdf"), pagesize=A4)

    c.setFont("Helvetica", 24)
    c.drawString(100, 750, "Hello, ReportLab!")

    c.setFont("Helvetica", 14)
    c.drawString(100, 710, "This is your first PDF document.")

    c.setStrokeColorRGB(0.2, 0.3, 0.7)
    c.setLineWidth(2)
    c.line(100, 700, 495, 700)

    c.setFillColorRGB(0.9, 0.95, 1.0)
    c.setStrokeColorRGB(0.2, 0.3, 0.7)
    c.roundRect(100, 600, 395, 80, 10, fill=1)

    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica", 12)
    c.drawString(120, 655, "ReportLab gives you complete control over")
    c.drawString(120, 638, "every pixel of your PDF output.")
    c.drawString(120, 618, "Coordinates start from the bottom-left corner.")

    c.save()


def make_text_demo_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("text_demo.pdf"), pagesize=A4)
    w, h = A4

    c.setFont("Helvetica", 16)
    c.drawString(72, h - 72, "drawString: Left-aligned text")

    c.drawCentredString(w / 2, h - 110, "drawCentredString: Centered on page")

    c.drawRightString(w - 72, h - 148, "drawRightString: Right-aligned")

    c.saveState()
    c.translate(72, h - 250)
    c.rotate(45)
    c.drawString(0, 0, "Rotated 45 degrees!")
    c.restoreState()

    fonts = [
        "Helvetica",
        "Helvetica-Bold",
        "Helvetica-Oblique",
        "Times-Roman",
        "Times-Bold",
        "Courier",
        "Courier-Bold",
    ]

    y = h - 320
    for font in fonts:
        c.setFont(font, 14)
        c.drawString(72, y, f"{font}: The quick brown fox jumps over the lazy dog")
        y -= 24

    c.save()


def make_shapes_demo_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm

    c = canvas.Canvas(_p("shapes_demo.pdf"), pagesize=A4)
    _, h = A4

    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.line(2 * cm, h - 3 * cm, 19 * cm, h - 3 * cm)

    c.setStrokeColorRGB(0.2, 0.4, 0.8)
    c.setLineWidth(4)
    c.line(2 * cm, h - 4 * cm, 19 * cm, h - 4 * cm)

    c.setDash(6, 3)
    c.line(2 * cm, h - 5 * cm, 19 * cm, h - 5 * cm)
    c.setDash()

    c.setStrokeColorRGB(0.8, 0.2, 0.2)
    c.setLineWidth(2)
    path = c.beginPath()
    path.moveTo(2 * cm, h - 8 * cm)
    path.lineTo(6 * cm, h - 6 * cm)
    path.lineTo(10 * cm, h - 8 * cm)
    path.lineTo(14 * cm, h - 6 * cm)
    path.lineTo(18 * cm, h - 8 * cm)
    c.drawPath(path)

    c.save()


def make_rectangles_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm

    c = canvas.Canvas(_p("rectangles.pdf"), pagesize=A4)
    _, h = A4

    c.rect(2 * cm, h - 5 * cm, 8 * cm, 3 * cm)

    c.setFillColorRGB(0.85, 0.92, 1.0)
    c.setStrokeColorRGB(0.2, 0.4, 0.8)
    c.rect(12 * cm, h - 5 * cm, 6 * cm, 3 * cm, fill=1)

    c.setFillColorRGB(1.0, 0.95, 0.85)
    c.setStrokeColorRGB(0.8, 0.5, 0.1)
    c.roundRect(2 * cm, h - 10 * cm, 8 * cm, 3 * cm, radius=10, fill=1)

    c.setFillColorRGB(0.9, 0.85, 1.0)
    c.setStrokeColorRGB(0.9, 0.85, 1.0)
    c.roundRect(12 * cm, h - 10 * cm, 6 * cm, 3 * cm, radius=15, fill=1, stroke=0)

    c.save()


def make_circles_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm

    c = canvas.Canvas(_p("circles.pdf"), pagesize=A4)
    _, h = A4

    c.setStrokeColorRGB(0.2, 0.6, 0.3)
    c.setFillColorRGB(0.85, 1.0, 0.9)
    c.circle(6 * cm, h - 5 * cm, 2 * cm, fill=1)

    c.setStrokeColorRGB(0.6, 0.2, 0.6)
    c.setFillColorRGB(0.95, 0.85, 1.0)
    c.ellipse(11 * cm, h - 7 * cm, 18 * cm, h - 3 * cm, fill=1)

    c.setFillColorRGB(1.0, 0.9, 0.8)
    c.setStrokeColorRGB(0.8, 0.4, 0.1)
    c.wedge(3 * cm, h - 14 * cm, 9 * cm, h - 8 * cm, startAng=0, extent=120, fill=1)

    c.save()


def make_paths_pdf() -> None:
    import math

    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm

    c = canvas.Canvas(_p("paths.pdf"), pagesize=A4)
    _, h = A4

    p = c.beginPath()
    cx, cy, r = 10 * cm, h - 8 * cm, 3 * cm
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

    p2 = c.beginPath()
    p2.moveTo(3 * cm, h - 16 * cm)
    p2.lineTo(6 * cm, h - 12 * cm)
    p2.lineTo(9 * cm, h - 16 * cm)
    p2.close()

    c.setFillColorRGB(0.8, 0.9, 1.0)
    c.setStrokeColorRGB(0.2, 0.4, 0.8)
    c.drawPath(p2, fill=1)

    p3 = c.beginPath()
    p3.moveTo(12 * cm, h - 16 * cm)
    p3.curveTo(13 * cm, h - 12 * cm, 16 * cm, h - 12 * cm, 18 * cm, h - 16 * cm)
    c.setStrokeColorRGB(0.8, 0.2, 0.2)
    c.setLineWidth(3)
    c.drawPath(p3)

    c.save()


def make_colors_demo_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import (
        red,
        blue,
        green,
        HexColor,
        CMYKColor,
        Color,
    )
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("colors_demo.pdf"), pagesize=A4)
    _, h = A4

    c.setFillColor(red)
    c.rect(72, h - 100, 60, 40, fill=1)

    c.setFillColor(blue)
    c.rect(142, h - 100, 60, 40, fill=1)

    c.setFillColor(green)
    c.rect(212, h - 100, 60, 40, fill=1)

    c.setFillColorRGB(0.95, 0.3, 0.1)
    c.rect(72, h - 160, 60, 40, fill=1)

    c.setFillColor(HexColor("#6366f1"))
    c.rect(142, h - 160, 60, 40, fill=1)

    cmyk = CMYKColor(0.1, 0.8, 0.9, 0.0)
    c.setFillColor(cmyk)
    c.rect(212, h - 160, 60, 40, fill=1)

    c.setFillColor(Color(0, 0, 1, alpha=0.3))
    c.rect(72, h - 220, 200, 40, fill=1)

    c.save()


def make_line_styles_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("line_styles.pdf"), pagesize=A4)
    _, h = A4
    x1, x2 = 72, 500

    c.setLineWidth(1)
    c.line(x1, h - 80, x2, h - 80)
    c.drawString(x1, h - 75, "Solid (default)")

    c.setLineWidth(4)
    c.line(x1, h - 120, x2, h - 120)
    c.drawString(x1, h - 115, "Thick (4pt)")

    c.setLineWidth(1)
    c.setDash(6, 3)
    c.line(x1, h - 160, x2, h - 160)
    c.drawString(x1, h - 155, "Dashed (6, 3)")

    c.setDash([1, 2, 6, 2])
    c.line(x1, h - 200, x2, h - 200)
    c.drawString(x1, h - 195, "Dot-dash pattern")

    c.setDash()

    c.setLineWidth(8)
    c.setLineCap(0)
    c.line(x1, h - 260, x2, h - 260)
    c.setFont("Helvetica", 10)
    c.drawString(x1, h - 248, "Butt cap (0)")

    c.setLineCap(1)
    c.line(x1, h - 300, x2, h - 300)
    c.drawString(x1, h - 288, "Round cap (1)")

    c.setLineCap(2)
    c.line(x1, h - 340, x2, h - 340)
    c.drawString(x1, h - 328, "Square cap (2)")

    c.setLineWidth(6)
    c.setLineCap(0)

    c.setLineJoin(0)
    p = c.beginPath()
    p.moveTo(x1, h - 400)
    p.lineTo(200, h - 370)
    p.lineTo(300, h - 400)
    c.drawPath(p)
    c.setFont("Helvetica", 10)
    c.drawString(x1, h - 415, "Miter join (0)")

    c.setLineJoin(1)
    p = c.beginPath()
    p.moveTo(x1, h - 460)
    p.lineTo(200, h - 430)
    p.lineTo(300, h - 460)
    c.drawPath(p)
    c.drawString(x1, h - 475, "Round join (1)")

    c.setLineJoin(2)
    p = c.beginPath()
    p.moveTo(x1, h - 520)
    p.lineTo(200, h - 490)
    p.lineTo(300, h - 520)
    c.drawPath(p)
    c.drawString(x1, h - 535, "Bevel join (2)")

    c.save()


def make_transforms_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm

    c = canvas.Canvas(_p("transforms.pdf"), pagesize=A4)
    _, h = A4

    c.saveState()
    c.translate(5 * cm, h - 6 * cm)
    c.rect(0, 0, 3 * cm, 2 * cm, fill=0)
    c.drawString(5, 10, "Translated")
    c.restoreState()

    c.saveState()
    c.translate(12 * cm, h - 6 * cm)
    c.rotate(30)
    c.rect(0, 0, 3 * cm, 2 * cm, fill=0)
    c.drawString(5, 10, "Rotated 30°")
    c.restoreState()

    c.saveState()
    c.translate(5 * cm, h - 12 * cm)
    c.scale(1.5, 1.5)
    c.rect(0, 0, 2 * cm, 1.5 * cm, fill=0)
    c.drawString(5, 10, "Scaled 1.5x")
    c.restoreState()

    c.saveState()
    c.translate(12 * cm, h - 12 * cm)
    c.skew(15, 0)
    c.rect(0, 0, 3 * cm, 2 * cm, fill=0)
    c.drawString(5, 10, "Skewed")
    c.restoreState()

    c.save()


def make_clipping_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm

    c = canvas.Canvas(_p("clipping.pdf"), pagesize=A4)
    _, h = A4

    c.saveState()
    p = c.beginPath()
    p.circle(10 * cm, h - 8 * cm, 3 * cm)
    c.clipPath(p, stroke=0)

    c.setStrokeColorRGB(0.2, 0.4, 0.8)
    for i in range(0, 25):
        x = (5 + i * 0.5) * cm
        c.line(x, h - 14 * cm, x, h - 2 * cm)
        y = (h - 14 * cm) + i * 0.5 * cm
        c.line(5 * cm, y, 15 * cm, y)

    c.restoreState()
    c.save()


def make_multipage_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("multipage.pdf"), pagesize=A4)
    w, h = A4

    for page_num in range(1, 6):
        c.setFont("Helvetica-Bold", 24)
        c.drawString(72, h - 72, f"Page {page_num} of 5")

        c.setFont("Helvetica", 12)
        c.drawString(72, h - 110, f"This is the content for page {page_num}.")

        c.setFont("Helvetica", 9)
        c.drawCentredString(w / 2, 30, f"— {page_num} —")

        if page_num < 5:
            c.showPage()

    c.save()


def make_text_basics_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("text_basics.pdf"), pagesize=A4)
    w, h = A4

    c.setFont("Helvetica", 14)
    c.drawString(72, h - 72, "This is drawString (left-aligned)")
    c.drawCentredString(w / 2, h - 110, "This is drawCentredString (centered)")
    c.drawRightString(w - 72, h - 148, "This is drawRightString (right)")

    c.save()


def make_text_align_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("text_align.pdf"), pagesize=A4)
    w, h = A4

    c.setDash(2, 2)
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.line(w / 2, h, w / 2, 0)
    c.setDash()

    c.setFont("Helvetica", 14)
    c.drawString(w / 2, h - 100, "← Left from center")
    c.drawCentredString(w / 2, h - 140, "Centered")
    c.drawRightString(w / 2, h - 180, "Right to center →")

    c.save()


def make_textobject_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("textobject.pdf"), pagesize=A4)
    _, h = A4

    text = c.beginText(72, h - 72)
    text.setFont("Helvetica", 12)
    text.setFillColorRGB(0, 0, 0)
    text.setLeading(18)

    paragraphs = [
        "ReportLab's TextObject is ideal for multi-line text blocks.",
        "Each call to textLine() advances to the next line automatically.",
        "",
        "You can change fonts and colors mid-stream:",
    ]
    for line in paragraphs:
        text.textLine(line)

    text.setFont("Helvetica-Bold", 12)
    text.setFillColorRGB(0.2, 0.4, 0.8)
    text.textLine("This line is bold and blue.")

    text.setFont("Courier", 11)
    text.setFillColorRGB(0.4, 0.4, 0.4)
    text.textLine("And this is in Courier.")

    c.drawText(text)
    c.save()


def make_output_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("output.pdf"), pagesize=A4)
    _, h = A4

    c.drawString(100, h - 142, "Text on page 1")

    c.showPage()
    c.drawString(100, h - 142, "Text on page 2")

    c.save()


def make_state_demo_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("state_demo.pdf"), pagesize=A4)
    _, h = A4

    c.saveState()
    c.setFont("Helvetica-Bold", 20)
    c.setFillColorRGB(1, 0, 0)
    c.drawString(100, h - 142, "Bold Red Text")
    c.restoreState()

    c.drawString(100, h - 172, "Back to defaults")
    c.save()


def make_font_list_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

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

    c = canvas.Canvas(_p("font_list.pdf"), pagesize=A4)
    _, h = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, h - 92, "Available Standard Fonts")

    y = h - 132
    for font_name in standard_fonts:
        c.setFont(font_name, 12)
        c.drawString(72, y, f"{font_name}: The quick brown fox jumps over the lazy dog")
        y -= 20

    c.save()


def make_platypus_intro_pdf() -> None:
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4

    doc = SimpleDocTemplate(_p("platypus_intro.pdf"), pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("My First Platypus Document", styles["Title"]))
    story.append(Spacer(1, 20))
    story.append(
        Paragraph(
            "Platypus automatically handles page breaks, text wrapping, "
            "and layout for you. Just add flowable objects to the story "
            "and call build().",
            styles["BodyText"],
        )
    )
    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            "This is a second paragraph. It will wrap naturally within "
            "the page margins and overflow to the next page if needed.",
            styles["BodyText"],
        )
    )

    doc.build(story)


def make_barcodes_platypus_pdf() -> None:
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.graphics.barcode.qr import QrCodeWidget
    from reportlab.graphics.barcode import code128
    from reportlab.graphics.shapes import Drawing

    doc = SimpleDocTemplate(_p("barcodes_platypus.pdf"), pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Barcode Examples", styles["Title"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph("Code128 Barcode:", styles["Heading2"]))
    barcode = code128.Code128(
        "ITEM-2026-001",
        barWidth=1.2,
        barHeight=40,
        humanReadable=True,
    )
    story.append(barcode)
    story.append(Spacer(1, 20))

    story.append(Paragraph("QR Code:", styles["Heading2"]))
    qr = QrCodeWidget("https://www.reportlab.com")
    qr.barWidth = 100
    qr.barHeight = 100

    d2 = Drawing(120, 120)
    d2.add(qr)
    story.append(d2)

    doc.build(story)


def make_transparency_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.colors import Color

    c = canvas.Canvas(_p("transparency.pdf"), pagesize=A4)
    _, _ = A4

    colors = [
        Color(1, 0, 0, alpha=0.4),
        Color(0, 1, 0, alpha=0.4),
        Color(0, 0, 1, alpha=0.4),
    ]
    positions = [(250, 500), (320, 500), (285, 560)]

    for color, (x, y) in zip(colors, positions):
        c.setFillColor(color)
        c.circle(x, y, 80, fill=1, stroke=0)

    c.save()


def make_gradient_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.colors import Color

    c = canvas.Canvas(_p("gradient.pdf"), pagesize=A4)
    _, _ = A4

    x, y, gw, gh = 72, 400, 400, 200
    steps = 100

    for i in range(steps):
        t = i / steps
        r = 0.39 + t * 0.2
        g = 0.40 + t * 0.35
        b = 0.95 - t * 0.1

        c.setFillColor(Color(r, g, b))
        stripe_h = gh / steps
        c.rect(x, y + i * stripe_h, gw, stripe_h + 1, fill=1, stroke=0)

    c.save()


def make_metadata_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("metadata.pdf"), pagesize=A4)
    _, h = A4

    c.setTitle("My Report Title")
    c.setAuthor("John Doe")
    c.setSubject("Monthly Sales Report - January 2026")
    c.setCreator("ReportLab PDF Generator")
    c.setKeywords(["report", "sales", "2026", "pdf"])

    c.drawString(100, h - 142, "Check File > Properties in your PDF viewer!")
    c.save()


def make_encrypted_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.pdfencrypt import StandardEncryption

    try:
        enc = StandardEncryption(
            userPassword="reader123",
            ownerPassword="admin456",
            canPrint=True,
            canModify=False,
            canCopy=False,
            canAnnotate=False,
            strength=128,
        )
    except Exception:
        enc = StandardEncryption(
            userPassword="reader123",
            ownerPassword="admin456",
            canPrint=True,
            canModify=False,
            canCopy=False,
            canAnnotate=False,
            strength=40,
        )

    c = canvas.Canvas(_p("encrypted.pdf"), pagesize=A4, encrypt=enc)
    _, h = A4
    c.drawString(100, h - 142, "This PDF is password-protected!")
    c.save()


def make_bookmarks_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    c = canvas.Canvas(_p("bookmarks.pdf"), pagesize=A4)
    _, h = A4

    c.bookmarkPage("page1")
    c.addOutlineEntry("Chapter 1 — Introduction", "page1", level=0)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(72, h - 72, "Chapter 1: Introduction")
    c.setFont("Helvetica", 12)
    c.drawString(72, h - 110, "Welcome to the document.")

    c.showPage()

    c.bookmarkPage("page2")
    c.addOutlineEntry("Chapter 2 — Details", "page2", level=0)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(72, h - 72, "Chapter 2: Details")

    c.bookmarkPage("page2_sect1")
    c.addOutlineEntry("Section 2.1 — Data", "page2_sect1", level=1)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, h - 130, "Section 2.1: Data")

    c.showPage()

    c.bookmarkPage("page3")
    c.addOutlineEntry("Chapter 3 — Conclusion", "page3", level=0)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(72, h - 72, "Chapter 3: Conclusion")

    c.save()


def make_hyperlinks_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.colors import HexColor

    c = canvas.Canvas(_p("hyperlinks.pdf"), pagesize=A4)
    w, h = A4

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#6366f1"))
    c.drawString(72, h - 72, "Click here to visit ReportLab")

    c.linkURL(
        "https://www.reportlab.com/",
        (72, h - 78, 340, h - 58),
        relative=0,
    )

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#000000"))
    c.drawString(72, h - 120, "Go to Chapter 2")
    c.linkRect(
        "Go to Chapter 2",
        "chapter2",
        (72, h - 126, 240, h - 106),
        relative=0,
    )

    c.showPage()

    c.bookmarkPage("chapter2")
    c.setFont("Helvetica-Bold", 20)
    c.drawString(72, h - 72, "Chapter 2")

    c.save()


def make_invoice_pdf() -> None:
    from datetime import date

    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib.colors import HexColor, white
    from reportlab.lib.enums import TA_RIGHT

    invoice_data = {
        "number": "INV-2026-001",
        "date": str(date(2026, 2, 16)),
        "due_date": str(date(2026, 3, 18)),
        "client_name": "Widget Co Ltd",
        "client_address": "456 Client Road, Manchester, M1 2AB",
        "items": [
            {"description": "Web Development - Homepage", "qty": 1, "price": 2500.00},
            {"description": "Web Development - API Integration", "qty": 1, "price": 1800.00},
            {"description": "UI/UX Design - Mockups", "qty": 3, "price": 450.00},
            {"description": "Hosting Setup (Annual)", "qty": 1, "price": 350.00},
        ],
    }

    doc = SimpleDocTemplate(
        _p("invoice.pdf"),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            "RightAligned",
            parent=styles["Normal"],
            alignment=TA_RIGHT,
        )
    )

    story = []

    header_data = [
        [
            Paragraph(
                "<b>ACME Corp</b><br/>123 Business St<br/>London, EC1A 1BB<br/>accounts@acme.com",
                styles["Normal"],
            ),
            Paragraph(
                f"<b>INVOICE</b><br/>"
                f"Invoice #: {invoice_data['number']}<br/>"
                f"Date: {invoice_data['date']}<br/>"
                f"Due: {invoice_data['due_date']}",
                styles["RightAligned"],
            ),
        ]
    ]
    header_table = Table(header_data, colWidths=[9 * cm, 8 * cm])
    header_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.append(header_table)
    story.append(Spacer(1, 20))

    story.append(Paragraph("<b>Bill To:</b>", styles["Normal"]))
    story.append(Paragraph(invoice_data["client_name"], styles["Normal"]))
    story.append(Paragraph(invoice_data["client_address"], styles["Normal"]))
    story.append(Spacer(1, 20))

    items_header = ["Description", "Qty", "Unit Price", "Total"]
    items_data = [items_header]

    subtotal = 0.0
    for item in invoice_data["items"]:
        total = float(item["qty"]) * float(item["price"])
        subtotal += total
        items_data.append(
            [
                item["description"],
                str(item["qty"]),
                f"£{item['price']:.2f}",
                f"£{total:.2f}",
            ]
        )

    vat = subtotal * 0.20
    grand_total = subtotal + vat

    items_data.append(["", "", "Subtotal:", f"£{subtotal:.2f}"])
    items_data.append(["", "", "VAT (20%):", f"£{vat:.2f}"])
    items_data.append(["", "", "TOTAL:", f"£{grand_total:.2f}"])

    items_table = Table(items_data, colWidths=[8 * cm, 2 * cm, 3.5 * cm, 3.5 * cm])
    items_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
                ("TEXTCOLOR", (0, 0), (-1, 0), white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("ALIGN", (1, 0), (-1, 0), "CENTER"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("GRID", (0, 0), (-1, -4), 0.5, HexColor("#e2e8f0")),
                ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
                ("FONTNAME", (2, -3), (-1, -1), "Helvetica-Bold"),
                ("LINEABOVE", (2, -3), (-1, -3), 1, HexColor("#e2e8f0")),
                ("FONTNAME", (2, -1), (-1, -1), "Helvetica-Bold"),
                ("FONTSIZE", (2, -1), (-1, -1), 12),
                ("BACKGROUND", (2, -1), (-1, -1), HexColor("#f1f5f9")),
            ]
        )
    )
    story.append(items_table)
    story.append(Spacer(1, 30))

    story.append(Paragraph("<b>Notes:</b>", styles["Normal"]))
    story.append(
        Paragraph(
            "Payment due within 30 days. Please reference the invoice number "
            "when making payment. Bank details: Sort Code 12-34-56, Account 12345678.",
            styles["BodyText"],
        )
    )

    doc.build(story)


def make_sales_report_pdf() -> None:
    from datetime import date

    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
        PageBreak,
    )
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib.colors import HexColor, white

    output_path = _p("sales_report.pdf")
    title = "Q1 Sales Report"

    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Spacer(1, 200))
    story.append(Paragraph(title, styles["Title"]))
    story.append(Spacer(1, 20))
    story.append(
        Paragraph(
            f"Generated on {date.today().strftime('%d %B %Y')}",
            styles["Normal"],
        )
    )
    story.append(PageBreak())

    headers = ["Date", "Region", "Product", "Units", "Revenue"]
    rows = []
    regions = ["North", "South", "East", "West"]
    products = ["Widget", "Gadget", "Service"]
    for i in range(1, 61):
        region = regions[i % len(regions)]
        product = products[i % len(products)]
        units = 5 + (i % 17)
        revenue = units * (49.99 + (i % 5) * 10)
        rows.append([f"2026-01-{(i % 28) + 1:02d}", region, product, str(units), f"£{revenue:.2f}"])

    story.append(Paragraph("Summary", styles["Heading1"]))
    story.append(Paragraph(f"Total records: <b>{len(rows)}</b>", styles["BodyText"]))
    story.append(Paragraph(f"Columns: <b>{', '.join(headers)}</b>", styles["BodyText"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph("Data", styles["Heading1"]))
    story.append(Spacer(1, 10))

    data = [headers] + rows
    num_cols = len(headers)
    col_width = (A4[0] - 4 * cm) / num_cols

    table = Table(data, colWidths=[col_width] * num_cols, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
                ("TEXTCOLOR", (0, 0), (-1, 0), white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [HexColor("#fff"), HexColor("#f8fafc")],
                ),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(table)

    doc.build(story)


def make_certificate_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import landscape, A4
    from reportlab.lib.units import cm
    from reportlab.lib.colors import HexColor

    filename = _p("certificate.pdf")
    name = "Alice Johnson"
    course = "Advanced Python Programming"
    date_str = "16 February 2026"
    cert_id = "CERT-2026-00142"

    page = landscape(A4)
    c = canvas.Canvas(filename, pagesize=page)
    w, h = page

    c.setStrokeColor(HexColor("#6366f1"))
    c.setLineWidth(3)
    c.rect(1.5 * cm, 1.5 * cm, w - 3 * cm, h - 3 * cm)
    c.setLineWidth(1)
    c.rect(2 * cm, 2 * cm, w - 4 * cm, h - 4 * cm)

    for x, y in [
        (2.5 * cm, h - 2.5 * cm),
        (w - 2.5 * cm, h - 2.5 * cm),
        (2.5 * cm, 2.5 * cm),
        (w - 2.5 * cm, 2.5 * cm),
    ]:
        c.setFillColor(HexColor("#6366f1"))
        c.circle(x, y, 4, fill=1)

    c.setFont("Times-Bold", 36)
    c.setFillColor(HexColor("#1e293b"))
    c.drawCentredString(w / 2, h - 5 * cm, "Certificate of Completion")

    c.setStrokeColor(HexColor("#6366f1"))
    c.setLineWidth(1.5)
    c.line(w / 2 - 8 * cm, h - 5.8 * cm, w / 2 + 8 * cm, h - 5.8 * cm)

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#64748b"))
    c.drawCentredString(w / 2, h - 7.5 * cm, "This certifies that")

    c.setFont("Times-BoldItalic", 32)
    c.setFillColor(HexColor("#1e293b"))
    c.drawCentredString(w / 2, h - 9.5 * cm, name)

    c.setStrokeColor(HexColor("#e2e8f0"))
    c.line(w / 2 - 6 * cm, h - 10 * cm, w / 2 + 6 * cm, h - 10 * cm)

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#64748b"))
    c.drawCentredString(w / 2, h - 11.5 * cm, "has successfully completed the course")

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(HexColor("#6366f1"))
    c.drawCentredString(w / 2, h - 13 * cm, course)

    c.setFont("Helvetica", 12)
    c.setFillColor(HexColor("#64748b"))
    c.drawCentredString(w / 2, h - 15 * cm, f"Date: {date_str}")

    c.setFont("Helvetica", 9)
    c.setFillColor(HexColor("#94a3b8"))
    c.drawCentredString(w / 2, 2.5 * cm, f"Certificate ID: {cert_id}")

    c.save()


def make_letter_pdf() -> None:
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib.colors import HexColor

    sender = {
        "company": "ACME Corp",
        "name": "John Smith",
        "title": "Managing Director",
        "address": "123 Business St, London, EC1A 1BB",
        "email": "john@acme.com",
    }
    recipient = {
        "name": "Jane Wilson",
        "address": "456 Client Road\nManchester, M1 2AB",
    }
    subject = "Partnership Proposal"
    body_paragraphs = [
        "Thank you for your interest in partnering with ACME Corp. We are delighted to present this proposal for your consideration.",
        "Our team has extensive experience in delivering high-quality solutions that drive business value. We believe a partnership would be mutually beneficial.",
        "Please find the detailed terms and conditions enclosed with this letter. We look forward to your response.",
    ]
    date_str = "16 February 2026"

    def letterhead(canvas, doc):
        canvas.saveState()
        w, h = A4

        canvas.setFont("Helvetica-Bold", 18)
        canvas.setFillColor(HexColor("#6366f1"))
        canvas.drawString(2 * cm, h - 2 * cm, sender["company"])

        canvas.setFont("Helvetica", 9)
        canvas.setFillColor(HexColor("#64748b"))
        canvas.drawString(2 * cm, h - 2.6 * cm, sender["address"])

        canvas.setStrokeColor(HexColor("#6366f1"))
        canvas.setLineWidth(2)
        canvas.line(2 * cm, h - 3 * cm, w - 2 * cm, h - 3 * cm)

        canvas.setStrokeColor(HexColor("#e2e8f0"))
        canvas.setLineWidth(0.5)
        canvas.line(2 * cm, 2 * cm, w - 2 * cm, 2 * cm)

        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(HexColor("#94a3b8"))
        canvas.drawCentredString(
            w / 2,
            1.3 * cm,
            f"{sender['company']} | {sender['address']} | {sender['email']}",
        )

        canvas.restoreState()

    doc = SimpleDocTemplate(
        _p("letter.pdf"),
        pagesize=A4,
        topMargin=4 * cm,
        bottomMargin=3 * cm,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
    )

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(date_str, styles["Normal"]))
    story.append(Spacer(1, 30))

    story.append(Paragraph(f"<b>{recipient['name']}</b>", styles["Normal"]))
    story.append(Paragraph(recipient["address"].replace("\n", "<br/>").strip(), styles["Normal"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph(f"<b>Re: {subject}</b>", styles["Normal"]))
    story.append(Spacer(1, 15))

    story.append(Paragraph(f"Dear {recipient['name']},", styles["Normal"]))
    story.append(Spacer(1, 12))

    for para in body_paragraphs:
        story.append(Paragraph(para, styles["BodyText"]))

    story.append(Spacer(1, 25))
    story.append(Paragraph("Kind regards,", styles["Normal"]))
    story.append(Spacer(1, 30))
    story.append(Paragraph(f"<b>{sender['name']}</b>", styles["Normal"]))
    story.append(Paragraph(sender["title"], styles["Normal"]))

    doc.build(story, onFirstPage=letterhead, onLaterPages=letterhead)


def make_basic_table_pdf() -> None:
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.colors import HexColor, white
    from reportlab.lib.units import cm

    doc = SimpleDocTemplate(_p("basic_table.pdf"), pagesize=A4)
    story = []

    data = [
        ["Name", "Role", "Department", "Salary"],
        ["Alice Johnson", "Engineer", "Engineering", "£55,000"],
        ["Bob Smith", "Designer", "Design", "£48,000"],
        ["Carol White", "Manager", "Engineering", "£65,000"],
        ["David Brown", "Analyst", "Finance", "£52,000"],
        ["Eve Davis", "Developer", "Engineering", "£58,000"],
    ]

    table = Table(data, colWidths=[5 * cm, 3.5 * cm, 4 * cm, 3 * cm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
                ("TEXTCOLOR", (0, 0), (-1, 0), white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 11),
                ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ("TOPPADDING", (0, 0), (-1, 0), 10),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 1), (-1, -1), 10),
                ("TOPPADDING", (0, 1), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),
                ("ALIGN", (-1, 1), (-1, -1), "RIGHT"),
            ]
        )
    )

    story.append(table)
    doc.build(story)


def make_rich_table_pdf() -> None:
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.colors import HexColor, white
    from reportlab.lib.units import cm

    doc = SimpleDocTemplate(_p("rich_table.pdf"), pagesize=A4)
    styles = getSampleStyleSheet()

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
                styles["BodyText"],
            ),
            Paragraph("<font color='green'>✓ Complete</font>", styles["BodyText"]),
        ],
        [
            Paragraph("Multi-page Support", styles["BodyText"]),
            Paragraph(
                "Automatic page breaks with <i>headers and footers</i> "
                "on every page.",
                styles["BodyText"],
            ),
            Paragraph("<font color='green'>✓ Complete</font>", styles["BodyText"]),
        ],
        [
            Paragraph("Chart Integration", styles["BodyText"]),
            Paragraph(
                "Built-in <b>pie</b>, <b>bar</b>, and <b>line</b> charts "
                "with customizable legends and colors.",
                styles["BodyText"],
            ),
            Paragraph("<font color='orange'>⏳ In Progress</font>", styles["BodyText"]),
        ],
    ]

    table = Table(data, colWidths=[4 * cm, 8 * cm, 3.5 * cm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
                ("TEXTCOLOR", (0, 0), (-1, 0), white),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [HexColor("#ffffff"), HexColor("#f8fafc")],
                ),
            ]
        )
    )

    doc.build([table])


def make_long_table_pdf() -> None:
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.colors import HexColor, white
    from reportlab.lib.units import cm

    _ = getSampleStyleSheet()
    doc = SimpleDocTemplate(_p("long_table.pdf"), pagesize=A4)

    header = ["ID", "Name", "Email", "Amount"]
    data = [header]
    for i in range(1, 101):
        data.append(
            [
                str(i).zfill(3),
                f"Person {i}",
                f"person{i}@example.com",
                f"£{(i * 13.5):.2f}",
            ]
        )

    table = Table(data, colWidths=[2 * cm, 4 * cm, 6 * cm, 3 * cm], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HexColor("#6366f1")),
                ("TEXTCOLOR", (0, 0), (-1, 0), white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                ("FONTSIZE", (0, 1), (-1, -1), 9),
                ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e2e8f0")),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [HexColor("#ffffff"), HexColor("#f8fafc")],
                ),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("ALIGN", (-1, 1), (-1, -1), "RIGHT"),
            ]
        )
    )

    doc.build([table])


def make_two_columns_pdf() -> None:
    from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm

    styles = getSampleStyleSheet()

    frame_left = Frame(2 * cm, 2 * cm, 8.5 * cm, 25 * cm, id="left")
    frame_right = Frame(11.5 * cm, 2 * cm, 8.5 * cm, 25 * cm, id="right")

    template = PageTemplate(id="two_col", frames=[frame_left, frame_right])

    doc = BaseDocTemplate(_p("two_columns.pdf"), pagesize=A4)
    doc.addPageTemplates([template])

    story = []
    for i in range(20):
        story.append(Paragraph(f"<b>Section {i+1}</b>", styles["Heading3"]))
        story.append(
            Paragraph(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                "Ut enim ad minim veniam, quis nostrud exercitation.",
                styles["BodyText"],
            )
        )
        story.append(Spacer(1, 8))

    doc.build(story)


def make_complex_layout_pdf() -> None:
    from reportlab.platypus import (
        BaseDocTemplate,
        Frame,
        PageTemplate,
        Paragraph,
        Spacer,
        NextPageTemplate,
        PageBreak,
    )
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib.colors import HexColor

    styles = getSampleStyleSheet()

    def cover_page_draw(canvas, doc):
        canvas.saveState()
        w, h = A4
        canvas.setFillColor(HexColor("#1e293b"))
        canvas.rect(0, 0, w, h, fill=1)
        canvas.setFillColor(HexColor("#ffffff"))
        canvas.setFont("Helvetica-Bold", 36)
        canvas.drawCentredString(w / 2, h / 2 + 40, "Annual Report")
        canvas.setFont("Helvetica", 16)
        canvas.drawCentredString(w / 2, h / 2 - 10, "2026 Edition")
        canvas.restoreState()

    def normal_page_draw(canvas, doc):
        canvas.saveState()
        w, _ = A4
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(HexColor("#94a3b8"))
        canvas.drawCentredString(w / 2, 1.5 * cm, f"Page {canvas.getPageNumber()}")
        canvas.restoreState()

    cover_frame = Frame(2 * cm, 2 * cm, A4[0] - 4 * cm, A4[1] - 4 * cm, id="cover")
    normal_frame = Frame(2 * cm, 3 * cm, A4[0] - 4 * cm, A4[1] - 5 * cm, id="normal")

    cover_template = PageTemplate(id="cover", frames=[cover_frame], onPage=cover_page_draw)
    normal_template = PageTemplate(
        id="normal", frames=[normal_frame], onPage=normal_page_draw
    )

    doc = BaseDocTemplate(_p("complex_layout.pdf"), pagesize=A4)
    doc.addPageTemplates([cover_template, normal_template])

    story = []
    story.append(Spacer(1, 1))
    story.append(NextPageTemplate("normal"))
    story.append(PageBreak())

    for i in range(1, 4):
        story.append(Paragraph(f"Chapter {i}", styles["Heading1"]))
        story.append(Spacer(1, 12))
        for _j in range(6):
            story.append(
                Paragraph(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                    "Vivamus lacinia odio vitae vestibulum vestibulum.",
                    styles["BodyText"],
                )
            )

    doc.build(story)


def make_header_footer_pdf() -> None:
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib.colors import HexColor

    def header_footer(canvas, doc):
        canvas.saveState()
        width, height = A4

        canvas.setStrokeColor(HexColor("#6366f1"))
        canvas.setLineWidth(2)
        canvas.line(2 * cm, height - 2 * cm, width - 2 * cm, height - 2 * cm)

        canvas.setFont("Helvetica-Bold", 10)
        canvas.setFillColor(HexColor("#6366f1"))
        canvas.drawString(2 * cm, height - 1.7 * cm, "My Company Report")

        canvas.setFont("Helvetica", 9)
        canvas.setFillColor(HexColor("#64748b"))
        canvas.drawRightString(width - 2 * cm, height - 1.7 * cm, "Confidential")

        canvas.setStrokeColor(HexColor("#e2e8f0"))
        canvas.setLineWidth(0.5)
        canvas.line(2 * cm, 2 * cm, width - 2 * cm, 2 * cm)

        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(HexColor("#94a3b8"))
        canvas.drawString(2 * cm, 1.2 * cm, "Generated with ReportLab")
        canvas.drawRightString(width - 2 * cm, 1.2 * cm, f"Page {canvas.getPageNumber()}")

        canvas.restoreState()

    doc = SimpleDocTemplate(
        _p("header_footer.pdf"),
        pagesize=A4,
        topMargin=3 * cm,
        bottomMargin=3 * cm,
    )

    styles = getSampleStyleSheet()
    story = []
    for i in range(1, 6):
        story.append(Paragraph(f"Chapter {i}", styles["Heading1"]))
        story.append(Spacer(1, 12))
        for j in range(8):
            story.append(
                Paragraph(
                    (
                        f"This is paragraph {j+1} of chapter {i}. "
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
                    ),
                    styles["BodyText"],
                )
            )
        if i < 5:
            story.append(PageBreak())

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)


def make_watermark_pdf() -> None:
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib.colors import Color, HexColor

    def add_watermark(canvas, doc):
        canvas.saveState()
        w, h = A4

        canvas.setFillColor(Color(0, 0, 0, alpha=0.06))
        canvas.setFont("Helvetica-Bold", 60)

        canvas.translate(w / 2, h / 2)
        canvas.rotate(45)
        canvas.drawCentredString(0, 0, "DRAFT")

        canvas.restoreState()

        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(HexColor("#94a3b8"))
        canvas.drawCentredString(w / 2, 1.5 * cm, f"Page {canvas.getPageNumber()}")
        canvas.restoreState()

    doc = SimpleDocTemplate(_p("watermark.pdf"), pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for i in range(5):
        story.append(Paragraph(f"Section {i+1}", styles["Heading1"]))
        story.append(
            Paragraph(
                "This document has a diagonal DRAFT watermark on every page. "
                "The watermark is drawn using canvas operations in a callback.",
                styles["BodyText"],
            )
        )
        story.append(Spacer(1, 200))

    doc.build(story, onFirstPage=add_watermark, onLaterPages=add_watermark)


def make_pie_chart_pdf() -> None:
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.graphics.shapes import Drawing
    from reportlab.graphics.charts.piecharts import Pie
    from reportlab.lib.colors import HexColor

    doc = SimpleDocTemplate(_p("pie_chart.pdf"), pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Sales by Region", styles["Title"]))
    story.append(Spacer(1, 20))

    drawing = Drawing(400, 250)

    pie = Pie()
    pie.x = 100
    pie.y = 25
    pie.width = 180
    pie.height = 180
    pie.data = [35, 25, 20, 15, 5]
    pie.labels = ["North", "South", "East", "West", "Other"]

    pie.slices[0].fillColor = HexColor("#6366f1")
    pie.slices[1].fillColor = HexColor("#ec4899")
    pie.slices[2].fillColor = HexColor("#f59e0b")
    pie.slices[3].fillColor = HexColor("#10b981")
    pie.slices[4].fillColor = HexColor("#94a3b8")

    pie.slices.strokeWidth = 0.5
    pie.slices.strokeColor = HexColor("#ffffff")
    pie.sideLabels = True
    pie.simpleLabels = False
    pie.slices.fontName = "Helvetica"
    pie.slices.fontSize = 10

    drawing.add(pie)
    story.append(drawing)

    doc.build(story)


def make_barcode_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.graphics.barcode import code128

    c = canvas.Canvas(_p("barcode.pdf"), pagesize=A4)
    _, h = A4

    barcode = code128.Code128(
        "ABC-12345-XYZ",
        barWidth=0.5 * cm / 10,
        barHeight=1.5 * cm,
        humanReadable=True,
    )

    barcode.drawOn(c, 2 * cm, h - 5 * cm)
    c.save()


def make_qrcode_pdf() -> None:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.graphics.barcode.qr import QrCodeWidget
    from reportlab.graphics.shapes import Drawing

    c = canvas.Canvas(_p("qrcode.pdf"), pagesize=A4)
    _, h = A4

    qr = QrCodeWidget("https://www.reportlab.com")
    qr.barWidth = 4 * cm
    qr.barHeight = 4 * cm
    qr.qrVersion = 1

    d = Drawing(4 * cm, 4 * cm)
    d.add(qr)
    d.drawOn(c, 2 * cm, h - 7 * cm)

    qr2 = QrCodeWidget("Name: John Doe\nEmail: john@example.com\nPhone: +44 123 456 7890")
    qr2.barWidth = 5 * cm
    qr2.barHeight = 5 * cm

    d2 = Drawing(5 * cm, 5 * cm)
    d2.add(qr2)
    d2.drawOn(c, 10 * cm, h - 8 * cm)

    c.save()


def main() -> None:
    _ensure_dir()

    makers = [
        make_test_pdf,
        make_output_pdf,
        make_hello_pdf,
        make_state_demo_pdf,
        make_text_demo_pdf,
        make_shapes_demo_pdf,
        make_rectangles_pdf,
        make_circles_pdf,
        make_paths_pdf,
        make_colors_demo_pdf,
        make_basic_table_pdf,
        make_invoice_pdf,
        make_sales_report_pdf,
        make_certificate_pdf,
        make_letter_pdf,
        make_pie_chart_pdf,
        make_barcode_pdf,
        make_qrcode_pdf,
        make_line_styles_pdf,
        make_transforms_pdf,
        make_clipping_pdf,
        make_multipage_pdf,
        make_text_basics_pdf,
        make_text_align_pdf,
        make_textobject_pdf,
        make_font_list_pdf,
        make_platypus_intro_pdf,
        make_rich_table_pdf,
        make_long_table_pdf,
        make_two_columns_pdf,
        make_complex_layout_pdf,
        make_header_footer_pdf,
        make_watermark_pdf,
        make_barcodes_platypus_pdf,
        make_transparency_pdf,
        make_gradient_pdf,
        make_metadata_pdf,
        make_encrypted_pdf,
        make_bookmarks_pdf,
        make_hyperlinks_pdf,
    ]

    successes = 0
    for fn in makers:
        try:
            fn()
        except Exception as e:
            print(f"[WARN] Skipped {fn.__name__}: {e}")
        else:
            successes += 1

    print(f"Generated {successes} assets in: {ASSETS_DIR}")


if __name__ == "__main__":
    main()
