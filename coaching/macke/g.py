# print("Hello")
#
# while True:
#     option = input("go left or right?")
#
#     if option not in ("left", "right"):
#         print("Invalid input, try again.")
#         continue
#
#     if option == "left":
#         print("You went left")
#
#     if option == "left":
#         print("You went right")

a = ["a", "b", "c"]
#     0    1    2

liv = 4

game_graph = {
    "0": ["1", "2"],
    "1": ["0", "3", "4"],
    "2": ["4", "5"],
    "5": ["6", "7"]
}

position = "0"

# Game loop
while True:
    connected_locations = game_graph[position]

    print("choose an alternative: ", connected_locations)

    # Make sure a choise is valid
    while True:
        choise = input("Input choise: ")
        if choise in connected_locations:
            break
        print("Invalid choise, try agian!")

    position = choise
