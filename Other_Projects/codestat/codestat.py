from dataclasses import dataclass
import os
from pathlib import Path
import typing

EXTENSIONS = [".rs", ".py", ".pyw", ".cpp", ".cs", ".java", ".js", ".cmd", ".bat", ".md"]
IGNORE = ["venv", ".idea", "obj", "Library", "target", "cmake-build-release", "cmake-build-debug", "Walnut"]

TOP_FILE_AMOUNT = 10


@dataclass
class FileInfo:
    path: Path
    line_amount: int
    word_amount: int
    char_amount: int


def get_words(s: str) -> list[str]:
    return s \
        .replace('.', ' ') \
        .replace(':', ' ') \
        .replace('(', ' ') \
        .replace(')', ' ') \
        .replace('[', ' ') \
        .replace(']', ' ') \
        .replace('{', ' ') \
        .replace('}', ' ') \
        .replace('_', "_ ") \
        .replace("_ _ ", "__") \
        .replace('=', "= ") \
        .replace("= =", "==") \
        .replace('\'', ' ') \
        .replace('\"', ' ') \
        .replace(';', ' ') \
        .replace(',', ' ') \
        .split()


def get_file_info(file_path: Path) -> FileInfo:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        line_amount = content.count('\n') - content.count("\n\n")
        word_amount = len(get_words(content))
        char_amount = len(content)

    return FileInfo(file_path, line_amount, word_amount, char_amount)


def file_paths(root: Path, file_extensions: typing.Iterable[str], ignore_dirs: typing.Iterable[str]) -> Path:
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
    print("Welcome to Code-Stat!\n")

    root = Path(input("Enter root [PATH]: "))
    files = []
    for file_path in file_paths(root, EXTENSIONS, IGNORE):
        files.append(get_file_info(file_path))

    print(f"\nFiles: {len(files)}")
    print(f"Total SLOC: {sum(file_info.line_amount for file_info in files):,}")
    print(f"Total words: {sum(file_info.word_amount for file_info in files):,}")
    print(f"Total characters: {sum(file_info.char_amount for file_info in files):,}")

    print(f"\nTop {min(TOP_FILE_AMOUNT, len(files))} largest files (most characters):\n")

    top_files = sorted(files, key=lambda f: f.char_amount, reverse=True)[:min(TOP_FILE_AMOUNT, len(files))]
    max_path_length = max(len(str(f.path.absolute())) for f in top_files)

    print(f"{'Path': ^{max_path_length + 4}}|{'SLOC': ^16}|{'Words': ^16}|{'Characters': ^16}")
    for file in top_files:
        print(f"{str(file.path.absolute()): <{max_path_length + 4}}|{file.line_amount: ^16,}|{file.word_amount: ^16,}|{file.char_amount: ^16,}")


if __name__ == "__main__":
    main()
    os.system("pause")
