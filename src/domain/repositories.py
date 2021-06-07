from abc import ABC, abstractmethod


class Match:

    def __init__(self, platformId: str, gameid: str, champion: int, queue: int,
                 season: int, timestamp: str, role: str, lane: str,
                 gamemode: str, gametype: str, teamid: int, win: str):
        self.platformid = platformId
        self.gameid = gameid
        self.champion = champion
        self.queue = queue
        self.season = season
        self.timestamp = timestamp
        self.role = role
        self.lane = lane
        self.gamemode = gamemode
        self.gametype = gametype
        self.teamid = teamid
        self.win = win


class TeamStatus:
    def __init__(self, teamId, win, firstBlood, firstTower, firstInhibitor,
                 firstBaron, firstDragon, firstRiftHerald, towerKills,
                 inhibitorKills, baronKills, dragonKills, vilemawKills,
                 riftHeraldKills, dominionVictoryScore, gameid):
        self.teamId = teamId
        self.win = win
        self.firstBlood = firstBlood
        self.firstTower = firstTower
        self.firstInhibitor = firstInhibitor
        self.firstBaron = firstBaron
        self.firstDragon = firstDragon
        self.firstRiftHerald = firstRiftHerald
        self.towerKills = towerKills
        self.inhibitorKills = inhibitorKills
        self.baronKills = baronKills
        self.dragonKills = dragonKills
        self.vilemawKills = vilemawKills
        self.riftHeraldKills = riftHeraldKills
        self.dominionVictoryScore = dominionVictoryScore
        self.gameid = gameid


class TeamMemberInfo:
    pass


class MatchRepository(ABC):

    @abstractmethod
    def insert_match(self, match: Match) -> Match:
        pass

    @abstractmethod
    def fetch_data(self):
        pass


class TeamRepository(ABC):

    @abstractmethod
    def insert_team_status(self, team_status: TeamStatus) -> TeamStatus:
        pass

    @abstractmethod
    def insert_team_member_info(
            self, team_member_info: TeamMemberInfo) -> TeamMemberInfo:
        pass

    @abstractmethod
    def fetch_team_data(self, match_id: str):
        pass
