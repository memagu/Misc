import requests
import curses
from curses.textpad import Textbox, rectangle


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
    data = requests.get(f"https://open.faceit.com/data/v4/players/{player_id}/stats/csgo",
                        headers={f"Authorization": f"Bearer {api_key}"}).json()
    levels = data["segments"]
    level_stats = {}

    for level in levels:
        if level["mode"] == "5v5":
            level_name = level["label"]
            # get %-winrate and amount of games
            level_stats[level_name] = [level["stats"]["Win Rate %"], level["stats"]["Matches"]]
    return level_stats


def compile_data(match_url, api_key):
    teams = get_teams(match_to_api(match_url), api_key)

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
        win_prob = (team1_values[0] / (team1_values[0] + team2_values[0])) * 100

        result.append([win_prob, level, team1_values, team2_values])

    result.sort(key=lambda x: x[0], reverse=True)
    return result, team_keys


API_key = "b3725f7a-6fa3-4517-a08d-a812b807b7f2"
stdscr = curses.initscr()


def draw_result(stdscr):
    input_win = curses.newwin(1, 76, 1, 26)
    box = Textbox(input_win)

    rectangle(stdscr, 0, 0, 2, 102)
    stdscr.addstr(1, 1, "Enter FACEIT match link: ")

    stdscr.refresh()
    box.edit()

    match_url = str(box.gather()).strip()
    data, team_names = compile_data(match_url, API_key)

    curses.curs_set(0)

    # Team headers
    rectangle(stdscr, 3, 0, 5, 59)
    stdscr.addstr(4, 30 - len(f"BEST MAPS FOR: {team_names[0]}") // 2, f"BEST MAPS FOR: {team_names[0]}")
    rectangle(stdscr, 3, 61, 5, 102)
    stdscr.addstr(4, 82 - len(f"MAP STATS FOR: {team_names[1]}") // 2, f"MAP STATS FOR: {team_names[1]}")

    # Headers
    rectangle(stdscr, 6, 0, 8, 16)
    stdscr.addstr(7, 7, "MAP")

    rectangle(stdscr, 6, 18, 8, 26)
    stdscr.addstr(7, 19, "WINRATE")

    rectangle(stdscr, 6, 28, 8, 41)
    stdscr.addstr(7, 29, "GAMES PLAYED")

    rectangle(stdscr, 6, 43, 8, 59)
    stdscr.addstr(7, 44, "WIN PROBABILITY")

    rectangle(stdscr, 6, 61, 8, 69)
    stdscr.addstr(7, 62, "WINRATE")

    rectangle(stdscr, 6, 71, 8, 84)
    stdscr.addstr(7, 72, "GAMES PLAYED")

    rectangle(stdscr, 6, 86, 8, 102)
    stdscr.addstr(7, 87, "WIN PROBABILITY")

    # Containers
    rectangle(stdscr, 9, 0, 20, 16)
    rectangle(stdscr, 9, 18, 20, 26)
    rectangle(stdscr, 9, 28, 20, 41)
    rectangle(stdscr, 9, 43, 20, 59)

    rectangle(stdscr, 9, 61, 20, 69)
    rectangle(stdscr, 9, 71, 20, 84)
    rectangle(stdscr, 9, 86, 20, 102)

    # Content
    for i, level in enumerate(data):
        stdscr.addstr(10 + i, 1, level[1])
        stdscr.addstr(10 + i, 19, str(round(level[2][0], 1)) + "%")
        stdscr.addstr(10 + i, 29, str(level[2][1]))
        stdscr.addstr(10 + i, 44, str(round(level[0], 2)) + "%")

        stdscr.addstr(10 + i, 62, str(round(level[3][0], 1)) + "%")
        stdscr.addstr(10 + i, 72, str(level[3][1]))
        stdscr.addstr(10 + i, 87, str(round(100 - level[0], 2)) + "%")

    stdscr.refresh()

    stdscr.getch()


curses.wrapper(draw_result)
