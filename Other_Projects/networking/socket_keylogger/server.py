import datetime
import os
import socket
import threading
from typing import Tuple


class Server:
    def __init__(self, host: str, port: int, *, header_length: int = 16, message_encoding: str = "utf-8",
                 stop_message: str = "stop", debug: bool = False):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.message_encoding = message_encoding
        self.header_length = header_length
        self.stop_message = stop_message
        self.debug = debug

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.address)
        self.stop = False

        self.active_connections = {}

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

    def send_message(self, connection: socket.socket, message: str):
        encoded_message = message.encode(self.message_encoding)
        header = str(len(encoded_message)).encode(self.message_encoding)
        header += b" " * (self.header_length - len(header))

        connection.send(header)
        connection.send(encoded_message)

    def receive_message(self, connection: socket.socket):
        remaining_header_bytes = self.header_length
        header = ""
        while remaining_header_bytes:
            encoded_header_chunk = connection.recv(remaining_header_bytes)
            remaining_header_bytes -= len(encoded_header_chunk)
            header += encoded_header_chunk.decode(self.message_encoding)

        if not header:
            self.debug_message("WARNING", "Zero bytes recieved")
            return

        remaining_message_bytes = int(header)
        message = ""
        while remaining_message_bytes:
            encoded_message = connection.recv(remaining_message_bytes)
            remaining_message_bytes -= len(encoded_message)
            message += encoded_message.decode(self.message_encoding)
        return message

    def disconnect_client(self, connection: socket.socket):
        try:
            self.send_message(connection, self.stop_message)
            client_address = connection.getpeername()
            connection.close()
        except OSError:
            client_address = ("0.0.0.0", 0)

        client_identity_list = [client_pair[0] for client_pair in self.active_connections.items() if
                                client_pair[1] == connection]
        if client_identity_list:
            del self.active_connections[client_identity_list[0]]
            self.debug_message("DISCONNECTION",
                               f"{client_identity_list[0]} ({':'.join(map(str, client_address))}) has disconnected from the server")
            self.debug_message("ACTIVE CONNECTIONS", len(self.active_connections))

    def handle_client(self, connection: socket.socket, client_address: Tuple[str, int]):
        client_identity = self.receive_message(connection)
        if client_identity in self.active_connections:
            self.disconnect_client(connection)
            self.debug_message("WARNING", f"Duplicate connection attempted by {client_identity}")
            return

        self.active_connections[client_identity] = connection
        self.debug_message("NEW CONNECTION",
                           f"{client_identity} ({':'.join(map(str, client_address))}) has connected to the server")
        self.debug_message("ACTIVE CONNECTIONS", len(self.active_connections))

        if not os.path.exists(f".\\logs\\{client_identity}.txt"):
            with open(f".\\logs\\{client_identity}.txt", "w", encoding=self.message_encoding):
                self.debug_message("LOGFILE CREATED", f"Created .\\logs\\{client_identity}.txt")

        while not self.stop:
            try:
                message = self.receive_message(connection)
                if message == self.stop_message:
                    self.disconnect_client(connection)
                    break

                self.debug_message(f"MESSAGE<{client_identity}>", message)
                with open(f".\\logs\\{client_identity}.txt", "a", encoding=self.message_encoding) as log:
                    log.write(f"[{datetime.datetime.now()}] {message}\n")

            except OSError:
                self.debug_message("WARNING",
                                   f"Connection with {client_identity} ({':'.join(map(str, client_address))}) is closed. Disconnecting client")
                self.disconnect_client(connection)
                break

    def connection_handler(self):
        while not self.stop:
            try:
                connection, client_address = self.server.accept()
                t_client_handler = threading.Thread(target=self.handle_client, args=(connection, client_address))
                t_client_handler.start()
            except OSError:
                self.debug_message("WARNING", "Server socket was closed")

    def parse_command(self, command: str):
        if not command.strip():
            self.debug_message("WARNING", "Invalid command")
            return

        command = command.split()
        instruction = command[0]
        try:
            arguments = command[1:]
        except IndexError:
            arguments = []

        try:
            if instruction == self.stop_message:
                self.stop = True
                self.debug_message("STOPPING", "Stopping server...")
                for client_identity, connection in self.active_connections.items():
                    self.send_message(connection, self.stop_message)
                    self.debug_message("STOPPING CLIENT",
                                       f"Stopping client script on {client_identity} ({':'.join(map(str, connection.getpeername()))})...")
                self.server.close()
                return

            if instruction == "clients":
                for client_identity, connection in self.active_connections.items():
                    print(client_identity, ":".join(map(str, connection.getpeername())), sep="\t")
                return

            if instruction == "command":  # command räzzeragnar shutdown /r /t 1
                if not len(arguments):
                    self.debug_message("WARNING", "Invalid command")
                    return
                connection = self.active_connections[arguments[0]]
                self.send_message(connection, "command " + " ".join(arguments[1:]))
                self.debug_message("CLIENT EXECUTION",
                                   f"Executing '{' '.join(arguments[1:])}' on {arguments[0]} ({':'.join(map(str, connection.getpeername()))})")
                return

            if instruction == "disconnect":
                if arguments[0] in self.active_connections:
                    self.disconnect_client(self.active_connections[arguments[0]])
                return

            if instruction in ["cls", "clear"]:
                os.system("cls")
                return

            raise Exception
        except Exception:
            self.debug_message("WARNING", "Invalid command")

    def start(self):
        self.debug_message("STARTING", "Server is starting...")
        self.server.listen()
        self.debug_message("LISTENING", f"Server is listening on {self.host}:{self.port}")

        td_connection_handler = threading.Thread(target=self.connection_handler, daemon=True)
        td_connection_handler.start()

        while not self.stop:
            self.parse_command(input())


if __name__ == "__main__":
    server = Server(socket.gethostbyname(socket.gethostname()), 5050, debug=True)
    server.start()
    server.debug_message("STOPPED", "The server has stopped")
