from application.repositories import PostGresRiotMatchRepository, PostGresRiotTeamRepository, \
    PostGresRiotTeamMemberRepository
from domain.services import PopulateMatches, PopulateTeam, PopulateTeamMember
from historic_legends import config
import fire


# Index until 1600 for full database.


def upload_match_summary_data(begin_index=None):
    """
    Uploads the Match Summary table to PostGres Database.

    Parameters
    ----------
    begin_index : Optional
    List of int values. They get next 100 data matches from the
    API starting from the begin_index element.

    Returns
    -------

    """
    if begin_index is None:
        begin_index = [0]

    repo = PostGresRiotMatchRepository()
    service = PopulateMatches(repo)
    index_list = begin_index
    service.execute(index_list)


def upload_team_summary_data():
    """
    Uploads the Team Summary table to PostGres Database.

    Returns
    -------

    """

    repo = PostGresRiotTeamRepository()
    service = PopulateTeam(repo)
    service.execute()


def upload_team_member_data():
    """
    Uploads the Team Member Summary table to PostGres Database.

    Returns
    -------

    """

    repo = PostGresRiotTeamMemberRepository()
    service = PopulateTeamMember(repo)
    service.execute()


def cli():
    """ Caller to transform module in a low-level CLI """
    return fire.Fire()


if __name__ == '__main__':
    cli()
