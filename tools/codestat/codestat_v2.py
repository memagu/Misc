from dataclasses import dataclass
import hashlib
import multiprocessing
import os
from pathlib import Path
import tqdm
from typing import Container, Generator, Iterable

ALLOWED_EXTENSIONS = {
    ".rs",
    ".py",
    ".pyw",
    ".cpp",
    ".cs",
    ".java",
    ".js",
    ".cmd",
    ".bat",
    ".md"}
EXCLUDED_DIRNAMES = {
    "venv",
    ".idea",
    "obj",
    "Library",
    "target",
    "cmake-build-release",
    "cmake-build-debug",
    "Walnut"
}
TOPLIST_size = 10


@dataclass
class FileInfo:
    path: Path
    checksum: str
    size: int
    n_sloc: int
    n_words: int
    n_characters: int

    def __hash__(self):
        return int(self.checksum, 16)


def filtered_walk(root: Path, allowed_extensions: Container, excluded_dirnames: Container) -> Generator[
    Path, None, None]:
    for dirpath, dirnames, filenames in root.walk():
        dirnames[:] = [dirname for dirname in dirnames if dirname not in excluded_dirnames]
        for filepath in map(dirpath.__truediv__, filenames):
            if filepath.suffix in allowed_extensions:
                yield filepath


def extract_words(file_content: bytes) -> list[bytes]:
    translation_table = bytes.maketrans(b".:()[]{}'\";,", b' ' * 12)

    return (
        file_content.translate(translation_table)
        .replace(b'_', b"_ ")
        .replace(b"_ _ ", b"__")
        .replace(b'=', b"= ")
        .replace(b"= =", b"==")
        .split()
    )


def process_file(path: Path) -> FileInfo:
    with open(path, "rb") as f:
        content = f.read()

    return FileInfo(
        path,
        hashlib.md5(content).hexdigest(),
        path.stat().st_size,
        content.count(b'\n') - (content.count(b"\n\n") or content.count(b"\r\n\r\n")),
        len(extract_words(content)),
        len(content)
    )


def display_results(result: Iterable[FileInfo], top_n: int = 10) -> None:
    result = tuple(result)
    top_n = min(top_n, len(result))

    print(f"\nFiles: {len(result)}")
    print(f"Total SLOC: {sum(file_info.n_sloc for file_info in result):,}")
    print(f"Total words: {sum(file_info.n_words for file_info in result):,}")
    print(f"Total characters: {sum(file_info.n_characters for file_info in result):,}")

    print(f"\nTop {top_n} largest files (sloc):\n")

    top_files = sorted(set(result), key=lambda f: f.n_sloc, reverse=True)[:top_n]
    max_path_length = max(len(str(f.path.absolute())) for f in top_files)

    print(f"{'Path': ^{max_path_length + 4}}|{'Size (bytes)': ^16}|{'SLOC': ^16}|{'Words': ^16}|{'Characters': ^16}")
    for file in top_files:
        print(
            f"{str(file.path.absolute()): <{max_path_length + 4}}|{file.size: ^16,}|{file.n_sloc: ^16,}|{file.n_words: ^16,}|{file.n_characters: ^16,}")


def main() -> None:
    workers = os.cpu_count()
    root = Path(r"C:/Users/melke/Dev/")

    with multiprocessing.Pool(workers) as p:
        file_data = set(tqdm.tqdm(
            p.imap(process_file, filtered_walk(root, ALLOWED_EXTENSIONS, EXCLUDED_DIRNAMES)),
            desc=f"Analyzing files in \"{root}\" using {workers} workers",
            unit=" files"
        ))

    display_results(file_data)


if __name__ == "__main__":
    main()
