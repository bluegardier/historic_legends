from abc import ABC, abstractmethod


class Match:

    def __init__(self, platformId: str, gameid: str, champion: int, queue: int,
                 season: int, timestamp: str, role: str, lane: str,
                 gamemode: str, gametype: str, teamid: int, win: str):
        """__init__ [summary]

        Parameters
        ----------
        platformId : str
            [description]
        gameid : str
            [description]
        champion : int
            [description]
        queue : int
            [description]
        season : int
            [description]
        timestamp : str
            [description]
        role : str
            [description]
        lane : str
            [description]
        gamemode : str
            [description]
        gametype : str
            [description]
        teamid : int
            [description]
        win : str
            [description]
        """

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
    def __init__(self, teamId: int, win: str, firstBlood: bool,
                 firstTower: bool, firstInhibitor: bool,
                 firstBaron: bool, firstDragon: bool, firstRiftHerald: bool,
                 towerKills: int, inhibitorKills: int, baronKills: int,
                 dragonKills: int, vilemawKills: int, riftHeraldKills: int,
                 dominionVictoryScore: int, gameId: str):
        """__init__ [summary]

        Parameters
        ----------
        teamId : int
            [description]
        win : str
            [description]
        firstBlood : bool
            [description]
        firstTower : bool
            [description]
        firstInhibitor : bool
            [description]
        firstBaron : bool
            [description]
        firstDragon : bool
            [description]
        firstRiftHerald : bool
            [description]
        towerKills : int
            [description]
        inhibitorKills : int
            [description]
        baronKills : int
            [description]
        dragonKills : int
            [description]
        vilemawKills : int
            [description]
        riftHeraldKills : int
            [description]
        dominionVictoryScore : int
            [description]
        gameid : str
            [description]
        """

        self.teamid = teamId
        self.win = win
        self.firstblood = firstBlood
        self.firsttower = firstTower
        self.firstinhibitor = firstInhibitor
        self.firstbaron = firstBaron
        self.firstdragon = firstDragon
        self.firstriftherald = firstRiftHerald
        self.towerkills = towerKills
        self.inhibitorkills = inhibitorKills
        self.baronkills = baronKills
        self.dragonKills = dragonKills
        self.vilemawkills = vilemawKills
        self.riftheraldkills = riftHeraldKills
        self.dominionvictoryscore = dominionVictoryScore
        self.gameid = gameId


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
