from domain.repositories import Match, MatchRepository


class PopulateMatches:
    def __init__(self, repository: MatchRepository) -> None:
        self.repository = repository

    def execute(self, index_list=None):

        if index_list is None:
            index_list = [0]
        data = self.repository.fetch_data(index_list)
        self.repository.insert_match(data)
