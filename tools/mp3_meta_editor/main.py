import os
from pathlib import Path
import re
import shutil

from mutagen.easyid3 import EasyID3

SONG_DIR = Path("./songs")
SAVE_DIR = Path("./processed/")
EXTENDED_MIX_FORMAT = "(Extended Mix)"


def cleanup(filestem: str) -> str:
    filestem = re.sub(r" +", ' ', filestem.replace('_', ' '))
    filestem = re.sub(r"[\(\[]?extended( (re)?mix)?[\)\]]?", EXTENDED_MIX_FORMAT, filestem, flags=re.IGNORECASE)
    filestem = re.match(r".*?(?=\(\d+\)$)|.*", filestem).group(0)
    return filestem


def main():
    if not SAVE_DIR.exists():
        SAVE_DIR.mkdir(parents=True, exist_ok=True)

    for path in SONG_DIR.iterdir():
        if path.is_dir():
            continue

        if path.suffix != ".mp3":
            shutil.copy(path, SAVE_DIR / (cleanup(path.stem) + path.suffix))
            continue

        stem_parts = cleanup(path.stem).split(" - ")

        if stem_parts[0] == "spotifydown.com":
            filename = SAVE_DIR / (' '.join(stem_parts[1:]) + ".mp3")

            title = stem_parts[1]
            artist = None
            website = "spotifydown.com"

        else:
            title_parts = stem_parts[1].split()

            filename = SAVE_DIR / (' '.join(title_parts[:-1]) + ".mp3")

            title = ' '.join(
                title_parts[:-1 - len(EXTENDED_MIX_FORMAT.split()) * (EXTENDED_MIX_FORMAT in stem_parts[1])])
            artist = stem_parts[0]
            website = title_parts[-1]

        if filename.exists():
            print(path, filename, sep='\n', end="\n\n")

        shutil.copy(path, filename)

        id3 = EasyID3(filename)
        id3["title"] = title
        id3["artist"] = artist or id3.get("artist", '')
        id3["albumartist"] = website
        id3.save()


if __name__ == '__main__':
    main()
    os.system("pause")