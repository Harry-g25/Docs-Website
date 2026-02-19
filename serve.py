"""
Local documentation server — double-click or run:
    python serve.py

Opens the Documentation Hub in your default browser.
Press Ctrl+C in the terminal to stop.
"""

from app.server import run_foreground_server

if __name__ == "__main__":
    run_foreground_server(port=8000, open_browser=True)
