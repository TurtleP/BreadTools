from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget

from .colors import get_color, toggle_colors
from .elements.imagebutton import ImageButton
from .elements.togglebutton import ToggleButton
from .page import Page


class SideBar(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.items = [
            ["", "image", "General Tools", Page(parent, "General")],
            ["", "image", "Command Line",  Page(parent, "Command")],
            ["", "image", "Power",         Page(parent, "Power")],
            ["", "image", "Windows Settings",      Page(parent, "WinSettings")],
            [],
            ["", "toggle", "Dark Mode", None],
            ["", "image", "About", Page(parent, "About")]
        ]

        self.buttons = []

        self.setFixedSize(192, parent.height())
        self.setAutoFillBackground(True)

        self.refresh()

        for index in range(len(self.items)):
            if not self.items[index]:
                continue

            button = None
            if self.items[index][1] == "image":
                if self.items[index][3]:
                    self.items[index][3].setText(self.items[index][2])

                button = ImageButton(self, 0, index * 44, self.items[index][3])
                button.setText(self.items[index][0], self.items[index][2])
            else:
                button = ToggleButton(self, 0, index * 44)
                button.setText(self.items[index][0], self.items[index][2])
                button.clicked.connect(self.on_toggle)

            self.buttons.append(button)

        self.lastItem = None

        self.show()

    def on_toggle(self):
        value = toggle_colors()

        if value:
            self.buttons[4].setText("", "Light Mode")
        else:
            self.buttons[4].setText("", "Dark Mode")

        self.refresh()
        self.parent().refresh()

        for item in self.buttons:
            item.refresh()

    def refresh(self):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(get_color("side")))
        self.setPalette(palette)
