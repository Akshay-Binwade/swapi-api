from models.datamodels.characters import Character_ as char_validity
from models.datamodels.films import Film_ as film_validity
from models.datamodels.planets import Planet_ as plan_validity
from models.datamodels.spacies import Species_ as spec_validity
from models.datamodels.starships import Starship_ as star_validity
from models.datamodels.vehicles import Vehicle_ as veh_validity

from resources.characters import Characters
from resources.films import Films
from resources.planets import Planets
from resources.spaceships import Spaceships
from resources.species import Species
from resources.vehicles import Vehicles

from pprint import pprint

if __name__ == '__main__':
    breakpoint()

    char_data = Characters().get_sample_data()
    v_chars = char_validity(**char_data)
    pprint(dict(v_chars), sort_dicts=False)

    film_data = Films().get_sample_data()
    v_films = film_validity(**film_data)

    planet_data = Planets().get_sample_data()
    v_planet = plan_validity(**planet_data)

    ships_data = Spaceships().get_sample_data()
    v_ships = star_validity(**ships_data)

    species_data = Species().get_sample_data()
    v_species = spec_validity(**species_data)

    veh_data = Vehicles().get_sample_data()
    v_veh = veh_validity(**veh_data)






