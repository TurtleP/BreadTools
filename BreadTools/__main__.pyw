from PyQt5.QtWidgets import QApplication
from .gui.window import Window


def main(args=None):
    app = QApplication([])
    window = Window()
    app.exec_()
    window.destroy()


if __name__ == "__main__":
    main()
