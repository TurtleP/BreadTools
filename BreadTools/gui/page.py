from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QFrame, QScrollArea, QSizePolicy, QVBoxLayout,
                             QWidget)

from ..storage import Storage
from .elements.heading import Header
from .elements.label import Label
from .elements.slider import Slider
from .elements.radiogroup import RadioGroup

from .colors import get_color


class Page(QWidget):

    def __init__(self, parent, name):
        super().__init__(parent)

        self.move(192, 51)
        self.name = name

        self.setFixedSize(parent.width() - 192,
                          parent.height() - 51)

        self.setAutoFillBackground(True)

        self.elements = []
        self.load_elements(name)

        self.refresh()

        self.hide()

    def refresh(self):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(get_color("main")))
        self.setPalette(palette)

        for item in self.elements:
            if hasattr(item, "refresh"):
                item.refresh()

        self.header.refresh()

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

        self.header = Header(self.parent(), name, page_data is not None)
        self.header.move(192, 0)

        if not page_data:
            return

        # Create layout and scroll region
        layout = QVBoxLayout()
        self.scroll_area = QScrollArea(self)

        # Content panel/widget with the Vertical layout
        content = QWidget(self.scroll_area)
        content.setLayout(layout)

        # self.m_layout.setSpacing(16)
        # self.m_layout.setContentsMargins(0, 20, 0, 0)

        # Set up our Scroll Area with the content panel
        # and other config stuff
        self.scroll_area.setWidget(content)
        self.scroll_area.setFixedWidth(self.width())
        self.scroll_area.setFixedHeight(self.height())

        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setFrameStyle(QFrame.NoFrame)

        if len(page_data["elements"]) > 5:
            layout.setSpacing(16)

        for row in page_data["elements"]:
            panel = QWidget()

            panel.setFixedWidth(self.width() - 32)
            panel.setMinimumHeight(120)

            item = None
            for index, element in enumerate(row):
                if element[0] == "label":
                    is_bold = len(element) > 2 and int(element[2]) or False
                    item = Label(panel, element[1], is_bold).move(16, index * 24)
                elif element[0] == "slider":
                    item = Slider(panel)
                    item.move(16, index * 26)
                    item.clicked.connect(lambda: self.header.setEnabled(True))
                elif element[0] == "menu":
                    item = RadioGroup(panel, 16, index * 24, 2, element[1:])

            panel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

            layout.addWidget(panel)
            self.elements.append(item)
