from typing import List
from utils.fetch_data import hit_url2
import time
from multiprocessing.pool import ThreadPool
from resources.films import Films
from models.datamodels.films import Film_
from models.datamodels.characters import Character_
from models.datamodels.planets import Planet_

from dal.store_to_db import store
def remove_cross_refer(data):
    filtered_data = {}
    for key_,val in data:
        if isinstance(val, str):
            filtered_data[key_]= val
        else:
            pass
    return filtered_data


def urls_to_data(url_list: List):
    start = time.time()
    pool_ = ThreadPool(15)
    data = pool_.map(hit_url2, url_list)
    print(f"Time to execute: {time.time() - start}")
    return data     # List of data extracted from urls


def valid_data(datas: List, validator: "pydantic datamodel"):
    filtered = []
    for data in datas:
        data = validator(**data)
        filtered_data = remove_cross_refer(data)
        filtered.append(filtered_data)
    return filtered





if __name__ == '__main__':
    # breakpoint()
    film_data = Films().get_sample_data()
    film_data = Film_(**film_data)
    # print(film_data)
    # breakpoint()

    char_urls = film_data.characters

    char_data = urls_to_data(char_urls)
    # print(char_data)
    char_data = valid_data(char_data, Character_)
