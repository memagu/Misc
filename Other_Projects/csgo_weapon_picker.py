from dataclasses import dataclass
from os import system
from random import choice
from time import sleep
from typing import Optional


@dataclass
class Items:
    weapons: Optional[tuple[tuple[str, int], ...]] = tuple()
    grenades: Optional[tuple[tuple[str, int], ...]] = tuple()
    utility: Optional[tuple[tuple[str, int], ...]] = tuple()
    armor: Optional[tuple[tuple[str, int], ...]] = tuple()


ITEMS_COMMON = Items(
    weapons=(
        ("Dual Berettas", 300),
        ("P250", 300),
        ("Desert Eagle", 700),
        ("Nova", 1050),
        ("XM1014", 2000),
        ("M249", 5200),
        ("Negev", 1700),
        ("MP7", 1500),
        ("UMP-45", 1200),
        ("P90", 2350),
        ("PP-Bizon", 1400),
        ("SSG08", 1700),
        ("AWP", 4750),
    ),
    grenades=(
        ("Flashbang", 200),
        ("Smoke Grenade", 300),
        ("High Explosive Grenade", 300),
        ("Decoy Grenade", 50),
    ),
    utility=(
        ("Zeus x27", 200),
    ),
    armor=(
        ("Kevlar Vest", 650),
        ("Kevlar + Helmet", 1000),
    )
)
ITEMS_CT = Items(
    weapons=(
        ("USP-S", 200),
        ("Five-SeveN", 500),
        ("MAG-7", 1300),
        ("MP9", 1250),
        ("FAMAS", 2050),
        ("M4A4", 3100),
        ("AUG", 3300),
        ("SCAR-20", 5000),
    ),
    grenades=(
        ("Incendiary Grenade", 600),
    ),
    utility=(
        ("Defuse Kit", 400),
    )
)
ITEMS_T = Items(
    weapons=(
        ("Glock-18", 200),
        ("Tec-9", 500),
        ("Sawed-Off", 1100),
        ("MAC-10", 1050),
        ("Galil AR", 1800),
        ("AK-47", 2700),
        ("SG 553", 3000),
        ("G3SG1", 5000),
    ),
    grenades=(
        ("Molotov", 400),
    )
)


def fetch_budget() -> int:
    while True:
        try:
            return int(input("Enter your budget: "))
        except ValueError:
            print("Invalid input, input must be a number. Try again!")


def fetch_team() -> str:
    while True:
        team = input("Enter team (ct or t): ").strip().lower()
        if team in ("ct", "t"):
            return team

        print("Invalid input, input must be either 'ct' or 't'. Try again!")


def get_possible_weapons(budget: int, team: str) -> list[tuple[str, int]]:
    weapons = ITEMS_COMMON.weapons + (ITEMS_CT.weapons if team == "ct" else ITEMS_T.weapons)
    return [weapon for weapon in weapons if weapon[1] <= budget]


def get_possible_armors(budget: int) -> list[tuple[str, int]]:
    return [armor for armor in ITEMS_COMMON.armor if armor[1] <= budget]


def get_possible_grenade_combos(budget: int, team: str) -> list[tuple[str, int]]:
    grenades = ITEMS_COMMON.grenades + (ITEMS_CT.grenades if team == "ct" else ITEMS_T.grenades)

    possible_grenade_combos = []

    for selection_bitmask in (bitmask for bitmask in range(1, 2 ** (len(grenades) + 1)) if
                              bitmask.bit_count() <= 4 and bitmask & 0b110000 ^ 0b010000):
        labels = []
        total_price = 0
        if selection_bitmask >= 0b100000:
            if selection_bitmask >= 0b110000:
                labels.append("2x Flashbang")
                total_price += 400
            else:
                labels.append("Flashbang")
                total_price += 200

        for i in range(len(grenades) - 1):
            if selection_bitmask & 1 << i:
                label, price = grenades[i + 1]
                labels.append(label)
                total_price += price

        if total_price <= budget:
            possible_grenade_combos.append((' + '.join(labels), total_price))

    return possible_grenade_combos


def get_possible_utility_combos(budget: int, team: str) -> list[tuple[str, int]]:
    utilities = ITEMS_COMMON.utility + (ITEMS_CT.utility if team == "ct" else ITEMS_T.utility)

    possible_utility_combos = []

    for selection_bitmask in (bitmask for bitmask in range(1, 2 ** len(utilities))):
        labels = []
        total_price = 0

        for i in range(len(utilities)):
            if selection_bitmask & 1 << i:
                label, price = utilities[i]
                labels.append(label)
                total_price += price

        if total_price <= budget:
            possible_utility_combos.append((' + '.join(labels), total_price))

    return possible_utility_combos


def fetch_option_cost(title: str, item_options: list[tuple[str, int]]) -> int:
    print(title)
    print(f"    1) $0    --Nothing--")
    for i, (label, price) in enumerate(item_options, 2):
        print(f"{i: >5}) ${price: <4} {label}")

    while True:
        try:
            option = int(input("Enter option: ")) - 2
            if not -1 <= option < len(item_options):
                print("Invalid input, option does not exist. Try again!")
                continue

            if option == -1:
                return 0

            return item_options[option][1]

        except ValueError:
            pass
        print("Invalid input, input must be an integer. Try again!")


def message_from_god() -> None:
    print("*God appears*")
    sleep(1.5)
    print("* AHEM *")
    sleep(2)
    print("Hear me, O my loyal warrior,")
    sleep(2.5)
    print("for I am the Eternal Creator thy God,")
    sleep(3)
    print("who hath forged thee and all things from endless void.")
    sleep(3.5)
    print("I bless thee with this sacred weapon,")
    sleep(3)
    print("the expression of my wrath and dominion.")
    sleep(3)
    print("By this weapon shalt thou purge the heretic, the terrorist, the antiterrorist, the smurf, the baiter,")
    sleep(5.5)
    print("and detonate their blasphemous devices and liberate their captives.")
    sleep(3.5)
    print("Thou art my chosen one, my beloved, my MVP.")
    sleep(3)
    print("BEHOLD! . . . ")
    sleep(1)


def display_item(item: tuple[str, int]) -> None:
    label, price = item

    weapon_label = f"Weapon: {label}"
    price_label = f"Price: ${price}"

    box_width = max(len(weapon_label), len(price_label) + 1) + 8

    lid = "#" * box_width
    lip = f"#{' ' * (box_width - 2)}#"

    print(lid, lip, weapon_label.center(box_width), price_label.center(box_width), lip, lid, sep='\n')


def main() -> None:
    budget = fetch_budget()
    team = fetch_team()

    armors = get_possible_armors(budget)
    budget -= fetch_option_cost("Armor options:", armors)
    print(f"\nYour updated budget is: ${budget}\n")

    grenade_combos = get_possible_grenade_combos(budget, team)
    budget -= fetch_option_cost("Grenade options:", grenade_combos)
    print(f"\nYour updated budget is: ${budget}\n")

    utility_combos = get_possible_utility_combos(budget, team)
    budget -= fetch_option_cost("Utility options:", utility_combos)
    print(f"\nYour updated budget is: ${budget}\n")

    weapons = get_possible_weapons(budget, team)

    if not weapons:
        print("No weapon could be chosen as you have to little money remaining, GLHF though!")
        return

    weapon = choice(weapons)

    message_from_god()

    display_item(weapon)

    input("Press enter to rerun.")


if __name__ == "__main__":
    while True:
        main()
        system("cls")
