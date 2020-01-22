import ctypes
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from storage import Storage

from gui.window import MainWindow

WINDOW = None
if __name__ == "__main__":
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    app = QApplication(sys.argv)

    if is_admin:
        WINDOW = MainWindow()

        sys.exit(app.exec_())
    else:
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Critical)

        icon = QIcon(Storage.resolve_image("icons/icon.ico"))
        message_box.setWindowIcon(icon)

        message_box.setWindowTitle("Bread Tools Failure")
        message_box.setText("Please run the tool as Administrator.")
        message_box.exec()

        sys.exit(1)
