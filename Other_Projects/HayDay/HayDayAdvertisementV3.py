
while True:

    if input("\nBuy or sell?: ") in ["Buy", "buy", "Buying", "buying", "b"]:
        buy = 1
    else:
        buy = -1

    BuyerProvides = input("What should the buyer provide?: ")

    PlayerLevel = input("What is your level?: ")

    Bolts = int(input("How many bolts?: "))
    Planks = int(input("How many planks?: "))
    DuctTapes = int(input("How many rolls of duct tape?: "))
    Nails = int(input("How many nails?: "))
    Screws = int(input("How many screws?: "))
    WoodPanels = int(input("How many wood panels?: "))
    LandDeeds = int(input("How many deeds of land?: "))
    Mallets = int(input("How many mallets?: "))
    MarkerStakes = int(input("How many marker stakes?: "))


    if buy > 0:
        print("\n**BUYING**\n")
    else:
        print("\n**SELLING**\n")

    if Bolts + Planks + DuctTapes > 0:
        print("\n--------BEM:s--------")

    if Bolts> 0:
        print("**" + str(Bolts) + "x:Bolt: 4k each**")

    if Planks > 0:
        print("**" + str(Planks) + "x:Plank: 4k each**")

    if DuctTapes > 0:
        print("**" + str(DuctTapes) + "x:DuctTape: 4k each**")

    if Nails + Screws + WoodPanels > 0:
        print("\n--------SEM:s--------")

    if Nails > 0:
        print("**" + str(Nails) + "x:Nail: 1.5k each**")

    if Screws > 0:
        print("**" + str(Screws) + "x:Screw: 1.5k each**")

    if WoodPanels > 0:
        print("**" + str(WoodPanels) + "x:WoodPanel: 500 each**")

    if LandDeeds + Mallets + MarkerStakes > 0:
        print("\n--------LEM:s--------")

    if LandDeeds > 0:
        print("**" + str(LandDeeds) + "x:LandDeed: 1.5k each**")

    if Mallets > 0:
        print("**" + str(Mallets) + "x:Mallet: 1.5k each**")

    if MarkerStakes > 0:
        print("**" + str(MarkerStakes) + "x:MarkerStake: 1.5k each**")

    print("\n\n**Buyer provides: " + BuyerProvides + " | (lvl. " + PlayerLevel + ") | DM ASAP**")


    if input("\n\nMake another one?: ") in ["No", "no", "n"]:
        break
    else:
        continue
