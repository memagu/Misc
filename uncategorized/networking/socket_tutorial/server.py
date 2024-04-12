import socket
import threading

HEADER_LENGTH = 64
SERVER_PORT = 5050
SERVER_IP = socket.gethostbyname(socket.gethostname())  # 192.168.0.50
SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
DISPLAY_STATUS_MESSAGES = True


def status_message(status_type, message):
    status_type = str(status_type)
    message = str(message)

    if DISPLAY_STATUS_MESSAGES:
        if status_type not in ["WARNING", "ERROR"]:
            status_type = f"\u001b[32m[{status_type}]\u001b[0m"
        elif status_type == "WARNING":
            status_type = f"\u001b[33m[{status_type}]\u001b[0m"
        else:
            status_type = f"\u001b[31m[{status_type}]\u001b[0m"

        print(f"{status_type} {message}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDRESS)


def handle_client(connection, client_address):
    status_message("NEW CONNECTION", f"New connetion from {client_address[0]}:{client_address[1]}")
    while True:  # While connected
        header = connection.recv(HEADER_LENGTH).decode(FORMAT)

        if not header:
            continue

        message_length = int(header)
        message = connection.recv(message_length).decode(FORMAT)
        status_message(f"{client_address[0]}:{client_address[1]}", message)

        if message == DISCONNECT_MESSAGE:
            break

    connection.close()
    status_message("DISCONNECTION", f"{client_address[0]}:{client_address[1]} disconnected from the server")


def start():
    status_message("STARTING", "Server is starting...")
    server.listen()
    status_message("LISTENING", f"Server is listening on {SERVER_IP}")
    while True:
        connection, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, client_address))
        thread.start()
        status_message("ACTIVE CONNECTIONS", threading.active_count() - 1)


if __name__ == "__main__":
    start()
