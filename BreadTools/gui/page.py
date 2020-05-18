from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QFrame, QScrollArea, QSizePolicy,
                             QVBoxLayout, QWidget)

from PyQt5.QtGui import QColor

from ..storage import Storage
from .elements.label import Label
from .elements.heading import Header


class Page(QWidget):

    def __init__(self, parent, name):
        super().__init__(parent)

        self.move(192, 51)
        self.name = name

        self.header = Header(parent, name)
        self.header.move(192, 0)

        self.setFixedSize(parent.width() - 192,
                          parent.height() - self.height())

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#eeeeee"))
        self.setPalette(palette)

        # Create layout and scroll region
        self.m_layout = QVBoxLayout()
        self.scroll_area = QScrollArea(self)

        # Content panel/widget with the Vertical layout
        self.content = QWidget(self.scroll_area)
        self.content.setLayout(self.m_layout)

        # Set up our Scroll Area with the content panel
        # and other config stuff
        self.scroll_area.setWidget(self.content)
        self.scroll_area.setFixedSize(self.width(), self.height())
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setFrameStyle(QFrame.NoFrame)

        self.elements = []
        self.load_elements(name)

        if len(self.elements) > 5:
            self.m_layout.setSpacing(16)

        self.hide()

    def show(self):
        self.header.show()
        return super().show()

    def hide(self):
        self.header.hide()
        return super().hide()

    def setText(self, text):
        self.header.setText(text)

    def load_elements(self, name):
        page_data = Storage.get_page_data(name)

        for index, element in enumerate(page_data["elements"]):
            panel = QWidget()

            panel.setFixedWidth(self.width() - 32)
            panel.setMinimumHeight(64)

            if element[0] == "label":
                Label(panel, element[1], True).move(16, 0)

            panel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
            panel.show()

            self.m_layout.addWidget(panel)
            self.elements.append(panel)
