import os
from typing import Match
import pandas as pd
from riotwatcher import LolWatcher, ApiError
import psycopg2
import sqlalchemy as db
from domain import repositories
from historic_legends import config
from infra import pandas_sql_connection as psc
from dotenv import load_dotenv
load_dotenv()


class PostGresRiotMatchRepository(repositories.MatchRepository):

    def fetch_data(self, index_list: list = [0]):
        RIOT_API = os.getenv("RIOT_API")
        RIOT_ACC_ID = os.getenv("RIOT_ACC_ID")
        lolwatcher = LolWatcher(RIOT_API)

        game_history_list = []
        for index in index_list:
            print("index = {}".format(index))

            game_history = lolwatcher.match.matchlist_by_account(
                config.REGION, begin_index=int(index),
                encrypted_account_id=RIOT_ACC_ID)["matches"]

            game_history = pd.DataFrame(game_history)
            game_history_list.append(game_history)

        matches = []
        for match in game_history_list:
            matches.append(repositories.Match(**match))

        return matches

    def insert_match(self, match: Match) -> Match:
        for i in range(len(match)):
            pd.DataFrame(match[i].__dict__).to_sql(config.TEST_MATCH_DATA,
                                                   con=psc.engine,
                                                   schema=config.SCHEMA_OUTPUT,
                                                   index=False,
                                                   chunksize=1000,
                                                   method='multi',
                                                   if_exists='append')
