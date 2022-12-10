import random

from resources.base import ResourceBase
from utils.fetch_data import hit_url


class Vehicles(ResourceBase):
    """
    Resource class (plural)
    """
    name = "Vehicles"

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/vehicles"  # plural
        self.__vehicles_range = [1, 39]

    def set_vehicles_range(self,start,stop):
        self.__vehicles_range = [start,stop]
        return self.__vehicles_range

    def get_vehicles_range(self):
        return self.__vehicles_range

    def get_count(self):
        plural_vehicles_url = self.home_url + self.__relative_url
        # print(plural_vehicles_url)
        response = hit_url(plural_vehicles_url)
        result = response.json()
        self.count = result.get("count")
        return self.count

    def get_resource_urls(self) -> str:
        singular_vehicels_url = self.home_url + self.__relative_url
        return singular_vehicels_url

    def random(self):
        return random.randrange(1,self.count)


# v = Vehicles()
# print(v.get_vehicles_range())
# print(v.set_vehicles_range (1,v.get_count()))
# print(v.get_vehicles_range())
# print("The count of planets is:",v.get_count())

