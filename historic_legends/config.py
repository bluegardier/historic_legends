# TODO: Import conn from infra instead of config.py

import os
import psycopg2
import sqlalchemy as db
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = db.create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)

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

GAMEID_MATCH_SUMMARY_QUERY = "SELECT DISTINCT gameid from league_data.match_summary"
GAMEID_TEAM_SUMMARY_QUERY = "SELECT DISTINCT gameid from league_data.match_team_status"

SCHEMA_OUTPUT = "league_data"
MATCHES_TABLE_OUTPUT = "match_summary"
