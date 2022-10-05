# elements = [i for i in range(10)]
#
# i = 0
# while i < len(elements):
#     if not elements[i] % 2:
#         elements.pop(i)
#         continue
#
#     i += 1
#
# print(elements)

# num = input("Enter a num: ")
# is_prime = input(f"Is {num} a prime? ")
# if is_prime.lower() in ["yes", "y"]:
#     print(f"{num} is a prime!")
# else:
#     print(f"{num} is not a prime :(")

from typing import List


class Data:
    def __init__(self, price: float = 0, date: str = "DD/MM/YYYY"):
        self.price = price
        self.date = date

    def __str__(self):
        return str(self.__dict__)


class DataManager:
    def __init__(self, data_list: List[Data]):
        self.data_list = data_list

    def print_data(self):
        for i, data in enumerate(self.data_list):
            print(i, data)


if __name__ == "__main__":
    data_manager = DataManager([Data(200, "20/04/2004"),
                                Data(123, "01/03/2013"),
                                Data(2435, "20/07/1998"),
                                Data(67457, "04/11/1337")])

    data_manager.print_data()

    options = ["add", "del", "list", "quit"]

    while True:
        option = input(f"Enter an option {options}: ")
        if option not in options:
            print("Invalid input\n")
            continue

        if option == "add":
            price = float(input("Enter price: "))
            date = input("Enter date DD/MM/YYYY: ")

            data_manager.data_list.append(Data(price, date))
            continue

        if option == "del":
            i = int(input("Enter index: "))
            data_manager.data_list.pop(i)
            continue

        if option == "list":
            data_manager.print_data()
            continue

        if option == "quit":
            break

        print()
