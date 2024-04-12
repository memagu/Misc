import requests
import tkinter as tk
from table import Table
from FaceitAPI import FaceitAPI
from Other_Projects.my_secrets import Faceit


class FaceitMapTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Faceit Map Tool")
        self.root.geometry("1280x480")
        self.FONT = "Calibri 14"
        self.text_color = "#ffffff"
        self.BG = "#1d1d1d"
        self.FG = "#2d2d2d"
        self.pad_amt = 8
        self.frame_border_thickness = 0
        self.border_thickness = 2
        self.root.config(bg=self.BG)
        self.API = FaceitAPI(Faceit.API_SECRET_KEY)

    def run(self):
        def stat_label(frame, text, pos):
            label = tk.Label(frame, text=text, font=self.FONT, background=self.FG, foreground=self.text_color)
            label.grid(column=pos[0], row=pos[1], sticky="ew", pady=2)
            label.grid_columnconfigure(0, weight=1)
            label.grid_rowconfigure(0, weight=1)

        def stat_button(frame, text, pos):
            button = tk.Button(frame, text=text, command=lambda: render_tables(*generate_tables(text, text)),
                               font=self.FONT, bg=self.FG, fg=self.text_color, highlightcolor=self.FG,
                               highlightthickness=self.border_thickness)
            button.grid(column=pos[0], row=pos[1], sticky="ew", pady=2)
            button.grid_columnconfigure(0, weight=1)
            button.grid_rowconfigure(0, weight=1)

        def parse_url(url: str):
            parts = url.split("/")
            for part in parts:
                if ord(part[0]) in range(48, 58):
                    return part

        def generate_tables(team_0_sort_mode="win probability", team_1_sort_mode="win probability"):
            faceit_match = self.API.get_match(parse_url(url_input_field.get()))
            team_1, team_2 = faceit_match.teams

            team_0_stat_table = Table(["map", "win probability", "win percentage", "matches played"])
            team_0_stat_table.append_row(len(data.keys()))
            for i, (level, teams_stats) in enumerate(data.items()):
                team_0_stat_table.insert_value("map", i, level)
                team_0_stat_table.insert_value("win probability", i, f"{round(teams_stats[team_0][0] * 100, 2)}%")
                team_0_stat_table.insert_value("win percentage", i, f"{round(teams_stats[team_0][1] * 100, 2)}%")
                team_0_stat_table.insert_value("matches played", i, teams_stats[team_0][2])
            team_0_stat_table.sort(team_0_sort_mode, True)

            team_1_stat_table = Table(["map", "win probability", "win percentage", "matches played"])
            team_1_stat_table.append_row(len(data.keys()))
            for i, (level, teams_stats) in enumerate(data.items()):
                team_1_stat_table.insert_value("map", i, level)
                team_1_stat_table.insert_value("win probability", i, f"{round(teams_stats[team_1][0] * 100, 2)}%")
                team_1_stat_table.insert_value("win percentage", i, f"{round(teams_stats[team_1][1] * 100, 2)}%")
                team_1_stat_table.insert_value("matches played", i, teams_stats[team_1][2])
            team_1_stat_table.sort(team_1_sort_mode, True)

            return team_0, team_0_stat_table, team_1, team_1_stat_table

        def render_tables(team_0, team_0_stat_table, team_1, team_1_stat_table):
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

            team_0_label = tk.Label(team_0_frame, text=team_0, font=self.FONT, background=self.FG,
                                    foreground=self.text_color)
            team_0_label.pack(side=tk.TOP)
            team_1_label = tk.Label(team_1_frame, text=team_1, font=self.FONT, background=self.FG,
                                    foreground=self.text_color)
            team_1_label.pack(side=tk.TOP)

            for i, column in enumerate(team_0_stat_table.columns):
                stat_button(team_0_stats_frame, column, [i, 0])

            for i, column in enumerate(team_1_stat_table.columns):
                stat_button(team_1_stats_frame, column, [i, 0])

            for i, row in enumerate(team_0_stat_table.rows):
                for j, value in enumerate(row):
                    stat_label(team_0_stats_frame, value, [j, i + 1])

            for i, row in enumerate(team_1_stat_table.rows):
                for j, value in enumerate(row):
                    stat_label(team_1_stats_frame, value, [j, i + 1])

        input_frame = tk.Frame(self.root, bg=self.BG, padx=self.pad_amt, pady=self.pad_amt, highlightcolor=self.FG,
                               highlightthickness=self.frame_border_thickness)
        input_frame.pack(side=tk.TOP, anchor="n", fill="x")

        url_input_field = tk.Entry(input_frame, font=self.FONT, bg=self.BG, fg=self.text_color, highlightcolor=self.FG,
                                   highlightbackground=self.FG, justify=tk.CENTER, insertbackground=self.text_color,
                                   highlightthickness=self.border_thickness * 4, border=False)
        url_input_field.pack(side=tk.LEFT, expand=True, fill="x", padx=self.pad_amt)
        url_input_button = tk.Button(input_frame, text="submit", command=lambda: render_tables(*generate_tables()),
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
