import json
import os
import sys
from pathlib import Path

from PyQt5.Qt import QFontDatabase


class Storage:
    DATABASE = None

    USER_PREFERENCES = Path(os.getenv("appdata")) / "Bread_Tools"
    USER_PREFERENCES_FILE = USER_PREFERENCES / "preferences.json"

    PAGE_DATA = None

    @staticmethod
    def load():
        Storage.DATABASE = QFontDatabase()

        if not Storage.USER_PREFERENCES.exists():
            Storage.USER_PREFERENCES.mkdir()

        with open(Storage.resolve_data("elements.json"), "r") as file:
            Storage.PAGE_DATA = json.loads(file.read())

    @staticmethod
    def get_page_data(page):
        if page in Storage.PAGE_DATA:
            return Storage.PAGE_DATA[page]

    @staticmethod
    def __resolve__(directory, relative_path):
        ret_path = None

        if hasattr(sys, '_MEIPASS'):
            ret_path = Path(sys._MEIPASS).joinpath(directory, relative_path)
        else:
            ret_path = Path(__file__).parent.joinpath(
                directory).absolute() / relative_path

        return str(ret_path).replace("\\", "/")

    @staticmethod
    def resolve_image(path):
        return Storage.__resolve__("graphics", path)

    @staticmethod
    def resolve_audio(path):
        return Storage.__resolve__("audio", path)

    @staticmethod
    def resolve_font(path):
        new_path = Storage.__resolve__("graphics/fonts", path)

        id = Storage.DATABASE.addApplicationFont(new_path)
        return QFontDatabase.applicationFontFamilies(id)[0]

    @staticmethod
    def resolve_data(path):
        return Storage.__resolve__("data", path)

    @staticmethod
    def save_file(filepath, content):
        pass

    @staticmethod
    def read_file(filepath):
        with open(Storage.__resolve__(filepath), "r") as file:
            return file.read()

    @staticmethod
    def version():
        return "0.1.0"
