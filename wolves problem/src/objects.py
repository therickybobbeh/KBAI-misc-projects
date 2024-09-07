class Bank:
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

    def set_sheep_count(self, count: int):
        self.__sheep_count = count

    def set_wolf_count(self, count: int):
        self.__wolves_count = count

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