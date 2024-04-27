from datetime import datetime, timedelta
import os
from pathlib import Path
import platform

from call import Call, CallManager
from menu import Menu, Option

CLEAR_COMMAND = "cls" if platform.system() == "Windows" else "clear"

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
REPORT_DIR = Path("./reports")


def prompt_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, enter an integer and try again.")


def prompt_datetime(prompt: str, _format: str) -> datetime:
    while True:
        try:
            return datetime.strptime(input(prompt), _format)
        except ValueError:
            print("Invalid format, try again.")


def register_call(call_manager: CallManager) -> None:
    call_manager.add_call(
        Call(
            input("Enter phone number: "),
            prompt_datetime("Enter call start (YYYY-mm-ddTHH:MM:SS): ", DATETIME_FORMAT),
            timedelta(minutes=prompt_int("Enter call and handling duration (minutes): ")),
            input("Enter case number: ")
        )
    )


def delete_call(call_manager: CallManager) -> None:
    calls = call_manager.get_calls()

    if not calls:
        return

    option_whitespace_buffer_size = len(str(len(calls))) + 2

    print(f"{"i": <{option_whitespace_buffer_size}}|{"Date and Time": ^24}|{"Phone Number": ^16}|{"Case Number": ^16}")
    for i, call in enumerate(calls):
        print(
            f"{i: <{option_whitespace_buffer_size}}|{call.start.isoformat(): ^24}|{call.phone_number: ^16}|{call.case_number: ^16}")
    print('\n')

    while True:
        index = prompt_int("Enter the index of the call to delete, -1 to return to main menu: ")

        if index == -1:
            return

        if 0 <= index < len(calls):
            break

        print(f"Invalid input, no item at index {index}. Try again.")

    call_manager.delete_call(index)


def create_report(call_manager: CallManager) -> None:
    start = prompt_datetime("Enter start of duration to report: ", DATETIME_FORMAT)
    end = prompt_datetime("Enter end of duration to report: ", DATETIME_FORMAT)

    if not REPORT_DIR.exists():
        REPORT_DIR.mkdir(parents=True)

    file = REPORT_DIR / f"{start.isoformat()}--{end.isoformat()}.txt".replace(':', '_')
    report = call_manager.create_report(start, end)

    file.write_text(report)


def main() -> None:
    call_manager = CallManager()
    menu = Menu(
        "Standby Shift Call Tracker",
        "A tool for tracking calls and calculating initialized half hours for easy reporting.",
        (
            Option(
                "Register a call",
                register_call,
                (call_manager,)
            ),
            Option(
                "Delete a call record",
                delete_call,
                (call_manager,)
            ),
            Option(
                "Create report",
                create_report,
                (call_manager,)
            ),
            Option(
                "Exit",
                exit
            )
        )

    )

    while True:
        menu.show()
        menu.prompt_option().execute_action()
        os.system(CLEAR_COMMAND)


if __name__ == "__main__":
    main()
