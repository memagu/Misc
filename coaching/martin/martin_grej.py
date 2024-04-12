def create_chocolate_bar(rader,
                         kolumner):  # definerar en funktion som skapar en chokladbar som består av rader och kolumner
    if rader <= 0 or kolumner <= 0:
        return None
    chocolate_bar = []  # skapar en tom lista för chokladbaren
    for i in range(rader):
        rad = []  # skapar en tom lista för raderna i chokladbaren
        for j in range(kolumner):
            if i == 0 and j == 0:
                rad.append("P ")  # Ersätter block "11" med "P"
            else:
                rad.append(f"{i + 1}{j + 1}")  # lägger in varje block i listan rad
        chocolate_bar.append(rad)  # lägger in listan rad i listan chocolate_bar
    return chocolate_bar  # returnerar chocolate_bar när varje rad har lagts in i listan


def print_chocolate_bar(chocolate_bar):  # skriver ut listan chocolate bar
    for rad in chocolate_bar:
        print(" ".join(rad))


def chomp(chocolate_bar, rad, column):
    for i in range(rad, len(chocolate_bar)):
        for j in range(column, len(chocolate_bar[0])):
            chocolate_bar[i][j] = ""
    return chocolate_bar


def is_game_over(chocolate_bar):
    if chocolate_bar[0][1] == "" and chocolate_bar[1][
        0] == "":  # funktionen avslutar spelet om block 12 och 21 är tomma
        return True
    else:
        return False


def main():
    print("Välkommen till Chomp-spelet")
    while True:  # loopen låter spelaren välja storleken på spelplanen
        try:
            rader = int(input("Hur många rader ska chokladbaren bestå av: "))
            kolumner = int(input("Hur många kolumner ska chokladbaren bestå av: "))

            if 1 < rader < 10 and 1 < kolumner < 10:  # Kontrollera att rad och kolumn är giltig
                break
            print("Antalet rader och kolumner måste vara större än ett och mindre än 10. Försök igen.")

        except ValueError:
            print(
                "Ogiltig inmatning. Ange ett heltal.")  # ser till att endast heltal kan läggas in som rad eller kolumn

    chocolate_bar = create_chocolate_bar(rader, kolumner)

    player = 1
    while not is_game_over(chocolate_bar):  # låter spelarna spela tills endast giftet är kvar på planen
        print_chocolate_bar(chocolate_bar)
        print(f"Spelare {player}'s tur")
        while True:
            try:
                val = int(input("Välj ett blocknummer: "))
                rad = int(val // 10) - 1  # tar ut raden från blocket
                column = int(val % 10) - 1  # tar ur kolumnen från blocket
                if val < 11 or val > rader * 10 + kolumner or chocolate_bar[rad][column] == "" :
                    print("Ogiltigt blocknummer. Försök igen.")
                else:
                    break
            except ValueError:
                print("Ogiltig inmatning. Ange ett heltal.")
        new_chocolate_bar = chomp(chocolate_bar, rad, column)  # skapar en ny spelplan efter att en spelare har "chompat"
        if new_chocolate_bar:
            chocolate_bar = new_chocolate_bar  # gör att spelplanen som används stämmer överens med dne nya
            player = 3 - player

    print_chocolate_bar(chocolate_bar)  # skriver ut den tomma spelplanen
    print(f"Spelet är slut. Spelare {3 - player} vinner!")  # skriver ut vilken spelare som vann


if __name__ == "__main__":
    main()
