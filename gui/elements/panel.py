from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QWidget

from gui.elements.imagebutton import ImageButton
from storage import Storage


class Panel(QWidget):
    sections = [
        ["", "General"],
        ["", "Command Line"],
        ["", "Power"],
        ["", "Settings"],
        [],
        ["", "About"]
    ]

    def __init__(self, parent, size):
        super().__init__(parent)
        self.setAutoFillBackground(True)

        self.items = list()
        self.setFixedSize(*size)

        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(243, 242, 241))

        self.setPalette(p)

        for index, item in enumerate(Panel.sections):
            if len(item) == 0:
                continue

            button = ImageButton(self, 0, (index * 38), item[0], item[1])
            button.setFixedWidth(self.width())
            button.center_content_height()

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

        for item in self.items:
            if item.get_clickable().contains(event.pos()):
                self.last_item = item

        if self.last_item:
            self.last_item.on_click(True)

    def mouseMoveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        for item in self.items:
            if item.get_clickable().contains(event.pos()):
                self.setCursor(Qt.PointingHandCursor)
