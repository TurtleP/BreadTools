from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QFont, QPainter, QPen
from PyQt5.QtWidgets import QPushButton

from storage import Storage


class ImageButton(QPushButton):
    def __init__(self, parent, x, y, glyph=None, text=None):
        super().__init__(parent)

        self.move(x, y)
        self.setFixedSize(128, 32)

        self.default_font = QFont("Segoe UI", 13)
        self.default_font.setBold(False)
        self.setText(text)

        font_path = Storage.resolve_font("FontAwesome 5 Solid.otf")
        self.glyph_font = QFont(font_path, 16)
        self.glyph_font.setBold(False)
        self.glyph = glyph

        self.content = [16, 0]
        self.selected = False

        self.setAttribute(Qt.WA_TransparentForMouseEvents)

    def center_content_height(self):
        self.content[1] = (self.height() - self.glyph_font.pixelSize()) / 2

    def on_click(self, is_clicked):
        self.default_font.setBold(is_clicked)
        self.glyph_font.setBold(is_clicked)

        self.selected = is_clicked

        self.repaint()

    def get_clickable(self):
        # this works because the Panel deals with clicking
        return QRect(self.x(), self.y(), self.width(), self.height())

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setPen(QPen(QColor(64, 64, 64)))

        painter.setFont(self.glyph_font)
        painter.drawText(self.x() + 16, 0, self.width() + 16, self.height(),
                         Qt.AlignVCenter, self.glyph)

        painter.setFont(self.default_font)
        painter.drawText(self.x() + 56, 0, self.width(), self.height(),
                         Qt.AlignVCenter, self.text())

        if self.selected:
            painter.setPen(QPen(QColor(0, 120, 212)))
            painter.drawRect(4, 3, 1, self.height() - 6)

        painter.end()
