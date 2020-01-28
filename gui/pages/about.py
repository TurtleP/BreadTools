from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter
from PyQt5.QtWidgets import QLabel

from gui.elements.button import Button
from gui.pages.page import Page
from storage import Storage


class AboutPage(Page):

    def __init__(self, parent):
        super().__init__(parent)

        self.title_font = QFont("Segoe UI", 14)
        self.title_font.setBold(True)

        self.body_font = QFont("Segoe UI", 11)

        self.label = QLabel(self)
        self.label.setFont(self.body_font)
        self.label.move(16, self.height() * 0.15)
        self.label.setFixedSize(self.width() * 0.90, self.height() * 0.70)
        self.label.setAlignment(Qt.AlignLeft)
        self.label.setWordWrap(True)

        self.button = Button(self, (self.width() - 128) * 0.5,
                             self.height() * 0.85, "Check for Updates")

        about_path = Storage.resolve_data("about.txt")
        with open(about_path, "r") as file:
            self.label.setText(file.read())

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setFont(self.title_font)
        painter.drawText(0, self.height() * 0.05, self.width(), self.height(),
                         Qt.AlignHCenter, "Bread Tools")

        painter.end()
