class Bank:
    def __init__(self, wolves_count=0, sheep_count=0, boat=None):
        self.__wolves_count = wolves_count
        self.__sheep_count = sheep_count
        self.__boat = boat

    def add_wolf(self):
        self.__wolves_count += 1

    def add_sheep(self):
        self.__sheep_count += 1

    def remove_wolf(self):
        self.__wolves_count -= 1

    def remove_sheep(self):
        self.__sheep_count -= 1

    def get_wolf_count(self):
        return self.__wolves_count

    def get_sheep_count(self):
        return self.__sheep_count

    def set_sheep_count(self, count: int):
        self.__sheep_count = count

    def set_wolf_count(self, count: int):
        self.__wolves_count = count

    def add_boat(self, boat):
        self.__boat = boat

    def remove_boat(self) -> 'Boat':
        boat = self.__boat
        self.__boat  = None
        return boat

    def get_boat_presence(self):
        return self.__boat

    def get_boat_wolf_count(self):
        if self.__boat is None:
            return 0
        return self.__boat.get_wolf_count()

    def get_boat_sheep_count(self):
        if self.__boat is None:
            return 0
        return self.__boat.get_sheep_count()




    def __repr__(self):
        return "Bank(wolves={}, sheep={})".format(self.__wolves_count, self.__sheep_count)


class Boat:
    def __init__(self):
        self.__wolves_count = 0
        self.__sheep_count = 0

    def add_wolf(self):
        self.__wolves_count += 1

    def add_sheep(self):
        self.__sheep_count += 1

    def remove_wolf(self):
        self.__wolves_count -= 1

    def remove_sheep(self):
        self.__sheep_count -= 1

    def get_wolf_count(self):
        return self.__wolves_count

    def get_sheep_count(self):
        return self.__sheep_count

    def get_animal_count(self):
        return self.__sheep_count + self.__wolves_count

    def set_sheep_count(self, count: int):
        self.__sheep_count = count

    def set_wolf_count(self, count: int):
        self.__wolves_count = count

    def __repr__(self):
        return "Boat(wolves={}, sheep={})".format(self.__wolves_count, self.__sheep_count)