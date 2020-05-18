from PyQt5.QtWidgets import QLabel, QFrame
from PyQt5.QtGui import QFont


class Label(QLabel):

    def __init__(self, parent, text=None, is_bold=False):
        super().__init__(parent)

        font = QFont("Segoe UI", 11)
        font.setBold(is_bold)

        self.setText(text)
        self.setFont(font)
