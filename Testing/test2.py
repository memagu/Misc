# conv = {" ": "0",
#         "a": "1",
#         "b": "2",
#         "c": "3",
#         "d": "4",
#         "e": "5",
#         "f": "6",
#         "g": "7",
#         "h": "8",
#         "i": "9",
#         "j": "10",
#         "k": "11",
#         "l": "12",
#         "m": "13",
#         "n": "14",
#         "o": "15",
#         "p": "16",
#         "q": "17",
#         "r": "18",
#         "s": "19",
#         "t": "20",
#         "u": "21",
#         "v": "22",
#         "w": "23",
#         "x": "24",
#         "y": "25",
#         "z": "26"}
#
# word = "create admin role"
# result = ""
# for char in word:
#     result += conv[char]
#
# print(result)


# def fib(n):
#     if n < 2:
#         return 1
#
#     return fib(n-1) + fib(n-2)
#
#
# # 1 1 2 3 5 8 13 21
#
#
# for i in range(10):
#     print(fib(i))

import keyboard
import string


def chunk_key_logger(chunk_size: int = 1):
    while True:
        keys = []
        while len(keys) < chunk_size:
            key_event = keyboard.read_event()
            if key_event.event_type == "up":
                continue
            key = key_event.name
            match key:
                case "uppil":
                    key = "↑"
                case "högerpil":
                    key = "→"
                case "nedpil":
                    key = "↓"
                case "vänsterpil":
                    key = "←"
                case "enter":
                    key = "↴"
                case "backspace":
                    key = "⇤"
                case "space":
                    key = " "
                case "tab":
                    key = "↹"
                case "skift":
                    key = "⇧"
                case "right shift":
                    key = "⇧"

            if len(key) > 1:
                keys.append(f" |{key}| ")
                continue
            keys.append(key)

        print("".join(keys), end="")


def entered_key_logger():
    while True:
        word = []
        word_processed = []
        pointer = 0

        while True:
            keyboard_event = keyboard.read_event()
            if keyboard_event.event_type == "up":
                continue

            key = keyboard_event.name

            if key == "space":
                print("_", "".join(word))
                print("_", "".join(word_processed))
                print()
                break

            if key == "enter":
                print("↴", "".join(word))
                print("↴", "".join(word_processed))
                print()
                break

            key_substitution_map = {"uppil": "↑",
                                    "högerpil": "→",
                                    "nedpil": "↓",
                                    "vänsterpil": "←",
                                    "backspace": "⇤",
                                    "tab": "↹",
                                    "skift": "⇧",
                                    "right shift": "⇧",
                                    "caps lock": "⇪"}

            if key in key_substitution_map:
                key = key_substitution_map[key]

            if len(key) > 1:
                word.append(f"|{key}|")
            else:
                word.append(key)

            if key == "→":
                pointer = min(len(word_processed) - 1, pointer + 1)
                continue

            if key == "←":
                pointer = max(0, pointer - 1)
                continue

            if key == "⇤":
                if not len(word_processed):
                    continue
                word_processed.pop(pointer)
                pointer = max(0, pointer - 1)
                continue

            if key not in string.printable:
                continue

            if pointer == len(word_processed) - 1:
                word_processed.append(key)
            else:
                word_processed.insert(pointer + bool(pointer), key)

            pointer = min(len(word_processed) - 1, pointer + 1)


key_substitution_map = {"uppil": "↑",
                        "högerpil": "→",
                        "nedpil": "↓",
                        "vänsterpil": "←",
                        "backspace": "⇤",
                        "tab": "↹",
                        "skift": "⇧",
                        "right shift": "⇧",
                        "caps lock": "⇪",
                        "enter": "↴"}

for key, value in key_substitution_map.items():
    print(key, value.encode("utf-8").decode("utf-8"))



