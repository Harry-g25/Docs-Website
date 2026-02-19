"""
Git operations for the Documentation Hub.

Provides:
  • Synchronous helpers — fast reads (branch, remote, status summary)
  • GitCommandThread — QThread that runs a git command and streams output
"""

import os
import subprocess

from PyQt6.QtCore import QThread, pyqtSignal

from app.config import BASE_DIR


# ── Synchronous helpers (cheap, non-blocking) ───────────────

def _run(args: list[str], cwd: str = BASE_DIR) -> tuple[int, str]:
    """Run a git command and return (returncode, combined output)."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
        )
        out = (result.stdout + result.stderr).strip()
        return result.returncode, out
    except FileNotFoundError:
        return -1, "git not found — is Git installed and on PATH?"
    except subprocess.TimeoutExpired:
        return -1, "git command timed out."
    except Exception as e:
        return -1, str(e)


def is_git_repo() -> bool:
    code, _ = _run(["rev-parse", "--is-inside-work-tree"])
    return code == 0


def get_branch() -> str:
    """Return the current branch name, or an empty string on failure."""
    code, out = _run(["rev-parse", "--abbrev-ref", "HEAD"])
    return out if code == 0 else ""


def get_remote_url() -> str:
    """Return the push URL for 'origin', or empty string."""
    code, out = _run(["remote", "get-url", "origin"])
    return out if code == 0 else ""


def get_status_lines() -> list[str]:
    """Return git status --short lines (e.g. ' M site/index.html')."""
    code, out = _run(["status", "--short"])
    if code != 0 or not out:
        return []
    return [line for line in out.splitlines() if line.strip()]


def get_unpushed_count() -> int:
    """Return the number of local commits not yet pushed."""
    code, out = _run(["rev-list", "--count", "@{u}..HEAD"])
    try:
        return int(out) if code == 0 else 0
    except ValueError:
        return 0


def has_remote() -> bool:
    code, out = _run(["remote"])
    return code == 0 and bool(out.strip())


# ── Async command thread ──────────────────────────────────────

class GitCommandThread(QThread):
    """
    Run a sequence of git commands (and optional post-commands) in a
    background thread, streaming output line-by-line via `output`.

    Signals:
        output(str)   — a line of stdout/stderr
        succeeded()   — all commands exited with code 0
        failed(str)   — one command failed; passes summary message
    """

    output = pyqtSignal(str)
    succeeded = pyqtSignal()
    failed = pyqtSignal(str)

    def __init__(self, commands: list[list[str]], cwd: str = BASE_DIR,
                 parent=None):
        """
        Args:
            commands: list of argument lists, e.g.
                      [["add", "-A"], ["commit", "-m", "msg"], ["push"]]
                      Each is prefixed with 'git' automatically.
        """
        super().__init__(parent)
        self._commands = commands
        self._cwd = cwd

    def run(self):
        for args in self._commands:
            cmd = ["git"] + args
            self.output.emit(f"$ git {' '.join(args)}")
            try:
                proc = subprocess.Popen(
                    cmd,
                    cwd=self._cwd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                )
                for line in proc.stdout:
                    stripped = line.rstrip()
                    if stripped:
                        self.output.emit(stripped)
                proc.wait()
                if proc.returncode != 0:
                    self.failed.emit(
                        f"`git {args[0]}` exited with code {proc.returncode}"
                    )
                    return
            except FileNotFoundError:
                self.failed.emit(
                    "git not found — is Git installed and on PATH?"
                )
                return
            except Exception as e:
                self.failed.emit(str(e))
                return

        self.succeeded.emit()
