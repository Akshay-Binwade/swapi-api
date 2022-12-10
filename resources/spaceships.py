import random

from resources.base import ResourceBase
from utils.fetch_data import hit_url


class Spaceships(ResourceBase):
    """
    Resource class (plural)
    """
    name = "Spaceships"

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/starships"  # plural
        self.__spaceships_range = [1, 36]

    def set_spaceships_range(self,start,stop):
        self.__spaceships_range = [start,stop]
        return self.__spaceships_range

    def get_spaceships_range(self):
        return self.__spaceships_range

    def get_count(self):
        plural_spaceships_url = self.home_url + self.__relative_url
        # print(plural_spaceships_url)
        response = hit_url(plural_spaceships_url)
        result = response.json()
        self.count = result.get("count")
        return self.count

    def get_resource_urls(self) -> str:
        singular_spaceships_url = self.home_url + self.__relative_url
        return singular_spaceships_url

    def random(self):
        return random.randrange(1,self.count)


# s = Spaceships()
# print(s.get_spaceships_range())
# print(s.set_spaceships_range(1,s.get_count()))
# print(s.get_spaceships_range())
# print("The count of planets is:",s.get_count())


