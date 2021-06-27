import os
import numpy as np
import pandas as pd
from typing import Match
from sqlalchemy import exc
from dotenv import load_dotenv
from domain import repositories
from riotwatcher import LolWatcher
from historic_legends import config, utils
from infra import pandas_sql_connection as psc
from psycopg2.extensions import register_adapter

from src.domain.repositories import TeamStatus, TeamMember

load_dotenv()

register_adapter(np.float64, utils.adapt_numpy_float64)
register_adapter(np.int64, utils.adapt_numpy_int64)


class PostGresRiotMatchRepository(repositories.MatchRepository):

    def fetch_data(self, index_list=[0]):
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

        riot_api = os.getenv("RIOT_API")
        riot_acc_id = os.getenv("RIOT_ACC_ID")
        lolwatcher = LolWatcher(riot_api)

        game_history_list = []
        for i, index in enumerate(index_list):
            print("Fetching Data From Index = {}".format(index))

            game_history = lolwatcher.match.matchlist_by_account(
                config.REGION, begin_index=int(index),
                encrypted_account_id=riot_acc_id)["matches"]

            game_history = pd.DataFrame(game_history)
            game_history = utils.create_final_match_table(
                game_history, i, len(index_list))
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
            print("Uploading Builded Data")
            for row in range(data.shape[0]):
                try:
                    data_for_upload = pd.DataFrame(data.iloc[row]).T
                    data_for_upload.to_sql(config.MATCHES_TABLE_OUTPUT,
                                           con=psc.engine,
                                           schema=config.SCHEMA_OUTPUT,
                                           index=False,
                                           chunksize=1000,
                                           method='multi',
                                           if_exists='append')
                except exc.IntegrityError:
                    print("This Match is already in the DataBase")


class PostGresRiotTeamRepository(repositories.TeamRepository):

    def fetch_team_data(self):

        print("Fetching Game IDs for Requests.")
        fetched_gameid_match_summary = utils.extracting_game_ids(config.GAMEID_MATCH_SUMMARY_QUERY)
        fetched_gameid_team_summary = utils.extracting_game_ids(config.GAMEID_TEAM_SUMMARY_QUERY)

        gameid_list = list(set(fetched_gameid_match_summary) - set(fetched_gameid_team_summary))

        print("We have {} new games to upload.".format(len(gameid_list)))
        print("Fetching Done!")

        team_status_data = utils.create_team_status_table(gameid_list)

        team_status_list = []
        for game in team_status_data:
            team_status_list.append(repositories.TeamStatus(**game))

        return team_status_list

    def insert_team_status(self, team_status: TeamStatus):
        for i in range(len(team_status)):
            print("Inserting Rows From Table Number: {}".format(i + 1))
            data = pd.DataFrame(team_status[i].__dict__)
            print("Uploading Builded Data")
            for row in range(data.shape[0]):
                try:
                    data_for_upload = pd.DataFrame(data.iloc[row]).T
                    data_for_upload.to_sql(config.TEAM_TABLE_OUTPUT,
                                           con=psc.engine,
                                           schema=config.SCHEMA_OUTPUT,
                                           index=False,
                                           chunksize=1000,
                                           method='multi',
                                           if_exists='append')
                except exc.IntegrityError:
                    print("This Match is already in the DataBase")


class PostGresRiotTeamMemberRepository(repositories.TeamMember):

    def fetch_team_member_data(self):

        print("Fetching Game IDs for Requests.")
        fetched_gameid_team_summary = utils.extracting_game_ids(config.GAMEID_TEAM_SUMMARY_QUERY)
        fetched_gameid_team_member_summary = utils.extracting_game_ids(config.GAMEID_TEAM_MEMBER_SUMMARY_QUERY)

        gameid_list = list(set(fetched_gameid_team_summary) - set(fetched_gameid_team_member_summary))

        print("We have {} new games to upload.".format(len(gameid_list)))
        print("Fetching Done!")

        team_member_data = utils.create_team_member_table(gameid_list)

        team_member_list = []
        for i in range(len(team_member_data)):
            team_member_list.append(repositories.TeamMember(**team_member_data.iloc[i]))

        return team_member_list

    def insert_team_member(self, team_member: TeamMember):
        for i in range(len(team_member)):
            print("Inserting Rows From Table Number: {}".format(i + 1))
            data = pd.DataFrame([team_member[i].__dict__])
            print("Uploading Builded Data")
            for row in range(data.shape[0]):
                try:
                    data_for_upload = pd.DataFrame(data.iloc[row]).T
                    data_for_upload.to_sql(config.TEAM_MEMBER_TABLE_OUTPUT,
                                           con=psc.engine,
                                           schema=config.SCHEMA_OUTPUT,
                                           index=False,
                                           chunksize=1000,
                                           method='multi',
                                           if_exists='append')
                except exc.IntegrityError:
                    print("This Match is already in the DataBase")

