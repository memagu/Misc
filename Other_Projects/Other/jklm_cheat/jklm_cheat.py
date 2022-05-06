import time
import json
import keyboard

with open("config.json", "r") as cfg:
    settings = json.load(cfg)


def initialize_words() -> [str]:
    import random
    word_list = []

    with open(settings['wordlist'], "r") as f:
        lines = f.readlines()
        for line in lines:
            word_list.append(line.strip())

    if settings["scramble_word_list"]:
        random.shuffle(word_list)

    if settings["sort_by_word_length"]:
        if settings["sort_by_word_length"] == "increasing":
            word_list.sort(key=lambda x: len(x))
            return word_list

        if settings["sort_by_word_length"] == "decreasing":
            word_list.sort(key=lambda x: len(x), reverse=True)

    return word_list


def main() -> None:
    ver = 3.0
    prog_name = __file__.split('\\')[-1]
    print(f"Initializing '{prog_name}' version {ver}\n")

    words = initialize_words()
    print(f"Initiation complete! {len(words)} words loaded into memory.\n\n{'=' * 64}\n")

    token = input("Input game code or url: ")
    if len(token) == 4:
        token = "https://jklm.fun/" + token.upper()

    import webscrape_3
    webscrape_3.connect(token)
    print(f"{'='*31}\n")

    used = []

    last_syllable = ""

    min_word_length = settings["min_word_length"]
    max_word_length = settings["max_word_length"]

    while True:
        temp = webscrape_3.get_syllable().lower()
        if temp != last_syllable:
            syllable = temp
            syllable_out = f"\033[92m{syllable}\033[0m"
            print(f"syllable = {syllable_out}")
            last_syllable = syllable

            for word in words:
                if syllable in word and word not in used and min_word_length < len(word) < max_word_length:
                    used.append(word)
                    keyboard.write(word)
                    keyboard.send('enter')
                    word = word.split(syllable, maxsplit=1)
                    print(f"Unused word containing {syllable_out} = {syllable_out.join(word)}")
                    break
            print("\n")
        time.sleep(settings["syllable_poll_rate"])


if __name__ == "__main__":
    main()
