from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QPen
from PyQt5.QtWidgets import QPushButton


class Checkbox(QPushButton):
    def __init__(self, parent, x, y, text=None):
        super().__init__(parent)

        self.move(x, y)
        self.setFixedSize(16, 16)
        self.setText(text)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(QPen(QColor(194, 194, 194)))
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 2, 2)

        painter.setPen(QColor(0, 0, 0))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

        painter.end()
