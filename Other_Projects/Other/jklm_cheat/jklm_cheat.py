def setup() -> None:
    ver = 1.0
    prog_name = __file__.split('\\')[-1]

    print(f"Initializing '{prog_name}' version {ver}\n")

    words = []
    used = []

    with open("words_alpha.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            words.append(line.strip())

    print(f"Initiation complete! {len(words)} words loaded into memory.\n\n{'=' * 16}\n")


def main() -> None:
    while True:
        hint = input("Input hint: ")
        for word in words:
            if hint in word and word not in used:
                used.append(word)
                print(f"Unused word containing {hint} = {word}")
                break
        print(f"\n{'-' * 16}\n")


if __name__ == "__main__":
    setup()
    main()
