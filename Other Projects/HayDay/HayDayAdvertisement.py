
while True:


    if input("\nBuy or sell?: ") in ["Buy", "buy", "Buying", "buying", "b"]:
        buy = 1
    else:
        buy = -1


    BuyerProvides = input("What should the buyer provide?: ")

    PlayerLevel = input("What is your level?: ")


    Bolts = input("How many bolts?: ")
    Planks = input("How many planks?: ")
    DuctTapes = input("How many rolls of duct tape?: ")
    Nails = input("How many nails?: ")
    Screws = input("How many screws?: ")
    WoodPanels = input("How many wood panels?: ")
    LandDeeds = input("How many deeds of land?: ")
    Mallets = input("How many mallets?: ")
    MarkerStakes = input("How many marker stakes?: ")


    if buy <= 0:
        print("\n**BUYING**\n\n--------BEM:s--------")
    else:
        print("\n**SELLING**\n\n--------BEM:s--------")


    print("**" + Bolts + "x:Bolt: 4k each**")
    print("**" + Planks + "x:Plank: 4k each**")
    print("**" + DuctTapes + "x:DuctTape: 4k each**")

    print("\n--------SEM:s--------")

    print("**" + Nails + "x:Nail: 1.5k each**")
    print("**" + Screws + "x:Screw: 1.5k each**")
    print("**" + WoodPanels + "x:WoodPanel: 500 each**")

    print("\n--------LEM:s--------")

    print("**" + LandDeeds + "x:LandDeed: 1.5k each**")
    print("**" + Mallets + "x:Mallet: 1.5k each**")
    print("**" + MarkerStakes + "x:MarkerStake: 1.5k each**")


    print("\n**Buyer provides: " + BuyerProvides + " | (lvl. " + PlayerLevel + ") | DM ASAP**")


    if input("\nMake another one?: ") in ["No", "no", "n"]:
        break
    else:
        continue
