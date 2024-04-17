import calendar
from datetime import datetime
import json
import locale
from pathlib import Path
from typing import Iterable

from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.ticker import FuncFormatter
import numpy as np

from util import utc_iso_to_datetime, CALLS_PATH, OUTPUT_DIR

Calls = list[dict[str, datetime | str]]


def load_calls(path: Path) -> Calls:
    return [
        {"datetime": utc_iso_to_datetime(call["datetime"]), "queue": call["queue"]}
        for call in json.loads(path.read_text())
    ]


def extract_stats(calls: Calls) -> tuple[np.ndarray[np.uint16], np.ndarray[np.uint16], np.ndarray[np.uint16]]:
    days = np.zeros(7, dtype=np.uint16)
    hours = np.zeros(24, dtype=np.uint16)
    minutes = np.zeros(60 * 24, dtype=np.uint16)

    increment = np.uint16(1)

    for call in calls:
        call_time = call["datetime"]
        weekday = call_time.weekday()

        days[weekday] += increment
        hours[call_time.hour] += increment
        minutes[call_time.hour * 60 + call_time.minute] += increment

    return days, hours, minutes


def plot_average_calls_per_day(days: np.ndarray) -> tuple[Figure, Axes]:
    x = np.arange(len(days))
    y = days / (91 / 7)

    fig = Figure((10, 8))
    ax = fig.subplots()

    ax.set_title("Genomsnittligt antal samtal per veckodag under en vecka (SE CSD All queues)")
    ax.set_xlabel("Veckodag")
    ax.set_ylabel("Antal samtal")

    ax.grid()
    ax.set_xticks(x, map(str.capitalize, calendar.day_name))
    ax.set_yticks(np.arange(0, np.ceil(y.max()), 5))

    ax.bar(x, y)

    return fig, ax


def plot_share_of_calls_per_day(days: np.ndarray) -> tuple[Figure, Axes]:
    x = np.arange(len(days))
    y = days / days.sum()

    fig = Figure((10, 8))
    ax = fig.subplots()

    ax.set_title("Andel samtal per veckodag i procent under en vecka (SE CSD All queues)")
    ax.set_xlabel("Veckodag")
    ax.set_ylabel("Andel samtal (%)")

    ax.grid()
    ax.set_xticks(x, map(str.capitalize, calendar.day_name))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda n, _: f"{n:.1%}"))
    ax.bar(x, y)

    return fig, ax


def plot_average_calls_per_hour(hours: np.ndarray) -> tuple[Figure, Axes]:
    x = np.arange(len(hours))
    y = hours / 91

    fig = Figure((10, 8))
    ax = fig.subplots()

    ax.set_title("Genomsnittligt antal samtal per timme under ett dygn (SE CSD All queues)")
    ax.set_xlabel("Timme på dagen")
    ax.set_ylabel("Antal samtal")

    ax.grid()
    ax.set_xticks(x, (f"{h:0>2}" for h in x))
    ax.set_yticks(np.arange(np.ceil(y.max())))

    ax.bar(x, y, align="edge", width=1)

    return fig, ax


def plot_share_of_calls_per_hour(hours: np.ndarray) -> tuple[Figure, Axes]:
    x = np.arange(len(hours))
    y = hours / sum(hours)

    fig = Figure((10, 8))
    ax = fig.subplots()

    ax.set_title("Andel samtal per timme under ett dygn (SE CSD All queues)")
    ax.set_xlabel("Timme på dagen")
    ax.set_ylabel("Andel samtal (%)")

    ax.grid()
    ax.set_xticks(x, (f"{h:0>2}" for h in x))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda n, _: f"{n:.1%}"))

    ax.bar(x, y, align="edge", width=1)

    return fig, ax


def plot_total_calls_per_minute(minutes: np.ndarray) -> tuple[Figure, Axes]:
    x = np.arange(len(minutes))
    y = minutes

    fig = Figure((10, 8))
    ax = fig.subplots()

    ax.set_title("Totalt antal samtal per minut under de senaste 91 dygnen (SE CSD All queues)")
    ax.set_xlabel("Tid")
    ax.set_ylabel("Antal samtal")

    ax.grid()
    ax.set_xticks(x[::60], map(lambda h: str(h).zfill(2), range(24)))
    ax.set_yticks(np.arange(np.ceil(y.max())))

    ax.bar(x, y, align="edge", width=1)
    ax.set_yticks(np.arange(np.ceil(y.max())))

    return fig, ax


def main() -> None:
    locale.setlocale(locale.LC_ALL, "sv_SE")
    calls = load_calls(CALLS_PATH)

    days, hours, minutes = extract_stats(calls)

    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True)

    plot_average_calls_per_day(days)[0].savefig(OUTPUT_DIR / "daily_average.png")
    plot_share_of_calls_per_day(days)[0].savefig(OUTPUT_DIR / "daily_share.png")
    plot_average_calls_per_hour(hours)[0].savefig(OUTPUT_DIR / "hourly_average.png")
    plot_share_of_calls_per_hour(hours)[0].savefig(OUTPUT_DIR / "hourly_share.png")
    plot_total_calls_per_minute(minutes)[0].savefig(OUTPUT_DIR / "minutely.png")


if __name__ == "__main__":
    main()
