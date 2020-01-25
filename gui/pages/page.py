from PyQt5.QtWidgets import QWidget


class Page(QWidget):
    def __init__(self, parent, x, y):
        super().__init__(parent)

        self.move(x, y)
        self.setFixedSize(318, 368)

        self.hide()
