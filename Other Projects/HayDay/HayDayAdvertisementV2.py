
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

    B = int(Bolts)
    P = int(Planks)
    DT = int(DuctTapes)
    N = int(Nails)
    S = int(Screws)
    WP = int(WoodPanels)
    LD = int(LandDeeds)
    M = int(Mallets)
    MS = int(MarkerStakes)

    if buy > 0:
        print("\n**BUYING**\n")
    else:
        print("\n**SELLING**\n")

    if B + P + DT > 0:
        print("\n--------BEM:s--------")

    if B > 0:
        print("**" + Bolts + "x:Bolt: 4k each**")

    if P > 0:
        print("**" + Planks + "x:Plank: 4k each**")

    if DT > 0:
        print("**" + DuctTapes + "x:DuctTape: 4k each**")

    if N + S + WP > 0:
        print("\n--------SEM:s--------")

    if N > 0:
        print("**" + Nails + "x:Nail: 1.5k each**")

    if S > 0:
        print("**" + Screws + "x:Screw: 1.5k each**")

    if WP > 0:
        print("**" + WoodPanels + "x:WoodPanel: 500 each**")

    if LD + M + MS > 0:
        print("\n--------LEM:s--------")

    if LD > 0:
        print("**" + LandDeeds + "x:LandDeed: 1.5k each**")

    if M > 0:
        print("**" + Mallets + "x:Mallet: 1.5k each**")

    if MS > 0:
        print("**" + MarkerStakes + "x:MarkerStake: 1.5k each**")

    print("\n\n**Buyer provides: " + BuyerProvides + " | (lvl. " + PlayerLevel + ") | DM ASAP**")


    if input("\n\nMake another one?: ") in ["No", "no", "n"]:
        break
    else:
        continue
