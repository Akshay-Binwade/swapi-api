# 1. TODO import all resource classes here
import requests
from pprint import pprint
from utils.fetch_data import hit_url
from resources.characters import Characters
from resources.planets import Planets
from resources.spaceships import Spaceships
from resources.species import Species
from resources.films import Films
from resources.vehicles import Vehicles

characters = Characters()
planets = Planets()
spaceships = Spaceships()
species = Species()
films = Films()
vehicles = Vehicles()
resources = [characters,planets,spaceships,species,films,vehicles]


# 2. TODO get count of each resource

def get_count_of_each():
    print("The counts of different resources are as follows:")
    counts = {}
    for res in resources:
        counts[res.name] = res.get_count()
    return counts


# 3. TODO get "singular" resource urls of each resource

def get_singular_url():
    urls = []
    for res in resources:
        urls.append(res.get_resource_urls() + str(1))
    return urls


# 4. TODO pull data from random 3 "singular" resource URLs
def get_random_singular_info():
    print("\nFollowing result is info of randomly chosen resource")
    info = {}
    for res in resources:
        ref = info.setdefault(res.name,[])
        for i in range(3):
            singular_url = res.get_resource_urls() + "/" + str(res.random())
            # print(singular_url)
            response = hit_url(singular_url)
            # breakpoint()
            if isinstance(response,str):
                pass
                # print(res.name,response)
            else:
                response = response.json()
                ref.append(response)
    return info


def task_three():
    '''
    This function returns count of resources and gets random three resource data of each resource.
    '''
    pprint(get_count_of_each())
    pprint(get_random_singular_info())

