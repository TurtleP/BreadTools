from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMainWindow

from gui.elements.button import Button
# from gui.elements.checkbox import Checkbox
from gui.elements.panel import Panel
from storage import Storage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        Storage.load_font_database()

        self.setFixedSize(500, 368)
        self.setWindowTitle("Bread Tools")

        icon_path = Storage.resolve_image("icons/icon.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.setAutoFillBackground(True)

        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))

        self.setPalette(p)

        Panel(self, [182, self.height()])

        Button(self, self.width() - 144, self.height() - 48, "TEST")
        # Checkbox(self, self.width() - 16, 64)

        self.show()
