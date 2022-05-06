def initialize_words(filename: str) -> [str]:
    word_list = []

    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            word_list.append(line.strip())

    return word_list


def main() -> None:
    ver = 2.0
    prog_name = __file__.split('\\')[-1]
    print(f"Initializing '{prog_name}' version {ver}\n")

    words = initialize_words("jklm_wordlist.txt")
    print(f"Initiation complete! {len(words)} words loaded into memory.\n\n{'=' * 64}\n")

    print("Input settings:\n")
    max_word_length = int(input("\tmax word length = "))
    print(f"\n{'=' * 64}\n")

    used = []

    while True:
        hint = input("Input hint: ")
        for word in words:
            if hint in word and word not in used and len(word) < max_word_length:
                used.append(word)
                print(f"Unused word containing {hint} = {word}")
                break
        print(f"\n{'-' * 16}\n")


if __name__ == "__main__":
    main()
