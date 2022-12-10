import random


def for_people():
    return (random.randrange(1,83)for i in range(1,16))

def for_films():
    return (random.randrange(1,7) for i in range(1,7))
