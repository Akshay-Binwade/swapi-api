import requests
from utils.randgen import for_people

'''`randgen` is used to generate random numbers between 1-82'''
f = for_people()

class Swapi:
    '''This class focuses on collecting info from swapi api'''
    def __init__(self):
        self.home_url = "https://swapi.dev"
        self.relative_url = "/api/people/"

    def fetch(self):
        '''Here the url is assembled and request is sent to collect data of particular character'''
        result = requests.get(self.home_url + self.relative_url + str(next(f)))
        result = result.json()
        print(result)


def task_one():
    c = Swapi()
    '''This loop invokes 'fetch' method of swapi in each iteration'''
    for i in range(1, 16):
        c.fetch()
        print("#" * 100)
        print()