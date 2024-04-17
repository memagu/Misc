from datetime import datetime, timezone
from pathlib import Path

DATA_DIR = Path("./data/")
OUTPUT_DIR = Path("./output/")

QUEUE_GROUPS_PATH = DATA_DIR / "onitio_queue_groups.json"
QUEUES_PATH = DATA_DIR / "onitio_queues.json"
CALLS_PATH = DATA_DIR / "calls.json"

def datetime_to_utc_iso(dt: datetime) -> str:
    """
    Convert a timezone-aware datetime object to an ISO 8601 string in UTC.

    :param dt: A timezone-aware datetime object.
    :type dt: datetime
    :return: The datetime as a string in the ISO 8601 format, in UTC.
    :rtype: str
    """
    return dt.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", 'Z')


def utc_iso_to_datetime(utc_iso: str) -> datetime:
    """
    Convert an ISO 8601 string in UTC to a timezone-aware datetime object.

    :param utc_iso: An ISO 8601 string representing a datetime in UTC.
    :type utc_iso: str
    :return: A datetime object representing the same moment in time as the input string, but adjusted to the system's local timezone.
    :rtype: datetime
    """
    return datetime.fromisoformat(utc_iso).astimezone()