from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QWidget

from gui.elements.imagebutton import ImageButton
from gui.pages.about import AboutPage
from gui.pages.command import CommandPage
from gui.pages.power import PowerPage
from gui.pages.settings import SettingsPage
from gui.pages.tools import ToolsPage
from storage import Storage


class Panel(QWidget):
    def __init__(self, parent, size):
        super().__init__(parent)
        self.setAutoFillBackground(True)

        self.items = list()
        self.setFixedSize(*size)

        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(243, 242, 241))

        self.setPalette(p)

        self.sections = [
            ["", "General", ToolsPage(parent)],
            ["", "Command Line", CommandPage(parent)],
            ["", "Power", PowerPage(parent)],
            ["", "Settings", SettingsPage(parent)],
            [],
            ["", "About", AboutPage(parent)]
        ]

        for index, item in enumerate(self.sections):
            if len(item) == 0:
                continue

            button = ImageButton(self, 0, (index * 38), item[0], item[1])
            button.setFixedWidth(self.width())

            if len(item) > 2:
                button.page = item[2]

            self.items.append(button)

        self.setMouseTracking(True)
        self.last_item = None

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.drawText(0, self.height() - 24, self.width(), 24,
                         Qt.AlignCenter, f"Version {Storage.version()}")

        painter.end()

    def mousePressEvent(self, event):
        if self.last_item:
            self.last_item.on_click(False)

            if hasattr(self.last_item, "page"):
                self.last_item.page.hide()

        for item in self.items:
            if item.get_clickable().contains(event.pos()):
                self.last_item = item

        if self.last_item and not self.last_item.selected:
            self.last_item.on_click(True)

            if hasattr(self.last_item, "page"):
                self.last_item.page.show()

            self.setCursor(Qt.ArrowCursor)

    def mouseMoveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        for item in self.items:
            if not item.selected:
                if item.get_clickable().contains(event.pos()):
                    self.setCursor(Qt.PointingHandCursor)
