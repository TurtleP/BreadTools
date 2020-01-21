import sys

from PyQt5.QtWidgets import QApplication

from gui.window import MainWindow

WINDOW = None
if __name__ == "__main__":
    app = QApplication(sys.argv)
    WINDOW = MainWindow()
    sys.exit(app.exec_())
