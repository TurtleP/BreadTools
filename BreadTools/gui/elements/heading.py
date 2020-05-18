from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont, QPainter, QColor
from PyQt5.QtCore import Qt


class Header(QWidget):

    def __init__(self, parent, text=None):
        super().__init__(parent)

        font = QFont("Segoe UI", 20)
        font.setBold(True)

        self.setFixedSize(parent.width() - 192, 50)

        self.text = text
        self.setFont(font)

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#eeeeee"))
        self.setPalette(palette)

        self.hide()

    def setText(self, text):
        self.text = text

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setFont(self.font())
        painter.drawText(18, self.y(),
                         self.width(), self.height(),
                         Qt.AlignVCenter, self.text)

        painter.end()
