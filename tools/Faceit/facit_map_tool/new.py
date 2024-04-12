import requests
import tkinter as tk
from table import Table
from Other_Projects.my_secrets import Faceit


class FaceitGrabber:
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
        # self.root.geometry("1280x480")
        # self.root.resizable(False, False)
        self.FONT = "Calibri 14"
        self.text_color = "#ffffff"
        self.BG = "#1d1d1d"
        self.FG = "#2d2d2d"
        self.pad_amt = 8
        self.frame_border_thickness = 0
        self.border_thickness = 2
        self.root.config(bg=self.BG)
        self.team_0 = None
        self.team_0_stat_table = None
        self.team_1 = None
        self.team_1_stat_table = None

    def run(self):
        def stat_label(frame, text, pos):
            label = tk.Label(frame, text=text, font=self.FONT, background=self.FG, foreground=self.text_color)
            label.grid(column=pos[0], row=pos[1], sticky="ew", pady=2)
            label.grid_columnconfigure(0, weight=1)
            label.grid_rowconfigure(0, weight=1)

        def stat_button(frame, text, pos, table):
            button = tk.Button(frame, text=text, command=lambda: [table.sort(text, True), render_tables()],
                               font=self.FONT, bg=self.FG, fg=self.text_color, highlightcolor=self.FG,
                               highlightthickness=self.border_thickness)

            button.grid(column=pos[0], row=pos[1], sticky="ew", pady=2)
            button.grid_columnconfigure(0, weight=1)
            button.grid_rowconfigure(0, weight=1)

        def generate_tables():
            faceit_match = FaceitGrabber(url_input_field.get(), Faceit.API_SECRET_KEY)
            data = faceit_match.compile_data()
            teams = list(data[list(data.keys())[0]].keys())
            self.team_0 = teams[0]
            self.team_1 = teams[1]

            self.team_0_stat_table = Table(["Map", "Win Probability", "Win Percentage", "Matches Played"])
            self.team_0_stat_table.append_row(len(data.keys()))
            for i, (level, teams_stats) in enumerate(data.items()):
                self.team_0_stat_table.insert_value("Map", i, level)
                self.team_0_stat_table.insert_value("Win Probability", i, f"{round(teams_stats[self.team_0][0] * 100, 2)}%")
                self.team_0_stat_table.insert_value("Win Percentage", i, f"{round(teams_stats[self.team_0][1] * 100, 2)}%")
                self.team_0_stat_table.insert_value("Matches Played", i, teams_stats[self.team_0][2])
            self.team_0_stat_table.sort("Win Probability", True)

            self.team_1_stat_table = Table(["Map", "Win Probability", "Win Percentage", "Matches Played"])
            self.team_1_stat_table.append_row(len(data.keys()))
            for i, (level, teams_stats) in enumerate(data.items()):
                self.team_1_stat_table.insert_value("Map", i, level)
                self.team_1_stat_table.insert_value("Win Probability", i, f"{round(teams_stats[self.team_1][0] * 100, 2)}%")
                self.team_1_stat_table.insert_value("Win Percentage", i, f"{round(teams_stats[self.team_1][1] * 100, 2)}%")
                self.team_1_stat_table.insert_value("Matches Played", i, teams_stats[self.team_1][2])
            self.team_1_stat_table.sort("Win Probability", True)

        def render_tables():
            for widgets in result_frame.winfo_children():
                widgets.destroy()

            # team_0 setup
            team_0_frame = tk.Frame(result_frame, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt,
                                    highlightcolor=self.FG, highlightthickness=self.frame_border_thickness)
            team_0_frame.pack(side=tk.LEFT, anchor="n", expand=True, fill="both")

            team_0_stats_frame = tk.Frame(team_0_frame, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt,
                                          highlightcolor=self.FG, highlightthickness=self.frame_border_thickness)
            team_0_stats_frame.pack(side=tk.BOTTOM, anchor="n", expand=True, fill="both")
            team_0_stats_frame.grid_columnconfigure(0, weight=1, uniform="all")
            team_0_stats_frame.grid_rowconfigure(0, weight=0, uniform="all")

            # team_1 setup
            team_1_frame = tk.Frame(result_frame, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt,
                                    highlightcolor=self.FG, highlightthickness=self.frame_border_thickness)
            team_1_frame.pack(side=tk.RIGHT, anchor="n", expand=True, fill="both")

            team_1_stats_frame = tk.Frame(team_1_frame, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt,
                                          highlightcolor=self.FG, highlightthickness=self.frame_border_thickness)
            team_1_stats_frame.pack(side=tk.BOTTOM, anchor="n", expand=True, fill="both")
            team_1_stats_frame.grid_columnconfigure(0, weight=1, uniform="all")
            team_1_stats_frame.grid_rowconfigure(0, weight=0, uniform="all")

            team_0_label = tk.Label(team_0_frame, text=self.team_0, font=self.FONT, background=self.FG,
                                    foreground=self.text_color)
            team_0_label.pack(side=tk.TOP)
            team_1_label = tk.Label(team_1_frame, text=self.team_1, font=self.FONT, background=self.FG,
                                    foreground=self.text_color)
            team_1_label.pack(side=tk.TOP)

            for i, column in enumerate(self.team_0_stat_table.columns):
                stat_button(team_0_stats_frame, column, [i, 0], self.team_0_stat_table)

            for i, column in enumerate(self.team_1_stat_table.columns):
                stat_button(team_1_stats_frame, column, [i, 0], self.team_1_stat_table)

            for i, row in enumerate(self.team_0_stat_table.rows):
                for j, value in enumerate(row):
                    stat_label(team_0_stats_frame, value, [j, i + 1])

            for i, row in enumerate(self.team_1_stat_table.rows):
                for j, value in enumerate(row):
                    stat_label(team_1_stats_frame, value, [j, i + 1])

        input_frame = tk.Frame(self.root, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt, highlightcolor=self.FG,
                               highlightthickness=self.frame_border_thickness)
        input_frame.pack(side=tk.TOP, anchor="n", fill="x")

        url_input_field = tk.Entry(input_frame, font=self.FONT, bg=self.BG, fg=self.text_color, highlightcolor=self.FG,
                                   highlightbackground=self.FG, justify=tk.CENTER, insertbackground=self.text_color,
                                   highlightthickness=self.border_thickness * 4, border=False)
        url_input_field.pack(side=tk.LEFT, expand=True, fill="x", padx=self.pad_amt)
        url_input_button = tk.Button(input_frame, text="submit", command=lambda: [generate_tables(), render_tables()],
                                     font=self.FONT, bg=self.FG, fg=self.text_color, highlightcolor=self.FG,
                                     highlightthickness=self.border_thickness)
        url_input_button.pack(side=tk.RIGHT, padx=2)

        result_frame = tk.Frame(self.root, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt, highlightcolor=self.FG,
                                highlightthickness=self.frame_border_thickness)
        result_frame.pack(side=tk.BOTTOM, expand=True, fill="both")

        self.root.mainloop()


if __name__ == "__main__":
    app = FaceitMapTool()
    app.run()
