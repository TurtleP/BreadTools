from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont


class Label(QLabel):

    def __init__(self, parent, x, y, text=None):
        super().__init__(parent)
        self.move(x, y)

        font = QFont("Segoe UI", 11)
        font.setBold(True)

        self.setText(text)
        self.setFont(font)
