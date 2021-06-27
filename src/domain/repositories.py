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
        self.dragonkills = dragonKills
        self.vilemawkills = vilemawKills
        self.riftheraldkills = riftHeraldKills
        self.dominionvictoryscore = dominionVictoryScore
        self.gameid = gameId


class TeamMember:
    def __init__(self, firstInhibitorKill=None, firstInhibitorAssist=None,
                 participantId=None, platformId=None, accountId=None,
                 summonerName=None, summonerId=None, currentPlatformId=None,
                 currentAccountId=None, matchHistoryUri=None, profileIcon=None,
                 gameid=None, win=None, item0=None, item1=None, item2=None, item3=None, item4=None,
                 item5=None, item6=None, kills=None, deaths=None, assists=None,
                 largestKillingSpree=None, largestMultiKill=None,
                 killingSprees=None, longestTimeSpentLiving=None, doubleKills=None,
                 tripleKills=None, quadraKills=None, pentaKills=None, unrealKills=None,
                 totalDamageDealt=None, magicDamageDealt=None, physicalDamageDealt=None,
                 trueDamageDealt=None, largestCriticalStrike=None, totalDamageDealtToChampions=None,
                 magicDamageDealtToChampions=None, physicalDamageDealtToChampions=None,
                 trueDamageDealtToChampions=None, totalHeal=None, totalUnitsHealed=None, damageSelfMitigated=None,
                 damageDealtToObjectives=None, damageDealtToTurrets=None, visionScore=None, timeCCingOthers=None,
                 totalDamageTaken=None, magicalDamageTaken=None, physicalDamageTaken=None,
                 trueDamageTaken=None, goldEarned=None, goldSpent=None, turretKills=None, inhibitorKills=None,
                 totalMinionsKilled=None, neutralMinionsKilled=None, neutralMinionsKilledTeamJungle=None,
                 neutralMinionsKilledEnemyJungle=None, totalTimeCrowdControlDealt=None,
                 champLevel=None, visionWardsBoughtInGame=None, sightWardsBoughtInGame=None,
                 wardsPlaced=None, wardsKilled=None, firstBloodKill=None, firstBloodAssist=None,
                 firstTowerKill=None, firstTowerAssist=None,
                 combatPlayerScore=None, objectivePlayerScore=None,
                 totalPlayerScore=None, totalScoreRank=None, playerScore0=None, playerScore1=None,
                 playerScore2=None, playerScore3=None, playerScore4=None, playerScore5=None, playerScore6=None,
                 playerScore7=None, playerScore8=None, playerScore9=None, perk0=None, perk0Var1=None,
                 perk0Var2=None, perk0Var3=None, perk1=None, perk1Var1=None, perk1Var2=None, perk1Var3=None,
                 perk2=None, perk2Var1=None, perk2Var2=None, perk2Var3=None, perk3=None, perk3Var1=None,
                 perk3Var2=None, perk3Var3=None, perk4=None, perk4Var1=None, perk4Var2=None, perk4Var3=None,
                 perk5=None, perk5Var1=None, perk5Var2=None, perk5Var3=None, perkPrimaryStyle=None,
                 perkSubStyle=None, statPerk0=None, statPerk1=None, statPerk2=None, teamId=None,
                 championId=None, spell1Id=None, spell2Id=None, highestAchievedSeasonTier=None):
        self.participantid = participantId
        self.platformid = platformId
        self.accountid = accountId
        self.summonername = summonerName
        self.summonerid = summonerId
        self.currentplatformid = currentPlatformId
        self.currentaccountid = currentAccountId
        self.matchhistoryuri = matchHistoryUri
        self.profileicon = profileIcon
        self.gameid = gameid
        self.win = win
        self.item0 = item0
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        self.item5 = item5
        self.item6 = item6
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.largestkillingspree = largestKillingSpree
        self.largestmultikill = largestMultiKill
        self.killingsprees = killingSprees
        self.longesttimespentliving = longestTimeSpentLiving
        self.doublekills = doubleKills
        self.triplekills = tripleKills
        self.quadrakills = quadraKills
        self.pentakills = pentaKills
        self.unrealkills = unrealKills
        self.totaldamagedealt = totalDamageDealt
        self.magicdamagedealt = magicDamageDealt
        self.physicaldamagedealt = physicalDamageDealt
        self.truedamagedealt = trueDamageDealt
        self.largestcriticalstrike = largestCriticalStrike
        self.totaldamagedealttochampions = totalDamageDealtToChampions
        self.magicdamagedealttochampions = magicDamageDealtToChampions
        self.physicaldamagedealttochampions = physicalDamageDealtToChampions
        self.truedamagedealttochampions = trueDamageDealtToChampions
        self.totalheal = totalHeal
        self.totalunitshealed = totalUnitsHealed
        self.damageselfmitigated = damageSelfMitigated
        self.damagedealttoobjectives = damageDealtToObjectives
        self.damagedealttoturrets = damageDealtToTurrets
        self.visionscore = visionScore
        self.timeccingothers = timeCCingOthers
        self.totaldamagetaken = totalDamageTaken
        self.magicaldamagetaken = magicalDamageTaken
        self.physicaldamagetaken = physicalDamageTaken
        self.truedamagetaken = trueDamageTaken
        self.goldearned = goldEarned
        self.goldspent = goldSpent
        self.turretkills = turretKills
        self.inhibitorkills = inhibitorKills
        self.totalminionskilled = totalMinionsKilled
        self.neutralminionskilled = neutralMinionsKilled
        self.neutralminionskilledteamjungle = neutralMinionsKilledTeamJungle
        self.neutralminionskilledenemyjungle = neutralMinionsKilledEnemyJungle
        self.totaltimecrowdcontroldealt = totalTimeCrowdControlDealt
        self.champlevel = champLevel
        self.visionwardsboughtingame = visionWardsBoughtInGame
        self.sightwardsboughtingame = sightWardsBoughtInGame
        self.wardsplaced = wardsPlaced
        self.wardskilled = wardsKilled
        self.firstbloodkill = firstBloodKill
        self.firstbloodassist = firstBloodAssist
        self.firsttowerkill = firstTowerKill
        self.firsttowerassist = firstTowerAssist
        self.firstinhibitorkill = firstInhibitorKill
        self.firstinhibitorassist = firstInhibitorAssist
        self.combatplayerscore = combatPlayerScore
        self.objectiveplayerscore = objectivePlayerScore
        self.totalplayerscore = totalPlayerScore
        self.totalscorerank = totalScoreRank
        self.playerscore0 = playerScore0
        self.playerscore1 = playerScore1
        self.playerscore2 = playerScore2
        self.playerscore3 = playerScore3
        self.playerscore4 = playerScore4
        self.playerscore5 = playerScore5
        self.playerscore6 = playerScore6
        self.playerscore7 = playerScore7
        self.playerscore8 = playerScore8
        self.playerscore9 = playerScore9
        self.perk0 = perk0
        self.perk0var1 = perk0Var1
        self.perk0var2 = perk0Var2
        self.perk0var3 = perk0Var3
        self.perk1 = perk1
        self.perk1var1 = perk1Var1
        self.perk1var2 = perk1Var2
        self.perk1var3 = perk1Var3
        self.perk2 = perk2
        self.perk2var1 = perk2Var1
        self.perk2var2 = perk2Var2
        self.perk2var3 = perk2Var3
        self.perk3 = perk3
        self.perk3var1 = perk3Var1
        self.perk3var2 = perk3Var2
        self.perk3var3 = perk3Var3
        self.perk4 = perk4
        self.perk4var1 = perk4Var1
        self.perk4var2 = perk4Var2
        self.perk4var3 = perk4Var3
        self.perk5 = perk5
        self.perk5var1 = perk5Var1
        self.perk5var2 = perk5Var2
        self.perk5var3 = perk5Var3
        self.perkprimarystyle = perkPrimaryStyle
        self.perksubstyle = perkSubStyle
        self.statperk0 = statPerk0
        self.statperk1 = statPerk1
        self.statperk2 = statPerk2
        self.teamid = teamId
        self.championid = championId
        self.spell1id = spell1Id
        self.spell2id = spell2Id
        self.highestachievedseasontier = highestAchievedSeasonTier


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
    def fetch_team_data(self):
        pass


class TeamMemberRepository(ABC):

    @abstractmethod
    def insert_team_member(self, team_member: TeamMember) -> TeamMember:
        pass

    @abstractmethod
    def fetch_team_member_data(self):
        pass
