"""Check fenced code block language tags in site/content/*.md.

This is a heuristic checker to catch obvious mismatches like:
- JSON content fenced as ```python
- shell sessions fenced as ```output
- output blocks fenced as ```bash

It prints a list of "have -> want" suggestions with file and line.

Usage:
    .venv\\Scripts\\python.exe tools\\check_fence_languages.py

Optional:
  --max N   limit output
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


# Matches a fence line like:
#   ```python
#   ```
#   ~~~json
# Allows 3+ fence chars, optional info string with no spaces.
FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([^\s`]*)\s*$")

PY_DEFCLASS_LINE = re.compile(r"^\s*(def|class)\b")
PY_IMPORT_LINE = re.compile(r"^\s*import\s+\S")
PY_FROM_IMPORT_LINE = re.compile(r"^\s*from\s+\S+\s+import\b")
PY_BLOCK_START = re.compile(r"^\s*(if|elif|else|for|while|try|except|with)\b.*:\s*$")
PY_MISC = re.compile(r"\b(None|True|False|lambda)\b")
PY_PRINT_CALL = re.compile(r"\bprint\s*\(")
JSON_START = re.compile(r"^\s*[\[{]")
HTML_START = re.compile(r"^\s*<(!doctype|html|div|span|p|a|script|style|head|body)\b", re.I)
HTML_HINT = re.compile(r"^\s*(?:<!--|<!doctype\b|</?[a-z][a-z0-9-]*\b)", re.I)
CSS_PROP = re.compile(r"^\s*[a-z-]+\s*:\s*[^;]+;\s*$", re.I)
SHELL_PROMPT = re.compile(r"^(\$\s|PS\s|C:\\\\|\w+@\w+[:~])")
BASH_COMMAND = re.compile(
    r"^\s*(?:sudo\s+)?(?:python3?|py|pip3?|git|npm|node|pnpm|yarn|cd|dir|ls|cat|echo|curl|wget|pwsh|powershell)(?:\s|$)",
    re.I,
)

OUTPUT_LANGS = {"output", "stdout", "stderr", "console", "terminal"}
SPECIAL_LANGS = OUTPUT_LANGS | {"ctk-preview", "html-live"}

LANG_SYNONYMS = {
    "sh": "bash",
    "shell": "bash",
    "py": "python",
    "js": "javascript",
}

CODE_LANGS = {"python", "json", "html", "css", "bash", "javascript"}


@dataclass(frozen=True)
class Issue:
    path: Path
    line: int
    have: str
    want: str
    confidence: str  # high | medium
    kind: str = "language"  # language | structure


@dataclass(frozen=True)
class FenceOpen:
    indent: str
    marker: str  # e.g. ``` or ~~~ (3+)
    info: str


def _parse_fence_line(line: str) -> FenceOpen | None:
    m = FENCE_RE.match(line)
    if not m:
        return None
    indent, marker, info = m.group(1), m.group(2), m.group(3) or ""
    return FenceOpen(indent=indent, marker=marker, info=info)


def _is_closing_fence(open_marker: str, fence: FenceOpen) -> bool:
    # Closing fence rules (Markdown): same fence char (` or ~), length >= opener, and no info string.
    if not fence.marker:
        return False
    if fence.info:
        return False
    if fence.marker[0] != open_marker[0]:
        return False
    return len(fence.marker) >= len(open_marker)


def _trim_blank_edges(lines: list[str]) -> list[str]:
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def _norm_lang(lang: str) -> str:
    lang = (lang or "").strip().lower()
    return LANG_SYNONYMS.get(lang, lang)


def guess_language(block_lines: list[str]) -> str | None:
    lines = _trim_blank_edges(block_lines)
    if not lines:
        return None

    text = "\n".join(lines)
    nonblank = [l for l in lines if l.strip()]
    first = nonblank[0].strip() if nonblank else ""

    if first.startswith((">>>", "...")):
        return "python"

    if SHELL_PROMPT.search(first):
        return "bash"

    # Many docs show commands without a $ prompt. Treat those as bash.
    if all(BASH_COMMAND.search(l) or not l.strip() or l.strip().startswith("#") for l in lines[:6]):
        if any(BASH_COMMAND.search(l) for l in lines[:6]):
            return "bash"

    if JSON_START.match(first):
        try:
            json.loads(text)
            return "json"
        except Exception:
            pass

    looks_html_immediate = (
        HTML_START.match(first)
        or HTML_HINT.match(first)
        or (len(nonblank) > 1 and HTML_HINT.match(nonblank[1]))
    )
    if looks_html_immediate:
        return "html"

    if ("{" in text and "}" in text) and any(CSS_PROP.match(l) for l in lines[:16]):
        return "css"

    python_score = 0
    if any(
        PY_DEFCLASS_LINE.match(l) or PY_IMPORT_LINE.match(l) or PY_FROM_IMPORT_LINE.match(l)
        for l in lines[:30]
    ):
        python_score += 3
    if any(PY_BLOCK_START.match(l) for l in lines[:50]):
        python_score += 2
    if PY_PRINT_CALL.search(text):
        python_score += 1
    if PY_MISC.search(text):
        python_score += 1
    if re.search(r"^\s*self\.", text, re.M):
        python_score += 1

    if python_score >= 3:
        return "python"

    return None


def guess_output_kind(block_lines: list[str]) -> str | None:
    """Return an output language kind when it's *very* likely output.

    This intentionally avoids weak heuristics (which create false positives).
    """

    lines = _trim_blank_edges(block_lines)
    if not lines:
        return None

    first = lines[0].lstrip()
    text = "\n".join(lines)

    if first.startswith((">>>", "...")):
        return None

    stderr_markers = (
        r"^Traceback \(most recent call last\):",
        r"^(?:[A-Za-z]+Error|Exception):\s+",
        r"^File \"[^\"]+\", line \d+",
        r"^SyntaxError:\s+",
        r"^ModuleNotFoundError:\s+",
    )

    if any(re.search(pat, text, re.M) for pat in stderr_markers):
        return "stderr"

    return None


def scan_file(path: Path, *, apply: bool) -> list[Issue]:
    lines = path.read_text(encoding="utf-8").splitlines()
    issues: list[Issue] = []
    changed = False

    i = 0
    prev_nonblank: str | None = None
    while i < len(lines):
        fence_open = _parse_fence_line(lines[i])
        if not fence_open:
            if lines[i].strip():
                prev_nonblank = lines[i].strip()
            i += 1
            continue

        indent = fence_open.indent
        open_marker = fence_open.marker
        lang_raw = fence_open.info
        lang = _norm_lang(lang_raw)
        start_line = i + 1

        # Find the closing fence.
        j = i + 1
        block: list[str] = []
        while j < len(lines):
            fence_close = _parse_fence_line(lines[j])
            if fence_close and _is_closing_fence(open_marker, fence_close):
                break
            block.append(lines[j])
            j += 1

        # Unclosed fence; report a structural issue and stop to avoid cascading noise.
        if j >= len(lines):
            issues.append(
                Issue(
                    path=path,
                    line=start_line,
                    have="unclosed fence",
                    want=f"close with {open_marker}",
                    confidence="high",
                    kind="structure",
                )
            )
            break

        guessed = guess_language(block)
        output_kind = guess_output_kind(block)

        hint_kind: str | None = None
        if prev_nonblank:
            hint = prev_nonblank.rstrip(":").strip().lower()
            if hint in {"output", "stdout", "stderr", "console", "terminal"}:
                hint_kind = "output" if hint == "output" else hint

        # Respect renderer-specific languages.
        if lang in SPECIAL_LANGS or (lang and lang not in CODE_LANGS and lang != ""):
            i = j + 1
            continue

        if not lang:
            if hint_kind:
                want_kind = output_kind or hint_kind
                issues.append(Issue(path=path, line=start_line, have="(none)", want=want_kind, confidence="high"))
                if apply:
                    lines[start_line - 1] = f"{indent}{open_marker}{want_kind}"
                    changed = True
            elif guessed:
                issues.append(Issue(path=path, line=start_line, have="(none)", want=guessed, confidence="high"))
                if apply:
                    lines[start_line - 1] = f"{indent}{open_marker}{guessed}"
                    changed = True
            elif output_kind:
                issues.append(Issue(path=path, line=start_line, have="(none)", want=output_kind, confidence="high"))
                if apply:
                    lines[start_line - 1] = f"{indent}{open_marker}{output_kind}"
                    changed = True

        elif lang in OUTPUT_LANGS:
            # Output block fenced as output, but the content is clearly code.
            if guessed and guessed in CODE_LANGS:
                issues.append(Issue(path=path, line=start_line, have=lang, want=guessed, confidence="high"))
                if apply:
                    lines[start_line - 1] = f"{indent}{open_marker}{guessed}"
                    changed = True
            elif output_kind and output_kind != lang:
                issues.append(Issue(path=path, line=start_line, have=lang, want=output_kind, confidence="high"))
                if apply:
                    lines[start_line - 1] = f"{indent}{open_marker}{output_kind}"
                    changed = True

        else:
            # Code block fenced as some code language, but it looks like a different one.
            if guessed and guessed in CODE_LANGS and guessed != lang:
                issues.append(Issue(path=path, line=start_line, have=lang, want=guessed, confidence="high"))
                if apply:
                    lines[start_line - 1] = f"{indent}{open_marker}{guessed}"
                    changed = True
            elif output_kind and lang in CODE_LANGS:
                # Only flip to stderr for very obvious error output.
                issues.append(Issue(path=path, line=start_line, have=lang, want=output_kind, confidence="medium"))
                if apply:
                    lines[start_line - 1] = f"{indent}{open_marker}{output_kind}"
                    changed = True

        i = j + 1

    if apply and changed:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=300)
    ap.add_argument("--apply", action="store_true", help="apply high-confidence fixes to files")
    args = ap.parse_args()

    content_dir = Path("site") / "content"
    paths = sorted(content_dir.glob("*.md"))

    all_issues: list[Issue] = []
    for p in paths:
        all_issues.extend(scan_file(p, apply=args.apply))

    structural = [x for x in all_issues if x.kind == "structure"]
    language = [x for x in all_issues if x.kind == "language"]

    print(f"Fence structure issues: {len(structural)}")
    print(f"Potential fence language issues: {len(language)}")

    shown = 0
    for issue in structural + language:
        if shown >= args.max:
            break
        rel = issue.path.as_posix()
        prefix = "STRUCT" if issue.kind == "structure" else "LANG"
        print(f"- {prefix}  {rel}:{issue.line}  {issue.have} -> {issue.want}  ({issue.confidence})")
        shown += 1

    if len(all_issues) > args.max:
        print(f"… {len(all_issues) - args.max} more")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
