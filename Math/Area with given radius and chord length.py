

import math


loop = True


while loop == True:

    r = float(input("Enter radius: "))
    k = float(input("Enter chord length: "))

    print("\nArea of sector: " + str(math.acos((k ** 2 - 2 * r ** 2) / (-2 * r ** 4)) / (math.pi * 2) * r ** 2 * math.pi))
    print("Area of triangle: " + str(r ** 2 * math.sin(math.acos((k ** 2 - 2 * r ** 2) / (-2 * r ** 4))) / 2))
    print("Area between circle and chord: " + str(math.acos((k ** 2 - 2 * r ** 2) / (-2 * r ** 4)) / (math.pi * 2) * r ** 2 * math.pi - (r ** 2 * math.sin(math.acos((k ** 2 - 2 * r ** 2) / (-2 * r ** 4))) / 2)) + "\n")

    if input("Again? [y/n]: ") != "y":
        break


