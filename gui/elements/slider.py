from PyQt5.QtCore import QRect
from PyQt5.QtGui import QColor, QPainter, QPen, QFont, QBrush
from PyQt5.QtWidgets import QPushButton

from storage import Storage


class Slider(QPushButton):
    def __init__(self, parent, x, y, text=None):
        super().__init__(parent)

        self.move(x, y)

        self.setMinimumWidth(72)
        self.setMinimumHeight(24)

        self.setText(text)

        font_path = Storage.resolve_font("FontAwesome 5 Solid.otf")
        self.glyph_font = QFont(font_path, 11)

        self.background_on = QColor(0, 120, 212)
        self.background_off = QColor(255, 255, 255)

        self.radius = 10
        self.click_width = 24

        self.click_rect = QRect(-self.click_width, -self.radius,
                                2 * self.click_width, 2 * self.radius)

        self.dot_rect = QRect(-self.click_width, -self.radius, 20, 20)

        self.background = self.background_off

        self.pen = QPen(QColor(194, 194, 194))
        self.pen.setWidth(2)
        self.setCheckable(True)

    def mousePressEvent(self, event):
        self.setChecked(not self.isChecked())

        background_color = self.background_off
        pen_color = QColor(194, 194, 194)

        if self.isChecked():
            background_color = self.background_on
            pen_color = background_color

        self.background = background_color
        self.pen.setColor(pen_color)

        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        painter.translate(self.rect().center())

        painter.setBrush(QBrush(self.background))
        painter.setPen(self.pen)
        painter.drawRoundedRect(self.click_rect, self.radius, self.radius)

        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.drawRoundedRect(self.dot_rect, 10, 10)

        if self.isChecked():
            self.dot_rect.moveRight(self.click_width)
        else:
            self.dot_rect.moveLeft(-self.click_width)

        painter.end()
