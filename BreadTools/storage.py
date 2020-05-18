import os
import sys
from pathlib import Path

import msgpack
import toml
from PyQt5.Qt import QFontDatabase, QSound


class Storage:
    DATABASE = None

    APPDATA_DIR = Path(os.getenv("appdata"))
    USER_PREFERENCES_DIR = APPDATA_DIR / "Bread_Tools"

    USER_DATA_FILE = USER_PREFERENCES_DIR / "preferences"
    PAGE_DATA = None

    SOUNDS = None

    @staticmethod
    def load():
        Storage.DATABASE = QFontDatabase()

        if not Storage.USER_PREFERENCES_DIR.exists():
            Storage.USER_PREFERENCES_DIR.mkdir()

        Storage.load_page_data()

        Storage.SOUNDS = {
            "tap": QSound(Storage.resolve_audio("navigation_forward-selection-minimal.wav"))
        }


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
    def load_page_data():
        with open(Storage.resolve_data("pages.toml"), "r") as file:
            Storage.PAGE_DATA = toml.load(file)

    @staticmethod
    def get_page_data(name):
        if name in Storage.PAGE_DATA:
            return Storage.PAGE_DATA[name]

        return None

    @staticmethod
    def get_sound(name):
        return Storage.SOUNDS[name]

    @staticmethod
    def resolve_image(path):
        return Storage.__resolve__("graphics", path)

    @staticmethod
    def resolve_audio(path):
        return Storage.__resolve__("data/audio", path)

    @staticmethod
    def resolve_font(path):
        new_path = Storage.__resolve__("data/fonts", path)

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
