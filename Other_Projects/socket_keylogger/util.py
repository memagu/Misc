import subprocess
import winreg


class WindowsRegistryEditor:
    @staticmethod
    def enum_key(key: int):
        subkeys = []
        try:
            i = 1
            while True:
                subkeys.append(winreg.EnumKey(key, i))
                i += 1
        except OSError:
            return subkeys

    @staticmethod
    def enum_value(key: int, sub_key: str):
        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_READ) as open_key:
            values = []
            try:
                i = 1
                while True:
                    values.append(winreg.EnumValue(open_key, i))
                    i += 1
            except OSError:
                return values

    @classmethod
    def value_exists(cls, key: int, sub_key: str, value_name: str):
        for value in cls.enum_value(key, sub_key):
            if value[0] == value_name:
                return True
        return False

    @classmethod
    def add_value(cls, key: int, sub_key: str, value_name: str, value: str):
        if cls.value_exists(key, sub_key, value_name):
            raise Exception(f"{value_name=} already exists at {key=} {sub_key=}")

        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_ALL_ACCESS) as open_key:
            winreg.SetValueEx(open_key, value_name, 0, winreg.REG_SZ, value)

    @classmethod
    def edit_value(cls, key: int, sub_key: str, value_name: str, value: str):
        if not cls.value_exists(key, sub_key, value_name):
            raise Exception(f"{value_name=} does not exist at {key=} {sub_key=}")

        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_ALL_ACCESS) as open_key:
            winreg.SetValueEx(open_key, value_name, 0, winreg.REG_SZ, value)

    @classmethod
    def remove_value(cls, key: int, sub_key: str, value_name: str):
        if not cls.value_exists(key, sub_key, value_name):
            raise Exception(f"{value_name=} does not exist at {key=} {sub_key=}")

        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_ALL_ACCESS) as open_key:
            winreg.DeleteValue(open_key, value_name)


class PackageManager:
    @staticmethod
    def package_is_installed(package: str):
        return package in subprocess.check_output(["pip", "list"]).decode("utf-8")

    @classmethod
    def install_package(cls, package: str):
        if cls.package_is_installed(package):
            return

        try:
            subprocess.run(["pip", "install", package], check=True)
        except subprocess.CalledProcessError:
            raise Exception(f"{package=} does not exist")

    @classmethod
    def uninstall_package(cls, package: str):
        if not cls.package_is_installed(package):
            return

        try:
            subprocess.run(["pip", "uninstall", package, "-y"], check=True)
        except subprocess.CalledProcessError:
            raise Exception(f"{package=} does not exist")


if __name__ == "__main__":
    key = winreg.HKEY_CURRENT_USER
    sub_key = "Software\Microsoft\Windows\CurrentVersion\Run"
    # add_value_to_startup_registry("test", "test")
    # print(WindowsRegistryEditor.enum_key(winreg.HKEY_CURRENT_USER))
    # print(WindowsRegistryEditor.enum_value(key, sub_key))
    # print(WindowsRegistryEditor.value_exists(key, sub_key, "Welcome"))
    # print(WindowsRegistryEditor.value_exists(key, sub_key, "Test"))
    # WindowsRegistryEditor.remove_value(key, sub_key, "welcome")
    # WindowsRegistryEditor.edit_value(key, sub_key, "welcome", r'"C:\Users\melke\AppData\Local\Programs\Python\Python310\python.exe" "C:\Users\melke\Dev\PycharmProjects\Misc\Other_Projects\socket_keylogger\welcome.py"')
    # WindowsRegistryEditor.remove_value(key, sub_key, "test")
    # PackageManager.install_package("keyboard ")
    client_address = ("127.0.0.1", 5050)
    print(f"New connection from {':'.join(map(str, client_address))}")

