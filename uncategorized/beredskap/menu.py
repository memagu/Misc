from dataclasses import dataclass, field
from typing import Any, Callable, Sequence


@dataclass(frozen=True)
class Option:
    name: str
    action: Callable
    args: Sequence = tuple()
    kwargs: dict[str, Any] = field(default_factory=dict)

    def execute_action(self) -> None:
        self.action(*self.args, **self.kwargs)


@dataclass(frozen=True)
class Menu:
    title: str = ""
    description: str = ""
    options: Sequence[Option] = tuple()

    def show(self) -> None:
        if self.title:
            print(self.title, "\n")

        if self.description:
            print(self.description, "\n")

        if self.options:
            option_number_pad_width = len(str(len(self.options))) + 2
            print(
                *(f"{i: <{option_number_pad_width}}{option.name}" for i, option in enumerate(self.options, 1)),
                '',
                sep='\n'
            )

    def prompt_option(self) -> Option:
        if not self.options:
            raise Exception("Menu object has no options.")

        while True:
            try:
                option_index = int(input("Enter option: ")) - 1

                if not 0 <= option_index < len(self.options):
                    raise IndexError

                print()
                return self.options[option_index]

            except ValueError:
                print(f"You must enter an integer! Try again.")
                continue

            except IndexError:
                print(f"That option does not exist! Try again.")
                continue


class MenuManager:
    def __init__(self, initial_state: Menu, transition_map: dict[tuple[Menu, int], Menu] = None):
        self.state = initial_state
        self.transition_map = transition_map

    def transition(self, index: int = 0) -> None:
        self.state = self.transition_map[(self.state, index)]
