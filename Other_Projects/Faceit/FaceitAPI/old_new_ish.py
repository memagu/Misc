
import requests


class FaceitAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def api_request(self, query):
        return requests.get(f"https://open.faceit.com/data/v4/{query}",
                            headers={f"Authorization": f"Bearer {self.api_key}"}).json()

    def get_match(self, match_id):
        data = self.api_request(f"matches/{match_id}")
        team1 = self.get_team(data["teams"]["faction1"]["faction_id"])
        team2 = self.get_team(data["teams"]["faction2"]["faction_id"])

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

    def get_team(self, team_id):
        data = self.api_request(f"teams/{team_id}")
        print(data)
        return Team(data["avatar"],
                    data["chat_room_id"],
                    data["cover_image"],
                    data["description"],
                    data["facebook"],
                    data["faceit_url"],
                    data["game"],
                    data["leader"],
                    [self.get_player(user["user_id"]) for user in data["members"]],
                    data["name"],
                    data["nickname"],
                    data["team_id"],
                    data["team_type"],
                    data["twitter"],
                    data["website"],
                    data["youtube"])

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
                 organizer_id, teams, voting, calculate_elo, configured_at, finished_at, demo_url, chat_room_id, best_of,
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
    def __init__(self, avatar, chat_room_id, cover_image, description, facebook, faceit_url, game, leader, members,
                 name, nickname, team_id, team_type, twitter, website, youtube):
        self.avatar = avatar
        self.chat_room_id = chat_room_id
        self.cover_image = cover_image
        self.description = description
        self.facebook = facebook
        self.faceit_url = faceit_url
        self.game = game
        self.leader = leader
        self.members = members
        self.name = name
        self.nickname = nickname
        self.team_id = team_id
        self.team_type = team_type
        self.twitter = twitter
        self.website = website
        self.youtube = youtube


    def __str__(self):
        return f"Team({[str(player) for player in self.members]})"


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
        return f"Player({self.nickname})"

    def get_matches(self, limit=20):
        data = API.api_request(f"players/{self.player_id}/history?game=csgo&offset=0&limit={limit}")
        return [API.get_match(match["match_id"]) for match in data["items"]]


if __name__ == "__main__":
    from Other_Projects.my_secrets import Faceit

    API = FaceitAPI(Faceit.API_SECRET_KEY)
    # match = API.get_match("1-7510a7c7-11f1-4ffd-8a5c-7b90c70e9858")
    # team = match.teams[0]
    # player = team.members[0]

    print(API.get_team("a7bc4140-e18d-4628-8bbf-998a9aabff9d"))

    # with open("match.json", "w") as m:
    #     m.write(str(API.api_request(f"matches/{match.match_id}")))
    #
    # with open("team.json", "w") as t:
    #     t.write(str(API.api_request(f"teams/{team.team_id}")))
    #
    # with open("player.json", "w") as p:
    #     p.write(str(API.api_request(f"players/{player.player_id}")))

