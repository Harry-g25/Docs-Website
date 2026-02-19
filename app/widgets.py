"""
Reusable Qt widgets for the Documentation Hub.

Contains small, shared widgets used across dialogs, views, and panels:
  • Helper widget factories (make_separator, label, btn)
  • MarkdownHighlighter — syntax highlighting for the editor
  • CodeEditor + LineNumberArea — editor with line-number gutter
  • FindReplaceBar — find/replace in the markdown editor
"""

import re

from PyQt6.QtCore import Qt, QRect, QRegularExpression, QSize
from PyQt6.QtGui import (
    QColor, QFont, QPainter, QSyntaxHighlighter, QTextCharFormat,
    QTextCursor, QTextDocument,
)
from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QVBoxLayout, QWidget,
)

from app.config import (
    ACCENT, ACCENT_L, BG_CARD, BG_DARK, BORDER, GREEN,
    TEXT, TEXT_DIM, TEXT_FAINT,
)


# ═════════════════════════════════════════════════════════════
#  Helper widget factories
# ═════════════════════════════════════════════════════════════

def make_separator() -> QFrame:
    sep = QFrame()
    sep.setObjectName("sep")
    sep.setFrameShape(QFrame.Shape.HLine)
    return sep


def label(text: str, name: str | None = None, bold: bool = False,
          size: int | None = None, wrap: bool = False) -> QLabel:
    lbl = QLabel(text)
    if name:
        lbl.setObjectName(name)
    ss = []
    if bold:
        ss.append("font-weight: 700;")
    if size:
        ss.append(f"font-size: {size}px;")
    if ss:
        lbl.setStyleSheet(" ".join(ss))
    if wrap:
        lbl.setWordWrap(True)
    return lbl


def btn(text: str, obj_name: str | None = None, clicked=None) -> QPushButton:
    b = QPushButton(text)
    if obj_name:
        b.setObjectName(obj_name)
    if clicked:
        b.clicked.connect(clicked)
    return b


# ═════════════════════════════════════════════════════════════
#  Markdown syntax highlighter
# ═════════════════════════════════════════════════════════════

class MarkdownHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._rules: list[tuple] = []

        heading = QTextCharFormat()
        heading.setForeground(QColor(ACCENT_L))
        heading.setFontWeight(QFont.Weight.Bold)
        self._rules.append((QRegularExpression(r"^#{1,6}\s.*$"), heading))

        bold = QTextCharFormat()
        bold.setFontWeight(QFont.Weight.Bold)
        bold.setForeground(QColor("#f1f5f9"))
        self._rules.append((QRegularExpression(r"\*\*[^*]+\*\*"), bold))

        italic = QTextCharFormat()
        italic.setFontItalic(True)
        italic.setForeground(QColor("#cbd5e1"))
        self._rules.append(
            (QRegularExpression(r"(?<!\*)\*(?!\*)[^*]+\*(?!\*)"), italic)
        )

        code = QTextCharFormat()
        code.setForeground(QColor(GREEN))
        code.setFontFamily("Cascadia Code")
        self._rules.append((QRegularExpression(r"`[^`]+`"), code))

        link = QTextCharFormat()
        link.setForeground(QColor(ACCENT_L))
        link.setFontUnderline(True)
        self._rules.append((QRegularExpression(r"\[([^\]]+)\]\([^)]+\)"), link))

        quote = QTextCharFormat()
        quote.setForeground(QColor(TEXT_FAINT))
        self._rules.append((QRegularExpression(r"^>\s.*$"), quote))

        list_fmt = QTextCharFormat()
        list_fmt.setForeground(QColor(ACCENT))
        self._rules.append(
            (QRegularExpression(r"^(\s*)([-*+]|\d+\.)\s"), list_fmt)
        )

        fence = QTextCharFormat()
        fence.setForeground(QColor(TEXT_FAINT))
        self._rules.append((QRegularExpression(r"^```.*$"), fence))

        hr = QTextCharFormat()
        hr.setForeground(QColor(TEXT_FAINT))
        self._rules.append((QRegularExpression(r"^-{3,}$"), hr))

    def highlightBlock(self, text: str) -> None:
        for pattern, fmt in self._rules:
            it = pattern.globalMatch(text)
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), fmt)


# ═════════════════════════════════════════════════════════════
#  Code editor with line-number gutter
# ═════════════════════════════════════════════════════════════

class LineNumberArea(QWidget):
    def __init__(self, editor: "CodeEditor"):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.editor.lineNumberAreaPaintEvent(event)


class CodeEditor(QPlainTextEdit):
    """QPlainTextEdit with a line-number gutter."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._line_area = LineNumberArea(self)
        self.blockCountChanged.connect(self._update_width)
        self.updateRequest.connect(self._update_area)
        self._update_width(0)

    def lineNumberAreaWidth(self) -> int:
        digits = max(3, len(str(max(1, self.blockCount()))))
        return 8 + self.fontMetrics().horizontalAdvance("9") * digits + 4

    def _update_width(self, _=0):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def _update_area(self, rect, dy):
        if dy:
            self._line_area.scroll(0, dy)
        else:
            self._line_area.update(
                0, rect.y(), self._line_area.width(), rect.height()
            )
        if rect.contains(self.viewport().rect()):
            self._update_width()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self._line_area.setGeometry(
            QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height())
        )

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self._line_area)
        painter.fillRect(event.rect(), QColor(BG_DARK))
        block = self.firstVisibleBlock()
        num = block.blockNumber()
        top = round(
            self.blockBoundingGeometry(block)
            .translated(self.contentOffset())
            .top()
        )
        bottom = top + round(self.blockBoundingRect(block).height())
        height = self.fontMetrics().height()
        painter.setPen(QColor(TEXT_FAINT))
        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                painter.drawText(
                    0, top, self._line_area.width() - 6, height,
                    Qt.AlignmentFlag.AlignRight, str(num + 1),
                )
            block = block.next()
            top = bottom
            bottom = top + round(self.blockBoundingRect(block).height())
            num += 1
        painter.end()


# ═════════════════════════════════════════════════════════════
#  Find/replace bar (for markdown editor)
# ═════════════════════════════════════════════════════════════

class FindReplaceBar(QWidget):
    def __init__(self, editor: CodeEditor, parent=None):
        super().__init__(parent)
        self.editor = editor
        self.setVisible(False)
        self._build()

    def _build(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(4)

        # Find row
        fr = QHBoxLayout()
        self.find_input = QLineEdit()
        self.find_input.setPlaceholderText("Find…")
        self.find_input.textChanged.connect(self._count_matches)
        self.find_input.returnPressed.connect(self.find_next)
        fr.addWidget(self.find_input, 1)

        self.count_label = QLabel("")
        self.count_label.setStyleSheet(
            f"color: {TEXT_DIM}; font-size: 11px; min-width: 65px;"
        )
        fr.addWidget(self.count_label)

        for text, slot in [("▲", self.find_prev), ("▼", self.find_next)]:
            b = QPushButton(text)
            b.setObjectName("smallBtn")
            b.setFixedWidth(28)
            b.clicked.connect(slot)
            fr.addWidget(b)

        cb = QPushButton("✕")
        cb.setObjectName("smallBtn")
        cb.setFixedWidth(28)
        cb.clicked.connect(self.hide_bar)
        fr.addWidget(cb)
        layout.addLayout(fr)

        # Replace row
        rr = QHBoxLayout()
        self.replace_input = QLineEdit()
        self.replace_input.setPlaceholderText("Replace…")
        rr.addWidget(self.replace_input, 1)
        rb = btn("Replace", clicked=self.replace_one)
        rb.setObjectName("smallBtn")
        rr.addWidget(rb)
        ra = btn("All", clicked=self.replace_all)
        ra.setObjectName("smallBtn")
        rr.addWidget(ra)
        layout.addLayout(rr)

        self.setStyleSheet(
            f"FindReplaceBar {{ background: {BG_CARD}; "
            f"border-top: 1px solid {BORDER}; }}"
        )

    def show_bar(self):
        self.setVisible(True)
        self.find_input.setFocus()
        self.find_input.selectAll()

    def hide_bar(self):
        self.setVisible(False)

    def _count_matches(self, text: str):
        if not text:
            self.count_label.setText("")
            return
        content = self.editor.toPlainText()
        count = content.lower().count(text.lower())
        self.count_label.setText(f"{count} found")

    def find_next(self):
        text = self.find_input.text()
        if not text:
            return
        cursor = self.editor.textCursor()
        found = self.editor.document().find(text, cursor)
        if found.isNull():
            found = self.editor.document().find(text, 0)
        if not found.isNull():
            self.editor.setTextCursor(found)

    def find_prev(self):
        text = self.find_input.text()
        if not text:
            return
        cursor = self.editor.textCursor()
        found = self.editor.document().find(
            text, cursor, QTextDocument.FindFlag.FindBackward
        )
        if found.isNull():
            end = QTextCursor(self.editor.document())
            end.movePosition(QTextCursor.MoveOperation.End)
            found = self.editor.document().find(
                text, end, QTextDocument.FindFlag.FindBackward
            )
        if not found.isNull():
            self.editor.setTextCursor(found)

    def replace_one(self):
        text = self.find_input.text()
        repl = self.replace_input.text()
        if not text:
            return
        cur = self.editor.textCursor()
        if cur.hasSelection() and cur.selectedText().lower() == text.lower():
            cur.insertText(repl)
        self.find_next()

    def replace_all(self):
        text = self.find_input.text()
        repl = self.replace_input.text()
        if not text:
            return
        content = self.editor.toPlainText()
        new_content, count = re.subn(
            re.escape(text), repl, content, flags=re.IGNORECASE
        )
        if count:
            pos = self.editor.textCursor().position()
            self.editor.setPlainText(new_content)
            self.count_label.setText(f"Replaced {count}")
            cur = self.editor.textCursor()
            cur.setPosition(min(pos, len(new_content)))
            self.editor.setTextCursor(cur)


