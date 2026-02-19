"""
Generate a proper app icon for the Documentation Hub browser.

Creates:
  site/icon.svg    — high-quality SVG for favicons
  site/icon.ico    — Windows .ico (16, 32, 48, 64, 128, 256 px)

Design: Open book on a rounded dark background with accent gradient.
"""

import os
import struct
import zlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(BASE_DIR, "site")


# ── SVG Icon ─────────────────────────────────────────────────────

SVG_ICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#111827"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#6366f1"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>
  </defs>
  <!-- Background -->
  <rect width="256" height="256" rx="48" fill="url(#bg)"/>
  <!-- Book body (left page) -->
  <path d="M56 72 C56 64, 62 58, 70 58 L120 58 L120 198 L70 198 C62 198, 56 192, 56 184 Z" fill="#e2e8f0" opacity="0.95"/>
  <!-- Book body (right page) -->
  <path d="M200 72 C200 64, 194 58, 186 58 L136 58 L136 198 L186 198 C194 198, 200 192, 200 184 Z" fill="#cbd5e1" opacity="0.9"/>
  <!-- Spine -->
  <rect x="120" y="54" width="16" height="148" rx="2" fill="url(#accent)"/>
  <!-- Left page lines -->
  <rect x="72" y="82" width="36" height="4" rx="2" fill="#94a3b8" opacity="0.5"/>
  <rect x="72" y="96" width="30" height="4" rx="2" fill="#94a3b8" opacity="0.4"/>
  <rect x="72" y="110" width="34" height="4" rx="2" fill="#94a3b8" opacity="0.35"/>
  <rect x="72" y="124" width="28" height="4" rx="2" fill="#94a3b8" opacity="0.3"/>
  <rect x="72" y="138" width="32" height="4" rx="2" fill="#94a3b8" opacity="0.25"/>
  <!-- Right page lines -->
  <rect x="148" y="82" width="36" height="4" rx="2" fill="#64748b" opacity="0.5"/>
  <rect x="148" y="96" width="30" height="4" rx="2" fill="#64748b" opacity="0.4"/>
  <rect x="148" y="110" width="34" height="4" rx="2" fill="#64748b" opacity="0.35"/>
  <rect x="148" y="124" width="28" height="4" rx="2" fill="#64748b" opacity="0.3"/>
  <rect x="148" y="138" width="32" height="4" rx="2" fill="#64748b" opacity="0.25"/>
  <!-- Accent bookmark ribbon -->
  <path d="M164 54 L164 86 L172 78 L180 86 L180 54 Z" fill="url(#accent)" opacity="0.9"/>
</svg>'''


def save_svg():
    path = os.path.join(SITE_DIR, "icon.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SVG_ICON)
    print(f"  SVG saved → {path}")
    return path


# ── PNG rendering (pure Python, no Pillow) ───────────────────────
# We'll use PyQt6 since it's already installed to render SVG → PNG → ICO

def generate_ico():
    """Generate .ico file using PyQt6 to render SVG at multiple sizes."""
    try:
        from PyQt6.QtCore import QByteArray, QBuffer, QIODevice, QSize
        from PyQt6.QtGui import QImage, QPainter, QColor
        from PyQt6.QtSvg import QSvgRenderer
        from PyQt6.QtWidgets import QApplication
        import sys

        # Need a QApplication to use Qt rendering
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)

        svg_data = QByteArray(SVG_ICON.encode("utf-8"))
        renderer = QSvgRenderer(svg_data)

        sizes = [16, 32, 48, 64, 128, 256]
        png_images = []

        for sz in sizes:
            img = QImage(sz, sz, QImage.Format.Format_ARGB32)
            img.fill(QColor(0, 0, 0, 0))
            painter = QPainter(img)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
            renderer.render(painter)
            painter.end()

            # Convert QImage to PNG bytes
            buf = QBuffer()
            buf.open(QIODevice.OpenModeFlag.WriteOnly)
            img.save(buf, "PNG")
            png_data = bytes(buf.data())
            buf.close()

            png_images.append((sz, png_data, img))

        # Build .ico file
        ico_path = os.path.join(SITE_DIR, "icon.ico")
        build_ico(ico_path, png_images)
        print(f"  ICO saved → {ico_path}  ({', '.join(str(s) for s in sizes)} px)")

        return ico_path

    except ImportError as e:
        print(f"  Warning: Could not generate .ico (missing {e.name})")
        print("  The SVG icon will still work for favicons.")
        return None


def build_ico(path, png_images):
    """Build a .ico file from a list of (size, png_bytes, qimage) tuples."""
    num = len(png_images)

    # ICO header: reserved(2) + type(2) + count(2)
    header = struct.pack('<HHH', 0, 1, num)

    # Calculate offsets: header(6) + entries(num * 16) = data start
    data_offset = 6 + num * 16
    entries = b''
    image_data = b''

    for sz, png_data, qimg in png_images:
        width = sz if sz < 256 else 0
        height = sz if sz < 256 else 0

        entry = struct.pack('<BBBBHHII',
            width,          # width (0 = 256)
            height,         # height (0 = 256)
            0,              # color palette
            0,              # reserved
            1,              # color planes
            32,             # bits per pixel
            len(png_data),  # size of image data
            data_offset + len(image_data),  # offset to image data
        )
        entries += entry
        image_data += png_data

    with open(path, 'wb') as f:
        f.write(header + entries + image_data)


# ── Main ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Generating Documentation Hub icons…\n")
    save_svg()
    generate_ico()
    print("\nDone!")
