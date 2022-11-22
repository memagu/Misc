print("Paste PGN sequence and submit by entering a blank line: ")

data_raw = []
while True:
    raw_input = input()
    if not raw_input:
        break

    data_raw += raw_input.split()

result = data_raw.pop()

moves = []
for i in range(0, len(data_raw) - 1, 3):
    white_move = data_raw[i + 1]
    black_move = '' if i + 2 >= len(data_raw) else data_raw[i + 2]
    moves.append((white_move, black_move))

print("Raw data read successfully!\n")

move_counter = {"pawn": ["pawn", 0],
                "B": ["bishop", 0],
                "N": ["knight", 0],
                "R": ["rook", 0],
                "Q": ["queen", 0],
                "K": ["king", 0],
                "0-0-0": ["queen side castle", 0],
                "0-0": ["king side castle", 0]}

round_limit = max(min(int(input(f"Enter maximum amount of rounds to count (20 is set as default if no number is entered): ") or 20), len(moves)), 0)

for round, (white_move, black_move) in enumerate(moves):
    if round == round_limit:
        break

    if white_move == "0-0-0":
        move_counter["0-0-0"][1] += 1
        continue

    if white_move == "0-0":
        move_counter["0-0"][1] += 1
        continue

    if (piece := white_move[0]) in move_counter:
        move_counter[piece][1] += 1
        continue

    move_counter["pawn"][1] += 1

print(f"\nGame result: {result}")
print(f"rounds: {len(moves)}\n")
print(f"Whites first {round_limit} moves:")
print(f"{'piece/action:':<20}{'count:':>10}")
for move, move_count in move_counter.values():
    print(f"{move:<20}{move_count:>10}")

input("\n\nDone! Press ENTER to exit.")
