from dataclasses import dataclass
import datetime
import pickle
import socket
import threading
from typing import Dict, Tuple

"""
Custom Exceptions
"""


class InvalidCommand(Exception):
    pass


@dataclass
class Identity:
    name: str
    address: Tuple[str, int]

    def __post_init__(self):
        self.address_str = ":".join(map(str, self.address))


@dataclass
class Packet:
    sender: Identity
    tag: str
    content: object


@dataclass()
class Command:
    raw_command: str

    def __post_init__(self):
        if not self.raw_command.strip():
            raise InvalidCommand

    @property
    def command(self) -> str:
        return self.raw_command.split()[0]

    @property
    def arguments(self) -> Tuple[str]:
        if len(self.raw_command.split()) == 1:
            return tuple()
        return tuple(self.raw_command.split()[1:])


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
        self.identity = Identity("host", self.address)
        self.stop = False

        self.connected_clients: Dict[Identity, socket.socket] = {}

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

    def send_packet(self, connection: socket.socket, packet: Packet):
        pickled_packet = pickle.dumps(packet)
        header = str(len(pickled_packet)).encode(self.message_encoding)
        header += b" " * (self.header_length - len(header))

        connection.send(header)
        connection.send(pickled_packet)

    def receive_packet(self, connection: socket.socket):
        remaining_header_bytes = self.header_length
        header = ""
        while remaining_header_bytes:
            encoded_header_chunk = connection.recv(remaining_header_bytes)
            remaining_header_bytes -= len(encoded_header_chunk)
            header += encoded_header_chunk.decode(self.message_encoding)

        if not header:
            self.debug_message("WARNING", "Zero bytes recieved")
            return

        remaining_bytes = int(header)
        pickled_packet = b""
        while remaining_bytes:
            pickled_packet_chunk = connection.recv(remaining_bytes)
            remaining_bytes -= len(pickled_packet_chunk)
            pickled_packet += pickled_packet_chunk
        return pickle.loads(pickled_packet)

    def disconnect_client(self, connection: socket.socket, client_identity: Identity):
        try:
            self.send_packet(connection, Packet(self.identity, "STOP", self.stop_message))
            connection.close()
        except OSError:
            pass

        if client_identity in self.connected_clients:
            del self.connected_clients[client_identity]
            self.debug_message("DISCONNECTION",
                               f"{client_identity.name} ({client_identity.address_str}) has disconnected from the server")
            self.debug_message("ACTIVE CONNECTIONS", len(self.connected_clients))

    def handle_client(self, connection: socket.socket, client_identity: Identity):

        """
        Your code here
        """

        self.disconnect_client(connection, client_identity)

    def connection_handler(self):
        while not self.stop:
            try:
                connection, _ = self.server.accept()
                client_identity = self.receive_packet(connection).sender
                if client_identity in self.connected_clients:
                    self.disconnect_client(client_identity)
                    self.debug_message("WARNING", f"Duplicate connection attempted by {client_identity}")
                else:
                    self.connected_clients[client_identity] = connection
                    self.debug_message("NEW CONNECTION", f"{client_identity} ({client_identity.address_str}) has connected to the server")
                    self.debug_message("ACTIVE CONNECTIONS", len(self.connected_clients))
                    t_client_handler = threading.Thread(target=self.handle_client, args=(connection, client_identity))
                    t_client_handler.start()
            except OSError:
                self.debug_message("WARNING", "Server socket was closed")

    def parse_command(self, command: Command):
        if command.command == "stop":
            self.stop = True

        if command.command == "clients":
            for client in self.connected_clients:
                print(client.name, client.address_str, sep="\t")

    def start(self):
        self.debug_message("STARTING", "Server is starting...")
        self.server.listen()
        self.debug_message("LISTENING", f"Server is listening on {self.host}:{self.port}")

        td_connection_handler = threading.Thread(target=self.connection_handler, daemon=True)
        td_connection_handler.start()

        while not self.stop:
            self.parse_command(Command(input()))


if __name__ == "__main__":
    server = Server(socket.gethostbyname(socket.gethostname()), 5050)
    server.start()
