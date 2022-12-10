import random

from resources.base import ResourceBase
from utils.fetch_data import hit_url


class Species(ResourceBase):
    """
    Resource class (plural)
    """
    name = "Species"

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/species"  # plural
        self.__species_range = [1, 37]

    def set_species_range(self,start,stop):
        self.__species_range = [start,stop]
        return self.__species_range

    def get_species_range(self):
        return self.__species_range

    def get_count(self):
        plural_species_url = self.home_url + self.__relative_url
        response = hit_url(plural_species_url)
        result = response.json()
        self.count = result.get("count")
        return self.count

    def get_resource_urls(self) -> str:
        singular_species_url = self.home_url + self.__relative_url
        return singular_species_url

    def random(self):
        return random.randrange(1,self.count)


# s = Species()
# print(s.get_species_range())
# print(s.set_species_range(1,s.get_count()))
# print(s.get_species_range())
# print("The count of planets is:",s.get_count())

