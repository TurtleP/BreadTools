from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QPainter
from PyQt5.QtWidgets import QWidget

from .roundbutton import RoundButton


class Header(QWidget):

    def __init__(self, parent, text=None, has_button=True):
        super().__init__(parent)

        font = QFont("Segoe UI", 20)
        font.setBold(True)

        self.setFixedSize(parent.width() - 192, 50)

        self.text = text
        self.setFont(font)

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#eeeeee"))
        self.setPalette(palette)

        if has_button:
            self.button = RoundButton(self)
            self.button.move((self.width() - self.button.width()) - 12,
                        (self.height() - self.button.height()) / 2)
            self.button.setText("Save")
            self.button.setEnabled(False)

        self.hide()

    def setText(self, text):
        self.text = text

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setFont(self.font())
        painter.drawText(18, self.y(),
                         self.width(), self.height(),
                         Qt.AlignVCenter, self.text)

        painter.end()
