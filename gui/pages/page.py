from PyQt5.QtWidgets import QWidget, QScrollArea, QFrame, QVBoxLayout

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

        scroll_area = QScrollArea(self)
        scroll_area.setFixedWidth(self.width())
        scroll_area.setFixedHeight(self.height())

        scroll_area.setFrameStyle(QFrame.NoFrame)
        scroll_area.setWidgetResizable(False)

        layout = QVBoxLayout()

        if not elements:
            return

        for item in elements:
            panel = QWidget()

            Label(panel, 16, 0, item[0])

            if item[1] == "Slider":
                Slider(panel, 32, 28)

            panel.adjustSize()
            layout.addWidget(panel)

        scroll_area.setLayout(layout)
