import requests


class FaceitAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def api_request(self, query):
        return requests.get(f"https://open.faceit.com/data/v4/{query}",
                            headers={f"Authorization": f"Bearer {self.api_key}"}).json()

    def get_match(self, match_id):
        data = self.api_request(f"matches/{match_id}")
        team1 = Team(data["teams"]["faction1"]["faction_id"],
                     data["teams"]["faction1"]["leader"],
                     data["teams"]["faction1"]["avatar"],
                     [self.get_player(player["player_id"]) for player in data["teams"]["faction1"]["roster"]],
                     data["teams"]["faction1"]["substituted"],
                     data["teams"]["faction1"]["name"],
                     data["teams"]["faction1"]["type"])

        team2 = Team(data["teams"]["faction2"]["faction_id"],
                     data["teams"]["faction2"]["leader"],
                     data["teams"]["faction2"]["avatar"],
                     [self.get_player(player["player_id"]) for player in data["teams"]["faction2"]["roster"]],
                     data["teams"]["faction2"]["substituted"],
                     data["teams"]["faction2"]["name"],
                     data["teams"]["faction2"]["type"])

        return Match(data["match_id"],
                     data["version"],
                     data["game"],
                     data["region"],
                     data["competition_id"],
                     data["competition_type"],
                     data["competition_name"],
                     data["organizer_id"],
                     [team1, team2],
                     data["voting"],
                     data["calculate_elo"],
                     data["configured_at"],
                     data["finished_at"],
                     data["demo_url"],
                     data["chat_room_id"],
                     data["best_of"],
                     data["results"],
                     data["status"],
                     data["faceit_url"])

    def get_player(self, player_id):
        data = self.api_request(f"players/{player_id}")
        return Player(data["player_id"],
                      data["nickname"],
                      data["avatar"],
                      data["country"],
                      data["cover_image"],
                      data["platforms"],
                      data["games"],
                      data["settings"],
                      data["friends_ids"],
                      data["new_steam_id"],
                      data["steam_id_64"],
                      data["steam_nickname"],
                      data["memberships"],
                      data["faceit_url"],
                      data["membership_type"],
                      data["cover_featured_image"],
                      data["infractions"])


class Match:
    def __init__(self, match_id, version, game, region, competition_id, competition_type, competition_name,
                 organizer_id, teams, voting, calculate_elo, configured_at, finished_at, demo_url, chat_room_id,
                 best_of,
                 results, status, faceit_url):
        self.match_id = match_id
        self.version = version
        self.game = game
        self.region = region
        self.competition_id = competition_id
        self.competition_type = competition_type
        self.competition_name = competition_name
        self.organizer_id = organizer_id
        self.teams = teams
        self.voting = voting
        self.calculate_elo = calculate_elo
        self.configured_at = configured_at
        self.finished_at = finished_at
        self.demo_url = demo_url
        self.chat_room_id = chat_room_id
        self.best_of = best_of
        self.results = results
        self.status = status
        self.faceit_url = faceit_url

    def __str__(self):
        return f"Match({self.teams[0].nickname} vs {self.teams[1].nickname})"


class Team:
    def __init__(self, team_id, leader, avatar, roster, substituted, name, team_type):
        self.team_id = team_id
        self.leader = leader
        self.avatar = avatar
        self.roster = roster
        self.substituted = substituted
        self.name = name
        self.type = team_type

    def __str__(self):
        return f"Team({[str(player) for player in self.roster]})"


class Player:
    def __init__(self, player_id, nickname, avatar, country, cover_image, platforms, games, settings, friends_ids,
                 new_steam_id, steam_id_64, steam_nickname, memberships, faceit_url, membership_type,
                 cover_featured_image, infractions):
        self.player_id = player_id
        self.nickname = nickname
        self.avatar = avatar
        self.country = country
        self.cover_image = cover_image
        self.platforms = platforms
        self.games = games
        self.settings = settings
        self.friends_ids = friends_ids
        self.new_steam_id = new_steam_id
        self.steam_id_64 = steam_id_64
        self.steam_nickname = steam_nickname
        self.memberships = memberships
        self.faceit_url = faceit_url
        self.membership_type = membership_type
        self.cover_featured_image = cover_featured_image
        self.infractions = infractions

    def __str__(self):
        return f"Player({self.nickname}, {self.player_id})"

    def get_matches(self, limit=20):
        data = API.api_request(f"players/{self.player_id}/history?game=csgo&offset=0&limit={limit}")
        return [API.get_match(match["match_id"]) for match in data["items"]]

    def get_stats(self):
        data = API.api_request(f"players/{self.player_id}/stats/csgo")
        map_statistics = [MapStatistics(statdata["type"],
                                        statdata["mode"],
                                        statdata["label"],
                                        float(statdata["stats"]["K/R Ratio"]),
                                        float(statdata["stats"]["Average MVPs"]),
                                        float(statdata["stats"]["Average Penta Kills"]),
                                        float(statdata["stats"]["Average Kills"]),
                                        float(statdata["stats"]["MVPs"]),
                                        float(statdata["stats"]["Average Quadro Kills"]),
                                        float(statdata["stats"]["Deaths"]),
                                        float(statdata["stats"]["Headshots"]),
                                        float(statdata["stats"]["Quadro Kills"]),
                                        float(statdata["stats"]["Average K/D Ratio"]),
                                        float(statdata["stats"]["Average Headshots %"]),
                                        float(statdata["stats"]["Penta Kills"]),
                                        float(statdata["stats"]["Wins"]),
                                        float(statdata["stats"]["Total Headshots %"]),
                                        float(statdata["stats"]["Rounds"]),
                                        float(statdata["stats"]["Win Rate %"]),
                                        float(statdata["stats"]["Average Assists"]),
                                        float(statdata["stats"]["Average K/R Ratio"]),
                                        float(statdata["stats"]["Triple Kills"]),
                                        float(statdata["stats"]["Assists"]),
                                        float(statdata["stats"]["Average Triple Kills"]),
                                        float(statdata["stats"]["Average Deaths"]),
                                        float(statdata["stats"]["K/D Ratio"]),
                                        float(statdata["stats"]["Matches"]),
                                        float(statdata["stats"]["Kills"]),
                                        float(statdata["stats"]["Headshots per Match"]))
                          for statdata in data["segments"]]

        return PlayerStatistics(data["player_id"],
                                data["game_id"],
                                float(data["lifetime"]["Current Win Streak"]),
                                data["lifetime"]["Recent Results"],
                                float(data["lifetime"]["Longest Win Streak"]),
                                float(data["lifetime"]["Win Rate %"]),
                                float(data["lifetime"]["Average K/D Ratio"]),
                                float(data["lifetime"]["Wins"]),
                                float(data["lifetime"]["Total Headshots %"]),
                                float(data["lifetime"]["K/D Ratio"]),
                                float(data["lifetime"]["Matches"]),
                                float(data["lifetime"]["Average Headshots %"]),
                                map_statistics)


class PlayerStatistics:
    def __init__(self, player_id, game_id, current_win_streak, recent_results, lifetime_longest_win_streak,
                 lifetime_win_rate_percentage, lifetime_avrage_kd_ratio, lifetime_wins, lifetime_total_headshots,
                 lifetime_kd_ratio, lifetime_matches, lifetime_avrage_headshots_percentage, map_statistics):
        self.player_id = player_id
        self.game_id = game_id
        self.current_win_streak = current_win_streak
        self.recent_results = recent_results
        self.lifetime_longest_win_streak = lifetime_longest_win_streak
        self.lifetime_win_rate_percentage = lifetime_win_rate_percentage
        self.lifetime_avrage_kd_ratio = lifetime_avrage_kd_ratio
        self.lifetime_wins = lifetime_wins
        self.lifetime_total_headshots = lifetime_total_headshots
        self.lifetime_kd_ratio = lifetime_kd_ratio
        self.lifetime_matches = lifetime_matches
        self.lifetime_avrage_headshots_percentage = lifetime_avrage_headshots_percentage
        self.map_statistics = map_statistics


class MapStatistics:
    def __init__(self, stat_type, mode, label, kr_ratio, avrage_mvps, avrage_penta_kills, avrage_kills, mvps,
                 avrage_quadro_kills, deaths, headshots, quadro_kills, avrage_kd_ratio, avrage_headshots_percentage,
                 penta_kills, wins,
                 total_headshots, rounds, win_rate_percentage, avrage_assists, avrage_kr_ratio, tripple_kills,
                 assists, avrage_tripple_kills, avrage_deaths, kd_ratio, matches, kills, headshots_per_match):
        self.stat_type = stat_type
        self.mode = mode
        self.label = label
        self.kr_ratio = kr_ratio
        self.avrage_mvps = avrage_mvps
        self.avrage_penta_kills = avrage_penta_kills
        self.avrage_kills = avrage_kills
        self.mvps = mvps
        self.avrage_quadro_kills = avrage_quadro_kills
        self.deaths = deaths
        self.headshots = headshots
        self.quadro_kills = quadro_kills
        self.avrage_kd_ratio = avrage_kd_ratio
        self.avrage_headshots_percentage = avrage_headshots_percentage
        self.penta_kills = penta_kills
        self.wins = wins
        self.total_headshots = total_headshots
        self.rounds = rounds
        self.win_rate_percentage = win_rate_percentage
        self.avrage_assists = avrage_assists
        self.avrage_kr_ratio = avrage_kr_ratio
        self.tripple_kills = tripple_kills
        self.assists = assists
        self.avrage_tripple_kills = avrage_tripple_kills
        self.avrage_deaths = avrage_deaths
        self.kd_ratio = kd_ratio
        self.matches = matches
        self.kills = kills
        self.headshots_per_match = headshots_per_match


if __name__ == "__main__":
    from Other_Projects.my_secrets import Faceit

    API = FaceitAPI(Faceit.API_SECRET_KEY)
    match = API.get_match("1-67dd18ae-0781-46f7-9201-6d1b7b24d946")
    team1 = match.teams[0]
    team2 = match.teams[1]
    player11 = team1.roster[0]
    player21 = team2.roster[0]
    memagu = team2.roster[4]

    print(player11)
    print(player21)
    print(memagu)

    memagu_stats = memagu.get_stats()

    for mapstat, value in memagu_stats.map_statistics[0].__dict__.items():
        print(mapstat, value, sep=": ")

    # with open("match.json", "w") as m:
    #     m.write(str(API.api_request(f"matches/{match.match_id}")))
    #
    # with open("team.json", "w") as t:
    #     t.write(str(API.api_request(f"teams/{team.team_id}")))
    #
    # with open("player.json", "w") as p:
    #     p.write(str(API.api_request(f"players/{player.player_id}")))
