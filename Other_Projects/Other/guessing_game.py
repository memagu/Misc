TARGET = 45
MIN = 0
MAX = 100

guesses = 0

while True:
    num = input(f"Enter your guess (a number between {MIN}-{MAX}): ")
    try:
        num = int(num)
    except ValueError:
        print("Invalid input, please enter a number.")
        continue

    if num < TARGET:
        print("Your guess is too low\n")
    elif num > TARGET:
        print("Your guess is too large\n")
    else:
        print(f"{TARGET} was the right number! You guessed it in {guesses} tries.")
        print("\nPress enter to exit.")
        break

    guesses += 1