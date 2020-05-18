from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMainWindow

from ..storage import Storage
from .panel import SideBar


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        Storage.load()

        self.setFixedSize(600, 478)

        self.setWindowTitle("Bread Tools")
        self.setWindowIcon(QIcon(Storage.resolve_data("icon.ico")))

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#e0e0e0"))
        self.setPalette(palette)

        SideBar(self)

        self.show()
