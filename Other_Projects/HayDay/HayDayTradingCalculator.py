
blankets = 1098
diamond_ring = 824
violet_dress = 327
wooly_chaps = 309
blackberry_muffin = 226
bacon_and_eggs = 201

aList = ["Bolts", "bolts", "B", "b", "Planks", "planks", "P", "p", "Duct Tape", "Duct tape",
         "duct tape", "DT", "dt"]

bList = ["Nails", "nails", "N", "n", "Screws", "screws", "S", "s", "Land Deeds", "Land deeds", "land deeds", "LD", "ld", "Mallets", "mallets",
         "M", "m", "Marker Stakes", "Marker stakes", "marker stakes", "MS", "ms"]


while True:

    numberOfItems, item = input("\nWhat do you want to calculate?: ").split(maxsplit=1)

    if item in aList:
        price = int(numberOfItems) * 4000
    elif item in bList:
        price = int(numberOfItems) * 1500
    else:
        price = int(numberOfItems) * 500


    def calcPrice(transferItem):
        return str(round(price / transferItem, 2))


    print("\n--------------------")
    print("\nTotal price of " + numberOfItems + " " + item + ": " + str(price) + " coins.\n")
    print("Price in Blankets: " + calcPrice(blankets))
    print("Price in Diamond Rings: " + calcPrice(diamond_ring))
    print("price in Violet Dresses: " + calcPrice(violet_dress))
    print("Price in Wooly Chaps: " + calcPrice(wooly_chaps))
    print("Price in Blackberry Muffins: " + calcPrice(blackberry_muffin))
    print("Price in Bacon and Eggs: " + calcPrice(bacon_and_eggs))
    print("\n\n--------------------")


    if input("\n\nMake another calculation?: ") in ["No", "no", "n"]:
        break
    else:
        continue
