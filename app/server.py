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


class _ReusableTCPServer(socketserver.TCPServer):
    # Helps with quick restart after Ctrl+C on some platforms.
    allow_reuse_address = True


# ── Server functions ─────────────────────────────────────────────

def start_background_server(port: int):
    """Start a silent HTTP server on *port* in a daemon thread."""
    httpd = _ReusableTCPServer(("127.0.0.1", port), _QuietHandler)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    return httpd


def run_foreground_server(port: int = 8000, open_browser: bool = True):
    """Run a foreground HTTP server (blocking) and optionally open the browser."""
    requested_port = port
    chosen_port = port

    while True:
        url = f"http://localhost:{chosen_port}/site/index.html"
        try:
            with _ReusableTCPServer(("127.0.0.1", chosen_port), _LoggingHandler) as httpd:
                if requested_port != chosen_port:
                    print(
                        f"  Port {requested_port} is busy; using {chosen_port} instead."
                    )
                print(f"  Serving docs at  {url}")
                print("  Press Ctrl+C to stop.\n")

                if open_browser:
                    threading.Timer(0.4, lambda: webbrowser.open(url)).start()

                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    print("\n  Server stopped.")
                return
        except OSError as e:
            # WinError 10048: only one usage of each socket address is normally permitted.
            if getattr(e, "winerror", None) == 10048 or e.errno in {48, 98}:
                chosen_port = find_free_port()
                continue
            raise
