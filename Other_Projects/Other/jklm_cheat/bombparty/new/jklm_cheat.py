import random
import time
import json
import keyboard

with open("config.json", "r") as cfg:
    settings = json.load(cfg)


def initialize_words(wordlist_path: str, sorting_mode: str) -> [str]:
    print(f"{sorting_mode=}")
    import random
    word_list = []

    with open(wordlist_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            word_list.append(line.strip())

    if settings["scramble_word_list"]:
        random.shuffle(word_list)

    if sorting_mode != "alphabetical":
        if sorting_mode == "increasing":
            word_list.sort(key=lambda x: len(x))
            return word_list

        if sorting_mode == "decreasing":
            word_list.sort(key=lambda x: len(x), reverse=True)
            return word_list

        if sorting_mode == "uniqueness":
            temp = []
            for word in word_list:
                temp.append((word, len(set(word))))

            temp.sort(key=lambda x: x[1], reverse=True)

            word_list = []

            for word_tuple in temp:
                word_list.append(word_tuple[0])
            return word_list

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

    words = initialize_words(settings['wordlist_path'], settings["wordlist_sorting_mode"])
    print(f"Initiation complete! {len(words)} words loaded into memory from {settings['wordlist_path']}.\n\n{'=' * 64}\n")

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
                to_print = word.split(syllable, maxsplit=1)
                if do_print:
                    print(f"Unused word containing {syllable_out} = {syllable_out.join(to_print)}")
                return word

        print(f"no words containing \033[92m{syllable}\033[0m in {settings['wordlist_path']}")
        return "none found"

    while True:
        temp = webscrape_3.get_syllable().lower()
        if temp != last_syllable:
            syllable = temp
            syllable_out = f"\033[92m{syllable}\033[0m"
            print(f"\n\nsyllable = {syllable_out}")
            last_syllable = syllable

            word = find_word(syllable)

        if settings["autotype"] and keyboard.is_pressed(settings["autotype_activation_key"]):
            used.add(word)
            keyboard_write(word, settings["autotype_wpm"], settings["autotype_accuracy"])

            word = find_word(syllable)

        time.sleep(1 / settings["syllable_poll_freq"])


if __name__ == "__main__":
    main()
