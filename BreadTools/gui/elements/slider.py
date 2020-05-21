from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QPainter, QPen, QBrush
from PyQt5.QtWidgets import QPushButton


class Slider(QPushButton):
    def __init__(self, parent, value=False):
        super().__init__(parent)

        self.setMinimumWidth(52)
        self.setMinimumHeight(24)

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
        self.setChecked(value)

    def refresh(self):
        pass

    def mousePressEvent(self, event):
        self.setChecked(not self.isChecked())

    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)

    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)

    def setChecked(self, value):
        super().setChecked(value)

        if self.isChecked():
            self.background = self.background_on
            self.pen.setColor(self.background)
            self.dot_rect.moveRight(self.click_width)
        else:
            self.background = self.background_off
            self.pen.setColor(QColor(194, 194, 194))
            self.dot_rect.moveLeft(-self.click_width)

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        # painter.drawRect(self.rect())
        painter.translate(self.rect().center())

        painter.setBrush(QBrush(self.background))
        painter.setPen(self.pen)
        painter.drawRoundedRect(self.click_rect, self.radius, self.radius)

        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.drawRoundedRect(self.dot_rect, 10, 10)

        painter.end()
