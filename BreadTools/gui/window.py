from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMainWindow

from ..storage import Storage
from .panel import SideBar

from .colors import get_color


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        Storage.load()

        self.setFixedSize(600, 478)

        self.setWindowTitle("Bread Tools")
        self.setWindowIcon(QIcon(Storage.resolve_data("icon.ico")))

        self.setAutoFillBackground(True)

        self.refresh()

        SideBar(self)

        self.show()

    def refresh(self):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(get_color("main")))
        self.setPalette(palette)
