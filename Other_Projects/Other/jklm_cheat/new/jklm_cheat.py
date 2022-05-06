import random
import time
import json
import keyboard

with open("config.json", "r") as cfg:
    settings = json.load(cfg)


def initialize_words(wordlist_path: str) -> [str]:
    import random
    word_list = []

    with open(wordlist_path, "r") as f:
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


def keyboard_write(string: str, wpm: float, accuracy: float) -> None:
    for char in string:
        if random.randint(0, 1000) / 1000 > accuracy:
            keyboard.write(chr(random.randint(97, 122)))
            time.sleep((random.randint(50, 200) / 50) / (wpm * 5 / 60))
            keyboard.send("backspace")
            time.sleep((random.randint(50, 200) / 50) / (wpm * 5 / 60))

        keyboard.write(char)
        time.sleep((random.randint(50, 200) / 100) / (wpm * 5 / 60))
    keyboard.send("enter")


def main() -> None:
    ver = 3.1
    prog_name = __file__.split('\\')[-1]
    print(f"Initializing '{prog_name}' version {ver}\n")

    words = initialize_words(settings['wordlist_path'])
    print(f"Initiation complete! {len(words)} words loaded into memory.\n\n{'=' * 64}\n")

    token = input("Input game code or url: ")
    if len(token) == 4:
        token = "https://jklm.fun/" + token.upper()

    import webscrape_3
    webscrape_3.connect(token)
    print(f"{'=' * 31}")

    used = set()

    min_word_length = settings["min_word_length"]
    max_word_length = settings["max_word_length"]

    syllable = ""
    last_syllable = ""
    syllable_out = f"\033[92m{syllable}\033[0m"
    word = ""

    def find_word(syllable: str, do_print=True) -> str:
        for word in words:
            if syllable in word and word not in used and min_word_length < len(word) < max_word_length:
                used.add(word)
                to_print = word.split(syllable, maxsplit=1)
                if do_print:
                    print(f"Unused word containing {syllable_out} = {syllable_out.join(to_print)}")
                return word

    while True:
        temp = webscrape_3.get_syllable().lower()
        if temp != last_syllable:
            syllable = temp
            syllable_out = f"\033[92m{syllable}\033[0m"
            print(f"\n\nsyllable = {syllable_out}")
            last_syllable = syllable

            word = find_word(syllable)

        if settings["autotype"] and keyboard.is_pressed(settings["autotype_activation_key"]):
            keyboard_write(word, settings["autotype_wpm"], settings["autotype_accuracy"])

            word = find_word(syllable)

        time.sleep(1 / settings["syllable_poll_rate"])


if __name__ == "__main__":
    main()
