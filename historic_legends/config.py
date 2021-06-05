match_data_columns = ["platformId",
                      "gameId",
                      "champion",
                      "queue",
                      "season",
                      "timestamp",
                      "role",
                      "lane"
                      ]

match_victory_columns = [
    "gameid",
    "gamemode",
    "gametype",
    "teamid",
    "win"
]

REGION = "br1"
PLAYER_NAME = "Blue Gardier"
BEGIN_INDEX = [0]


DB_GAMEID_QUERY = "SELECT DISTINCT gameid FROM league_data.match_summary"

SCHEMA_OUTPUT = "league_data"
MATCHES_TABLE_OUTPUT = "match_summary"
