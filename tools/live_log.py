import argparse
from pathlib import Path
import time
from typing import Never

POLLING_INTERVAL_SECONDS = 0.1
MAX_READ_SIZE = 1 << 17  # 128 KiB


def monitor_file(file: Path, max_read_size: int = -1, polling_interval_seconds: float = 0.1) -> Never:
    """
    Continuously monitors a file for new entries and prints them out as they are added.

    :param file: Path to the file to be monitored.
    :type file: pathlib.Path
    :param max_read_size: Maximum number of bytes to read at a time. If set to -1, the function will read as much data as available without limit.
    :type max_read_size: int
    :param polling_interval_seconds: Interval in seconds at which to attempt reading new data from the file.
    :type polling_interval_seconds: float
    :return: This function never returns.
    :rtype: typing.Never
    """
    with file.open("rb") as f:
        while True:
            new_data = f.read(max_read_size)
            if new_data:
                print(new_data.decode("UTF-8"), end='')
            time.sleep(polling_interval_seconds)


def main() -> None:
    """
    usage: live_log.py [-h] file

    A continuous log file monitor that reads and prints new entries in real-time.

    positional arguments:
      file        The file to be monitored.

    options:
      -h, --help  show this help message and exit
    """
    parser = argparse.ArgumentParser(description="A continuous log file monitor that reads and prints new entries in real-time.")
    parser.add_argument("file", type=Path, help="The file to be monitored.")
    args = parser.parse_args()

    monitor_file(args.file)


if __name__ == "__main__":
    main()
