from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QFont, QPainter, QPen
from PyQt5.QtWidgets import QPushButton

from ...storage import Storage


class ImageButton(QPushButton):
    def __init__(self, parent, x, y):
        super().__init__(parent)

        self.move(x, y)
        self.setFixedSize(parent.width(), 44)

        self.setAutoFillBackground(True)
        self.setBackgroundRole(parent.backgroundRole())

        self.setCheckable(True)

        self.default_font = QFont("Segoe UI", 11)
        self.default_font.setBold(False)

        resolved_font = Storage.resolve_font("FontAwesome 5 Solid.otf")
        self.glyph_font = QFont(resolved_font, 11)

    def setText(self, glyph, text):
        super().setText(text)
        self.glyph = glyph

    def mousePressEvent(self, event):
        self.default_font.setBold(True)
        self.glyph_font.setBold(True)

        super().setChecked(True)

        if self.parent().lastItem != self:
            if self.parent().lastItem:
                self.parent().lastItem.unSelect()
            self.parent().lastItem = self

        self.repaint()

    def unSelect(self):
        self.default_font.setBold(False)
        self.glyph_font.setBold(False)

        super().setChecked(False)

        self.repaint()

    def setBackgroundColor(self, color):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(color))
        self.setPalette(palette)

    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        self.setBackgroundColor("#cfcfcf")

    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)

        palette = self.parent().palette()
        self.setPalette(palette)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setPen(QPen(QColor(64, 64, 64)))

        # Paint our glpyh
        if self.glyph:
            painter.setFont(self.glyph_font)
            painter.drawText(self.x() + 14, 0, self.width(), self.height(),
                             Qt.AlignVCenter, self.glyph)
        # Paint our text
        painter.setFont(self.default_font)
        painter.drawText(self.x() + 43, 0, self.width(), self.height(),
                         Qt.AlignVCenter, self.text())

        if self.isChecked():
            painter.fillRect(2, 1, 2, self.height() - 2, QColor("#2196f3"))

        painter.end()
