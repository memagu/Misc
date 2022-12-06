import os
from typing import Set, Tuple

HANGMAN_DRAWINGS = [r"""  +---+
      |
      |
      |
      |
      |
=========""", r"""  +---+
  |   |
      |
      |
      |
      |
=========""", r"""  +---+
  |   |
  O   |
      |
      |
      |
=========""", r"""  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", r"""  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", r"""  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", r"""  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", r"""  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def load_wordlist(file_path: str) -> Set[str]:
    words = set()

    with open(file_path, 'r', encoding="utf-8") as f:
        for line in map(str.strip, f.readlines()):
            words.add(line)

    return words


def welcome_message(available_word_lists: Tuple[str]) -> None:
    print(f"{'Welcome to': ^79}")
    print(f"{' H_ngm_n by melle ':~^79}\n")
    print(f"{'Available word lists:':^79}")
    print(f"{', '.join(map(str.capitalize, available_word_lists)): ^79}\n\n")


def fetch_target_word(available_word_lists: Tuple[str]) -> str:
    target_word = ""

    while True:
        response = input("Please select word list: ").lower()

        if not response:
            print("Invalid input! Try again.\n")
            continue

        for word_list in available_word_lists:
            if response in word_list:
                print(f"{word_list.capitalize()} has been selected!")
                print("Choosing random word...")
                target_word = load_wordlist(f"word_lists/{word_list}.txt").pop()
                print(f"Done! A random word has been chosen from {word_list}. The game can now begin.\n")
                break

        if target_word:
            return target_word

        print(f"{response.capitalize()} is not available. Try another word list.\n")


def hangman() -> None:
    available_word_lists = tuple(word_list.removesuffix('.txt') for word_list in os.listdir('word_lists'))

    welcome_message(available_word_lists)

    target_word = fetch_target_word(available_word_lists)
    target_word_letters = set(target_word)

    uncovered = ["_"] * len(target_word)
    correct_letters = 0
    used_letters = set()
    wrong_guesses = 0

    while True:
        print(
            f"\n{HANGMAN_DRAWINGS[wrong_guesses]} - {''.join(uncovered)}\n{correct_letters} / {len(target_word)} letters uncovered\n")
        if used_letters:
            print(f"Used letters: {' '.join(used_letters)}\n")

        if correct_letters == len(target_word):
            print(f"Congratulations, you won!!! The word was {target_word}.")
            break

        if wrong_guesses == len(HANGMAN_DRAWINGS) - 1:
            print(f"Game Over, you lost... The word was {target_word}.")
            break

        while True:
            guess = input("Guess a letter or a word: ").strip().lower()
            if not guess:
                print("Invalid guess. Try guessing a letter or a word.\n")
                continue

            if len(guess) == 1:
                if guess in used_letters:
                    print("That letter has already been used. Try another one.\n")
                    continue

                used_letters.add(guess)

                if guess not in target_word_letters:
                    wrong_guesses += 1
                    break

                for i, letter in enumerate(target_word):
                    if guess == letter:
                        uncovered[i] = guess
                        correct_letters += 1

                break

            if guess == target_word:
                uncovered = list(target_word)
                correct_letters = len(target_word)
                used_letters.union((set(target_word)))
                break

            wrong_guesses += 1
            break


def main():
    while True:
        hangman()
        response = input("\n\nDo you want to play again [Y/n]?: ").strip().lower()
        if response != 'y':
            break

        if os.name == 'nt':
            os.system("cls")
            continue

        os.system("clear")

    input("\n\nDone! Press enter to exit.")


if __name__ == "__main__":
    main()
