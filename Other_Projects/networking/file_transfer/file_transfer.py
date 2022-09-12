import os
import socket
import subprocess
import sys

PORT = 5051
HEADER_SIZE = 32
RECEIVE_BUFFER = 1024 ** 2  # 1 MiB
DATA_CHUNK_SIZE = 4096  # 4 KiB


def send(file_path: str) -> None:
    host = socket.gethostbyname(socket.gethostname())
    address = (host, PORT)
    public_ip = subprocess.check_output(["curl", "-s", "ifconfig.me"], shell=True, encoding=sys.stdout.encoding)
    print(f"Your public IPv4 address is {public_ip}")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(address)
    s.listen()
    print("Waiting for connection receiver connection...")
    connection, receiver_address = s.accept()
    print(f"Receiver connected from {receiver_address}")

    header = str(os.path.getsize(file_path)).encode(sys.stdout.encoding)
    header += b" " * (HEADER_SIZE - len(header))
    connection.send(header)

    print("Sending data...")
    total_data_bytes = os.path.getsize(file_path)
    remaining_data_bytes = total_data_bytes
    with open(file_path, "rb") as f:
        remaining_data_bytes = os.path.getsize(file_path)
        while remaining_data_bytes:
            print(
                f"Sending [{1 - (remaining_data_bytes / total_data_bytes):.8f}%] {remaining_data_bytes:,} bytes remaining...",
                end="\r")
            data = f.read(min(remaining_data_bytes, DATA_CHUNK_SIZE))
            remaining_data_bytes -= connection.send(data)

    print("Data sent")


def receive(host: str, output_path: str) -> None:
    address = (host, PORT)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Attempting connection to {address}")
    s.connect(address)
    print(f"Connected to sender at {address}")

    remaining_header_bytes = HEADER_SIZE
    header = ""
    while remaining_header_bytes:
        encoded_header_chunk = s.recv(remaining_header_bytes)
        remaining_header_bytes -= len(encoded_header_chunk)
        header += encoded_header_chunk.decode(sys.stdout.encoding)

    total_data_bytes = int(header)
    with open(output_path, "wb") as f:
        remaining_data_bytes = total_data_bytes
        while remaining_data_bytes:
            print(
                f"Downloading [{1 - (remaining_data_bytes / total_data_bytes):.8f}%] {remaining_data_bytes:,} bytes remaining...",
                end="\r")
            data = s.recv(min(remaining_data_bytes, RECEIVE_BUFFER))
            remaining_data_bytes -= len(data)

            f.write(data)

    s.close()


def main() -> None:
    option = ""
    while option not in ("send", "s", "receive", "r"):
        if option:
            print("[WARN] Invalid input!")
        option = input("Enter mode (Send/Recieve) [s/r]: ").lower()

    if option in ("send", "s"):
        file_path = ""
        while not os.path.exists(file_path):
            if file_path:
                print("[WARN] Path does not exist!")
            file_path = input("Input file path: ").replace('"', "").replace('"', " ")

        send(file_path)

    else:
        host = input("Input the senders public IPv4 address: ")
        output_path = input("Enter output path: ").replace('"', "").replace('"', " ")

        receive(host, output_path)

    input("\nDone! Press Enter to exit.")


if __name__ == "__main__":
    main()
