from data.registry import RegEdit
from gui.elements.checkbox import Checkbox
from gui.elements.label import Label
from gui.pages.page import Page


class ToolsPage(Page):

    def __init__(self, parent):
        super().__init__(parent, 182, 0)

        Label(self, 16, self.height() * 0.12, "Toggle Hidden Files/Folders")
        Label(self, 16, self.height() * 0.32, "RegEdit")
        Label(self, 16, self.height() * 0.52, "Restart Explorer")
        Label(self, 16, self.height() * 0.72, "Show Extensions")

        Checkbox(self, 32, self.height() * 0.19)
