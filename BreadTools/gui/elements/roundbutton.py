from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont, QPainter, QPainterPath, QColor
from PyQt5.QtCore import Qt


class RoundButton(QPushButton):

    def __init__(self, parent):
        super().__init__(parent)

        font = QFont("Segoe UI", 12)
        font.setBold(True)

        self.setFixedSize(96, 32)

        self.setFont(font)

    def setEnabled(self, flag):
        super().setEnabled(flag)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 2, 2)

        color = QColor(0, 120, 212)

        if not self.isEnabled():
            color = QColor("#bdbdbd")

        painter.fillPath(path, color)

        color = QColor("#fafafa")

        if not self.isEnabled():
            color = QColor("#8d8d8d")

        painter.setPen(color)
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())
        painter.end()
