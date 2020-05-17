from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor

from .elements.imagebutton import ImageButton


class SideBar(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.items = [
            ["", "General Tools"],
            ["", "Command Line"],
            ["", "Power"],
            ["", "Settings"],
            [],
            ["", "About"]
        ]

        self.setFixedSize(192, parent.height())
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#e0e0e0"))
        self.setPalette(palette)

        for index in range(len(self.items)):
            if not self.items[index]:
                continue

            button = ImageButton(self, 0, index * 44)
            button.setText(*self.items[index])

        self.lastItem = None

        self.show()
