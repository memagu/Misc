from collections import defaultdict
from typing import Generator

USED_SEAT_SYMBOL = "XX"

MESSAGE_BOOKING_CANCELLATION = "Din bokning avbryts, eftersom inga platser bokades."
MESSAGE_BOOKING_REMOVAL = "Din bokning tas bort, eftersom alla platser i den avbokats."
MESSAGE_EXIT = "Tack! Programmet avslutas."
MESSAGE_GREETING = "Hej, välkommen till SJ bokning för tåg X1337: Stockholm - Göteborg."
MESSAGE_INVALID_BOOKING_CODE = "Bokningskoden som angetts är ogiltig. Var vänlig försök igen."
MESSAGE_UNBOOK_COMPLETED = "Tack för din avbokning, synd att du inte kommer resa med oss på X1337."

PROMPT_BOOKING_CODE = "Ange bokningskod: "
PROMPT_MODE = "1. Boka Platser\n2. Avboka Platser\n3. Avsluta\n\nVad vill du göra?: "
PROMPT_SEATS = "Ange platser. Om flera platser anges ska de separeras med mellanslag: "


def print_seats(seats: list[list[str]]) -> None:
    print(f"|{'-' * (len(max(seats, key=len)) * 3 - 1)}|")
    for i, seat_row in enumerate(seats):
        print(' ' + '|'.join(seat_row))
        if i % 2 and i < len(seats) - 1:
            print()
    print(f"|{'-' * (len(max(seats, key=len)) * 3 - 1)}|")


def seat_to_indices(seat: str) -> tuple[int, int]:
    return ord(seat[1]) - ord('a'), int(seat[0]) - 1


def indices_to_seat(indices: tuple[int, int]) -> str:
    return str(indices[1] + 1) + chr(indices[0] + ord('a'))


def booking_code_generator() -> Generator[str, None, None]:
    next_booking_number = 0

    while next_booking_number < 10e7:
        booking_number = str(next_booking_number).rjust(8, "0")
        yield f"SJ-{booking_number[:4]}-{booking_number[4:]}"

        next_booking_number += 1

    raise Exception("Maximum amount of booking codes generated.")


def main() -> None:
    seats = [[str(num) + letter for num in range(1, 10)] for letter in "abcd"]
    bookings = defaultdict(list)
    booking_codes = booking_code_generator()

    print(f"{MESSAGE_GREETING}\n")

    while True:
        mode = input(PROMPT_MODE)
        print()

        if mode == '1':
            print_seats(seats)
            print()

            booking_code = next(booking_codes)
            wanted_seats = input(PROMPT_SEATS).lower().split()
            for seat in wanted_seats:
                row, col = seat_to_indices(seat)
                if not (0 <= row < len(seats) and 0 <= col < len(seats[0])):
                    print(f"Plats {seat} kunde inte bokas, eftersom den inte existerar.")
                    continue

                if seats[row][col] == USED_SEAT_SYMBOL:
                    print(f"Tyvärr är plats {seat} redan bokad. Du kan försöka boka den igen senare.")
                    continue

                bookings[booking_code].append((row, col))
                seats[row][col] = USED_SEAT_SYMBOL

            if not bookings[booking_code]:
                print(f"{MESSAGE_BOOKING_CANCELLATION}\n")
                continue

            print(f"Tack för din bokning! Här är din bokningskod som du behöver vid avbokningen: {booking_code}\n")
            continue

        if mode == '2':
            booking_code = input(PROMPT_BOOKING_CODE)
            if not booking_code in bookings:
                print(f"{MESSAGE_INVALID_BOOKING_CODE}\n")
                continue

            print(f"Dina bokade platser är: {' '.join(indices_to_seat(indices) for indices in bookings[booking_code])}")
            seats_to_unbook = input(PROMPT_SEATS).lower().split()

            for seat in seats_to_unbook:
                row, col = seat_to_indices(seat)
                if seat_to_indices(seat) not in bookings[booking_code]:
                    print(f"Plats {seat} kunde inte avbokas, eftersom den inte ingår i denna bokning.")
                    continue

                bookings[booking_code].remove((row, col))
                seats[row][col] = seat

            if not bookings[booking_code]:
                print(MESSAGE_BOOKING_REMOVAL)
                del bookings[booking_code]

            print(f"{MESSAGE_UNBOOK_COMPLETED}\n")
            continue

        if mode == '3':
            print(MESSAGE_EXIT)
            break

        print(f'"{mode}" är inte ett giltigt alternativ. Var vänlig försök igen.')


if __name__ == "__main__":
    main()
