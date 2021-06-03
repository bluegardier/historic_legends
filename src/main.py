from application.repositories import PostGresRiotMatchRepository
from domain.services import PopulateMatches
import sys

repo = PostGresRiotMatchRepository()

service = PopulateMatches(repo)
index_list = list(map(lambda x: int(x), sys.argv[1:]))
service.execute(index_list)
