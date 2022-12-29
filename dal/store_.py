import pymysql
from typing import List, Optional,Dict

def store(table: str, primary_key: str, datas: [List,Dict]):
    connection = pymysql.connect(user='root', password='root', database='starwarsDB')
    mycursor = connection.cursor()

    if isinstance(datas,list):

        for data in datas:
            columns_ = ", ".join(data.keys())
            primary_value = data.get("url").split("/")[-2]
            # print(primary_value)
            # print()
            values_1 = list(data.values())
            values_1.append(primary_value)
            # print("values_2:", values_1)

            # query = f"insert into {table} ({', '.join(data.keys())}) values {tuple(data.values())}"
            # query = f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)}"
            # print(query)
            # print()
            # print()

            try:
                # mycursor.execute(f"insert into {table} ({', '.join(data.keys())}) values {tuple(data.values())}")
                mycursor.execute(f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)}")
                connection.commit()
                print(f"{table} is updated with id {primary_value}...!!!")

            except:
                print(f"Could not add data in {table} for id {primary_value}")
        print("*"*30)


    else:
        columns_ = ", ".join(datas.keys())
        primary_value = datas.get("url").split("/")[-2]
        print(primary_value)
        # print()
        values_1 = list(datas.values())
        values_1.append(primary_value)
        # print("values_2:", values_1)

        # query = f"insert into {table} ({', '.join(data.keys())}) values {tuple(data.values())}"
        # query = f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)}"
        # print(query)
        # print()
        # print()

        try:
            # mycursor.execute(f"insert into {table} ({', '.join(data.keys())}) values {tuple(data.values())}")
            mycursor.execute(f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)}")
            connection.commit()
            print(f"{table} is updated with id {primary_value}...!!!")

        except:
            print(f"Could not add data in {table} for id {primary_value}")
        print("*" * 30)


if __name__ == '__main__':

    lis = [{'created': '2014-12-09', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/1/', 'name': 'Luke Skywalker', 'height': '1.72 mtr', 'mass': '77 kgs', 'hair_color': 'blond', 'skin_color': 'fair', 'eye_color': 'blue', 'birth_year': '19BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/1/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/2/', 'name': 'C-3PO', 'height': '1.67 mtr', 'mass': '75 kgs', 'hair_color': 'n/a', 'skin_color': 'gold', 'eye_color': 'yellow', 'birth_year': '112BBY', 'gender': 'n/a', 'homeworld': 'https://swapi.dev/api/planets/1/'}, {'created': '2014-12-10', 'edited': '2014-12-20', 'url': 'https://swapi.dev/api/people/3/', 'name': 'R2-D2', 'height': '0.96 mtr', 'mass': '32 kgs', 'hair_color': 'n/a', 'skin_color': 'white, blue', 'eye_color': 'red', 'birth_year': '33BBY', 'gender': 'n/a', 'homeworld': 'https://swapi.dev/api/planets/8/'}]
    store("characters3", "char_id", lis)