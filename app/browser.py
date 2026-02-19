"""
DocsBrowser — main application window.

Single-window shell: toolbar, find-bar, QWebEngineView, and an
optional ContentManager side panel via QSplitter.
"""

import sys
from pathlib import Path

from PyQt6.QtCore import Qt, QSize, QUrl, QSettings, QStandardPaths
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMenu,
    QPushButton, QSizePolicy, QSplitter, QStyle, QSystemTrayIcon,
    QToolBar, QVBoxLayout, QWidget,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import (
    QWebEnginePage,
    QWebEngineSettings,
    QWebEngineDownloadRequest,
)

from app.config import SETTINGS_ORG, SETTINGS_APP
from app.icons import (
    SVG_ADD, SVG_BACK, SVG_FORWARD, SVG_HOME, make_app_icon, svg_icon,
)
from app.styles import MAIN_WINDOW_SS, FIND_BAR_SS
from app.content_manager import ContentManager
from app.dialogs import AddDocWizard, CMLoginDialog


# ── Find-in-page bar ───────────────────────────────────
class FindBar(QWidget):
    """Find-in-page bar that slides in above the web view."""

    def __init__(self, web_view: QWebEngineView, parent=None):
        super().__init__(parent)
        self.web_view = web_view
        self.setVisible(False)
        self.setStyleSheet(FIND_BAR_SS)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 4, 12, 4)
        layout.setSpacing(6)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Find in page\u2026")
        self.input.textChanged.connect(self._on_text_changed)
        self.input.returnPressed.connect(self._find_next)

        self.status_label = QLabel("")
        self.prev_btn = QPushButton("\u25b2")
        self.prev_btn.setToolTip("Previous (Shift+Enter)")
        self.prev_btn.clicked.connect(self._find_prev)
        self.next_btn = QPushButton("\u25bc")
        self.next_btn.setToolTip("Next (Enter)")
        self.next_btn.clicked.connect(self._find_next)
        self.close_btn = QPushButton("\u2715")
        self.close_btn.setToolTip("Close (Esc)")
        self.close_btn.clicked.connect(self.hide_bar)

        layout.addWidget(self.input)
        layout.addWidget(self.prev_btn)
        layout.addWidget(self.next_btn)
        layout.addWidget(self.status_label)
        layout.addStretch()
        layout.addWidget(self.close_btn)

    def show_bar(self):
        self.setVisible(True)
        self.input.setFocus()
        self.input.selectAll()

    def hide_bar(self):
        self.setVisible(False)
        self.web_view.findText("")

    def _on_text_changed(self, text: str):
        self.web_view.findText(text) if text else (
            self.web_view.findText(""), self.status_label.setText("")
        )

    def _find_next(self):
        if t := self.input.text():
            self.web_view.findText(t)

    def _find_prev(self):
        if t := self.input.text():
            self.web_view.findText(t, QWebEnginePage.FindFlag.FindBackward)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.hide_bar()
        elif (event.key() == Qt.Key.Key_Return
              and event.modifiers() & Qt.KeyboardModifier.ShiftModifier):
            self._find_prev()
        else:
            super().keyPressEvent(event)


class DocsBrowser(QMainWindow):
    """Lightweight documentation browser with integrated content management."""

    def __init__(self, port: int):
        super().__init__()
        self.port = port
        self.home_url = QUrl(f"http://127.0.0.1:{port}/site/index.html")
        self._settings = QSettings(SETTINGS_ORG, SETTINGS_APP)

        self._init_window()
        self._init_web()
        self._init_layout()
        self._init_toolbar()
        self._init_shortcuts()
        self._init_tray()

    # ── Window ──────────────────────────────────────────
    def _init_window(self):
        self.setWindowTitle("Documentation Hub")
        self.app_icon = make_app_icon()
        self.setWindowIcon(self.app_icon)
        self.setStyleSheet(MAIN_WINDOW_SS)

        screen = QApplication.primaryScreen().availableGeometry()
        w = int(screen.width() * 0.8)
        h = int(screen.height() * 0.8)
        x = screen.x() + (screen.width() - w) // 2
        y = screen.y() + (screen.height() - h) // 2

        saved = self._settings.value("geometry")
        if saved:
            self.restoreGeometry(saved)
        else:
            self.setGeometry(x, y, w, h)

    # ── WebView ─────────────────────────────────────────
    def _init_web(self):
        self.web = QWebEngineView()

        settings = self.web.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.PdfViewerEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)

        profile = self.web.page().profile()
        profile.downloadRequested.connect(self._on_download_requested)

        self.web.setUrl(self.home_url)
        self.web.urlChanged.connect(self._on_url_changed)
        self.web.titleChanged.connect(self._on_title_changed)

    def _on_download_requested(self, download: QWebEngineDownloadRequest):
        download_dir = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.DownloadLocation
        )
        if not download_dir:
            download_dir = str(Path.home() / "Downloads")

        try:
            Path(download_dir).mkdir(parents=True, exist_ok=True)
        except Exception:
            download_dir = str(Path.home())

        download.setDownloadDirectory(download_dir)

        def _maybe_open_when_done():
            try:
                if download.state() != QWebEngineDownloadRequest.DownloadState.DownloadCompleted:
                    return
                name = (download.downloadFileName() or "").lower()
                if not name.endswith(".pdf"):
                    return
                local_path = str(Path(download.downloadDirectory()) / download.downloadFileName())
                QDesktopServices.openUrl(QUrl.fromLocalFile(local_path))
            except Exception:
                return

        download.stateChanged.connect(lambda _state: _maybe_open_when_done())
        download.accept()

    # ── Central layout (splitter) ───────────────────────
    def _init_layout(self):
        self.find_bar = FindBar(self.web)

        browser_side = QWidget()
        vbox = QVBoxLayout(browser_side)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        vbox.addWidget(self.find_bar)
        vbox.addWidget(self.web, 1)

        self.content_manager = ContentManager()
        self.content_manager.closed.connect(self._close_cm)
        self.content_manager.request_reload.connect(self.web.reload)
        self.content_manager.request_add_doc.connect(self._open_add_wizard)
        self.content_manager.hide()

        self._splitter = QSplitter(Qt.Orientation.Horizontal)
        self._splitter.setChildrenCollapsible(False)
        self._splitter.addWidget(browser_side)
        self._splitter.addWidget(self.content_manager)
        self._splitter.setStretchFactor(0, 1)
        self._splitter.setStretchFactor(1, 0)
        self._splitter.setStyleSheet(
            "QSplitter::handle { background: rgba(255,255,255,0.06); width: 1px; }"
        )
        self.setCentralWidget(self._splitter)

    # ── Toolbar ─────────────────────────────────────────
    def _init_toolbar(self):
        tb = QToolBar("Navigation")
        tb.setMovable(False)
        tb.setFloatable(False)
        tb.setIconSize(QSize(20, 20))
        tb.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        try:
            back_icon = svg_icon(SVG_BACK)
            fwd_icon = svg_icon(SVG_FORWARD)
            home_icon = svg_icon(SVG_HOME)
            add_icon = svg_icon(SVG_ADD)
        except ImportError:
            sp = self.style()
            back_icon = sp.standardIcon(QStyle.StandardPixmap.SP_ArrowBack)
            fwd_icon = sp.standardIcon(QStyle.StandardPixmap.SP_ArrowForward)
            home_icon = sp.standardIcon(QStyle.StandardPixmap.SP_DirHomeIcon)
            add_icon = sp.standardIcon(QStyle.StandardPixmap.SP_FileIcon)

        self.back_action = tb.addAction(back_icon, "Back")
        self.back_action.setToolTip("Back  (Alt+\u2190)")
        self.back_action.triggered.connect(self.web.back)
        self.back_action.setEnabled(False)

        self.fwd_action = tb.addAction(fwd_icon, "Forward")
        self.fwd_action.setToolTip("Forward  (Alt+\u2192)")
        self.fwd_action.triggered.connect(self.web.forward)
        self.fwd_action.setEnabled(False)

        self.home_action = tb.addAction(home_icon, "Home")
        self.home_action.setToolTip("Documentation Hub  (Alt+Home)")
        self.home_action.triggered.connect(self._go_home)

        spacer = QWidget()
        spacer.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred,
        )
        tb.addWidget(spacer)

        self.cm_action = tb.addAction(add_icon, "Content Manager")
        self.cm_action.setToolTip("Toggle Content Manager  (Ctrl+M)")
        self.cm_action.triggered.connect(self._toggle_cm)

        self.page_label = QLabel("Documentation Hub")
        self.page_label.setStyleSheet(
            "color: #64748b; font-size: 12px; padding-right: 12px;"
        )
        tb.addWidget(self.page_label)
        self.addToolBar(tb)

    # ── Shortcuts ───────────────────────────────────────
    def _init_shortcuts(self):
        QShortcut(QKeySequence("Ctrl+F"), self, activated=self.find_bar.show_bar)
        QShortcut(QKeySequence("Escape"), self, activated=self.find_bar.hide_bar)
        QShortcut(QKeySequence("Alt+Left"), self, activated=self.web.back)
        QShortcut(QKeySequence("Alt+Right"), self, activated=self.web.forward)
        QShortcut(QKeySequence("Alt+Home"), self, activated=self._go_home)
        QShortcut(QKeySequence("Ctrl+M"), self, activated=self._toggle_cm)
        QShortcut(QKeySequence("Ctrl+Q"), self, activated=self._quit)

    # ── System tray ─────────────────────────────────────
    def _init_tray(self):
        if not QSystemTrayIcon.isSystemTrayAvailable():
            self.tray = None
            return

        self.tray = QSystemTrayIcon(self.app_icon, self)
        self.tray.setToolTip("Documentation Hub")

        menu = QMenu()
        menu.addAction("Show", self._tray_restore)
        menu.addAction("Go to Hub", lambda: (self._tray_restore(), self._go_home()))
        menu.addSeparator()
        menu.addAction("Content Manager",
                       lambda: (self._tray_restore(), self._toggle_cm()))
        menu.addSeparator()
        menu.addAction("Quit", self._quit)

        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self._on_tray_activated)
        self.tray.show()

    # ── Navigation ──────────────────────────────────────
    def _go_home(self):
        self.web.setUrl(self.home_url)

    def _on_url_changed(self, url: QUrl):
        history = self.web.history()
        self.back_action.setEnabled(history.canGoBack())
        self.fwd_action.setEnabled(history.canGoForward())

    def _on_title_changed(self, title: str):
        display = title or "Documentation Hub"
        self.setWindowTitle(f"{display} \u2014 Docs Browser")
        self.page_label.setText(display)

    # ── Content Manager ─────────────────────────────────
    def _toggle_cm(self):
        if self.content_manager.isVisible():
            self._close_cm()
        else:
            self._open_cm()

    def _open_cm(self):
        dlg = CMLoginDialog(self)
        if dlg.exec() != CMLoginDialog.DialogCode.Accepted:
            return
        self.content_manager.show()
        saved = self._settings.value("splitter_sizes")
        if saved:
            self._splitter.restoreState(saved)
        else:
            total = self._splitter.width()
            self._splitter.setSizes([int(total * 0.45), int(total * 0.55)])
        self.content_manager.switch_tab(0)

    def _close_cm(self):
        if not self.content_manager.check_can_close():
            return
        self._settings.setValue("splitter_sizes", self._splitter.saveState())
        self.content_manager.hide()

    # ── Add Doc Wizard ──────────────────────────────────
    def _open_add_wizard(self):
        wizard = AddDocWizard(self, on_complete=self._on_doc_added)
        wizard.exec()

    def _on_doc_added(self):
        self.web.reload()
        if self.content_manager.isVisible():
            self.content_manager.mark_all_stale()
            self.content_manager.refresh_current()

    # ── Tray ────────────────────────────────────────────
    def _on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self._tray_restore()

    def _tray_restore(self):
        self.showNormal()
        self.activateWindow()
        self.raise_()

    # ── Window events ───────────────────────────────────
    def closeEvent(self, event):
        self._settings.setValue("geometry", self.saveGeometry())
        if self.tray and self.tray.isVisible():
            self.hide()
            self.tray.showMessage(
                "Documentation Hub",
                "Still running in the system tray. Right-click \u2192 Quit to exit.",
                QSystemTrayIcon.MessageIcon.Information,
                2000,
            )
            event.ignore()
        else:
            event.accept()

    def _quit(self):
        self._settings.setValue("geometry", self.saveGeometry())
        if self.tray:
            self.tray.hide()
        QApplication.quit()


# ── Dark title bar (Windows) ───────────────────────────
def set_dark_title_bar(hwnd: int):
    """Enable dark title bar on Windows 10 build 18985+ / Windows 11."""
    try:
        import ctypes
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd, 20,
            ctypes.byref(ctypes.c_int(1)),
            ctypes.sizeof(ctypes.c_int),
        )
    except Exception:
        pass
