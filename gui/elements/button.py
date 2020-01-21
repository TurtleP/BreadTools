from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QPainter, QPainterPath, QPen
from PyQt5.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, parent, x, y, text):
        super().__init__(parent)
        self.setText(text)

        self.move(x, y)
        self.setFixedSize(128, 32)

        font = QFont()
        font.setBold(True)

        self.setFont(font)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 2, 2)
        painter.fillPath(path, QColor(0, 120, 212))

        painter.setPen(QColor(255, 255, 255))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())
        painter.end()
