import pymysql as ps
import csv

connector = ps.connect(
    host="localhost",
    user="root",
    password="root",
    database='practice'
)
mycursor = connector.cursor()

# try:
#     # mycursor.execute("use sakila")
#     # # mycursor.execute("create table Trial (full_name VARCHAR(20), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#     # # db = "INSERT INTO Trial (full_name, age) VALUES('suraj',19)"
#     # # mycursor.execute(db)
#     # # connector.commit()
#     # db = "select * from category"
#     # mycursor.execute(db)
#     # for i in mycursor:
#     #     print(i)
#     # # print(type(mycursor))
#     # # print(mycursor)
#     print("Connected to MySQL".center(60, "-"))
#     mycursor = connector.cursor()
#     sql = "select * from category;"
#
#     print(f"No. of rows - {mycursor.execute(sql)}")
#     result = mycursor.fetchall()
#     for row in result:
#         print(row)
#     # for i in mycursor:
#     #     print(i)
#
#     connector.close()
#     mycursor.close()
#     print("MySQL connection closed.".center(60, "-"))


from task2 import Swapi
val = []
s = Swapi()

for key,value in s.result.items():
    if isinstance(value, list):
        # pass
        val.append(", ".join(value))
    else:
        val.append(value)
# print(tuple(val))



# columns = (film_id, title, episode_id, opening_crawl, director, producer, release_date, created, edited, url)
# #
# try :
#     print("in")
#     mycursor.execute("use practice;")
#     # mycursor.execute(f"""INSERT INTO film (title, episode_id, opening_crawl, director, producer, release_date, characters, planets, starships,vehicles,species, created, edited, url) VALUES {tuple(val)};""")
#     mycursor.execute(f"""INSERT INTO film (", ".join(s.result.keys()) VALUES {tuple(val)};""")
#
#     connector.commit()
#     print("done")
#
# except:
#     print("Database error")

# f = ["https://swapi.dev/api/people/1/", "https://swapi.dev/api/people/2/", "https://swapi.dev/api/people/3/", "https://swapi.dev/api/people/4/", "https://swapi.dev/api/people/5/", "https://swapi.dev/api/people/10/", "https://swapi.dev/api/people/13/", "https://swapi.dev/api/people/14/", "https://swapi.dev/api/people/18/", "https://swapi.dev/api/people/20/", "https://swapi.dev/api/people/21/", "https://swapi.dev/api/people/22/", "https://swapi.dev/api/people/23/", "https://swapi.dev/api/people/24/", "https://swapi.dev/api/people/25/", "https://swapi.dev/api/people/26/"]
# print(", ".join(f))
# # a = (str(f))
# # print(a)