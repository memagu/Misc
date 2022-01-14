import re

item_name = 0
item_level = 1
item_cost = 2
item_production = 3

def check_whitespace(string):
    if string != "" and string != " ":
        return string


with open("items.txt", "w+") as f:
    with open("items_unrefined.txt", "r") as f_in:

        items = []
        for line in f_in.read().splitlines():
            temp = list(filter(check_whitespace, re.split(r"(\D+)", line)))
            for i in range(4):
                if i == 1 or i == 2:
                    temp[i] = int(temp[i].strip())
                else:
                    temp[i] = temp[i].strip()

            print(temp)
            items.append(temp)

        #f.write(str(items))

        items = sorted(items, key=lambda x: x[item_cost], reverse=True)

        # for item in items:
        #     f.write(item[item_name] + " | " + str(item[item_cost]) + " Coins" + "\n")

        for item in items:
            print(f'"{item[item_name]}": {item[item_cost]}')
            f.write(f'"{item[item_name].lower()}": {item[item_cost]}, ' + "\n")


