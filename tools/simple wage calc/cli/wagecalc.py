import pathlib
from datetime import datetime, timedelta
import os
import json
from pathlib import Path

TIME_INPUT_FORMAT = "%H%M"
TIME_OUTPUT_FORMAT = "%H:%M"
DATETIME_KEYS = ("start", "end")

CURRENCY = "SEK"

SHIFTS_PATH = Path("./shifts.json")
PAY_PATH = Path("./pay.json")


def time_interval_to_str(start: datetime, end: datetime, format: str = TIME_OUTPUT_FORMAT) -> str:
    return f"{start.strftime(format)}-{end.strftime(format)}"


def datetime_decoder(dictionary: dict) -> dict:
    for datetime_key in DATETIME_KEYS:
        if datetime_key in dictionary:
            dictionary[datetime_key] = datetime.strptime(dictionary[datetime_key], TIME_INPUT_FORMAT)

    return dictionary


def load_json_with_datetime(path: Path) -> dict:
    with open(path, "r") as f:
        return json.load(f, object_hook=datetime_decoder)


def calculate_duration_seconds(start: datetime, end: datetime, interval_start: datetime, interval_end: datetime) -> float:
    return max(timedelta(), min(end, interval_end) - max(start, interval_start)).total_seconds()


def main() -> None:
    shift_data = load_json_with_datetime(SHIFTS_PATH)
    pay_data = load_json_with_datetime(PAY_PATH)

    secondly_wage = pay_data["base_hourly_wage"] / 3600

    for day_type, shifts in shift_data.items():
        print(day_type.center(32, '-'))
        for shift in shifts:
            shift_pay = 0
            for pay_interval in pay_data[day_type]:
                interval_work_duration = calculate_duration_seconds(
                    shift["start"],
                    shift["end"],
                    pay_interval["start"],
                    pay_interval["end"]
                )

                interval_break_duration = sum(
                    calculate_duration_seconds(
                        _break["start"],
                        _break["end"],
                        pay_interval["start"],
                        pay_interval["end"]
                    ) for _break in shift["breaks"]
                )

                shift_pay += (interval_work_duration - interval_break_duration) * secondly_wage * pay_interval["pay_ratio"]

            print(f"{shift_pay:.2f} {CURRENCY} @ {time_interval_to_str(shift["start"], shift["end"])} / {", ".join(time_interval_to_str(_break["start"], _break["end"]) for _break in shift["breaks"])}")


if __name__ == '__main__':
    main()
    os.system("pause")
