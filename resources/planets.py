import random

from resources.base import ResourceBase
from utils.fetch_data import hit_url


class Planets(ResourceBase):
    """
    Resource class (plural)
    """
    name = "Planets"

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/planets"  # plural
        self.__planets_range = [1, 60]

    def set_planets_range(self,start,stop):
        self.__planets_range = [start,stop]
        return self.__planets_range

    def get_planets_range(self):
        return self.__planets_range

    def get_count(self):
        plural_planet_url = self.home_url + self.__relative_url
        response = hit_url(plural_planet_url)
        result = response.json()
        self.count = result.get("count")
        return self.count

    def get_resource_urls(self) -> str:
        singular_planet_url = self.home_url + self.__relative_url
        return singular_planet_url

    def get_sample_data(self):
        sample = self.home_url + self.__relative_url + "/1"
        response = hit_url(sample)
        return response.json()

    def random(self):
        return random.randrange(1,self.count)


# p = Planets()
# print(p.get_planets_range())
# print(p.set_planets_range(1,p.get_count()))
# print(p.get_planets_range())
# print("The count of planets is:",p.get_count())

