from collections import defaultdict
import os
import string

from bs4 import BeautifulSoup
import pyperclip
import requests


def process_string(s: str) -> str:
    if len(s) <= 1:
        return s

    s = s.strip()
    for char in string.whitespace:
        s = s.replace(char, ' ')

    processed = s[0]

    for i in range(1, len(s)):
        char = s[i]
        prev_char = s[i - 1]

        if char == prev_char == ' ':
            continue

        processed += char

    return processed


def get_words_and_definitions() -> dict[str, list[str]]:
    response = requests.get("https://www.braord.se/")
    soup = BeautifulSoup(response.content, "html.parser")
    entries = soup.find("div", class_="wordgrid").find_all("div", class_="row")

    words_and_definitions = defaultdict(list[str])

    for entry in entries:
        word_div = entry.find("div", class_="col-12 col-md-3")
        definition_div = entry.find("div", class_="col-12 col-md-9")

        if word_div is None or definition_div is None:
            continue

        word = process_string(word_div.text)
        definition = process_string(definition_div.text)

        if not definition:
            continue

        words_and_definitions[word].append(definition)

    return words_and_definitions


def format_data(data: dict[str, list[str]],
                word_definition_separator: str,
                pair_separator: str,
                definitions_separator: str = " | ") -> str:
    return pair_separator.join(f"{word}{word_definition_separator}{definitions_separator.join(definitions)}"
                               for word, definitions in data.items())


def main() -> None:
    print("Fetching words and definitions . . .")
    words_and_definitions = get_words_and_definitions()

    print("Formatting data . . .")
    formatted_data = format_data(words_and_definitions, ' # ', '\n')

    print("Copying formatted data to clipboard . . .")
    pyperclip.copy(formatted_data)
    print('Done! Paste the formatted data at https://quizlet.com/create-set using "Import from Word, Excel, Google Docs, etc."\n')

    os.system("pause")


if __name__ == "__main__":
    main()
