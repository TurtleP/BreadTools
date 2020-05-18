from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget

from .elements.imagebutton import ImageButton
from .page import Page


class SideBar(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.items = [
            ["", "General Tools", Page(parent, "General")],
            ["", "Command Line",  Page(parent, "Command")],
            ["", "Power",         Page(parent, "Power")],
            ["", "Settings",      Page(parent, "Settings")],
            [],
            ["", "About", Page(parent, "About")]
        ]

        self.buttons = []

        self.setFixedSize(192, parent.height())
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#e0e0e0"))
        self.setPalette(palette)

        for index in range(len(self.items)):
            if not self.items[index]:
                continue

            self.items[index][2].setText(self.items[index][1])
            button = ImageButton(self, 0, index * 44, self.items[index][2])
            button.setText(self.items[index][0], self.items[index][1])

            self.buttons.append(button)

        self.lastItem = None

        self.show()
