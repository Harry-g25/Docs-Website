"""
Qt stylesheet constants for the Documentation Hub.

All dark-theme stylesheets are defined here to avoid duplication
across browser, content manager, and dialog modules.
"""

from app.config import (
    ACCENT, ACCENT_L, BG_CARD, BG_DARK, BG_HOVER, BG_PANEL,
    BORDER, RED, TEXT, TEXT_DIM, TEXT_FAINT,
)

# ── Main window & toolbar ────────────────────────────────────────

MAIN_WINDOW_SS = """
QMainWindow {
    background: #0c1018;
}
QToolBar {
    background: #111827;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    padding: 4px 8px;
    spacing: 4px;
}
QToolButton {
    background: transparent;
    border: none;
    border-radius: 6px;
    padding: 6px;
    color: #94a3b8;
}
QToolButton:hover {
    background: rgba(255,255,255,0.08);
    color: #e2e8f0;
}
QToolButton:disabled {
    color: rgba(148,163,184,0.3);
}
"""

# ── Find bar (browser) ──────────────────────────────────────────

FIND_BAR_SS = """
FindBar {
    background: #1e293b;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding: 6px 12px;
}
QLineEdit {
    background: #0f172a;
    color: #e2e8f0;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 6px;
    padding: 5px 10px;
    font-size: 13px;
    min-width: 260px;
    selection-background-color: #6366f1;
}
QLineEdit:focus {
    border-color: #6366f1;
}
QLabel {
    color: #94a3b8;
    font-size: 12px;
    margin-left: 8px;
}
QPushButton {
    background: transparent;
    border: none;
    color: #94a3b8;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 13px;
}
QPushButton:hover {
    background: rgba(255,255,255,0.08);
    color: #e2e8f0;
}
"""

# ── Content manager panel ────────────────────────────────────────

CM_PANEL_SS = f"""
QWidget#cmPanel {{
    background: {BG_PANEL};
    border-left: 1px solid {BORDER};
}}
QLabel {{
    color: {TEXT};
}}
QLabel#dimLabel {{
    color: {TEXT_DIM};
    font-size: 12px;
}}
QLabel#faintLabel {{
    color: {TEXT_FAINT};
    font-size: 11px;
}}
QLabel#panelTitle {{
    font-size: 16px;
    font-weight: 700;
    color: #f1f5f9;
}}
QLabel#sectionHead {{
    font-size: 13px;
    font-weight: 600;
    color: {ACCENT_L};
    padding: 8px 0 4px 0;
}}
QLineEdit, QTextEdit, QPlainTextEdit {{
    background: {BG_DARK};
    color: {TEXT};
    border: 1px solid {BORDER};
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 13px;
    selection-background-color: {ACCENT};
}}
QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {{
    border-color: {ACCENT};
}}
QComboBox {{
    background: {BG_DARK};
    color: {TEXT};
    border: 1px solid {BORDER};
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 13px;
    min-height: 20px;
}}
QComboBox::drop-down {{ border: none; width: 24px; }}
QComboBox::down-arrow {{ image: none; border: none; }}
QComboBox QAbstractItemView {{
    background: {BG_DARK};
    color: {TEXT};
    border: 1px solid {BORDER};
    selection-background-color: {ACCENT};
    outline: none;
}}
QPushButton {{
    background: {BG_HOVER};
    color: {TEXT};
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 6px;
    padding: 6px 14px;
    font-size: 12px;
    font-weight: 600;
}}
QPushButton:hover {{
    background: #475569;
    border-color: rgba(255,255,255,0.15);
}}
QPushButton#accent {{
    background: {ACCENT};
    color: #fff;
    border: none;
}}
QPushButton#accent:hover {{
    background: {ACCENT_L};
}}
QPushButton#danger {{
    background: transparent;
    color: {RED};
    border: 1px solid rgba(248,113,113,0.3);
}}
QPushButton#danger:hover {{
    background: rgba(248,113,113,0.12);
}}
QPushButton#navBtn {{
    background: transparent;
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 12px;
    font-weight: 600;
    color: {TEXT_DIM};
}}
QPushButton#navBtn:hover {{
    background: rgba(255,255,255,0.06);
    color: {TEXT};
}}
QPushButton#navBtnActive {{
    background: rgba(99,102,241,0.15);
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 12px;
    font-weight: 600;
    color: {ACCENT_L};
}}
QPushButton#closeBtn {{
    background: transparent;
    border: none;
    padding: 4px;
    color: {TEXT_DIM};
    font-size: 18px;
    min-width: 28px; max-width: 28px;
    min-height: 28px; max-height: 28px;
    border-radius: 6px;
}}
QPushButton#closeBtn:hover {{
    background: rgba(255,255,255,0.08);
    color: {TEXT};
}}
QPushButton#smallBtn {{
    padding: 3px 8px;
    font-size: 11px;
    min-width: 24px;
    border-radius: 4px;
}}
QPushButton#colorBtn {{
    min-width: 36px; max-width: 36px;
    min-height: 24px;
    border-radius: 6px;
    border: 2px solid rgba(255,255,255,0.15);
}}
QScrollArea {{
    border: none;
    background: transparent;
}}
QFrame#sep {{
    background: {BORDER};
    max-height: 1px; min-height: 1px;
}}
QFrame#card {{
    background: {BG_CARD};
    border: 1px solid {BORDER};
    border-radius: 10px;
}}
QFrame#card:hover {{
    border-color: rgba(255,255,255,0.12);
}}
QFrame#statCard {{
    background: {BG_CARD};
    border: 1px solid {BORDER};
    border-radius: 10px;
}}
"""

# ── Dialog stylesheet (shared by all dialogs) ───────────────────

DIALOG_SS = f"""
QDialog {{
    background: {BG_CARD};
    color: {TEXT};
}}
QLabel {{
    color: {TEXT};
    font-size: 13px;
}}
QLabel#heading {{
    font-size: 18px;
    font-weight: 700;
    color: #f1f5f9;
    padding: 4px 0;
}}
QLabel#subheading {{
    font-size: 12px;
    color: {TEXT_DIM};
    padding-bottom: 8px;
}}
QLabel#sectionLabel {{
    font-size: 14px;
    font-weight: 600;
    color: #a5b4fc;
    padding-top: 12px;
    padding-bottom: 2px;
}}
QLineEdit, QTextEdit {{
    background: {BG_DARK};
    color: {TEXT};
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 6px;
    padding: 7px 10px;
    font-size: 13px;
    font-family: 'Segoe UI', sans-serif;
    selection-background-color: {ACCENT};
}}
QLineEdit:focus, QTextEdit:focus {{
    border-color: {ACCENT};
}}
QComboBox {{
    background: {BG_DARK};
    color: {TEXT};
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 6px;
    padding: 7px 10px;
    font-size: 13px;
    min-height: 20px;
}}
QComboBox:focus {{ border-color: {ACCENT}; }}
QComboBox::drop-down {{ border: none; width: 24px; }}
QComboBox::down-arrow {{ image: none; border: none; }}
QComboBox QAbstractItemView {{
    background: {BG_DARK};
    color: {TEXT};
    border: 1px solid rgba(255,255,255,0.1);
    selection-background-color: {ACCENT};
    outline: none;
}}
QPushButton {{
    background: #334155;
    color: {TEXT};
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 8px;
    padding: 8px 20px;
    font-size: 13px;
    font-weight: 600;
}}
QPushButton:hover {{
    background: #475569;
    border-color: rgba(255,255,255,0.15);
}}
QPushButton#primary {{
    background: {ACCENT};
    color: #fff;
    border: none;
}}
QPushButton#primary:hover {{
    background: {ACCENT_L};
}}
QPushButton#primary:disabled {{
    background: #334155;
    color: {TEXT_FAINT};
}}
QPushButton#accent {{
    background: {ACCENT};
    color: #fff;
    border: none;
}}
QPushButton#accent:hover {{
    background: {ACCENT_L};
}}
QPushButton#browse {{
    padding: 8px 14px;
    min-width: 0;
}}
QPushButton#colorBtn {{
    min-width: 48px; max-width: 48px;
    min-height: 32px;
    border-radius: 6px;
    border: 2px solid rgba(255,255,255,0.15);
}}
QPushButton#colorBtn:hover {{
    border-color: rgba(255,255,255,0.3);
}}
QScrollArea {{
    border: none;
    background: transparent;
}}
QFrame#separator {{
    background: rgba(255,255,255,0.06);
    max-height: 1px; min-height: 1px;
    margin: 4px 0;
}}
"""
