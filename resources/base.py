not_implemented_error_msg = "This method has not been implemented"


# TODO - you can also convert this class into abstract class and
# define methods as abstract methods


class ResourceBase(object):
    """
    Base class representing required methods to be implemented by all resource
    classes
    """

    resources = ["planets", "spaceships", "people", "vehicles", "films", "species"]

    def __init__(self):
        self.home_url = "https://swapi.dev/"

    def get_count(self):
        raise NotImplementedError(not_implemented_error_msg)

    def get_resource_urls(self):
        raise NotImplementedError(not_implemented_error_msg)

# print("https://swapi.dev/api/planets")
# print("https://swapi.dev/api/starships")
# print("https://swapi.dev/api/species")
# print("https://swapi.dev/api/films")