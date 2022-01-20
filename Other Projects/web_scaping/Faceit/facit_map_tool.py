import requests
import copy


def match_to_api(match_url):
    return "https://open.faceit.com/data/v4/matches/" + match_url[36:]


def get_teams(api_url, api_key):
    data = requests.get(api_url, headers={f"Authorization": f"Bearer {api_key}"}).json()
    teams = data["teams"]

    result = {}

    for team_key in teams:
        team = teams[team_key]
        roster = team["roster"]
        team_name = team["name"]
        result[team_name] = []

        for player in roster:
            result[team_name].append(player["player_id"])

    return result


def get_level_stats(player_id, api_key):
    data = requests.get(f"https://open.faceit.com/data/v4/players/{player_id}/stats/csgo", headers={f"Authorization": f"Bearer {api_key}"}).json()
    levels = data["segments"]
    level_stats = {}

    for level in levels:
        if level["mode"] == "5v5":
            level_name = level["label"]
            # get %-winrate and amount of games
            level_stats[level_name] = [level["stats"]["Win Rate %"], level["stats"]["Matches"]]
    return level_stats


API_key = "b3725f7a-6fa3-4517-a08d-a812b807b7f2"
#match_url = "https://www.faceit.com/en/csgo/room/1-cccbc7ec-ddfc-48e6-986b-1ed8b8f41559"
match_url = input("Input match URL: ")

teams = get_teams(match_to_api(match_url), API_key)

team_stats = {}

for team in teams:
    team_stats[team] = {}
    players = teams[team]

    for player in players:
        stats = get_level_stats(player, API_key)

        for level in stats:
            try:
                if team_stats[team][level]:
                    pass
            except KeyError:
                team_stats[team][level] = [0, 0]

            win_rate = int(stats[level][0])
            games_played = int(stats[level][1])

            team_stats[team][level][0] += win_rate / 5
            team_stats[team][level][1] += games_played


result = []

team_keys = list(team_stats.keys())
for level in team_stats[team_keys[0]]:
    if level not in dict.keys(team_stats[team_keys[1]]):
        continue
    team1_values = team_stats[team_keys[0]][level]
    team2_values = team_stats[team_keys[1]][level]

    result.append([team1_values[0] / team2_values[0], level, team1_values, team2_values])

result.sort(key=lambda x: x[0], reverse=True)

print("|----------------------------------------------------------|------------------------------------------|")
print("|\t\t\t  BEST MAPS FOR " + team_keys[0] + ("\t" * (6 - (len(team_keys[1])-5) // 4)) + "   |\t\t\tSTATS FOR " + team_keys[1] + ("\t" * (3 - (len(team_keys[1])-5) // 4)) + "  |")
print("|----------------------------------------------------------|------------------------------------------|")
print("|\t   MAP\t\t| WINRATE | GAMES PLAYED | WIN PROBABILITY | WINRATE | GAMES PLAYED | WIN PROBABILITY |")
for level in result:
    t1 = "| " + level[1] + ("\t" if len(level[1]) > 9 else "\t\t") + "|  " + str(round(level[2][0], 1)) + "%  |\t   " + str(level[2][1]) + "\t\t |\t  " + str(round((level[0] - 0.5) * 100, 2)) + "% \t   "
    t2 = "|  " + str(round(level[3][0], 1)) + "%  |\t   " + str(level[3][1]) + "\t\t|\t  " + str(round((1-(level[0] - 0.5)) * 100, 2)) + "% \t  |"
    print(t1 + t2)
print("|----------------------------------------------------------|------------------------------------------|")
_ = input()
