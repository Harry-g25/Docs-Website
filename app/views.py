"""
Content Manager views — the four tab panels.

  • DashboardView — stats, quick actions, activity log, storage
  • DocsListView — filterable / sortable document list with CRUD
  • CategoryManagerView — create, rename, reorder, delete categories
  • MarkdownEditorView — split-view live-preview markdown editor
"""

import json
import os

from PyQt6.QtCore import Qt, QTimer, QUrl, pyqtSignal
from PyQt6.QtGui import QFont, QKeySequence, QShortcut
from PyQt6.QtWidgets import (
    QComboBox, QDialog, QFileDialog, QFrame, QGridLayout, QHBoxLayout,
    QInputDialog, QLabel, QLineEdit, QMessageBox, QPlainTextEdit,
    QScrollArea, QSplitter, QVBoxLayout, QWidget,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView

from app.config import (
    ACCENT, ACCENT_L, BG_CARD, BG_DARK, BG_PANEL, BORDER,
    CONTENT_DIR, PAGES_DIR, SITE_DIR, TEXT, TEXT_DIM, TEXT_FAINT,
)
from app.data import (
    ACTION_LABELS, atomic_write, cached_categories, cached_docs,
    delete_category, delete_doc, dir_size_bytes, format_bytes,
    get_recent_activity, move_doc_to_category, recent_content_files,
    relative_time, rename_category, swap_categories, update_doc_metadata,
)
from app.dialogs import (
    AddCategoryDialog, EditDocDialog, MoveDocDialog, RenameCategoryDialog,
)
from app.site_engine import slugify
from app.widgets import (
    CodeEditor, FindReplaceBar, MarkdownHighlighter, btn, label,
    make_separator,
)
from app.data import add_category as data_add_category


# ═════════════════════════════════════════════════════════════
#  1. DASHBOARD VIEW
# ═════════════════════════════════════════════════════════════

class DashboardView(QWidget):
    navigate_to = pyqtSignal(int)
    request_add_doc = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._stale = True
        self._build()

    def mark_stale(self):
        self._stale = True

    def refresh(self):
        if not self._stale:
            return
        self._stale = False
        while self._content_layout.count():
            item = self._content_layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()
            elif item.layout():
                self._clear_layout(item.layout())
        self._populate()

    def _clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()
            elif item.layout():
                self._clear_layout(item.layout())

    def _build(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_w = QWidget()
        self._content_layout = QVBoxLayout(scroll_w)
        self._content_layout.setContentsMargins(20, 16, 20, 20)
        self._content_layout.setSpacing(12)
        scroll.setWidget(scroll_w)
        outer.addWidget(scroll)
        self._populate()
        self._stale = False

    def _populate(self):
        lay = self._content_layout
        docs = cached_docs()
        cats = cached_categories()

        # Stats row
        sr = QHBoxLayout()
        sr.setSpacing(10)
        sr.addWidget(self._stat_card("Docs", str(len(docs)), ACCENT))
        sr.addWidget(self._stat_card("Categories", str(len(cats)), "#06b6d4"))
        content_sz = dir_size_bytes(CONTENT_DIR) + dir_size_bytes(PAGES_DIR)
        sr.addWidget(self._stat_card("Storage", format_bytes(content_sz), "#f59e0b"))
        sw = QWidget()
        sw.setLayout(sr)
        lay.addWidget(sw)

        # Quick actions
        lay.addWidget(label("Quick Actions", "sectionHead"))
        qa = QHBoxLayout()
        qa.setSpacing(10)

        def _qa_btn(text, sub, slot):
            from PyQt6.QtWidgets import QPushButton
            b = QPushButton(f"{text}\n{sub}")
            b.setStyleSheet(
                f"background: {BG_CARD}; border: 1px solid {BORDER}; border-radius: 10px;"
                f"padding: 14px; text-align: left; font-size: 12px; color: {TEXT};"
            )
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.clicked.connect(slot)
            return b

        qa.addWidget(_qa_btn("\uff0b  Add Doc", "Add a new doc", self.request_add_doc.emit))
        qa.addWidget(_qa_btn("\u270e  Editor", "Markdown editor", lambda: self.navigate_to.emit(3)))
        qa.addWidget(_qa_btn("\u2630  Categories", "Manage categories", lambda: self.navigate_to.emit(2)))
        qw = QWidget()
        qw.setLayout(qa)
        lay.addWidget(qw)

        # Category breakdown
        lay.addWidget(label("Categories", "sectionHead"))
        for c in cats:
            row = QHBoxLayout()
            row.setSpacing(8)
            dot = QLabel("\u25cf")
            dot.setStyleSheet(f"color: {c['color1']}; font-size: 16px;")
            dot.setFixedWidth(20)
            row.addWidget(dot)
            row.addWidget(label(c["name"], size=13, bold=True))
            row.addStretch()
            cnt = c["doc_count"]
            row.addWidget(label(f"{cnt} doc{'s' if cnt != 1 else ''}", "dimLabel"))
            rw = QWidget()
            rw.setLayout(row)
            lay.addWidget(rw)

        # Activity log
        lay.addWidget(label("Recent Activity", "sectionHead"))
        activity = get_recent_activity(8)
        if activity:
            for entry in activity:
                row = QHBoxLayout()
                row.setSpacing(8)
                lbl = ACTION_LABELS.get(entry.get("action", ""), "\u2022")
                row.addWidget(label(lbl, size=12))
                detail = entry.get("detail", entry.get("target", ""))
                row.addWidget(label(detail, "dimLabel"))
                row.addStretch()
                row.addWidget(
                    label(relative_time(entry.get("time", 0)), "faintLabel")
                )
                rw = QWidget()
                rw.setLayout(row)
                lay.addWidget(rw)
        else:
            recent = recent_content_files(6)
            if recent:
                for fn, mtime in recent:
                    row = QHBoxLayout()
                    row.addWidget(label(fn, size=12))
                    row.addStretch()
                    row.addWidget(label(relative_time(mtime), "faintLabel"))
                    rw = QWidget()
                    rw.setLayout(row)
                    lay.addWidget(rw)
            else:
                lay.addWidget(label("No activity yet.", "dimLabel"))

        # Storage detail
        lay.addWidget(label("Storage Detail", "sectionHead"))
        for lbl_text, sz in [
            ("content/  (markdown)", dir_size_bytes(CONTENT_DIR)),
            ("site/pages/  (HTML)", dir_size_bytes(PAGES_DIR)),
            ("site/  (total)", dir_size_bytes(SITE_DIR)),
        ]:
            row = QHBoxLayout()
            row.addWidget(label(lbl_text, "dimLabel"))
            row.addStretch()
            row.addWidget(label(format_bytes(sz), size=12, bold=True))
            rw = QWidget()
            rw.setLayout(row)
            lay.addWidget(rw)

        lay.addStretch()

    def _stat_card(self, title: str, value: str, color: str) -> QFrame:
        f = QFrame()
        f.setObjectName("statCard")
        v = QVBoxLayout(f)
        v.setContentsMargins(14, 12, 14, 12)
        v.setSpacing(2)
        vl = QLabel(value)
        vl.setStyleSheet(f"font-size: 28px; font-weight: 800; color: {color};")
        vl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v.addWidget(vl)
        tl = QLabel(title)
        tl.setStyleSheet(f"font-size: 11px; color: {TEXT_DIM};")
        tl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v.addWidget(tl)
        return f


# ═════════════════════════════════════════════════════════════
#  2. DOCUMENTS LIST VIEW
# ═════════════════════════════════════════════════════════════

class DocsListView(QWidget):
    doc_changed = pyqtSignal()
    open_editor = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._stale = True
        self._build()

    def mark_stale(self):
        self._stale = True

    def refresh(self):
        if not self._stale:
            return
        self._stale = False
        self._rebuild_list()

    def _build(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(20, 16, 20, 12)
        outer.setSpacing(8)

        top = QHBoxLayout()
        top.addWidget(label("Documents", "panelTitle"))
        top.addStretch()
        self.sort_combo = QComboBox()
        self.sort_combo.addItem("A \u2192 Z", "alpha")
        self.sort_combo.addItem("Category", "category")
        self.sort_combo.addItem("Recent", "recent")
        self.sort_combo.setFixedWidth(100)
        self.sort_combo.currentIndexChanged.connect(lambda _: self._rebuild_list())
        top.addWidget(self.sort_combo)
        outer.addLayout(top)

        filter_row = QHBoxLayout()
        filter_row.setSpacing(6)
        self.filter_combo = QComboBox()
        self.filter_combo.setFixedWidth(150)
        self.filter_combo.currentIndexChanged.connect(lambda _: self._rebuild_list())
        filter_row.addWidget(self.filter_combo)
        self.tag_combo = QComboBox()
        self.tag_combo.setFixedWidth(120)
        self.tag_combo.currentIndexChanged.connect(lambda _: self._rebuild_list())
        filter_row.addWidget(self.tag_combo)
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Filter docs…")
        self.search_input.textChanged.connect(lambda _: self._rebuild_list())
        filter_row.addWidget(self.search_input, 1)
        outer.addLayout(filter_row)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        self._list_widget = QWidget()
        self._list_layout = QVBoxLayout(self._list_widget)
        self._list_layout.setContentsMargins(0, 0, 0, 0)
        self._list_layout.setSpacing(8)
        scroll.setWidget(self._list_widget)
        outer.addWidget(scroll, 1)

        self._rebuild_list()
        self._stale = False

    def _rebuild_list(self):
        cur_filter = self.filter_combo.currentData()
        cur_tag = (
            self.tag_combo.currentData()
            if self.tag_combo.currentIndex() > 0
            else None
        )

        self.filter_combo.blockSignals(True)
        self.filter_combo.clear()
        self.filter_combo.addItem("All categories", "__all__")
        cats = cached_categories()
        for c in cats:
            self.filter_combo.addItem(c["name"], c["id"])
        for i in range(self.filter_combo.count()):
            if self.filter_combo.itemData(i) == cur_filter:
                self.filter_combo.setCurrentIndex(i)
                break
        self.filter_combo.blockSignals(False)

        docs = cached_docs()
        all_tags = sorted({t for d in docs for t in d["tags"]})
        self.tag_combo.blockSignals(True)
        self.tag_combo.clear()
        self.tag_combo.addItem("All tags", "__all__")
        for t in all_tags:
            self.tag_combo.addItem(t, t)
        if cur_tag:
            for i in range(self.tag_combo.count()):
                if self.tag_combo.itemData(i) == cur_tag:
                    self.tag_combo.setCurrentIndex(i)
                    break
        self.tag_combo.blockSignals(False)

        while self._list_layout.count():
            item = self._list_layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()

        search = self.search_input.text().lower().strip()
        filter_cat = self.filter_combo.currentData()
        filter_tag = self.tag_combo.currentData()

        filtered = []
        for doc in docs:
            if filter_cat and filter_cat != "__all__" and doc["category_id"] != filter_cat:
                continue
            if filter_tag and filter_tag != "__all__" and filter_tag not in doc["tags"]:
                continue
            if search and search not in doc["title"].lower() and search not in doc["slug"].lower():
                continue
            filtered.append(doc)

        sort_key = self.sort_combo.currentData()
        if sort_key == "alpha":
            filtered.sort(key=lambda d: d["title"].lower())
        elif sort_key == "category":
            filtered.sort(key=lambda d: (d["category_name"].lower(), d["title"].lower()))

        for doc in filtered:
            self._list_layout.addWidget(self._doc_card(doc))
        self._list_layout.addStretch()

    def _doc_card(self, doc: dict) -> QFrame:
        frame = QFrame()
        frame.setObjectName("card")
        v = QVBoxLayout(frame)
        v.setContentsMargins(16, 14, 16, 14)
        v.setSpacing(6)

        top = QHBoxLayout()
        dot = QLabel("\u25cf")
        dot.setStyleSheet(f"color: {doc['color1']}; font-size: 18px;")
        dot.setFixedWidth(22)
        top.addWidget(dot)
        top.addWidget(label(doc["title"], bold=True, size=14))
        top.addWidget(label(doc["version"], "dimLabel"))
        top.addStretch()
        badge = QLabel(doc["category_name"])
        badge.setStyleSheet(
            f"background: rgba(99,102,241,0.15); color: {ACCENT_L};"
            f"border-radius: 4px; padding: 2px 8px; font-size: 11px; font-weight: 600;"
        )
        top.addWidget(badge)
        v.addLayout(top)

        desc_text = doc["description"]
        desc = QLabel(desc_text)
        desc.setObjectName("dimLabel")
        desc.setWordWrap(False)
        fm = desc.fontMetrics()
        elided = fm.elidedText(desc_text, Qt.TextElideMode.ElideRight, 500)
        desc.setText(elided)
        desc.setToolTip(desc_text)
        v.addWidget(desc)

        if doc["tags"]:
            tr = QHBoxLayout()
            tr.setSpacing(4)
            for t in doc["tags"][:5]:
                tl = QLabel(t)
                tl.setStyleSheet(
                    f"background: {BG_DARK}; color: {TEXT_DIM};"
                    f"border-radius: 3px; padding: 2px 6px; font-size: 10px;"
                )
                tr.addWidget(tl)
            tr.addStretch()
            tw = QWidget()
            tw.setLayout(tr)
            v.addWidget(tw)

        br = QHBoxLayout()
        br.setSpacing(6)
        br.addWidget(btn("Edit Content", clicked=lambda _=False, s=doc["slug"]: self.open_editor.emit(s)))
        br.addWidget(btn("Edit Details…", clicked=lambda _=False, d=doc: self._edit_meta(d)))
        br.addWidget(btn("Move…", clicked=lambda _=False, s=doc["slug"]: self._move_doc(s)))
        br.addStretch()
        br.addWidget(btn("Delete", "danger", clicked=lambda _=False, d=doc: self._delete_doc(d)))
        bw = QWidget()
        bw.setLayout(br)
        v.addWidget(bw)
        return frame

    def _edit_meta(self, doc: dict):
        dlg = EditDocDialog(doc, self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            d = dlg.result_data
            update_doc_metadata(
                doc["slug"], d["title"], d["version"], d["description"],
                d["tags"], d["color1"], d["color2"],
            )
            self.doc_changed.emit()
            self.mark_stale()
            self.refresh()

    def _delete_doc(self, doc: dict):
        reply = QMessageBox.question(
            self, "Delete Documentation",
            f"Delete <b>{doc['title']}</b>?<br><br>"
            f"Files will be moved to .trash/ for recovery.<br>"
            f"<i>The card, page, and search entry will be removed.</i>",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
        )
        if reply == QMessageBox.StandardButton.Yes:
            delete_doc(doc["slug"])
            self.doc_changed.emit()
            self.mark_stale()
            self.refresh()

    def _move_doc(self, slug: str):
        cats = cached_categories()
        dlg = MoveDocDialog(slug, cats, self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            if move_doc_to_category(slug, dlg.selected_cat_id):
                self.doc_changed.emit()
                self.mark_stale()
                self.refresh()
            else:
                QMessageBox.warning(self, "Error", "Failed to move document.")


# ═════════════════════════════════════════════════════════════
#  3. CATEGORY MANAGER VIEW
# ═════════════════════════════════════════════════════════════

class CategoryManagerView(QWidget):
    cat_changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._stale = True
        self._build()

    def mark_stale(self):
        self._stale = True

    def refresh(self):
        if not self._stale:
            return
        self._stale = False
        self._rebuild_list()

    def _build(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(20, 16, 20, 12)
        outer.setSpacing(8)

        top = QHBoxLayout()
        top.addWidget(label("Categories", "panelTitle"))
        top.addStretch()
        top.addWidget(btn("\uff0b New Category", "accent", clicked=self._add_category))
        outer.addLayout(top)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        self._list_widget = QWidget()
        self._list_layout = QVBoxLayout(self._list_widget)
        self._list_layout.setContentsMargins(0, 0, 0, 0)
        self._list_layout.setSpacing(8)
        scroll.setWidget(self._list_widget)
        outer.addWidget(scroll, 1)

        self._rebuild_list()
        self._stale = False

    def _rebuild_list(self):
        while self._list_layout.count():
            item = self._list_layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()
        self._cats = cached_categories()
        for i, c in enumerate(self._cats):
            self._list_layout.addWidget(self._cat_card(c, i))
        self._list_layout.addStretch()

    def _cat_card(self, cat: dict, index: int) -> QFrame:
        frame = QFrame()
        frame.setObjectName("card")
        v = QVBoxLayout(frame)
        v.setContentsMargins(16, 14, 16, 14)
        v.setSpacing(6)

        top = QHBoxLayout()
        dot = QLabel("\u25cf")
        dot.setStyleSheet(f"color: {cat['color1']}; font-size: 20px;")
        dot.setFixedWidth(24)
        top.addWidget(dot)
        top.addWidget(label(cat["name"], bold=True, size=15))
        top.addStretch()
        cnt = cat["doc_count"]
        badge_text = f"{cnt} doc{'s' if cnt != 1 else ''}" if cnt > 0 else "empty"
        badge = QLabel(badge_text)
        badge.setStyleSheet(
            f"background: {BG_DARK}; "
            f"color: {TEXT_DIM if cnt > 0 else TEXT_FAINT};"
            f"border-radius: 4px; padding: 2px 8px; font-size: 11px;"
        )
        top.addWidget(badge)
        v.addLayout(top)

        if cat.get("description"):
            v.addWidget(label(cat["description"], "dimLabel", wrap=True))

        br = QHBoxLayout()
        br.setSpacing(6)
        br.addWidget(btn("Rename", clicked=lambda _=False, c=cat: self._rename_cat(c)))
        if index > 0:
            br.addWidget(
                btn("\u25b2", "smallBtn",
                    clicked=lambda _=False, c=cat, i=index: self._move_up(c, i))
            )
        if index < len(self._cats) - 1:
            br.addWidget(
                btn("\u25bc", "smallBtn",
                    clicked=lambda _=False, c=cat, i=index: self._move_down(c, i))
            )
        br.addStretch()
        br.addWidget(
            btn("Delete", "danger", clicked=lambda _=False, c=cat: self._delete_cat(c))
        )
        bw = QWidget()
        bw.setLayout(br)
        v.addWidget(bw)
        return frame

    def _add_category(self):
        dlg = AddCategoryDialog(self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            d = dlg.result_data
            ok, err = data_add_category(
                d["name"], d["description"], d["color1"], d["color2"], d["icon_key"]
            )
            if ok:
                self.cat_changed.emit()
                self.mark_stale()
                self.refresh()
            else:
                QMessageBox.warning(self, "Error", err or "Failed to create category.")

    def _rename_cat(self, cat: dict):
        dlg = RenameCategoryDialog(cat, self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            d = dlg.result_data
            rename_category(cat["id"], d["name"], d["description"])
            self.cat_changed.emit()
            self.mark_stale()
            self.refresh()

    def _delete_cat(self, cat: dict):
        cnt = cat["doc_count"]
        if cnt > 0:
            reply = QMessageBox.warning(
                self, "Delete Category",
                f"Delete <b>{cat['name']}</b> and its "
                f"<b>{cnt} document{'s' if cnt != 1 else ''}</b>?<br><br>"
                f"All files will be moved to .trash/ for recovery.<br>"
                f"<i>This cannot be easily undone.</i>",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            )
        else:
            reply = QMessageBox.question(
                self, "Delete Category",
                f"Delete the empty <b>{cat['name']}</b> category?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            )
        if reply == QMessageBox.StandardButton.Yes:
            delete_category(cat["id"])
            self.cat_changed.emit()
            self.mark_stale()
            self.refresh()

    def _move_up(self, cat: dict, index: int):
        if index > 0:
            other = self._cats[index - 1]
            swap_categories(cat["id"], other["id"])
            self.cat_changed.emit()
            self.mark_stale()
            self.refresh()

    def _move_down(self, cat: dict, index: int):
        if index < len(self._cats) - 1:
            other = self._cats[index + 1]
            swap_categories(cat["id"], other["id"])
            self.cat_changed.emit()
            self.mark_stale()
            self.refresh()


# ═════════════════════════════════════════════════════════════
#  4. MARKDOWN EDITOR VIEW
# ═════════════════════════════════════════════════════════════

_PREVIEW_HTML = """<!DOCTYPE html>
<html data-theme="dark">
<head>
<meta charset="utf-8">
<style>
:root { color-scheme: dark; }
html, body {
    margin: 0; padding: 16px 20px;
    background: #0f172a; color: #e2e8f0;
    font-family: 'Segoe UI', system-ui, sans-serif; font-size: 15px; line-height: 1.7;
}
h1,h2,h3,h4 { color: #f1f5f9; margin-top: 1.4em; }
h1 { font-size: 1.8em; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 8px; }
h2 { font-size: 1.4em; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 6px; }
h3 { font-size: 1.15em; }
a { color: #818cf8; }
code {
    background: rgba(255,255,255,0.06); padding: 2px 6px; border-radius: 4px;
    font-family: 'Cascadia Code', 'Fira Code', monospace; font-size: 0.88em;
}
pre {
    background: #1e293b; border-radius: 8px; padding: 16px; overflow-x: auto;
    border: 1px solid rgba(255,255,255,0.06);
}
pre code { background: none; padding: 0; }
blockquote {
    border-left: 3px solid #6366f1; margin: 1em 0; padding: 8px 16px;
    background: rgba(99,102,241,0.06); color: #94a3b8;
}
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th, td { border: 1px solid rgba(255,255,255,0.08); padding: 8px 12px; text-align: left; }
th { background: rgba(255,255,255,0.04); font-weight: 600; }
ul, ol { padding-left: 24px; }
li { margin: 4px 0; }
img { max-width: 100%; border-radius: 6px; }
hr { border: none; border-top: 1px solid rgba(255,255,255,0.08); margin: 1.5em 0; }
.empty-msg { color: #64748b; text-align: center; padding: 80px 20px; font-style: italic; }
</style>
</head>
<body>
<div id="content"><p class="empty-msg">Open a markdown file to see the preview here…</p></div>
<script src="marked.min.js"></script>
<script>
marked.setOptions({ gfm: true, breaks: false });
function renderMD(md) {
    document.getElementById('content').innerHTML = marked.parse(md || '');
}
</script>
</body>
</html>"""


class MarkdownEditorView(QWidget):
    doc_saved = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._current_path = None
        self._dirty = False
        self._preview_ready = False
        self._pending_md = None
        self._stale = True
        self._build()

    @property
    def is_dirty(self) -> bool:
        return self._dirty

    def mark_stale(self):
        self._stale = True

    def refresh(self):
        if not self._stale:
            return
        self._stale = False
        self._refresh_file_combo()

    def open_file(self, slug: str):
        path = os.path.join(CONTENT_DIR, f"{slug}.md")
        if os.path.isfile(path):
            for i in range(self.file_combo.count()):
                if self.file_combo.itemData(i) == path:
                    self.file_combo.setCurrentIndex(i)
                    return
            self.file_combo.addItem(f"{slug}.md", path)
            self.file_combo.setCurrentIndex(self.file_combo.count() - 1)

    def _build(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        # Top bar
        top_bar = QWidget()
        top_bar.setStyleSheet(
            f"background: {BG_PANEL}; border-bottom: 1px solid {BORDER};"
        )
        tl = QHBoxLayout(top_bar)
        tl.setContentsMargins(16, 8, 16, 8)
        tl.setSpacing(8)
        tl.addWidget(label("Editor", "panelTitle"))

        self.file_combo = QComboBox()
        self.file_combo.setMinimumWidth(180)
        self._refresh_file_combo()
        self.file_combo.currentIndexChanged.connect(self._on_file_selected)
        tl.addWidget(self.file_combo, 1)

        tl.addWidget(btn("New", clicked=self._new_file))
        tl.addWidget(btn("Open…", clicked=self._browse_file))
        self.save_btn = btn("Save", "accent", clicked=self._save)
        self.save_btn.setEnabled(False)
        tl.addWidget(self.save_btn)
        self.status = label("", "dimLabel")
        tl.addWidget(self.status)
        outer.addWidget(top_bar)

        # Splitter: editor | preview
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Editor side
        editor_side = QWidget()
        ev = QVBoxLayout(editor_side)
        ev.setContentsMargins(0, 0, 0, 0)
        ev.setSpacing(0)

        self.editor = CodeEditor()
        self.editor.setPlaceholderText("Open a file to start editing…")
        self.editor.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        font = QFont("Cascadia Code", 12)
        font.setStyleHint(QFont.StyleHint.Monospace)
        self.editor.setFont(font)
        self.editor.setTabStopDistance(
            self.editor.fontMetrics().horizontalAdvance(" ") * 4
        )
        self.editor.textChanged.connect(self._on_text_changed)
        self.editor.cursorPositionChanged.connect(self._update_cursor_info)
        self.editor.setStyleSheet(
            f"CodeEditor {{ background: {BG_DARK}; color: {TEXT}; border: none;"
            f"selection-background-color: {ACCENT}; padding: 12px; }}"
        )

        self._highlighter = MarkdownHighlighter(self.editor.document())
        ev.addWidget(self.editor, 1)

        self.find_bar = FindReplaceBar(self.editor)
        ev.addWidget(self.find_bar)

        # Status bar
        self._status_bar = QWidget()
        self._status_bar.setStyleSheet(
            f"background: {BG_PANEL}; border-top: 1px solid {BORDER};"
        )
        sb_layout = QHBoxLayout(self._status_bar)
        sb_layout.setContentsMargins(12, 4, 12, 4)
        sb_layout.setSpacing(16)
        self._cursor_label = QLabel("Ln 1, Col 1")
        self._cursor_label.setStyleSheet(f"color: {TEXT_FAINT}; font-size: 11px;")
        sb_layout.addWidget(self._cursor_label)
        self._word_label = QLabel("")
        self._word_label.setStyleSheet(f"color: {TEXT_FAINT}; font-size: 11px;")
        sb_layout.addWidget(self._word_label)
        sb_layout.addStretch()
        self._autosave_label = QLabel("")
        self._autosave_label.setStyleSheet(f"color: {TEXT_FAINT}; font-size: 11px;")
        sb_layout.addWidget(self._autosave_label)
        ev.addWidget(self._status_bar)

        splitter.addWidget(editor_side)

        # Preview
        self.preview = QWebEngineView()
        self.preview.setStyleSheet("border: none;")
        self.preview.loadFinished.connect(self._on_preview_ready)
        base_url = QUrl.fromLocalFile(os.path.join(SITE_DIR, "js", ""))
        self.preview.setHtml(_PREVIEW_HTML, base_url)
        splitter.addWidget(self.preview)

        splitter.setSizes([500, 500])
        splitter.setStyleSheet(
            f"QSplitter::handle {{ background: {BORDER}; width: 1px; }}"
        )
        outer.addWidget(splitter, 1)

        # Shortcuts
        QShortcut(QKeySequence("Ctrl+S"), self, activated=self._save)
        QShortcut(QKeySequence("Ctrl+F"), self.editor, activated=self.find_bar.show_bar)
        QShortcut(QKeySequence("Ctrl+H"), self.editor, activated=self.find_bar.show_bar)
        QShortcut(QKeySequence("Escape"), self.editor, activated=self.find_bar.hide_bar)

        # Debounce timers
        self._preview_timer = QTimer()
        self._preview_timer.setSingleShot(True)
        self._preview_timer.setInterval(300)
        self._preview_timer.timeout.connect(self._update_preview)

        self._word_count_timer = QTimer()
        self._word_count_timer.setSingleShot(True)
        self._word_count_timer.setInterval(500)
        self._word_count_timer.timeout.connect(self._update_word_count)

        # Autosave (30 s)
        self._autosave_timer = QTimer()
        self._autosave_timer.setInterval(30_000)
        self._autosave_timer.timeout.connect(self._autosave)
        self._autosave_timer.start()

    def _on_preview_ready(self, ok):
        self._preview_ready = True
        if self._pending_md is not None:
            self._send_to_preview(self._pending_md)
            self._pending_md = None

    def _refresh_file_combo(self):
        self.file_combo.blockSignals(True)
        cur = self.file_combo.currentData()
        self.file_combo.clear()
        self.file_combo.addItem("\u2014 select file \u2014", None)
        if os.path.isdir(CONTENT_DIR):
            for fn in sorted(os.listdir(CONTENT_DIR)):
                if fn.endswith(".md"):
                    self.file_combo.addItem(fn, os.path.join(CONTENT_DIR, fn))
        for i in range(self.file_combo.count()):
            if self.file_combo.itemData(i) == cur:
                self.file_combo.setCurrentIndex(i)
                break
        self.file_combo.blockSignals(False)

    def _on_file_selected(self, idx):
        self._load_file(self.file_combo.itemData(idx))

    def _load_file(self, path):
        if self._dirty and self._current_path:
            reply = QMessageBox.question(
                self, "Unsaved Changes", "Save changes before switching?",
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No
                | QMessageBox.StandardButton.Cancel,
            )
            if reply == QMessageBox.StandardButton.Yes:
                self._save()
            elif reply == QMessageBox.StandardButton.Cancel:
                return

        if path and os.path.isfile(path):
            autosave_path = path + ".autosave"
            content = None
            if os.path.isfile(autosave_path):
                as_mtime = os.path.getmtime(autosave_path)
                f_mtime = os.path.getmtime(path)
                if as_mtime > f_mtime:
                    reply = QMessageBox.question(
                        self, "Recover Autosave",
                        f"An autosaved version exists ({relative_time(as_mtime)}).\n"
                        f"Recover it?",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    )
                    if reply == QMessageBox.StandardButton.Yes:
                        with open(autosave_path, "r", encoding="utf-8") as f:
                            content = f.read()

            if content is None:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

            self._current_path = path
            self.editor.blockSignals(True)
            self.editor.setPlainText(content)
            self.editor.blockSignals(False)
            self._dirty = False
            self.save_btn.setEnabled(False)
            self.status.setText(os.path.basename(path))
            self._update_preview()
            self._update_word_count()
        else:
            self._current_path = None
            self.editor.blockSignals(True)
            self.editor.clear()
            self.editor.blockSignals(False)
            self._dirty = False
            self.save_btn.setEnabled(False)
            self.status.setText("")
            self._word_label.setText("")

    def _browse_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Open Markdown File", CONTENT_DIR,
            "Markdown (*.md);;All Files (*)",
        )
        if path:
            for i in range(self.file_combo.count()):
                if self.file_combo.itemData(i) == path:
                    self.file_combo.setCurrentIndex(i)
                    return
            self.file_combo.addItem(os.path.basename(path), path)
            self.file_combo.setCurrentIndex(self.file_combo.count() - 1)

    def _new_file(self):
        name, ok = QInputDialog.getText(self, "New File", "Filename (without .md):")
        if ok and name.strip():
            slug = slugify(name.strip())
            path = os.path.join(CONTENT_DIR, f"{slug}.md")
            if os.path.exists(path):
                QMessageBox.warning(self, "File Exists", f"{slug}.md already exists.")
                return
            os.makedirs(CONTENT_DIR, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"# {name.strip()}\n\n")
            self._refresh_file_combo()
            for i in range(self.file_combo.count()):
                if self.file_combo.itemData(i) == path:
                    self.file_combo.setCurrentIndex(i)
                    break

    def _on_text_changed(self):
        self._dirty = True
        self.save_btn.setEnabled(True)
        self._preview_timer.start()
        self._word_count_timer.start()

    def _update_preview(self):
        md = self.editor.toPlainText()
        if self._preview_ready:
            self._send_to_preview(md)
        else:
            self._pending_md = md

    def _send_to_preview(self, md: str):
        safe = json.dumps(md)
        self.preview.page().runJavaScript(f"renderMD({safe})")

    def _update_cursor_info(self):
        cur = self.editor.textCursor()
        self._cursor_label.setText(
            f"Ln {cur.blockNumber() + 1}, Col {cur.columnNumber() + 1}"
        )

    def _update_word_count(self):
        text = self.editor.toPlainText()
        words = len(text.split()) if text.strip() else 0
        chars = len(text)
        lines = text.count("\n") + 1 if text else 0
        self._word_label.setText(
            f"{words:,} words  \u2022  {chars:,} chars  \u2022  {lines:,} lines"
        )

    def _autosave(self):
        if not self._dirty or not self._current_path:
            return
        autosave_path = self._current_path + ".autosave"
        try:
            atomic_write(autosave_path, self.editor.toPlainText())
            self._autosave_label.setText("Autosaved")
            QTimer.singleShot(3000, lambda: self._autosave_label.setText(""))
        except Exception:
            pass

    def _save(self):
        if not self._current_path:
            return
        try:
            atomic_write(self._current_path, self.editor.toPlainText())
            self._dirty = False
            self.save_btn.setEnabled(False)
            self.status.setText(f"Saved  \u2022  {os.path.basename(self._current_path)}")
            autosave_path = self._current_path + ".autosave"
            if os.path.exists(autosave_path):
                os.remove(autosave_path)
            self.doc_saved.emit()
        except Exception as e:
            QMessageBox.critical(self, "Save Error", str(e))
