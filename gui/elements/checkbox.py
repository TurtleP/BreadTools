from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QPen, QFont
from PyQt5.QtWidgets import QCheckBox, QLabel

from storage import Storage


class Checkbox(QCheckBox):
    def __init__(self, parent, x, y, text=None):
        super().__init__(parent)

        self.move(x, y)
        self.setFixedSize(96, 18)
        self.setText(text)

        font_path = Storage.resolve_font("FontAwesome 5 Solid.otf")
        self.glyph_font = QFont(font_path, 11)

        self.pen = QPen(QColor(194, 194, 194))
        self.pen.setWidth(2)

        self.label = QLabel(self)
        self.label.setText("Off")
        self.label.move(24, 0)
        self.label.setFixedHeight(self.height())
        self.label.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        state_info = "On"
        if self.isChecked():
            state_info = "Off"

        self.label.setText(state_info)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        painter.setPen(self.pen)
        painter.drawRoundedRect(0, 0, 48, 17, 2, 2)

        painter.end()
