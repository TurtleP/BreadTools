from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QFrame, QScrollArea, QSizePolicy, QVBoxLayout,
                             QWidget, QRadioButton)

from gui.elements.label import Label
from gui.elements.slider import Slider
from storage import Storage


class Page(QWidget):
    def __init__(self, parent, name=None):
        super().__init__(parent)

        self.move(182, 0)
        self.setFixedSize(318, 368)

        self.elements = list()
        self.load_elements(name)

        self.hide()

    def load_elements(self, page):
        elements = Storage.get_page_data(page)

        if elements is None:
            return

        layout = QVBoxLayout()

        scroll_area = QScrollArea(self)

        inner = QWidget(scroll_area)
        inner.setLayout(layout)

        scroll_area.setWidget(inner)
        scroll_area.setFixedWidth(self.width())
        scroll_area.setFixedHeight(self.height())

        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setFrameStyle(QFrame.NoFrame)

        if len(elements) > 5:
            layout.setSpacing(16)

        for index, item in enumerate(elements):
            panel = QWidget()

            panel.setFixedWidth(self.width() - 32)
            panel.setMinimumHeight(64)

            Label(panel, 16, 0, item[0])

            if item[1] == "Slider":
                Slider(panel, 32, 28)
            elif item[1] == "Radio":
                if isinstance(item[2], list):
                    for index, text in enumerate(item[2]):
                        QRadioButton(text, panel).move(32, 28 + (index * 18))

            panel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

            layout.addWidget(panel)
            self.elements.append(panel)
