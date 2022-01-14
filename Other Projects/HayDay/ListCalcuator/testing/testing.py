import os
import sys


def create_files():
    count = 0
    if not os.path.exists("README.txt"):
        count += 1
        with open("README.txt", "w") as htu:
            htu.write("Settings:\n")
            htu.write("1. Choose to alphabetically sort your list by setting 'Sort list:' to either 'True' of 'False'.")
            htu.write("\n2. You can change any number of items by using the 'settings.txt' file. Use the following ")
            htu.write("format: <old value> -> <new value>.\n   Example: 8 -> 6. The example will change ")
            htu.write("the number of eight items to six (8 goat milk --> 6 goat milk).\n\n")
            htu.write("How to use:\n")
            htu.write("1. Put your list in 'input.txt'. Input must be entered accordingly: <number of items> <item>.")
            htu.write(" Example input: 10 brown sugar.\n")
            htu.write("2. Output will be provided in the console and in a text file called: 'output.txt'.")

    if not os.path.exists("settings.txt"):
        count += 1
        with open("settings.txt", "w") as settings:
            settings.write("Sort list | <True or False>:\n")
            settings.write("True\n\n")
            settings.write("Custom mapping | <old value> -> <new value>:\n")

    if not os.path.exists("input.txt"):
        count += 1
        open("input.txt", "w").close()

    if not os.path.exists("output.txt"):
        count += 1
        open("output.txt", "w").close()

    if count > 0:
        input("Necessary files created, press enter to exit.")
        sys.exit()


def settings_to_dictionary():
    conversion_table = {}

    with open("settings.txt") as settings:
        conversions = settings.readlines()
        for line in conversions[4:]:
            conversion_table[int(line.split()[0])] = int(line.split()[2])

    return conversion_table


def convert(number, dictionary):
    if number in dictionary:
        return dictionary[number]
    return number


def make_list():

    number_of_items = 0
    number_of_unique_items = 0

    with open("settings.txt", "r") as settings:
        conversion_table = settings_to_dictionary()
        set_sort = settings.readlines()
        if set_sort[1] == "True\n":
            sort_list = True
        else:
            sort_list = False

        with open("output.txt", "w", ) as data_out:
            with open("input.txt", "r") as data_in:
                new_lines = []
                for line in data_in.readlines():
                    number_of_unique_items += 1

                    number_of_current_item = convert(int(line.split()[0]), conversion_table)
                    item = ' '.join(line.split(maxsplit=2)[1:]).strip('\n')

                    new_lines.append(f"{item}: {number_of_current_item}")

                    number_of_items += number_of_current_item

                if sort_list == True:
                   new_lines.sort()

                for new_line in new_lines:
                    data_out.write(new_line + "\n")
                    print(new_line)

            data_out.write(f"\nTotal number of items: {number_of_items}\nTotal number of unique items: {number_of_unique_items}")

            print(f"\nTotal number of items: {number_of_items}\nTotal number of unique items: {number_of_unique_items}")

    input("\n----------------\n\nPress enter to exit.")


if __name__ == "__main__":
    create_files()
    make_list()