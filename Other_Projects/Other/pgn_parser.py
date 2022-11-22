print("Paste PGN sequence and submit by entering a blank line: ")

data_raw = []
while True:
    raw_input = input()
    if not raw_input:
        break

    data_raw += raw_input.split()

result = data_raw.pop()

data = []
for i in range(0, len(data_raw) - 1, 3):
    white_move = data_raw[i + 1]
    black_move = '' if i + 2 >= len(data_raw) else data_raw[i + 2]
    data.append((white_move, black_move))

moves = {"pawn": ["pawn", 0],
         "B": ["bishop", 0],
         "N": ["knight", 0],
         "R": ["rook", 0],
         "Q": ["queen", 0],
         "K": ["king", 0],
         "0-0-0": ["queen side castle", 0],
         "0-0": ["king side castle", 0]}

for white_move, black_move in data:
    if white_move == "0-0-0":
        moves["0-0-0"][1] += 1
        continue

    if white_move == "0-0":
        moves["0-0"][1] += 1
        continue

    if (piece := white_move[0]) in moves:
        moves[piece][1] += 1
        continue

    moves["pawn"][1] += 1

print(f"Game result: {result}")
print(f"rounds: {len(data)}\n")
print(f"{'piece/action:':<20}{'count:':>10}")
for move, move_count in moves.values():
    print(f"{move:<20}{move_count:>10}")

input("\n\nDone! Press ENTER to exit.")
