N = 143
M = 120


# E = 7
# D = 2023


def encrypt(plain_text: str, key: int) -> str:
    cipher_text = ""
    for char in plain_text:
        cipher_text += chr(pow(ord(char), key, N))

    return cipher_text


def decrypt(cipher_text: str, key: int) -> str:
    plain_text = ""
    for char in cipher_text:
        plain_text += chr(pow(ord(char), key, N))

    return plain_text


while True:
    option = input("Enter mode (e/d) or exit: ").strip().lower()

    if option == "exit":
        break

    if option == "e":
        plain_text = input("Enter plain text: ")
        key = int(input("Enter key: "))
        print(f"Encrypted text: {encrypt(plain_text, key)}\n")
        continue

    if option == "d":
        cipher_text = input("Enter cipher text: ")
        key = int(input("Enter key: "))
        print(f"Decrypted text: {decrypt(cipher_text, key)}\n")
        continue

    print("Invalid input!\n")

