"""
Embedded HTTP server for the Documentation Hub.

Provides both a foreground server (for ``serve.py``) and a background
daemon-thread server (for the desktop browser).
"""

import http.server
import os
import socket
import socketserver
import threading
import webbrowser

from app.config import BASE_DIR


# ── Utilities ────────────────────────────────────────────────────

def find_free_port() -> int:
    """Return a free TCP port on localhost."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    """Serves files from BASE_DIR, suppresses noisy access logs."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def log_message(self, fmt, *args):
        pass


class _LoggingHandler(http.server.SimpleHTTPRequestHandler):
    """Serves files from BASE_DIR, only logs 404 errors."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def log_message(self, fmt, *args):
        if args and "404" in str(args[0]):
            super().log_message(fmt, *args)


# ── Server functions ─────────────────────────────────────────────

def start_background_server(port: int):
    """Start a silent HTTP server on *port* in a daemon thread."""
    httpd = socketserver.TCPServer(("127.0.0.1", port), _QuietHandler)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    return httpd


def run_foreground_server(port: int = 8000, open_browser: bool = True):
    """Run a foreground HTTP server (blocking) and optionally open the browser."""
    url = f"http://localhost:{port}/site/index.html"

    with socketserver.TCPServer(("", port), _LoggingHandler) as httpd:
        print(f"  Serving docs at  {url}")
        print(f"  Press Ctrl+C to stop.\n")

        if open_browser:
            threading.Timer(0.4, lambda: webbrowser.open(url)).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Server stopped.")
