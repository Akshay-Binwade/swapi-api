import random

from resources.base import ResourceBase
from utils.fetch_data import hit_url


class Films(ResourceBase):
    """
    Resource class (plural)
    """
    name = "Films"

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/films"  # plural
        self.__films_range = [1, 6]

    def set_films_range(self,start,stop):
        self.__films_range = [start,stop]
        return self.__films_range

    def get_films_range(self):
        return self.__films_range

    def get_count(self):
        plural_films_url = self.home_url + self.__relative_url
        # print(plural_films_url)
        response = hit_url(plural_films_url)
        result = response.json()
        self.count = result.get("count")
        return self.count

    def get_resource_urls(self) -> str:
        singular_films_url = self.home_url + self.__relative_url
        return singular_films_url

    def random(self):
        return random.randrange(1,self.count)


# f = Films()
# print(f.get_films_range())
# print(f.set_films_range (1,f.get_count()))
# print(f.get_films_range())
# print("The count of planets is:",f.get_count())

