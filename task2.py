import requests
from pprint import pprint


class Swapi:
    '''Here the information of film 1 from swapi api is collected'''
    def __init__(self):
        self.home_url = "https://swapi.dev"
        self.relative_url = "/api/films/1"
        self.result = requests.get(self.home_url + self.relative_url)
        self.result = self.result.json()   # Info of film 1 is collected here in dict format

    def get_characters(self):
        '''This method returns list of character names'''
        chars = list(self.result.get("characters"))
        chars_lis = self.loop(chars)   # loop returns the list of names out of unnecessary info
        return chars_lis

    def get_planets(self):
        '''This method returns list of planets names'''
        planets = self.result.get("planets")
        planets_lis = self.loop(planets)
        return planets_lis
        # print(planets)

    def get_vehicles(self):
        '''This method returns list of vehicles names'''
        vehicles = self.result.get("vehicles")
        vehicles_lis = self.loop(vehicles)
        return vehicles_lis

    def loop(self,param):
        '''This method takes list of urls as input and return only names from their info'''
        lis = []
        for char in (param):
            res = requests.get(char)
            res = res.json()
            lis.append(res.get("name"))
        return lis


obj = Swapi()
if __name__ == '__main__':
    with open("output_task2.txt","a") as file:
        file.write(f"Characters in film1 are: {obj.get_characters()}\n")
        print("Done")
        file.write(f"Planets in film 1 are: {obj.get_planets()}\n")
        print("Done")
        file.write(f"Vehicles in film 1 are: {obj.get_vehicles()}")
        print("Done")


def task_two():
    print(f"Characters in film1 are: {obj.get_characters()}\n")
    print(f"Planets in film 1 are: {obj.get_planets()}\n")
    print(f"Vehicles in film 1 are: {obj.get_vehicles()}")
