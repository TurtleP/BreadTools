from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QColor, QIcon

from .elements.roundbutton import RoundButton
from .panel import SideBar

from ..storage import Storage

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

        button = RoundButton(self)
        button.move((self.width() - button.width()) - 12,
                    (self.height() - button.height()) - 12)
        button.setText("Save")
        button.setEnabled(False)

        self.show()
