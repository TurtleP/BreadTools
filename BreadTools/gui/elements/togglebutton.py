from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QFont, QPainter, QPen
from PyQt5.QtWidgets import QPushButton

from ...storage import Storage
from ..colors import get_color

class ToggleButton(QPushButton):
    def __init__(self, parent, x, y):
        super().__init__(parent)

        self.move(x, y)
        self.setFixedSize(parent.width(), 44)

        self.setAutoFillBackground(True)
        self.refresh()

        self.setCheckable(True)

        self.default_font = QFont("Segoe UI", 11)
        self.default_font.setBold(False)

        resolved_font = Storage.resolve_font("FontAwesome 5 Solid.otf")
        self.glyph_font = QFont(resolved_font, 11)

    def refresh(self):
        self.setBackgroundColor(get_color("side"))

    def setText(self, glyph, text):
        super().setText(text)
        self.glyph = glyph

    def setBackgroundColor(self, color):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(color))
        self.setPalette(palette)

    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        self.setBackgroundColor(get_color("high"))

    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        self.setBackgroundColor(get_color("side"))

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setPen(QPen(QColor(get_color("text"))))

        # Paint our glpyh
        if self.glyph:
            painter.setFont(self.glyph_font)
            painter.drawText(self.x() + 14, 0, self.width(), self.height(),
                             Qt.AlignVCenter, self.glyph)
        # Paint our text
        painter.setFont(self.default_font)
        painter.drawText(self.x() + 43, 0, self.width(), self.height(),
                         Qt.AlignVCenter, self.text())

        painter.end()
