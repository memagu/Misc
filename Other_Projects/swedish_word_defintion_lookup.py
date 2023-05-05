from bs4 import BeautifulSoup
import os
import requests


def get_info(word: str) -> tuple[str, str]:
    url = f"https://svenska.se/tri/f_saol.php?sok={word}"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

    response = requests.get(url, headers={"User-Agent": user_agent})
    soup = BeautifulSoup(response.content, "html.parser")

    word_class = soup.find("a", class_="ordklass")
    definition = soup.find("span", class_="def")

    if definition and word_class:
        return word_class.text, definition.text

    if definition:
        return "N/A", definition.text

    if word_class:
        return word_class.text, "N/A"

    return "N/A", "N/A"


def main():
    words = map(lambda s: s.strip().lower(),
                input("Enter words for definition lookup (separate words with space): ").split())

    for word in words:
        word_class, definition = get_info(word)
        print(f"{word} [{word_class}]: {definition}")

    os.system("pause")


if __name__ == "__main__":
    main()

