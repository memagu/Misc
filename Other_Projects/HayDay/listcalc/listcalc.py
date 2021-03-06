import os, sys


def create_files():
    count = 0

    if not os.path.exists("list.txt"):
        count += 1
        with open("list.txt", "w") as f_list:
            f_list.write("multiplier: 1\n420 Bread\n69 Blanket")

    if not os.path.exists("result.txt"):
        count += 1
        open("result.txt", "w").close()

    if count > 0:
        input("Necessary files created, press any key to exit.")
        sys.exit()


pricedict = {"blanket": 1098,
             "lemon cake": 896,
             "diamond ring": 824,
             "seafood salad": 763,
             "pasta salad": 759,
             "feta salad": 745,
             "necklace": 727,
             "blt salad": 723,
             "flower pendant": 698,
             "jelly beans": 684,
             "pillow": 676,
             "fried candy bar": 658,
             "iron bracelet": 658,
             "bacon toast": 648,
             "big sushi roll": 648,
             "lobster pasta": 637,
             "lobstersushi": 637,
             "chocolate fondue": 626,
             "top hat": 619,
             "peanut butter milkshake": 619,
             "lobster soup": 612,
             "chocolate roll": 604,
             "peanut butter sandwich": 601,
             "fruit salad": 597,
             "peanut noodles": 597,
             "crunchy donut": 594,
             "egg sandwich": 583,
             "spicy pasta": 576,
             "sun hat": 558,
             "candy bouquet": 554,
             "summer salad": 554,
             "egg sushi": 550,
             "berry smoothie": 547,
             "spicy fish": 543,
             "veggie lasagna": 532,
             "veggie bagel": 532,
             "corn dog": 529,
             "plum smoothie": 522,
             "bracelet": 514,
             "chocolate pie": 514,
             "cocoa smoothie": 511,
             "bacon fondue": 507,
             "mixed smoothie": 504,
             "gracious bouquet": 500,
             "cheese fondue": 493,
             "sushiroll": 489,
             "honey apple cake": 482,
             "tomato soup": 478,
             "gnocchi": 475,
             "onion melt": 471,
             "honey peanuts": 468,
             "cloche hat": 468,
             "coleslaw": 468,
             "olive dip": 468,
             "peach jam": 464,
             "cucumber sandwich": 464,
             "rice ball": 464,
             "chocolate": 460,
             "lemon candle": 457,
             "marmelade": 457,
             "fruit cake": 450,
             "fancy cake": 450,
             "peach ice cream": 450,
             "lemon pie": 446,
             "floral candle": 442,
             "eggplant parmesan": 442,
             "bell pepper soup": 439,
             "peach tart": 435,
             "noodle soup": 432,
             "nachos": 432,
             "banana bread": 424,
             "lobster skewer": 417,
             "pasta carbonara": 410,
             "chili poppers": 406,
             "lemon lotion": 403,
             "frutti di mare pizza": 403,
             "filled donut": 403,
             "banana split": 403,
             "orange sorbet": 399,
             "taco": 396,
             "pumpkin soup": 392,
             "fish taco": 392,
             "bacon donut": 388,
             "blackberry jam": 388,
             "plum jam": 385,
             "lemon curd": 378,
             "strawberry candle": 370,
             "hot dog": 370,
             "tofu dog": 367,
             "casserole": 367,
             "mayonaise": 367,
             "exfoliating soap": 363,
             "raspberry candle": 360,
             "honey popcorn": 360,
             "banana pancakes": 352,
             "stuffed peppers": 352,
             "veggie bouquet": 352,
             "cherry popsicle": 352,
             "birthday bouquet": 349,
             "yogurt smoothie": 349,
             "caramel latte": 345,
             "broccoli pasta": 345,
             "lollipop": 342,
             "chocolate ice cream": 342,
             "bright bouquet": 338,
             "cherry jam": 334,
             "flower crown": 331,
             "strawberry ice cream": 331,
             "honey soap": 327,
             "violet dress": 327,
             "onion soup": 327,
             "grilled eggplant": 324,
             "colorful candle": 324,
             "honey mask": 320,
             "chocolate cake": 320,
             "green smoothie": 320,
             "strawberry cake": 316,
             "hot chocolate": 316,
             "summer rolls": 316,
             "sprinkled donut": 313,
             "black sesame smoothie": 313,
             "honey tea": 313,
             "potato feta cake": 309,
             "snack mix": 309,
             "wooly pants": 309,
             "onion dog": 306,
             "tofu stir fry": 306,
             "bacon fries": 302,
             "goat cheese toast": 302,
             "baked potato": 298,
             "soft bouquet": 298,
             "fish soup": 298,
             "hand pies": 295,
             "flower shawl": 295,
             "caffe mocha": 291,
             "mint ice cream": 288,
             "red scarf": 288,
             "potato bread": 284,
             "cheese cake": 284,
             "mushroom pasta": 280,
             "shepherds pie": 280,
             "iced banana latte": 277,
             "olive oil": 277,
             "gingerbread cookie": 273,
             "sesame brittle": 270,
             "strawberry jam": 270,
             "apple pie": 270,
             "cabbage soup": 270,
             "veggie platter": 266,
             "cucumber smoothie": 266,
             "pineapple cake": 259,
             "raspberry mocha": 259,
             "red berry cake": 255,
             "caramel apple": 255,
             "honey toast": 255,
             "potato soup": 255,
             "orange tea": 255,
             "mint tea": 255,
             "raspberry jam": 252,
             "salsa": 252,
             "ice tea": 252,
             "espresso": 248,
             "chocolate popcorn": 248,
             "fish and chips": 244,
             "cotton shirt": 241,
             "quesadilla": 241,
             "green tea": 241,
             "lemon tea": 241,
             "broccoli soup": 237,
             "beeswax": 234,
             "orange juice": 234,
             "beetroot salad": 234,
             "peanuts": 234,
             "cream donut": 230,
             "tomato sauce": 230,
             "spicy pizza": 226,
             "blackberry muffin": 226,
             "fishburger": 226,
             "cotton candy": 226,
             "fish pie": 226,
             "feta pie": 223,
             "cream cake": 219,
             "caffe latte": 219,
             "apple jam": 219,
             "bacon pie": 219,
             "cherry juice": 216,
             "mushroom salad": 216,
             "rustic bouquet": 208,
             "blue sweater": 208,
             "berry juice": 205,
             "platinum bar": 205,
             "fried rice": 205,
             "bacon and eggs": 201,
             "lobsters": 201,
             "winter veggies": 198,
             "garlic bread": 198,
             "pizza": 190,
             "grilled onion": 190,
             "milk tea": 190,
             "hamburger": 180,
             "gold bar": 180,
             "fish skewer": 176,
             "toffee": 176,
             "sesame ice cream": 176,
             "mushroom soup": 176,
             "vanilla ice cream": 172,
             "apple ginger tea": 169,
             "carrot cake": 165,
             "goat cheese": 162,
             "grape jam": 162,
             "tomato juice": 162,
             "mushroom pot pie": 162,
             "pumpkin pie": 158,
             "honey": 154,
             "soy sauce": 154,
             "sweater": 151,
             "silver bar": 147,
             "raspberry muffin": 140,
             "duck feather": 140,
             "plain donut": 129,
             "apple juice": 129,
             "iron bar": 129,
             "pickaxe": 126,
             "butter popcorn": 126,
             "cheese": 122,
             "chili popcorn": 122,
             "roasted tomatoes": 118,
             "blue woolly hat": 111,
             "shovels": 108,
             "pancakes": 108,
             "watermelon juice": 108,
             "cotton fabrics": 108,
             "coal bar": 108,
             "cookie": 104,
             "grape juice": 104,
             "rice noodles": 100,
             "syrup": 90,
             "butter": 82,
             "carrot pie": 82,
             "tnt barrels": 72,
             "corn bread": 72,
             "pineapple juice": 68,
             "saws": 54,
             "fish fillets": 54,
             "cream": 50,
             "white sugar": 50,
             "carrot juice": 46,
             "fresh pasta": 43,
             "axes": 36,
             "popcorn": 32,
             "brown sugar": 32,
             "dynamites": 25,
             "bread": 21}


def main():
    with open("list.txt", "r") as f:
        multiplier = int(f.readline().split()[1])

        total = 0
        total_amount = 0
        errors = []

        for line in f.readlines():
            if line != "\n":
                try:
                    line = line.strip().split(maxsplit=1)
                    item = line[1].lower()
                    amount = int(line[0])

                    total += pricedict[item] * amount * multiplier
                    total_amount += amount
                except Exception as e:
                    if type(e) == IndexError:
                        e = "Invalid format! Should be <amount> <item>. Empty lines must not contain any spaces."
                    errors.append(f"Error: {e}")
            else:
                continue

        if len(errors) > 0:
            with open("result.txt", "w") as f:
                for error in errors:
                    print(error)
                    f.write(error + "\n")
            input(f"\n{len(errors)} errors detected, press any key to exit.")
            sys.exit()


        print(f"The total price of the {total_amount} items at {multiplier}X max price is: {total} coins.")
        print(f"{total} coins is equal to {round(total / pricedict['diamond ring'], 2)} diamond rings or "
              f"{round(total / pricedict['wooly pants'], 2)} wooly chaps.")
        input("\nPress any key to exit and save the result the in 'result.txt'")

    with open("result.txt", "w") as f:
        f.write(f"The total price of the {total_amount} items at {multiplier} times max price is: {total} coins.")
        f.write(f"\n{total} coins is equal to {round(total / pricedict['diamond ring'], 2)} diamond rings or "
                f"{round(total / pricedict['wooly pants'], 2)} wooly chaps.")


create_files()

if __name__ == "__main__":
    main()
