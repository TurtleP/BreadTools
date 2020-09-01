from PyQt5.QtWidgets import QRadioButton, QWidget
from PyQt5.QtGui import QFont

from ..colors import get_color


class RadioGroup(QWidget):

    def __init__(self, parent, x, y, count, text):
        super().__init__(parent)

        self.move(x, y)
        self.radios = []

        for i in range(count):
            radio_button = QRadioButton(text[i], self)
            radio_button.move(0, (i * 22))

            radio_button.setFont(QFont("Segoe UI", 10))

            self.radios.append(radio_button)

        self.refresh()

    def refresh(self):
        print("refresh")
        for item in self.radios:
            color = get_color("text")
            item.setStyleSheet("color: " + color + ";")
