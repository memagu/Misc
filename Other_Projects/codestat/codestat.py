import os
from pathlib import Path
import typing

EXTENSIONS = [".rs", ".py", ".pyw", ".cpp", ".cs"]
IGNORE = ["venv", ".idea", "obj", "Library", "target", "cmake-build-release", "cmake-build-debug", "Walnut"]


def files(root: Path, file_extensions: typing.Iterable[str], ignore_dirs: typing.Iterable[str]) -> Path:
    queue = [root]

    while queue:
        path = queue.pop()

        if path.is_dir():
            if path.name in ignore_dirs:
                continue

            try:
                queue.extend(path.iterdir())
            except OSError:
                pass

            continue

        if path.suffix not in file_extensions:
            continue

        yield path


def main():
    root = Path(input("Enter root [PATH]: "))

    n_files = 0
    n_lines = 0
    n_words = 0
    n_chars = 0

    for path in files(root, EXTENSIONS, IGNORE):
        n_files += 1

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            n_lines += content.count('\n') - content.count("\n\n")
            n_chars += len(content)
            n_words += len(content
                           .replace('.', ' ')
                           .replace(':', ' ')
                           .replace('(', ' ')
                           .replace(')', ' ')
                           .replace('[', ' ')
                           .replace(']', ' ')
                           .replace('{', ' ')
                           .replace('}', ' ')
                           .replace('_', "_ ")
                           .replace("_ _", "__")
                           .replace('=', "= ")
                           .replace("= =", "==")
                           .replace('\'', ' ')
                           .replace('\"', ' ')
                           .replace(';', ' ')
                           .replace(',', ' ')
                           .split())

    print(f"{n_files=:,}")
    print(f"{n_lines=:,}")
    print(f"{n_words=:,}")
    print(f"{n_chars=:,}")


if __name__ == "__main__":
    main()
    os.system("pause")
