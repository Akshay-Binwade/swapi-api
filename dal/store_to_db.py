import pymysql
from typing import List, Dict

def store(title: str, datas: List[Dict]):
    '''
    film is an example here to store the info in the respective database
    '''

    connector = pymysql.connect(host="localhost",user="root",password="root",database="practice")
    mycursor = connector.cursor()


    for data in datas:
        try:
            mycursor.execute("use practice;")
            # To pass the command to the mysql we have to use .execute followed by command.
            # mycursor.execute(f"""INSERT INTO {title} VALUES {tuple(data.values())};""")
            mycursor.execute(f"""INSERT INTO {title} ({", ".join(data.keys())}) VALUES {tuple(data.values())};""")
            # We here are passing the columns and values in the insert command
            connector.commit()
            print("done")


        except:
            print("Database Error")
        # # breakpoint()
        # print(f"""INSERT INTO {title} ({", ".join(data.keys())}) VALUES {tuple(data.values())};""")
        # print(f"INSERT INTO {title} {tuple(data.keys())} VALUES {tuple(data.values())};")
# lis = [{'created': '2014-12-09', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/1/', 'name': 'Luke Skywalker', 'height': '1.72 mtr', 'mass': '77 kgs', 'hair_color': 'blond', 'skin_color': 'fair', 'eye_color': 'blue', 'birth_year': '19BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/1/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/2/', 'name': 'C-3PO', 'height': '1.67 mtr', 'mass': '75 kgs', 'hair_color': 'n/a', 'skin_color': 'gold', 'eye_color': 'yellow', 'birth_year': '112BBY', 'gender': 'n/a', 'homeworld': 'https://swapi.dev/api/planets/1/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/3/', 'name': 'R2-D2', 'height': '0.96 mtr', 'mass': '32 kgs', 'hair_color': 'n/a', 'skin_color': 'white, blue', 'eye_color': 'red', 'birth_year': '33BBY', 'gender': 'n/a', 'homeworld': 'https://swapi.dev/api/planets/8/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/4/', 'name': 'Darth Vader', 'height': '2.02 mtr', 'mass': '136 kgs', 'hair_color': 'none', 'skin_color': 'white', 'eye_color': 'yellow', 'birth_year': '41.9BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/1/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/5/', 'name': 'Leia Organa', 'height': '1.5 mtr', 'mass': '49 kgs', 'hair_color': 'brown', 'skin_color': 'light', 'eye_color': 'brown', 'birth_year': '19BBY', 'gender': 'female', 'homeworld': 'https://swapi.dev/api/planets/2/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/6/', 'name': 'Owen Lars', 'height': '1.78 mtr', 'mass': '120 kgs', 'hair_color': 'brown, grey', 'skin_color': 'light', 'eye_color': 'blue', 'birth_year': '52BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/1/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/7/', 'name': 'Beru Whitesun lars', 'height': '1.65 mtr', 'mass': '75 kgs', 'hair_color': 'brown', 'skin_color': 'light', 'eye_color': 'blue', 'birth_year': '47BBY', 'gender': 'female', 'homeworld': 'https://swapi.dev/api/planets/1/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/8/', 'name': 'R5-D4', 'height': '0.97 mtr', 'mass': '32 kgs', 'hair_color': 'n/a', 'skin_color': 'white, red', 'eye_color': 'red', 'birth_year': 'unknown', 'gender': 'n/a', 'homeworld': 'https://swapi.dev/api/planets/1/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/9/', 'name': 'Biggs Darklighter', 'height': '1.83 mtr', 'mass': '84 kgs', 'hair_color': 'black', 'skin_color': 'light', 'eye_color': 'brown', 'birth_year': '24BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/1/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/10/', 'name': 'Obi-Wan Kenobi', 'height': '1.82 mtr', 'mass': '77 kgs', 'hair_color': 'auburn, white', 'skin_color': 'fair', 'eye_color': 'blue-gray', 'birth_year': '57BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/20/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/12/', 'name': 'Wilhuff Tarkin', 'height': '1.8 mtr', 'mass': 'unknown kgs', 'hair_color': 'auburn, grey', 'skin_color': 'fair', 'eye_color': 'blue', 'birth_year': '64BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/21/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/13/', 'name': 'Chewbacca', 'height': '2.28 mtr', 'mass': '112 kgs', 'hair_color': 'brown', 'skin_color': 'unknown', 'eye_color': 'blue', 'birth_year': '200BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/14/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/14/', 'name': 'Han Solo', 'height': '1.8 mtr', 'mass': '80 kgs', 'hair_color': 'brown', 'skin_color': 'fair', 'eye_color': 'brown', 'birth_year': '29BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/22/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/15/', 'name': 'Greedo', 'height': '1.73 mtr', 'mass': '74 kgs', 'hair_color': 'n/a', 'skin_color': 'green', 'eye_color': 'black', 'birth_year': '44BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/23/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/16/', 'name': 'Jabba Desilijic Tiure', 'height': '1.75 mtr', 'mass': '1,358 kgs', 'hair_color': 'n/a', 'skin_color': 'green-tan, brown', 'eye_color': 'orange', 'birth_year': '600BBY', 'gender': 'hermaphrodite', 'homeworld': 'https://swapi.dev/api/planets/24/'}, {'created': '2014-12-12', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/18/', 'name': 'Wedge Antilles', 'height': '1.7 mtr', 'mass': '77 kgs', 'hair_color': 'brown', 'skin_color': 'fair', 'eye_color': 'hazel', 'birth_year': '21BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/22/'}, {'created': '2014-12-12', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/19/', 'name': 'Jek Tono Porkins', 'height': '1.8 mtr', 'mass': '110 kgs', 'hair_color': 'brown', 'skin_color': 'fair', 'eye_color': 'blue', 'birth_year': 'unknown', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/26/'}, {'created': '2014-12-20', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/81/', 'name': 'Raymus Antilles', 'height': '1.88 mtr', 'mass': '79 kgs', 'hair_color': 'brown', 'skin_color': 'light', 'eye_color': 'brown', 'birth_year': 'unknown', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/2/'}]
# store('characters', lis)