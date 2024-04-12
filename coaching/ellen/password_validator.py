import os
import string
from typing import List


def validate_password(password: str) -> List[str]:
    results = []

    if len(password) < 8:
        results.append("password needs to be at least 8 characters long.")

    if password.islower():
        results.append("Password needs at least one uppercase letter.")

    if password.isupper():
        results.append("Password needs at least one lowercase letter.")

    if not any((str(digit) in password for digit in range(10))):
        results.append("Password needs at least one digit.")

    if not any((char in password for char in string.punctuation)):
        results.append("Password needs at least one special character.")

    if any(char not in string.printable.rstrip() for char in password):
        results.append(f"Password must only contain these characters: {string.printable.rstrip()}")

    if not results:
        results.append("valid")

    return results


while True:
    response = validate_password(input("Enter a password to check: "))

    if response[0] == "valid":
        print("The entered password is valid!")
        break

    print("The entered password is invalid! Please correct the following: ", *response, sep='\n', end="\n\n")

os.system("pause")
