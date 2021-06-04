import os
import numpy as np
import pandas as pd
from typing import Match
from sqlalchemy import exc
from dotenv import load_dotenv
from domain import repositories
from riotwatcher import LolWatcher
from historic_legends import config
from infra import pandas_sql_connection as psc
from psycopg2.extensions import register_adapter, AsIs

load_dotenv()


def addapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)


def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)


register_adapter(np.float64, addapt_numpy_float64)
register_adapter(np.int64, addapt_numpy_int64)


class PostGresRiotMatchRepository(repositories.MatchRepository):

    def fetch_data(self, index_list=None):
        """
        Fetch data from Riot API ad turns it into a Dataframe.

        Parameters
        ----------
        index_list : None
            Int list for fetching match data by it's index.
            Gather the next 100 data match for each element
            interaction.

        Returns
        -------

        """

        if index_list is None:
            index_list = [0]
        riot_api = os.getenv("RIOT_API")
        riot_acc_id = os.getenv("RIOT_ACC_ID")
        lolwatcher = LolWatcher(riot_api)

        game_history_list = []
        for index in index_list:
            print("index = {}".format(index))

            game_history = lolwatcher.match.matchlist_by_account(
                config.REGION, begin_index=int(index),
                encrypted_account_id=riot_acc_id)["matches"]

            game_history = pd.DataFrame(game_history)
            game_history_list.append(game_history)

        matches = []
        for match in game_history_list:
            matches.append(repositories.Match(**match))

        return matches

    def insert_match(self, match: Match):
        """
        Inserts the Dataframe into a PostGres database.

        Parameters
        ----------
        match : Match
        The domain as a object containing the match data to be
        uploaded to the PostGres database.

        Returns
        -------

        """
        for i in range(len(match)):
            print("Inserting Rows From Table Number: {}".format(i + 1))
            data = pd.DataFrame(match[i].__dict__)
            for row in range(data.shape[0]):
                try:
                    pd.DataFrame(data.iloc[row]). \
                        T.to_sql(config.MATCHES_TABLE_OUTPUT,
                                 con=psc.engine,
                                 schema=config.SCHEMA_OUTPUT,
                                 index=False,
                                 chunksize=1000,
                                 method='multi',
                                 if_exists='append')
                except exc.IntegrityError:
                    print("This Match is already in the DataBase")
