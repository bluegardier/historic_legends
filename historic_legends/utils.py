import os
import time
import pandas as pd
from pandas.io import json
from historic_legends import config
from riotwatcher import LolWatcher, ApiError
from psycopg2.extensions import AsIs
import psycopg2


def _gather_team_id(df: json) -> int:
    """
    Fetch the player's Team Id from a Match

    Parameters
    ----------
    df : json
        A Json containing the "participantIdentities" key, fetched
        from Riot's API.

    Returns
    -------
    int
        Player's Team ID code.
    """

    for i in range(10):
        name = df["participantIdentities"][i]["player"]["summonerName"]
        if name == config.PLAYER_NAME:
            participantid = df["participantIdentities"][i]["participantId"]
            teamid = df["participants"][participantid - 1]["teamId"]
            return teamid
        else:
            continue


def _gather_win_condition(teamid: int, api_data: json) -> str:
    """
    Fetch the player's victory condition from a match.

    Parameters
    ----------
    teamid : int
        Player's team id for that match.
    api_data : json
        Json data from Riot's Api, containing the "teams" key.

    Returns
    -------
    str
        Match's victory condition.
    """
    if api_data["teams"][0] == teamid:
        win = api_data["teams"][0]['win']
    else:
        win = api_data["teams"][1]['win']
    return win


def create_final_match_table(
        df: pd.DataFrame,
        table_number: int,
        total_number_tables: int) -> pd.DataFrame:
    """
    Fetch the match's victory status from Riot's API.
    The function sleeps for 150 secods after each 40th request to prevent
    request limit error.

    For each iteration, for each game id, the function creates the final
    columns for the dataframe fetched from "by_account"'s Riot Watcher method.

    The columns are: Game Mode, Game Type, Team ID and Win.

    The final step is to merge the newly created table with the 
    previously passed as a parameter.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with gameId variable.
    table_number : int
        The current Table being uploaded. Only for print information.
    total_number_tables : int
        The total number of Tables being uploaded. Only for print information.

    Returns
    -------
    pd.DataFrame
        The final match dataframe for upload.
    """

    riot_api = os.getenv("RIOT_API")
    lolwatcher = LolWatcher(riot_api)
    df_copy = df.copy()
    df_copy.rename(columns={"gameId": "gameid"}, inplace=True)

    match_df = pd.DataFrame(columns=config.match_victory_columns)
    gameid_list = df['gameId'].unique()

    for i, gameid in enumerate(gameid_list):
        print("Building: Table Number - {} / Total Tables - {}".format(
            table_number + 1, total_number_tables
        ))
        print("Match Info - {} / Total Matches - {}".format(
            i,
            len(gameid_list)
        )
        )
        print("\n")

        try:
            match_status = lolwatcher.match.by_id(config.REGION, gameid)
        except ApiError as err:
            if err.response.status_code == 504:
                print("ERROR 504. Retrying in 150 seconds.")
                time.sleep(200)
                print("Fetching the Data Again.")
                match_status = lolwatcher.match.by_id(
                    config.REGION, gameid)
                print("Data Successfully Fetched!")

        gameid = match_status['gameId']
        gamemode = match_status['gameMode']
        gametype = match_status['gameType']
        teamid = _gather_team_id(match_status)
        win = _gather_win_condition(teamid, match_status)
        match_variables = [gameid, gamemode, gametype, teamid, win]

        data = pd.DataFrame([match_variables],
                            columns=config.match_victory_columns)
        match_df = match_df.append(data)

    final_df = df_copy.merge(match_df, on="gameid", how="left")

    return final_df


def create_sql_pandas_table(sql_query: str, conn) -> pd.DataFrame:
    """
    Creates a Pandas DataFrame from the query.

    Parameters
    ----------
    sql_query : str
        A SQL query.
    conn :

    Returns
    -------
    pd.DataFrame
        A dataframe table with the correspondent query.
    """

    table = pd.read_sql_query(sql_query, conn)
    return table


def _fetching_game_id_from_league_data(query)-> tuple:
    """

    Parameters
    ----------
    query : A SQL query. Use to fetch gameid from a table.

    Returns
    -------

    """
    connection = None
    try:
        connection = config.conn
        cursor = connection.cursor()
        postgreSQL_select_Query = query

        cursor.execute(postgreSQL_select_Query)
        rows = cursor.fetchall()
        print("Rows fetched with success!")
        return rows


    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)




def extracting_game_ids(query)-> list:
    """
    Extract gameids from a table as a list
    Parameters
    ----------
    query : A SQL query. Use to fetch gameid from a table.

    Returns
    -------
    A list of gameids.

    """

    fetched_game_ids = _fetching_game_id_from_league_data(query)
    gameid_list = [fetched_game_ids[i][0] for i in range(len(fetched_game_ids))]
    return gameid_list


def adapt_numpy_float64(numpy_float64):
    """
    Adapts psycopg2 to understand a numpy float64 value.
    """
    return AsIs(numpy_float64)


def adapt_numpy_int64(numpy_int64):
    """
    Adapts psycopg2 to understand a numpy int64 value.
    """
    return AsIs(numpy_int64)
