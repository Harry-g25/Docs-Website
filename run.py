"""
Documentation Hub — Entry Point

Launch the desktop documentation browser with an embedded HTTP server.

Usage:
    python run.py
"""

import signal
import sys

# QWebEngineWidgets MUST be imported before QApplication is created
import PyQt6.QtWebEngineWidgets  # noqa: F401
from PyQt6.QtWidgets import QApplication

from app.config import SETTINGS_ORG
from app.server import find_free_port, start_background_server
from app.browser import DocsBrowser, set_dark_title_bar


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    port = find_free_port()
    start_background_server(port)

    app = QApplication(sys.argv)
    app.setApplicationName("Documentation Hub")
    app.setOrganizationName(SETTINGS_ORG)

    window = DocsBrowser(port)

    if sys.platform == "win32":
        window.show()
        set_dark_title_bar(int(window.winId()))
    else:
        window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
