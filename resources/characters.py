import random

from resources.base import ResourceBase
from utils.fetch_data import hit_url


class Characters(ResourceBase):
    """
    Resource class (plural)
    """
    name = "Characters"

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/people"  # plural
        self.__character_range = [1, 82]

    def set_character_range(self,start,stop):
        self.__character_range = [start,stop]
        return self.__character_range

    def get_character_range(self):
        return self.__character_range

    def get_count(self):
        plural_character_url = self.home_url + self.__relative_url
        response = hit_url(plural_character_url)
        result = response.json()
        self.count = result.get("count")
        return self.count

    def get_resource_urls(self) -> str:
        singular_character_url = self.home_url + self.__relative_url
        return singular_character_url

    def get_sample_data(self):
        sample = self.home_url + self.__relative_url+ "/1"
        response = hit_url(sample)
        if isinstance(response, str):
            return "Data not found"
        return response.json()

    def random(self):
        return random.randrange(1,self.count)


c = Characters()
# print("The count of Characters is:",c.get_count())
# re = c.generator()
# print(c.get_resource_urls(next(re)))

# print(c.get_sample_data())