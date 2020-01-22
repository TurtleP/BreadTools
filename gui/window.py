from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMainWindow

from data.registry import RegEdit

from gui.elements.button import Button
# from gui.elements.checkbox import Checkbox
from gui.elements.panel import Panel
from storage import Storage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        Storage.load_font_database()

        self.setFixedSize(500, 368)
        self.setWindowTitle("Bread Tools")

        icon_path = Storage.resolve_image("icon.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.setAutoFillBackground(True)

        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))

        self.setPalette(p)

        Panel(self, [182, self.height()])

        save_button = Button(self, self.width() - 76, self.height() - 36)
        save_button.setText("Save")
        save_button.setFixedWidth(72)
        # Checkbox(self, self.width() - 16, 64)

        # handle = RegEdit.create_key(RegEdit.HKEY_CLASSES_ROOT, r"DesktopBackground\Shell\Settings")
        # RegEdit.set_value(handle, "Icon", "SystemSettingsBroker.exe")
        # RegEdit.set_value(handle, "Position", "Bottom")
        # RegEdit.set_value(handle, "SubCommands", "BreadTools.WindowsSettings;")

        # RegEdit.flush_key(handle)

        # handle = RegEdit.create_key(RegEdit.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\BreadTools.WindowsSettings")
        # RegEdit.set_value(handle, "Icon", "SystemSettingsBroker.exe")
        # RegEdit.set_value(handle, "SettingsUri", "ms-settings:")
        # RegEdit.set_value(handle, "MUIVerb", "Windows Settings")

        # command_handle = RegEdit.create_key(handle, "command")
        # RegEdit.set_value(command_handle, "DelegateExecute", "{556FF0D6-A1EE-49E5-9FA4-90AE116AD744}")

        # RegEdit.flush_key(handle)

        self.show()
