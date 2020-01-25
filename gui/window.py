from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMainWindow

from gui.elements.panel import Panel
from storage import Storage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        Storage.load()

        self.setFixedSize(500, 368)
        self.setWindowTitle("Bread Tools")

        icon_path = Storage.resolve_image("icon.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.setAutoFillBackground(True)

        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))

        self.setPalette(p)

        Panel(self, [182, self.height()])

        self.show()
