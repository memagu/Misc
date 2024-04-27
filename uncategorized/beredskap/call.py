from __future__ import annotations
import bisect
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from functools import reduce, total_ordering
from hashlib import sha1
from pathlib import Path
import pickle
from typing import Sequence, Optional


@dataclass(frozen=True)
@total_ordering
class Call:
    phone_number: str
    start: datetime
    duration: timedelta
    case_number: str

    def __eq__(self, other: Call) -> bool:
        return self.start == other.start

    def __lt__(self, other: Call) -> bool:
        return self.start < other.start

    def __hash__(self) -> int:
        return int(sha1(str(self).encode("utf-8")).hexdigest(), 16)

    @property
    def end(self) -> datetime:
        return self.start + self.duration

    def half_hours(self, initial_half_hour: datetime) -> list[datetime]:
        if initial_half_hour + timedelta(minutes=30) < self.start:
            initial_half_hour = self.start

        return [
            initial_half_hour + timedelta(minutes=30 * i)
            for i in
            range((self.end - initial_half_hour).seconds // 1800 + 1)
        ]


class CallManager:
    def __init__(self, data_file: Path = Path("./calls.pkl")):
        self._data_file = data_file
        self._calls = self._load() or []

    def _load(self) -> Optional[list[Call]]:
        if not self._data_file.exists():
            return

        with self._data_file.open("rb") as f:
            return pickle.load(f)

    def _save(self):
        if not self._data_file.parent.exists():
            self._data_file.mkdir(parents=True)

        with self._data_file.open("wb") as f:
            pickle.dump(self._calls, f)

    def get_calls(self) -> list[Call]:
        return self._calls

    def add_call(self, call: Call):
        bisect.insort(self._calls, call)
        self._save()

    def delete_call(self, index: int):
        self._calls.pop(index)
        self._save()

    def calls_during_period(self, start: datetime, end: datetime) -> list[Call]:
        start_i = bisect.bisect_left(self._calls, start, key=lambda c: c.start)
        end_i = bisect.bisect_right(self._calls, end, key=lambda c: c.end)

        return self._calls[start_i:end_i]

    @staticmethod
    def half_hour_groups(calls: Sequence[Call]) -> dict[datetime, list[Call]]:
        half_hour_groups = defaultdict(list)
        active_half_hour = datetime.min

        for call in calls:
            half_hours = call.half_hours(active_half_hour)
            active_half_hour = half_hours[-1]

            for half_hour in half_hours:
                half_hour_groups[half_hour].append(call)

        return half_hour_groups

    def create_report(self, start: datetime, end: datetime, group_sep: str = '#', call_sep: str = '-') -> str:
        calls = self.calls_during_period(start, end)
        half_hour_groups = sorted(self.half_hour_groups(calls).items())

        report = [
            f"Period: {start.astimezone().isoformat()} -> {end.astimezone().isoformat()}",
            "",
            f"Calls: {len(calls)}", f"Initiated half hours: {len(half_hour_groups)}",
            f"Active work time: {reduce(lambda td, c: td + c.duration, calls, timedelta())}",
            ""
        ]

        for n, (half_hour, group) in enumerate(half_hour_groups, 1):
            report.append(f"{f' {n}. {half_hour:%H:%M:%S} '.center(32, group_sep)}")
            report.append("")
            report.append(
                f"\n\n{call_sep * 32}\n\n".join((
                    '\n'.join((
                        f"Tel: {call.phone_number}",
                        f"Start: {call.start:%H:%M:%S}",
                        f"Duration: Ca. {call.duration}",
                        f"Case: {call.case_number}",
                        f"Half hour: {half_hour:%H:%M:%S}"
                    )) for call in group
                ))
            )
            report.append("")

        return '\n'.join(report)