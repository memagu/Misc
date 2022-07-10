import socket

HEADER_LENGTH = 64
SERVER_PORT = 5050
SERVER_IP = "mewi.dev"
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


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER_ADDRESS)
status_message("CONNECTED", f"Connected to {SERVER_IP}:{SERVER_PORT}")


def send(message):
    # message to send
    message = str(message)
    message = message.encode(FORMAT)

    # header
    message_length = str(len(message))
    header = message_length.encode(FORMAT)
    header += b" " * (HEADER_LENGTH - len(header))

    client.send(header)
    client.send(message)


while True:
    message = input()
    if not message:
        continue
    if message == DISCONNECT_MESSAGE:
        send(DISCONNECT_MESSAGE)
        status_message("DISCONNECTED", f"Disconnected from {SERVER_IP}:{SERVER_PORT}")
        break
    send(message)