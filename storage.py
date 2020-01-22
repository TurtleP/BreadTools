import sys
from pathlib import Path

from PyQt5.Qt import QFontDatabase


class Storage:
    DATABASE = None

    @staticmethod
    def load_font_database():
        Storage.DATABASE = QFontDatabase()

    @staticmethod
    def __resolve__(directory, relative_path):
        ret_path = None

        if hasattr(sys, '_MEIPASS'):
            ret_path = Path(sys._MEIPASS).joinpath(directory, relative_path)
        else:
            ret_path = Path(__file__).parent.joinpath(directory).absolute() / relative_path

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
    def save_file(filepath):
        pass

    @staticmethod
    def read_file(filepath):
        pass

    @staticmethod
    def version():
        return "0.1.0"
