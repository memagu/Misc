import random

pos_to_name = ['start', 'seville', 'madrid', 'resort_bali', 'hongkong', 'bejing', 'shanghai', 'lost_island', 'venice',
               'milan', 'rome', 'chance_1', 'hamburg', 'resort_cyprus', 'berlin', 'world_championships', 'london', 'resort_dubai',
               'sydney', 'chanse_2', 'chicago', 'las_vegas', 'world_tour', 'resort_nice', 'lyon', 'paris', 'chance_3',
               'osaka', 'tokyo']

visited = dict.fromkeys(pos_to_name, 0)

player_positions = [0, 0, 0, 0]

number_of_rounds = 50

for i in range(number_of_rounds):
    for j in range(len(player_positions)):
        player_position = player_positions[j]
        player_positions[j] = (player_position + random.randint(1, 6) + random.randint(1, 6)) % len(pos_to_name)
        visited[pos_to_name[player_position]] += 1

avrage = 0

for (key, value) in visited.items():
    avrage += value
    print(f"{key}: {value}")

print(f"avrage = {avrage // len(pos_to_name)}")
