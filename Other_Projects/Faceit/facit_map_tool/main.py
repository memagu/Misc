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
        self.root.geometry("1280x480")
        # self.root.resizable(False, False)
        self.FONT = "Monoton 16"
        self.BG = "#1d1d1d"
        self.FG = "#E8E8E8"
        self.pad_amt = 8
        self.border_thickness = 1
        self.root.config(bg=self.BG)

    def run(self):
        def stat_label(frame, text, pos):
            label = tk.Label(frame, text=text, font=self.FONT, background=self.BG, foreground=self.FG)
            label.grid(column=pos[0], row=pos[1], sticky="ew", padx=self.pad_amt / 2)
            label.grid_columnconfigure(0, weight=1)
            label.grid_rowconfigure(0, weight=1)

        def generate_table():
            for widgets in result_frame.winfo_children():
                widgets.destroy()

            # team_0 setup
            team_0_frame = tk.Frame(result_frame, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt,
                                    highlightcolor=self.FG, highlightthickness=self.border_thickness)
            team_0_frame.pack(side=tk.LEFT, anchor="n", expand=True, fill="both")

            team_0_stats_frame = tk.Frame(team_0_frame, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt,
                                          highlightcolor=self.FG, highlightthickness=self.border_thickness)
            team_0_stats_frame.pack(side=tk.BOTTOM, anchor="n", expand=True, fill="both")
            team_0_stats_frame.grid_columnconfigure(0, weight=1, uniform="all")
            team_0_stats_frame.grid_rowconfigure(0, weight=0, uniform="all")

            #team_1 setup
            team_1_frame = tk.Frame(result_frame, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt,
                                    highlightcolor=self.FG, highlightthickness=self.border_thickness)
            team_1_frame.pack(side=tk.RIGHT, anchor="n", expand=True, fill="both")

            team_1_stats_frame = tk.Frame(team_1_frame, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt,
                                          highlightcolor=self.FG, highlightthickness=self.border_thickness)
            team_1_stats_frame.pack(side=tk.BOTTOM, anchor="n", expand=True, fill="both")
            team_1_stats_frame.grid_columnconfigure(0, weight=1, uniform="all")
            team_1_stats_frame.grid_rowconfigure(0, weight=0, uniform="all")

            faceit_match = FaceitGame(url_input_field.get(), Faceit.API_SECRET_KEY)
            data = faceit_match.compile_data()
            levels = len(data.keys())
            team_0 = list(data[list(data.keys())[0]].keys())[0]
            team_1 = list(data[list(data.keys())[0]].keys())[1]

            team_0_label = tk.Label(team_0_frame, text=team_0, font=self.FONT, background=self.BG, foreground=self.FG)
            team_0_label.pack(side=tk.TOP)
            team_1_label = tk.Label(team_1_frame, text=team_1, font=self.FONT, background=self.BG, foreground=self.FG)
            team_1_label.pack(side=tk.TOP)
            stat_label(team_0_stats_frame, "map", [0, 0])
            stat_label(team_0_stats_frame, "win probability", [1, 0])
            stat_label(team_0_stats_frame, "win percentage", [2, 0])
            stat_label(team_0_stats_frame, "matches played", [3, 0])
            stat_label(team_1_stats_frame, "map", [0, 0])
            stat_label(team_1_stats_frame, "win probability", [1, 0])
            stat_label(team_1_stats_frame, "win percentage", [2, 0])
            stat_label(team_1_stats_frame, "matches played", [3, 0])

            for i, (level, teams_stats) in enumerate(data.items()):
                stat_label(team_0_stats_frame, level, [0, i+1])
                stat_label(team_1_stats_frame, level, [0, i+1])
                for team, stat in teams_stats.items():
                    if team == team_0:
                        frame = team_0_stats_frame
                    else:
                        frame = team_1_stats_frame

                    stat_label(frame, f"{round(stat[0]*100, 2)}%", [1, i+1])
                    stat_label(frame, f"{round(stat[1]*100, 2)}%", [2, i+1])
                    stat_label(frame, stat[2], [3, i+1])

        # import operator
        # x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
        # sorted_x = sorted(x.items(), key=operator.itemgetter(1))

        input_frame = tk.Frame(self.root, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt, highlightcolor=self.FG, highlightthickness=self.border_thickness)
        input_frame.pack(side=tk.TOP, anchor="n", fill="x")

        url_input_field = tk.Entry(input_frame, font=self.FONT, bg=self.BG, fg=self.FG, highlightcolor=self.FG, highlightbackground=self.FG, justify=tk.CENTER, insertbackground=self.FG)
        url_input_field.pack(side=tk.LEFT, expand=True, fill="x", padx=self.pad_amt)
        url_input_button = tk.Button(input_frame, text="submit", command=generate_table, font=self.FONT, bg=self.BG, fg=self.FG, highlightcolor=self.FG, highlightbackground=self.FG)
        url_input_button.pack(side=tk.RIGHT, padx=2)

        result_frame = tk.Frame(self.root, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt, highlightcolor=self.FG, highlightthickness=self.border_thickness)
        result_frame.pack(side=tk.BOTTOM, expand=True, fill="both")

        self.root.mainloop()


if __name__ == "__main__":
    app = FaceitMapTool()
    app.run()


