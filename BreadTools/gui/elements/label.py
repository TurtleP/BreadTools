from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont, QColor, QPainter, QPen
from PyQt5.QtCore import Qt

from ..colors import get_color


class Label(QLabel):

    def __init__(self, parent, text=None, is_bold=False):
        super().__init__(parent)

        font = QFont("Segoe UI", 11)
        font.setBold(is_bold)

        self.setAutoFillBackground(True)

        self.refresh()

        self.setText(text)
        self.setFont(font)

    def refresh(self):
        pass

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setPen(QPen(QColor(get_color("text"))))

        painter.drawText(0, 0, self.width(), self.height(),
                         Qt.AlignLeft, self.text())
