"""
Dialog windows for the Documentation Hub.

  • CMLoginDialog — password gate for the Content Manager
  • AddDocWizard — full wizard for adding a new doc to the hub
  • EditDocDialog — edit doc title, version, description, tags, colors
  • MoveDocDialog — move doc to a different category
  • AddCategoryDialog — create a new category
  • RenameCategoryDialog — rename + update description
"""

import os
import re
import shutil

from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QColorDialog, QComboBox, QDialog, QFileDialog, QFormLayout,
    QGridLayout, QFrame, QHBoxLayout, QLabel, QLineEdit, QMessageBox,
    QPushButton, QScrollArea, QTextEdit, QVBoxLayout, QWidget,
)

from app.config import (
    ACCENT, BG_DARK, BG_PANEL, CONTENT_DIR, INDEX_HTML, PAGES_DIR,
    SETTINGS_APP, SETTINGS_ORG, TEXT, TEXT_DIM,
)
from app.data import atomic_write, cached_categories, log_activity
from app.icons import CARD_ICONS, SECTION_ICONS
from app.site_engine import (
    count_cards_in_category,
    generate_card_html,
    generate_doc_page,
    generate_new_section_html,
    get_existing_categories,
    inject_card_into_existing_section,
    inject_new_section,
    register_in_search,
    slugify,
    update_hub_stats,
    validate_hex,
)
from app.styles import DIALOG_SS
from app.widgets import btn


# ═════════════════════════════════════════════════════════════
#  Content Manager Login Dialog
# ═════════════════════════════════════════════════════════════

class CMLoginDialog(QDialog):
    """Password gate for opening the Content Manager."""

    _SETTINGS_KEY = "cm_password"
    _DEFAULT_PASSWORD = "admin"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Content Manager — Login")
        self.setFixedWidth(320)
        self.setStyleSheet(DIALOG_SS)
        self._settings = QSettings(SETTINGS_ORG, SETTINGS_APP)
        self._build()

    def _build(self):
        lay = QVBoxLayout(self)
        lay.setContentsMargins(24, 20, 24, 20)
        lay.setSpacing(12)

        title = QLabel("Content Manager")
        title.setStyleSheet(
            f"font-size: 15px; font-weight: 700; color: {TEXT};"
        )
        lay.addWidget(title)

        sub = QLabel("Enter password to continue")
        sub.setStyleSheet(f"font-size: 12px; color: {TEXT_DIM};")
        lay.addWidget(sub)

        lay.addSpacing(4)

        self._pw_input = QLineEdit()
        self._pw_input.setPlaceholderText("Password")
        self._pw_input.setEchoMode(QLineEdit.EchoMode.Password)
        self._pw_input.returnPressed.connect(self._attempt_login)
        lay.addWidget(self._pw_input)

        self._error_label = QLabel("")
        self._error_label.setStyleSheet("font-size: 11px; color: #f87171;")
        lay.addWidget(self._error_label)

        login_btn = QPushButton("Login")
        login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        login_btn.setStyleSheet(
            f"QPushButton {{ background: {ACCENT}; color: #fff; border: none;"
            f"border-radius: 6px; padding: 8px 16px; font-weight: 600; }}"
            f"QPushButton:hover {{ background: #818cf8; }}"
        )
        login_btn.clicked.connect(self._attempt_login)
        lay.addWidget(login_btn)

        lay.addSpacing(4)

        change_pw_btn = QPushButton("Change password\u2026")
        change_pw_btn.setFlat(True)
        change_pw_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        change_pw_btn.setStyleSheet(
            f"QPushButton {{ background: transparent; border: none;"
            f"color: {TEXT_DIM}; font-size: 11px; text-decoration: underline;"
            f"padding: 0; }}"
            f"QPushButton:hover {{ color: {TEXT}; }}"
        )
        change_pw_btn.clicked.connect(self._change_password)
        lay.addWidget(change_pw_btn, alignment=Qt.AlignmentFlag.AlignLeft)

    def _stored_password(self) -> str:
        return self._settings.value(self._SETTINGS_KEY, self._DEFAULT_PASSWORD)

    def _attempt_login(self):
        if self._pw_input.text() == self._stored_password():
            self.accept()
        else:
            self._error_label.setText("Incorrect password.")
            self._pw_input.clear()
            self._pw_input.setFocus()

    def _change_password(self):
        if self._pw_input.text() != self._stored_password():
            QMessageBox.warning(
                self, "Authentication Required",
                "Enter the correct current password first.",
            )
            return
        dlg = _ChangePasswordDialog(self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self._settings.setValue(self._SETTINGS_KEY, dlg.new_password)
            QMessageBox.information(self, "Password Changed", "Password updated successfully.")


class _ChangePasswordDialog(QDialog):
    """Helper dialog for changing the Content Manager password."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Change Password")
        self.setFixedWidth(300)
        self.setStyleSheet(DIALOG_SS)
        self.new_password = ""
        self._build()

    def _build(self):
        lay = QVBoxLayout(self)
        lay.setContentsMargins(20, 16, 20, 16)
        lay.setSpacing(10)

        lay.addWidget(QLabel("New password:"))
        self._new_pw = QLineEdit()
        self._new_pw.setEchoMode(QLineEdit.EchoMode.Password)
        lay.addWidget(self._new_pw)

        lay.addWidget(QLabel("Confirm password:"))
        self._confirm_pw = QLineEdit()
        self._confirm_pw.setEchoMode(QLineEdit.EchoMode.Password)
        self._confirm_pw.returnPressed.connect(self._confirm)
        lay.addWidget(self._confirm_pw)

        self._err = QLabel("")
        self._err.setStyleSheet("color: #f87171; font-size: 11px;")
        lay.addWidget(self._err)

        ok_btn = QPushButton("Set Password")
        ok_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        ok_btn.setStyleSheet(
            f"QPushButton {{ background: {ACCENT}; color: #fff; border: none;"
            f"border-radius: 6px; padding: 8px 16px; font-weight: 600; }}"
            f"QPushButton:hover {{ background: #818cf8; }}"
        )
        ok_btn.clicked.connect(self._confirm)
        lay.addWidget(ok_btn)

    def _confirm(self):
        new = self._new_pw.text()
        confirm = self._confirm_pw.text()
        if not new:
            self._err.setText("Password cannot be empty.")
            return
        if new != confirm:
            self._err.setText("Passwords do not match.")
            return
        self.new_password = new
        self.accept()


# ═════════════════════════════════════════════════════════════
#  Edit Doc Dialog
# ═════════════════════════════════════════════════════════════

class EditDocDialog(QDialog):
    """Edit a doc's title, version, description, tags, colors."""

    def __init__(self, doc: dict, parent=None):
        super().__init__(parent)
        self.doc = doc
        self.setWindowTitle(f"Edit — {doc['title']}")
        self.setMinimumWidth(440)
        self.setStyleSheet(DIALOG_SS)
        self._c1 = doc["color1"]
        self._c2 = doc["color2"]
        self._build()

    def _build(self):
        layout = QFormLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(10)

        self.title_input = QLineEdit(self.doc["title"])
        layout.addRow("Title:", self.title_input)

        self.version_input = QLineEdit(self.doc["version"])
        layout.addRow("Version:", self.version_input)

        self.desc_input = QTextEdit(self.doc["description"])
        self.desc_input.setMaximumHeight(80)
        layout.addRow("Description:", self.desc_input)

        self.tags_input = QLineEdit(", ".join(self.doc["tags"]))
        layout.addRow("Tags:", self.tags_input)

        # Colors
        color_row = QHBoxLayout()
        self.c1_btn = QPushButton()
        self.c1_btn.setObjectName("colorBtn")
        self._set_color_style(self.c1_btn, self._c1)
        self.c1_btn.clicked.connect(lambda: self._pick_color(1))
        self.c1_hex = QLineEdit(self._c1)
        self.c1_hex.setMaximumWidth(80)
        self.c1_hex.textChanged.connect(lambda t: self._on_hex(1, t))
        color_row.addWidget(QLabel("Start:"))
        color_row.addWidget(self.c1_btn)
        color_row.addWidget(self.c1_hex)
        color_row.addSpacing(12)

        self.c2_btn = QPushButton()
        self.c2_btn.setObjectName("colorBtn")
        self._set_color_style(self.c2_btn, self._c2)
        self.c2_btn.clicked.connect(lambda: self._pick_color(2))
        self.c2_hex = QLineEdit(self._c2)
        self.c2_hex.setMaximumWidth(80)
        self.c2_hex.textChanged.connect(lambda t: self._on_hex(2, t))
        color_row.addWidget(QLabel("End:"))
        color_row.addWidget(self.c2_btn)
        color_row.addWidget(self.c2_hex)
        color_row.addStretch()
        layout.addRow("Colors:", color_row)

        # Buttons
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_row.addWidget(btn("Cancel", clicked=self.reject))
        btn_row.addWidget(btn("Save Changes", "accent", clicked=self._save))
        layout.addRow("", btn_row)

    @staticmethod
    def _set_color_style(button: QPushButton, color: str):
        button.setStyleSheet(
            f"background: {color}; border: 2px solid rgba(255,255,255,0.15);"
            f"border-radius: 6px; min-width: 36px; max-width: 36px; min-height: 24px;"
        )

    def _pick_color(self, which: int):
        c = QColorDialog.getColor(
            QColor(self._c1 if which == 1 else self._c2), self
        )
        if not c.isValid():
            return
        h = c.name()
        if which == 1:
            self._c1 = h
            self._set_color_style(self.c1_btn, h)
            self.c1_hex.setText(h)
        else:
            self._c2 = h
            self._set_color_style(self.c2_btn, h)
            self.c2_hex.setText(h)

    def _on_hex(self, which: int, text: str):
        t = text.strip()
        if not t.startswith("#"):
            t = "#" + t
        if validate_hex(t):
            if which == 1:
                self._c1 = t
                self._set_color_style(self.c1_btn, t)
            else:
                self._c2 = t
                self._set_color_style(self.c2_btn, t)

    def _save(self):
        title = self.title_input.text().strip()
        if not title:
            QMessageBox.warning(self, "Validation", "Title is required.")
            return
        self.result_data = {
            "title": title,
            "version": self.version_input.text().strip() or self.doc["version"],
            "description": self.desc_input.toPlainText().strip(),
            "tags": [
                t.strip() for t in self.tags_input.text().split(",") if t.strip()
            ],
            "color1": self._c1,
            "color2": self._c2,
        }
        self.accept()


# ═════════════════════════════════════════════════════════════
#  Move Doc Dialog
# ═════════════════════════════════════════════════════════════

class MoveDocDialog(QDialog):
    def __init__(self, slug: str, categories: list[dict], parent=None):
        super().__init__(parent)
        self.setWindowTitle("Move Document")
        self.setMinimumWidth(340)
        self.setStyleSheet(DIALOG_SS)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)
        layout.addWidget(QLabel("Move to which category?"))

        self.combo = QComboBox()
        for c in categories:
            self.combo.addItem(c["name"], c["id"])
        layout.addWidget(self.combo)

        br = QHBoxLayout()
        br.addStretch()
        br.addWidget(btn("Cancel", clicked=self.reject))
        br.addWidget(btn("Move", "accent", clicked=self.accept))
        layout.addLayout(br)

    @property
    def selected_cat_id(self) -> str:
        return self.combo.currentData()


# ═════════════════════════════════════════════════════════════
#  Add Category Dialog
# ═════════════════════════════════════════════════════════════

class AddCategoryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New Category")
        self.setMinimumWidth(420)
        self.setStyleSheet(DIALOG_SS)
        self._c1 = "#6366f1"
        self._c2 = "#818cf8"
        self._icon_key = "book"
        self._build()

    def _build(self):
        layout = QFormLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(10)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("e.g. Machine Learning")
        layout.addRow("Name:", self.name_input)

        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText("Description for the section header")
        layout.addRow("Description:", self.desc_input)

        # Colors
        cr = QHBoxLayout()
        self.c1_btn = QPushButton()
        self.c1_btn.setObjectName("colorBtn")
        EditDocDialog._set_color_style(self.c1_btn, self._c1)
        self.c1_btn.clicked.connect(lambda: self._pick(1))
        self.c1_hex = QLineEdit(self._c1)
        self.c1_hex.setMaximumWidth(80)
        self.c1_hex.textChanged.connect(lambda t: self._hex_edit(1, t))
        cr.addWidget(self.c1_btn)
        cr.addWidget(self.c1_hex)
        cr.addSpacing(8)
        self.c2_btn = QPushButton()
        self.c2_btn.setObjectName("colorBtn")
        EditDocDialog._set_color_style(self.c2_btn, self._c2)
        self.c2_btn.clicked.connect(lambda: self._pick(2))
        self.c2_hex = QLineEdit(self._c2)
        self.c2_hex.setMaximumWidth(80)
        self.c2_hex.textChanged.connect(lambda t: self._hex_edit(2, t))
        cr.addWidget(self.c2_btn)
        cr.addWidget(self.c2_hex)
        cr.addStretch()
        layout.addRow("Colors:", cr)

        # Icon selector
        icon_row = QHBoxLayout()
        self._icon_btns: dict[str, QPushButton] = {}
        for name in SECTION_ICONS:
            b = QPushButton(name)
            b.setFixedSize(60, 30)
            b.setStyleSheet(self._icon_style(name == self._icon_key))
            b.clicked.connect(lambda _, n=name: self._pick_icon(n))
            icon_row.addWidget(b)
            self._icon_btns[name] = b
        icon_row.addStretch()
        layout.addRow("Icon:", icon_row)

        br = QHBoxLayout()
        br.addStretch()
        br.addWidget(btn("Cancel", clicked=self.reject))
        br.addWidget(btn("Create", "accent", clicked=self._create))
        layout.addRow("", br)

    def _icon_style(self, sel: bool) -> str:
        border = ACCENT if sel else "transparent"
        bg = "rgba(99,102,241,0.15)" if sel else BG_DARK
        return (
            f"background: {bg}; border: 2px solid {border}; border-radius: 6px;"
            f"padding: 2px 4px; font-size: 10px; color: {TEXT};"
        )

    def _pick_icon(self, name: str):
        self._icon_key = name
        for n, b in self._icon_btns.items():
            b.setStyleSheet(self._icon_style(n == name))

    def _pick(self, which: int):
        c = QColorDialog.getColor(
            QColor(self._c1 if which == 1 else self._c2), self
        )
        if not c.isValid():
            return
        h = c.name()
        b = self.c1_btn if which == 1 else self.c2_btn
        hf = self.c1_hex if which == 1 else self.c2_hex
        if which == 1:
            self._c1 = h
        else:
            self._c2 = h
        EditDocDialog._set_color_style(b, h)
        hf.setText(h)

    def _hex_edit(self, which: int, text: str):
        t = text.strip()
        if not t.startswith("#"):
            t = "#" + t
        if validate_hex(t):
            if which == 1:
                self._c1 = t
            else:
                self._c2 = t

    def _create(self):
        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Validation", "Name is required.")
            return
        desc = self.desc_input.text().strip() or f"{name} documentation and guides"
        self.result_data = {
            "name": name,
            "description": desc,
            "color1": self._c1,
            "color2": self._c2,
            "icon_key": self._icon_key,
        }
        self.accept()


# ═════════════════════════════════════════════════════════════
#  Rename Category Dialog
# ═════════════════════════════════════════════════════════════

class RenameCategoryDialog(QDialog):
    def __init__(self, cat: dict, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Rename — {cat['name']}")
        self.setMinimumWidth(380)
        self.setStyleSheet(DIALOG_SS)

        layout = QFormLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(10)

        self.name_input = QLineEdit(cat["name"])
        layout.addRow("Name:", self.name_input)

        self.desc_input = QLineEdit(cat.get("description", ""))
        layout.addRow("Description:", self.desc_input)

        br = QHBoxLayout()
        br.addStretch()
        br.addWidget(btn("Cancel", clicked=self.reject))
        br.addWidget(btn("Save", "accent", clicked=self._save))
        layout.addRow("", br)

    def _save(self):
        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Validation", "Name is required.")
            return
        self.result_data = {
            "name": name,
            "description": self.desc_input.text().strip(),
        }
        self.accept()


# ═════════════════════════════════════════════════════════════
#  Add Doc Wizard
# ═════════════════════════════════════════════════════════════

class AddDocWizard(QDialog):
    """GUI wizard for adding a new doc to the Documentation Hub."""

    def __init__(self, parent=None, on_complete=None):
        super().__init__(parent)
        self.on_complete = on_complete
        self.setWindowTitle("Add New Documentation")
        self.setMinimumSize(540, 620)
        self.resize(560, 700)
        self.setStyleSheet(DIALOG_SS)

        self._selected_icon = "book"
        self._color1 = "#6366f1"
        self._color2 = "#818cf8"
        self._md_path = ""

        self._build_ui()

    def _build_ui(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QWidget()
        layout = QVBoxLayout(scroll_widget)
        layout.setContentsMargins(28, 24, 28, 12)
        layout.setSpacing(6)
        scroll.setWidget(scroll_widget)
        outer.addWidget(scroll, 1)

        # Header
        heading = QLabel("Add New Documentation")
        heading.setObjectName("heading")
        layout.addWidget(heading)
        sub = QLabel(
            "Fill in the details below and the doc will be wired into the hub automatically."
        )
        sub.setObjectName("subheading")
        sub.setWordWrap(True)
        layout.addWidget(sub)
        self._add_separator(layout)

        # 1. Markdown file
        self._section_label(layout, "1. Markdown File")
        file_row = QHBoxLayout()
        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("Path to .md file…")
        self.file_input.setReadOnly(True)
        file_row.addWidget(self.file_input, 1)
        browse_btn = QPushButton("Browse…")
        browse_btn.setObjectName("browse")
        browse_btn.clicked.connect(self._browse_file)
        file_row.addWidget(browse_btn)
        layout.addLayout(file_row)

        # 2. Title & Version
        self._section_label(layout, "2. Title & Version")
        title_row = QHBoxLayout()
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("e.g. Flask")
        title_row.addWidget(self.title_input, 3)
        self.version_input = QLineEdit()
        self.version_input.setPlaceholderText("e.g. v3.1")
        self.version_input.setMaximumWidth(100)
        title_row.addWidget(self.version_input, 1)
        layout.addLayout(title_row)

        self.slug_hint = QLabel("")
        self.slug_hint.setObjectName("subheading")
        self.slug_hint.setStyleSheet("font-size: 11px; color: #64748b; padding: 0;")
        layout.addWidget(self.slug_hint)
        self.title_input.textChanged.connect(self._update_slug_hint)

        # 3. Category
        self._section_label(layout, "3. Category")
        self.cat_combo = QComboBox()
        self._refresh_categories()
        layout.addWidget(self.cat_combo)

        # New category fields
        self.new_cat_widget = QWidget()
        nc_layout = QVBoxLayout(self.new_cat_widget)
        nc_layout.setContentsMargins(0, 4, 0, 0)
        nc_layout.setSpacing(4)
        self.new_cat_name = QLineEdit()
        self.new_cat_name.setPlaceholderText("New category name (e.g. Machine Learning)")
        nc_layout.addWidget(self.new_cat_name)
        self.new_cat_desc = QLineEdit()
        self.new_cat_desc.setPlaceholderText("Category description")
        nc_layout.addWidget(self.new_cat_desc)

        nc_icon_label = QLabel("Section header icon:")
        nc_icon_label.setStyleSheet(
            f"font-size: 12px; color: {TEXT_DIM}; padding-top: 4px;"
        )
        nc_layout.addWidget(nc_icon_label)

        sig_widget = QWidget()
        sig_layout = QHBoxLayout(sig_widget)
        sig_layout.setContentsMargins(0, 0, 0, 0)
        sig_layout.setSpacing(6)
        self._sec_icon_buttons: dict[str, QPushButton] = {}
        self._selected_sec_icon = "book"
        for name in SECTION_ICONS:
            b = QPushButton(name)
            b.setStyleSheet(self._icon_pick_style(False))
            b.setFixedSize(64, 36)
            b.clicked.connect(lambda _, n=name: self._pick_sec_icon(n))
            sig_layout.addWidget(b)
            self._sec_icon_buttons[name] = b
        sig_layout.addStretch()
        nc_layout.addWidget(sig_widget)
        self._pick_sec_icon("book")

        self.new_cat_widget.setVisible(False)
        layout.addWidget(self.new_cat_widget)
        self.cat_combo.currentIndexChanged.connect(self._on_cat_changed)

        # 4. Description
        self._section_label(layout, "4. Description")
        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText(
            "Short description for the homepage card (1–2 sentences)…"
        )
        self.desc_input.setMaximumHeight(72)
        layout.addWidget(self.desc_input)

        # 5. Tags
        self._section_label(layout, "5. Tags")
        self.tags_input = QLineEdit()
        self.tags_input.setPlaceholderText("Comma-separated, e.g. API, REST, HTTP")
        layout.addWidget(self.tags_input)

        # 6. Colors
        self._section_label(layout, "6. Card Gradient Colors")
        color_row = QHBoxLayout()
        color_row.setSpacing(10)

        color_row.addWidget(
            QLabel("Start:", styleSheet=f"font-size: 12px; color: {TEXT_DIM};")
        )
        self.color1_btn = QPushButton("")
        self.color1_btn.setObjectName("colorBtn")
        EditDocDialog._set_color_style(self.color1_btn, self._color1)
        self.color1_btn.clicked.connect(lambda: self._pick_color(1))
        color_row.addWidget(self.color1_btn)
        self.color1_hex = QLineEdit(self._color1)
        self.color1_hex.setMaximumWidth(90)
        self.color1_hex.textChanged.connect(lambda t: self._on_hex_edited(1, t))
        color_row.addWidget(self.color1_hex)
        color_row.addSpacing(16)

        color_row.addWidget(
            QLabel("End:", styleSheet=f"font-size: 12px; color: {TEXT_DIM};")
        )
        self.color2_btn = QPushButton("")
        self.color2_btn.setObjectName("colorBtn")
        EditDocDialog._set_color_style(self.color2_btn, self._color2)
        self.color2_btn.clicked.connect(lambda: self._pick_color(2))
        color_row.addWidget(self.color2_btn)
        self.color2_hex = QLineEdit(self._color2)
        self.color2_hex.setMaximumWidth(90)
        self.color2_hex.textChanged.connect(lambda t: self._on_hex_edited(2, t))
        color_row.addWidget(self.color2_hex)
        color_row.addStretch()
        layout.addLayout(color_row)

        # 7. Card Icon
        self._section_label(layout, "7. Card Icon")
        icon_grid = QGridLayout()
        icon_grid.setSpacing(8)
        self._icon_buttons: dict[str, QPushButton] = {}
        icon_keys = list(CARD_ICONS.keys())
        cols = 6
        for i, name in enumerate(icon_keys):
            b = QPushButton(name)
            b.setStyleSheet(self._icon_pick_style(name == self._selected_icon))
            b.setFixedSize(72, 48)
            b.clicked.connect(lambda _, n=name: self._pick_icon(n))
            icon_grid.addWidget(b, i // cols, i % cols)
            self._icon_buttons[name] = b
        layout.addLayout(icon_grid)

        self._add_separator(layout)
        layout.addStretch()

        # Bottom button bar
        btn_bar = QWidget()
        btn_bar.setStyleSheet(
            f"background: {BG_PANEL}; border-top: 1px solid rgba(255,255,255,0.06);"
        )
        btn_layout = QHBoxLayout(btn_bar)
        btn_layout.setContentsMargins(28, 12, 28, 12)

        self.status_label = QLabel("")
        self.status_label.setStyleSheet(f"font-size: 12px; color: {TEXT_DIM};")
        btn_layout.addWidget(self.status_label, 1)

        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(cancel_btn)

        self.add_btn = QPushButton("Add Documentation")
        self.add_btn.setObjectName("primary")
        self.add_btn.clicked.connect(self._do_add)
        btn_layout.addWidget(self.add_btn)

        outer.addWidget(btn_bar)

    # ── Helpers ──

    @staticmethod
    def _section_label(layout, text: str):
        lbl = QLabel(text)
        lbl.setObjectName("sectionLabel")
        layout.addWidget(lbl)

    @staticmethod
    def _add_separator(layout):
        sep = QFrame()
        sep.setObjectName("separator")
        sep.setFrameShape(QFrame.Shape.HLine)
        layout.addWidget(sep)

    @staticmethod
    def _icon_pick_style(selected: bool) -> str:
        border = "#6366f1" if selected else "transparent"
        bg = "rgba(99,102,241,0.15)" if selected else "#0f172a"
        return (
            f"min-width: 56px; max-width: 80px; min-height: 36px; max-height: 48px;"
            f"border-radius: 8px; padding: 4px; font-size: 11px; font-weight: 500;"
            f"background: {bg}; border: 2px solid {border}; color: #e2e8f0;"
        )

    @staticmethod
    def _suggest_metadata_from_markdown(md_path: str) -> dict:
        """Best-effort extraction of metadata from a markdown file.

        Supported sources:
        - YAML frontmatter at the top (--- ... ---): title/version/description/tags
        - First H1 (# ...)
        - "Version:" or "**Version:**" lines
        - First intro paragraph or blockquote after H1 (for description)
        """
        meta = {
            "title": "",
            "version": "",
            "description": "",
            "tags": [],
        }

        def _clean(s: str) -> str:
            return " ".join(s.strip().split())

        def _parse_frontmatter(front_lines: list[str]) -> dict:
            fm = {"title": "", "version": "", "description": "", "tags": []}
            i = 0
            while i < len(front_lines):
                raw = front_lines[i].rstrip("\n")
                if not raw.strip() or raw.lstrip().startswith("#"):
                    i += 1
                    continue

                m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", raw)
                if not m:
                    i += 1
                    continue

                key = m.group(1).strip().lower()
                val = m.group(2).strip()

                if key in {"title", "version", "description"}:
                    if val and ((val[0] == val[-1] == '"') or (val[0] == val[-1] == "'")):
                        val = val[1:-1]
                    fm[key] = _clean(val)
                    i += 1
                    continue

                if key == "tags":
                    tags: list[str] = []
                    # tags: [a, b]
                    if val.startswith("[") and val.endswith("]"):
                        inner = val[1:-1]
                        for part in inner.split(","):
                            t = _clean(part.strip(" ' \""))
                            if t:
                                tags.append(t)
                        fm["tags"] = tags
                        i += 1
                        continue

                    # tags:
                    #  - a
                    #  - b
                    if not val:
                        j = i + 1
                        while j < len(front_lines):
                            nxt = front_lines[j].rstrip("\n")
                            m2 = re.match(r"^\s*-\s*(.+)$", nxt)
                            if not m2:
                                break
                            t = _clean(m2.group(1).strip(" ' \""))
                            if t:
                                tags.append(t)
                            j += 1
                        fm["tags"] = tags
                        i = j
                        continue

                    # tags: a, b
                    for part in val.split(","):
                        t = _clean(part.strip(" ' \""))
                        if t:
                            tags.append(t)
                    fm["tags"] = tags
                    i += 1
                    continue

                i += 1
            return fm

        try:
            with open(md_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # Scan the top of the file first (fast for very large docs)
            head = lines[:400]

            # 0) Optional YAML frontmatter
            if head and head[0].strip() == "---":
                fm_lines: list[str] = []
                for raw in head[1:]:
                    if raw.strip() == "---":
                        break
                    fm_lines.append(raw)
                fm = _parse_frontmatter(fm_lines)
                for k in ("title", "version", "description"):
                    if fm.get(k):
                        meta[k] = fm[k]
                if fm.get("tags"):
                    meta["tags"] = fm["tags"]

            # 1) Title: first H1
            if not meta["title"]:
                for raw in head:
                    m = re.match(r"^#\s+(.+)", raw.strip())
                    if m:
                        meta["title"] = _clean(m.group(1))
                        break

            # 2) Version: common metadata line
            if not meta["version"]:
                for raw in head:
                    s = raw.strip()
                    m = re.match(r"^\*\*Version:\*\*\s*(.+)$", s, flags=re.IGNORECASE)
                    if not m:
                        m = re.match(r"^Version:\s*(.+)$", s, flags=re.IGNORECASE)
                    if m:
                        token = m.group(1)
                        m2 = re.search(
                            r"\b(v?\d+(?:\.\d+){1,3})\b",
                            token,
                            flags=re.IGNORECASE,
                        )
                        if m2:
                            meta["version"] = m2.group(1)
                        break

            # 3) Fallback: infer version from title (e.g. "Python 3.14" -> v3.14)
            if not meta["version"] and meta["title"]:
                m = re.search(
                    r"\b(v?\d+(?:\.\d+){1,3})\b",
                    meta["title"],
                    flags=re.IGNORECASE,
                )
                if m:
                    meta["version"] = m.group(1)

            # 4) Description: first intro paragraph or blockquote after H1
            if not meta["description"]:
                h1_idx = -1
                for i, raw in enumerate(head):
                    if re.match(r"^#\s+", raw.strip()):
                        h1_idx = i
                        break

                if h1_idx != -1:
                    buf: list[str] = []
                    started = False
                    for raw in head[h1_idx + 1 :]:
                        s = raw.rstrip("\n")
                        st = s.strip()

                        if st.startswith("##"):
                            break
                        if st == "---":
                            if started:
                                break
                            continue
                        if not st:
                            if started:
                                break
                            continue

                        # Ignore obvious metadata rows like **Version:** (colon inside bold)
                        if re.match(
                            r"^\*\*(Version|Last Updated|Official Website|PyPI)\s*:\*\*\s*",
                            st,
                            flags=re.IGNORECASE,
                        ):
                            continue
                        # Ignore metadata rows like **Version**: (colon outside bold)
                        if re.match(
                            r"^\*\*(Version|Last Updated|Official Website|PyPI)\*\*\s*:\s*",
                            st,
                            flags=re.IGNORECASE,
                        ):
                            continue
                        if re.match(r"^(Version|Last Updated|Official Website|PyPI)\s*:\s*", st, flags=re.IGNORECASE):
                            continue

                        started = True
                        if st.startswith(">"):
                            st = st.lstrip(">").strip()
                        buf.append(st)
                        if len(" ".join(buf)) >= 220:
                            break

                    meta["description"] = _clean(" ".join(buf))

        except Exception:
            return meta

        if meta["version"] and not meta["version"].lower().startswith("v"):
            meta["version"] = "v" + meta["version"]
        return meta

    def _browse_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select Markdown File", "",
            "Markdown Files (*.md);;All Files (*)",
        )
        if path:
            self._md_path = path
            self.file_input.setText(path)
            meta = self._suggest_metadata_from_markdown(path)
            if meta.get("title"):
                self.title_input.setText(meta["title"])
            if meta.get("version") and not self.version_input.text().strip():
                self.version_input.setText(meta["version"])
            if meta.get("description") and not self.desc_input.toPlainText().strip():
                self.desc_input.setPlainText(meta["description"])
            if meta.get("tags") and not self.tags_input.text().strip():
                self.tags_input.setText(", ".join(meta["tags"]))

    def _update_slug_hint(self, text: str):
        s = slugify(text) if text.strip() else "…"
        self.slug_hint.setText(f"Slug: {s}")

    def _refresh_categories(self):
        self.cat_combo.clear()
        try:
            with open(INDEX_HTML, "r", encoding="utf-8") as f:
                html = f.read()
            cats = get_existing_categories(html)
            for cid, cname in cats.items():
                count = count_cards_in_category(html, cid)
                lbl = f"{count} docs" if count > 0 else "empty"
                self.cat_combo.addItem(f"{cname}  ({lbl})", cid)
        except Exception:
            pass
        self.cat_combo.addItem("\u2795 Create new category…", "__new__")

    def _on_cat_changed(self, _idx):
        self.new_cat_widget.setVisible(self.cat_combo.currentData() == "__new__")

    def _pick_color(self, which: int):
        current = QColor(self._color1 if which == 1 else self._color2)
        color = QColorDialog.getColor(current, self, "Pick Color")
        if not color.isValid():
            return
        h = color.name()
        if which == 1:
            self._color1 = h
            EditDocDialog._set_color_style(self.color1_btn, h)
            self.color1_hex.setText(h)
        else:
            self._color2 = h
            EditDocDialog._set_color_style(self.color2_btn, h)
            self.color2_hex.setText(h)

    def _on_hex_edited(self, which: int, text: str):
        t = text.strip()
        if not t.startswith("#"):
            t = "#" + t
        if validate_hex(t):
            if which == 1:
                self._color1 = t
                EditDocDialog._set_color_style(self.color1_btn, t)
            else:
                self._color2 = t
                EditDocDialog._set_color_style(self.color2_btn, t)

    def _pick_icon(self, name: str):
        for n, b in self._icon_buttons.items():
            b.setStyleSheet(self._icon_pick_style(n == name))
        self._selected_icon = name

    def _pick_sec_icon(self, name: str):
        for n, b in self._sec_icon_buttons.items():
            b.setStyleSheet(self._icon_pick_style(n == name))
        self._selected_sec_icon = name

    def _validate(self) -> str | None:
        if not self._md_path or not os.path.isfile(self._md_path):
            return "Please select a markdown file."
        if not self.title_input.text().strip():
            return "Please enter a title."
        if not self.desc_input.toPlainText().strip():
            return "Please enter a description."
        if not self.tags_input.text().strip():
            return "Please enter at least one tag."
        cat_data = self.cat_combo.currentData()
        if cat_data == "__new__" and not self.new_cat_name.text().strip():
            return "Please enter a name for the new category."
        if not validate_hex(self._color1) or not validate_hex(self._color2):
            return "Please enter valid hex colors."
        return None

    def _do_add(self):
        err = self._validate()
        if err:
            self.status_label.setText(f"\u26a0  {err}")
            self.status_label.setStyleSheet("font-size: 12px; color: #f87171;")
            return

        self.add_btn.setEnabled(False)
        self.status_label.setText("Adding…")
        self.status_label.setStyleSheet("font-size: 12px; color: #fbbf24;")

        try:
            title = self.title_input.text().strip()
            version = self.version_input.text().strip() or "v1.0"
            if not version.startswith("v"):
                version = "v" + version
            slug = slugify(title)
            doc_id = slug.replace("-", "")
            description = self.desc_input.toPlainText().strip().replace("\n", " ")
            tags = [
                t.strip() for t in self.tags_input.text().split(",") if t.strip()
            ]
            icon_svg = CARD_ICONS[self._selected_icon]

            cat_data = self.cat_combo.currentData()
            is_new_category = cat_data == "__new__"

            if is_new_category:
                cat_title = self.new_cat_name.text().strip()
                cat_id = slugify(cat_title)
                cat_desc = (
                    self.new_cat_desc.text().strip()
                    or f"{cat_title} documentation and guides"
                )
                section_icon_svg = SECTION_ICONS[self._selected_sec_icon]
            else:
                cat_id = cat_data
                cat_title = self.cat_combo.currentText().split("  (")[0]

            actions = []

            # 1. Copy markdown
            dest_md = os.path.join(CONTENT_DIR, f"{slug}.md")
            shutil.copy2(self._md_path, dest_md)
            actions.append(f"content/{slug}.md")

            # 2. Generate doc page
            page_html = generate_doc_page(slug, title, version, doc_id, self._color1)
            page_path = os.path.join(PAGES_DIR, f"{slug}.html")
            atomic_write(page_path, page_html)
            actions.append(f"site/pages/{slug}.html")

            # 3. Update index.html
            with open(INDEX_HTML, "r", encoding="utf-8") as f:
                index_html = f.read()

            card_html = generate_card_html(
                slug, title, version, description, tags,
                self._color1, self._color2, icon_svg,
            )

            if is_new_category:
                section_html = generate_new_section_html(
                    cat_id, cat_title, cat_desc,
                    self._color1, self._color2, section_icon_svg, card_html,
                )
                index_html, _ok = inject_new_section(index_html, section_html)
            else:
                index_html, _ok = inject_card_into_existing_section(
                    index_html, cat_id, card_html,
                )

            index_html = update_hub_stats(index_html)
            atomic_write(INDEX_HTML, index_html)
            actions.append("index.html updated")

            # 4. Register in global search
            register_in_search(slug, title, self._color1)
            actions.append("global-search.js updated")

            log_activity("added", slug, f"Added: {title}")

            self.status_label.setText("\u2713 Done!")
            self.status_label.setStyleSheet("font-size: 12px; color: #34d399;")

            QMessageBox.information(
                self,
                "Documentation Added",
                f"<b>{title}</b> has been added to the hub!<br><br>"
                f"<b>Files created/updated:</b><br>"
                + "<br>".join(f"\u2022 {a}" for a in actions)
                + "<br><br>The homepage will refresh automatically.",
            )

            if self.on_complete:
                self.on_complete()
            self.accept()

        except Exception as e:
            self.add_btn.setEnabled(True)
            self.status_label.setText(f"\u2717 Error: {e}")
            self.status_label.setStyleSheet("font-size: 12px; color: #f87171;")
            QMessageBox.critical(
                self, "Error", f"Failed to add documentation:\n\n{e}"
            )
