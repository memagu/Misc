def filter_invalid_words(source_file: str, destination_file: str) -> None:
    with open(source_file, 'r', encoding="utf-8") as raw:
        with open(destination_file, 'w', encoding="utf-8") as out:
            for i, line in enumerate(map(str.strip, raw.readlines())):

                for forbidden in "0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ 	":
                    if forbidden in line:
                        break
                else:
                    out.write(line + '\n')


filter_invalid_words("words_alpha.txt", "../word_lists/english.txt")
filter_invalid_words("swe_wordlist.txt", "../word_lists/swedish.txt")
