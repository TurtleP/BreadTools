import winreg


class RegEdit:
    HKEY_CLASSES_ROOT = winreg.HKEY_CLASSES_ROOT
    HKEY_LOCAL_MACHINE = winreg.HKEY_LOCAL_MACHINE

    @staticmethod
    def create_key(key, subkey=None):
        """Defaults to `winreg.HKEY_CLASSES_ROOT` for the actual key.
        Returns the handle created by this key"""

        try:
            registry_flags = (winreg.KEY_WOW64_64KEY | winreg.KEY_WRITE)
            return winreg.CreateKeyEx(key, subkey, 0, registry_flags)
        except OSError as error:
            print(str(error))

    @staticmethod
    def set_value(key, name, value):
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)

    @staticmethod
    def flush_key(key):
        winreg.FlushKey(key)
