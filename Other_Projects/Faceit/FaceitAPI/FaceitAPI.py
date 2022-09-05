import requests
from dataclasses import dataclass


class FaceitAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def api_request(self, query):
        return requests.get(f"https://open.faceit.com/data/v4/{query}",
                            headers={f"Authorization": f"Bearer {self.api_key}"}).json()

    def get_match(self, match_id):
        data = self.api_request(f"matches/{match_id}")
        print(data)
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


@dataclass(frozen=True)
class Player:
    player_id: str
    nickname: str
    avatar: str
    country: str
    cover_image: str
    platforms: str
    games: dict
    settings: dict
    friends_ids: list
    new_steam_id: str
    steam_id_64: str
    steam_nickname: str
    memberships: list
    faceit_url: str
    membership_type: str
    cover_featured_image: str
    infractions: dict

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


@dataclass(frozen=True)
class Team:
    team_id: str
    leader: str
    avatar: str
    roster: list[Player]
    substituted: bool
    name: str
    type: str

    def __str__(self):
        return f"Team({[str(player) for player in self.roster]})"


@dataclass(frozen=True)
class Match:
    match_id: str
    version: float
    game: str
    region: str
    competition_id:  str
    competition_type: str
    competition_name: str
    organizer_id: str
    teams: list[Team]
    voting: dict
    calculate_elo: bool
    configured_at: float
    finished_at: int
    demo_url: int
    chat_room_id: str
    best_of: int
    results: dict
    status: str
    faceit_url: str

    def __str__(self):
        return f"Match({' vs '.join([team.name for team in self.teams])})"


@dataclass(frozen=True)
class MapStatistics:
    stat_type: str
    mode: str
    label: str
    kr_ratio: float
    avrage_mvps: float
    avrage_penta_kills: float
    avrage_kills: float
    mvps: float
    avrage_quadro_kills: float
    deaths: float
    headshots: float
    quadro_kills: float
    avrage_kd_ratio: float
    avrage_headshots_percentage: float
    penta_kills: float
    wins: float
    total_headshots: float
    rounds: float
    win_rate_percentage: float
    avrage_assists: float
    avrage_kr_ratio: float
    tripple_kills: float
    assists: float
    avrage_tripple_kills: float
    avrage_deaths: float
    kd_ratio: float
    matches: float
    kills: float
    headshots_per_match: float


@dataclass(frozen=True)
class PlayerStatistics:
    player_id: str
    game_id: str
    current_win_streak: float
    recent_results: list
    lifetime_longest_win_streak: float
    lifetime_win_rate_percentage: float
    lifetime_avrage_kd_ratio: float
    lifetime_wins: float
    lifetime_total_headshots: float
    lifetime_kd_ratio: float
    lifetime_matches: float
    lifetime_avrage_headshots_percentage: float
    map_statistics: list[MapStatistics]


if __name__ == "__main__":
    from Other_Projects.my_secrets import Faceit

    API = FaceitAPI(Faceit.API_SECRET_KEY)
    match = API.get_match("1-31646cb4-d305-48d7-acc4-38a88f8d3a4f")
    print(match.teams[0].roster[1].avatar)
