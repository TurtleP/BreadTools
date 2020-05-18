from PyQt5.QtWidgets import QRadioButton, QWidget, QSizePolicy
from PyQt5.QtGui import QFont


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
