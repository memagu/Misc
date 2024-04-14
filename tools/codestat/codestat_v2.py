import argparse
from dataclasses import dataclass
import hashlib
import multiprocessing
import os
from pathlib import Path
from typing import Container, Generator, Iterable
import warnings

warnings.formatwarning = lambda message, category, *_: f"{category.__name__}: {message}\n"

try:
    import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False

VERSION = "2.0.0"

ALLOWED_EXTENSIONS = {
    ".rs",
    ".py",
    ".pyw",
    ".cpp",
    ".cs",
    ".java",
    ".asm",
    ".S",
    ".pl",
    ".bf"
    ".js",
    "html",
    "css",
    "scss",
    ".go",
    ".jl"
    ".cmd",
    ".bat",
    ".md"
}
EXCLUDED_DIRNAMES = {
    "venv",
    ".idea",
    "obj",
    "Library",
    "target",
    "cmake-build-release",
    "cmake-build-debug",
    "node_modules",
    "__pycache__",
    ".julia"
    ".git",
    ".vscode",
    ".gradle",
    "dist",
    "build",
    "debug",
    "release",
    "bin",
    "out",
    ".DS_Store"
    "data",
    "raw_data",
    "dataset",
    "datasets",
    "Walnut"
}


@dataclass
class FileInfo:
    path: Path
    checksum: str
    size: int
    n_sloc: int
    n_words: int
    n_chars: int

    def __hash__(self):
        return int(self.checksum, 16)


def filtered_walk(root: Path, allowed_extensions: Container, excluded_dirnames: Container) -> Generator[
    Path, None, None]:
    for dirpath, dirnames, filenames in root.walk():
        dirnames[:] = [dirname for dirname in dirnames if dirname not in excluded_dirnames]
        yield from (filepath for filepath in map(dirpath.__truediv__, filenames) if filepath.suffix in allowed_extensions)


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
    content = path.read_bytes()

    return FileInfo(
        path,
        hashlib.md5(content).hexdigest(),
        path.stat().st_size,
        content.count(b'\n') - (content.count(b"\n\n") or content.count(b"\r\n\r\n")) or bool(content),
        len(extract_words(content)),
        len(content)
    )


def display_results(results: Iterable[FileInfo], top_n: int = 10, sort_by: str = "sloc") -> None:
    results = tuple(results)
    unique_results = set(results)
    top_n = min(top_n, len(results)) if top_n >= 0 else len(unique_results)

    sort_options = {
        "size": lambda f: f.size,
        "sloc": lambda f: f.n_sloc,
        "words": lambda f: f.n_words,
        "chars": lambda f: f.n_chars
    }

    if sort_by not in sort_options:
        raise ValueError(f"Invalid column for sorting: {sort_by}")

    top_files = sorted(unique_results, key=sort_options[sort_by], reverse=True)[:top_n]
    max_path_length = max(len(str(f.path.absolute())) for f in top_files)

    print(
        "",
        f"Files: {len(results)}",
        f"Unique files {len(unique_results)}",
        f"Totals (unique files):",
        f"- SLOC: {sum(file_info.n_sloc for file_info in unique_results):,}",
        f"- Words: {sum(file_info.n_words for file_info in unique_results):,}",
        f"- Characters: {sum(file_info.n_chars for file_info in unique_results):,}",
        "",
        f"\nTop {top_n} files ({sort_by}):\n",
        '|'.join((
            "Path".center(max_path_length + 4),
            "Size (bytes)".center(24),
            "SLOC".center(24),
            "Words".center(24),
            "Characters".center(24)
        )),
        sep='\n'
    )
    for file in top_files:
        print('|'.join((
            f"{str(file.path.absolute()): <{max_path_length + 4}}",
            f"{file.size: ^24,}",
            f"{file.n_sloc: ^24,}",
            f"{file.n_words: ^24,}",
            f"{file.n_chars: ^24,}"
        )))


def main() -> None:
    parser = argparse.ArgumentParser(description="get statistics for all source code files in a directory")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 2.0.0",
        help="show program's version number end exit"
    )
    parser.add_argument(
        "path",
        type=Path,
        default=Path(),
        nargs="?",
        help="path to root search directory"
    )
    parser.add_argument(
        "-t",
        "--top",
        type=int,
        default=10,
        help="display top n rows (use a negative value to display all rows)"
    )
    parser.add_argument(
        "-s",
        "--sort-by",
        type=str,
        choices=("size", "sloc", "words", "chars"),
        default="sloc",
        help="sort table by column."
    )
    parser.add_argument(
        "-w",
        "--workers",
        type=int,
        default=os.cpu_count(),
        help="amount of worker threads"
    )
    args = parser.parse_args()

    workers = args.workers
    root_dir = args.path

    with multiprocessing.Pool(workers) as p:
        results = p.imap(process_file, filtered_walk(root_dir, ALLOWED_EXTENSIONS, EXCLUDED_DIRNAMES))

        if TQDM_AVAILABLE:
            file_data = tqdm.tqdm(
                results,
                desc=f"Analyzing files in \"{root_dir}\" using {workers} workers",
                unit=" files"
            )
        else:
            file_data = results
            warnings.warn("tqdm is not installed. Install tqdm using \"pip install tqdm\" to display a progress bar while processing.")

        display_results(file_data, args.top, args.sort_by)


if __name__ == "__main__":
    main()
