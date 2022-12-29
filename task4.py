from resources.films import Films
from models.datamodels.films import Film_
from utils.fetch_data import hit_url2
from dal.store_ import store

from models.datamodels.characters import Character_
from models.datamodels.planets import Planet_
from models.datamodels.starships import Starship_
from models.datamodels.spacies import Species_
from models.datamodels.vehicles import Vehicle_

from multiprocessing.pool import ThreadPool


def url_to_data(urls):
    pool_ = ThreadPool(15)
    datas = pool_.map(hit_url2, urls)
    # print(datas)
    return datas


def valid_data(datas, validator):
    lis = []
    for data in datas:
        Vdata = validator(**data)
        filtered_data = remove_url_list(Vdata)
        lis.append(filtered_data)
    return lis


def remove_url_list(data):
    dic = {}
    for key_, val in data:
        if isinstance(val, str):
            dic[key_] = val
    return dic


def task_four():
    film_data = Films().get_sample_data()
    film_data = Film_(**film_data)
    v_film_data = remove_url_list(film_data)
    print(v_film_data)
    # print(film_data)

    # # To get the list of urls
    char_urls = film_data.characters
    plan_urls = film_data.planets
    star_urls = film_data.starships
    spec_urls = film_data.species
    veh_urls = film_data.vehicles
    #
    char_data = url_to_data(char_urls)
    plan_data = url_to_data(plan_urls)
    star_data = url_to_data(star_urls)
    spec_data = url_to_data(spec_urls)
    veh_data = url_to_data(veh_urls)

    char_data = valid_data(char_data, Character_)
    plan_data = valid_data(plan_data, Planet_)
    star_data = valid_data(star_data, Starship_)
    spec_data = valid_data(spec_data, Species_)
    veh_data = valid_data(veh_data, Vehicle_)

    store("species","species_id",spec_data)
    store("vehicles","vehicle_id", veh_data)
    store("characters","char_id", char_data)
    store("planets","planet_id", plan_data)
    store("starships","starship_id", star_data)
    store("films", "film_id", v_film_data)


if __name__ == '__main__':
    task_four()






