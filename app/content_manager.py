"""
ContentManager panel — the left-side dock that orchestrates all four views.
"""

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel, QPushButton, QStackedWidget, QVBoxLayout,
    QWidget,
)

from app.config import ACCENT, BG_DARK, BG_PANEL, BORDER, TEXT, TEXT_DIM
from app.styles import CM_PANEL_SS
from app.views import (
    CategoryManagerView, DashboardView, DocsListView, MarkdownEditorView,
)

_TABS = ["Dashboard", "Documents", "Categories", "Editor"]


class ContentManager(QWidget):
    """Vertical panel with nav tabs and a stacked set of views."""

    closed = pyqtSignal()
    request_reload = pyqtSignal()
    request_add_doc = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("contentManager")
        self.setStyleSheet(CM_PANEL_SS)
        self._build()

    # ── Construction ────────────────────────────────────
    def _build(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        # Header bar
        header = QWidget()
        header.setObjectName("cmHeader")
        header.setStyleSheet(
            f"#cmHeader {{ background: {BG_PANEL};"
            f"border-bottom: 1px solid {BORDER}; }}"
        )
        hl = QHBoxLayout(header)
        hl.setContentsMargins(16, 8, 12, 8)
        title = QLabel("Content Manager")
        title.setStyleSheet(
            f"font-size: 14px; font-weight: 700; color: {TEXT};"
        )
        hl.addWidget(title)
        hl.addStretch()
        close_btn = QPushButton("\u2715")
        close_btn.setFixedSize(28, 28)
        close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        close_btn.setStyleSheet(
            f"QPushButton {{ background: transparent; border: none;"
            f"color: {TEXT_DIM}; font-size: 16px; border-radius: 4px; }}"
            f"QPushButton:hover {{ background: rgba(255,255,255,0.06);"
            f"color: {TEXT}; }}"
        )
        close_btn.clicked.connect(self.closed.emit)
        hl.addWidget(close_btn)
        outer.addWidget(header)

        # Tab bar
        tab_bar = QWidget()
        tab_bar.setObjectName("cmTabBar")
        tab_bar.setStyleSheet(
            f"#cmTabBar {{ background: {BG_DARK};"
            f"border-bottom: 1px solid {BORDER}; }}"
        )
        tl = QHBoxLayout(tab_bar)
        tl.setContentsMargins(8, 4, 8, 0)
        tl.setSpacing(0)
        self._tab_buttons: list[QPushButton] = []
        for i, name in enumerate(_TABS):
            b = QPushButton(name)
            b.setCheckable(True)
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setFixedHeight(32)
            b.clicked.connect(lambda _, idx=i: self.switch_tab(idx))
            self._tab_buttons.append(b)
            tl.addWidget(b)
        tl.addStretch()
        outer.addWidget(tab_bar)
        self._update_tab_style(0)

        # Views stack
        self._stack = QStackedWidget()
        self.dashboard = DashboardView()
        self.docs_list = DocsListView()
        self.cat_manager = CategoryManagerView()
        self.editor = MarkdownEditorView()

        self._stack.addWidget(self.dashboard)
        self._stack.addWidget(self.docs_list)
        self._stack.addWidget(self.cat_manager)
        self._stack.addWidget(self.editor)
        outer.addWidget(self._stack, 1)

        # Wire signals
        self.dashboard.navigate_to.connect(self.switch_tab)
        self.dashboard.request_add_doc.connect(self.request_add_doc.emit)

        self.docs_list.doc_changed.connect(self._on_data_changed)
        self.docs_list.open_editor.connect(self._open_in_editor)

        self.cat_manager.cat_changed.connect(self._on_data_changed)

        self.editor.doc_saved.connect(self._on_data_changed)

    # ── Public API ──────────────────────────────────────
    def switch_tab(self, index: int):
        self._stack.setCurrentIndex(index)
        self._update_tab_style(index)
        view = self._stack.widget(index)
        if hasattr(view, "refresh"):
            view.refresh()

    def mark_all_stale(self):
        self.dashboard.mark_stale()
        self.docs_list.mark_stale()
        self.cat_manager.mark_stale()
        self.editor.mark_stale()

    def refresh_current(self):
        view = self._stack.currentWidget()
        if hasattr(view, "mark_stale"):
            view.mark_stale()
        if hasattr(view, "refresh"):
            view.refresh()

    def check_can_close(self) -> bool:
        """Return True if it's safe to close (no unsaved changes)."""
        if self.editor.is_dirty:
            from PyQt6.QtWidgets import QMessageBox
            reply = QMessageBox.question(
                self, "Unsaved Changes",
                "The editor has unsaved changes. Discard them?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            )
            return reply == QMessageBox.StandardButton.Yes
        return True

    # ── Private ─────────────────────────────────────────
    def _update_tab_style(self, active_idx: int):
        for i, b in enumerate(self._tab_buttons):
            b.setChecked(i == active_idx)
            if i == active_idx:
                b.setStyleSheet(
                    f"QPushButton {{ background: {BG_PANEL}; color: {ACCENT};"
                    f"border: none; border-bottom: 2px solid {ACCENT};"
                    f"font-weight: 600; font-size: 12px; padding: 4px 14px; }}"
                )
            else:
                b.setStyleSheet(
                    f"QPushButton {{ background: transparent; color: {TEXT_DIM};"
                    f"border: none; border-bottom: 2px solid transparent;"
                    f"font-size: 12px; padding: 4px 14px; }}"
                    f"QPushButton:hover {{ color: {TEXT}; }}"
                )

    def _on_data_changed(self):
        self.mark_all_stale()
        self.request_reload.emit()

    def _open_in_editor(self, slug: str):
        self.editor.open_file(slug)
        self.switch_tab(3)
