import requests
import tkinter as tk
from Other_Projects.my_secrets import Faceit


class FaceitGame:
    def __init__(self, game_url, api_key):
        self.game_url = game_url
        self.api_key = api_key
        self.api_url = "https://open.faceit.com/data/v4/matches/" + self.game_url.split("/")[-1]

    def get_teams(self):
        data = requests.get(self.api_url, headers={f"Authorization": f"Bearer {self.api_key}"}).json()
        teams = data["teams"]

        result = {}

        for team in teams.values():
            team_name = team["name"]
            result[team_name] = []

            for player in team["roster"]:
                result[team_name].append(player["player_id"])
        return result

    def player_level_stats(self, player_id):
        data = requests.get(f"https://open.faceit.com/data/v4/players/{player_id}/stats/csgo",
                            headers={f"Authorization": f"Bearer {self.api_key}"}).json()
        levels = data["segments"]
        level_stats = {}

        for level in levels:
            if level["mode"] == "5v5":
                level_name = level["label"]
                stats = level["stats"]
                level_stats[level_name] = [stats["Win Rate %"], stats["Matches"]]
        return level_stats

    def team_level_stats(self):
        teams = self.get_teams()

        team_stats = {}

        for team in teams:
            team_stats[team] = {}
            player_ids = teams[team]

            for player_id in player_ids:
                level_stats = self.player_level_stats(player_id)

                for level in level_stats:
                    if level not in team_stats[team]:
                        team_stats[team][level] = [0, 0]

                    win_percentage, played_matches = map(int, level_stats[level])

                    team_stats[team][level][0] += win_percentage / 500
                    team_stats[team][level][1] += played_matches

        return team_stats

    def compile_data(self):
        team_stats = self.team_level_stats()
        team_0, team_1 = team_stats.keys()

        result = {}

        for level in team_stats[team_0]:
            if level not in team_stats[team_1]:
                continue

        # win_probability = (team1_values[0] / (team1_values[0] + team2_values[0])) * 100
            team_0_win_percentage = team_stats[team_0][level][0]
            team_0_played_matches = team_stats[team_0][level][1]
            team_1_win_percentage = team_stats[team_1][level][0]
            team_1_played_matches = team_stats[team_1][level][1]

            team_0_win_probability = team_0_win_percentage / (team_0_win_percentage + team_1_win_percentage)
            team_1_win_probability = 1 - team_0_win_probability

            result[level] = {team_0: [team_0_win_probability, team_0_win_percentage, team_0_played_matches],
                             team_1: [team_1_win_probability, team_1_win_percentage, team_1_played_matches]}

        return result


class FaceitMapTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Faceit Map Tool")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.FONT = "Monoton 12"
        self.BG = "#1d1d1d"
        self.FG = "#E8E8E8"
        self.pad_amt = 8
        self.root.config(bg=self.BG)

    def run(self):
        input_frame = tk.Frame(self.root, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt)
        input_frame.pack(side=tk.TOP, anchor="nw", expand=True, fill="x")
        result_frame = tk.Frame(self.root, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt)
        result_frame.pack(side=tk.BOTTOM)


        url_input_field = tk.Entry(input_frame, font=self.FONT, bg=self.BG, fg=self.FG, highlightcolor=self.FG, highlightbackground=self.FG, justify=tk.CENTER, insertbackground=self.FG)
        url_input_button = tk.Button(input_frame, text="submit", font=self.FONT, bg=self.BG, fg=self.FG, highlightcolor=self.FG, highlightbackground=self.FG)
        url_input_field.pack(side=tk.LEFT, expand=True, fill="x", padx=2)
        url_input_button.pack(side=tk.RIGHT, padx=2)


        self.root.mainloop()


if __name__ == "__main__":
    app = FaceitMapTool()
    app.run()

# # url = "https://www.faceit.com/en/csgo/room/1-0b733a04-ae80-40dd-a281-fa8ad987aa37"
# url = "https://www.faceit.com/en/csgo/room/1-e4d30a6a-b26b-45ff-8f9d-fda277729781"
# match = FaceitGame(url, Faceit.API_SECRET_KEY)
#
# # print(match.team_level_stats())
# print(match.compile_data())


