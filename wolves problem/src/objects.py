class Bank:
    def __init__(self):
        self.wolves = []
        self.sheep = []

    def add_wolf(self, wolf):
        self.wolves.append(wolf)
    def add_sheep(self, sheep):
        self.sheep.append(sheep)

    def __repr__(self):
        return "Bank(wolves={}, sheep={})".format(self.wolves.len, self.sheep.len)

class Boat:
    def __init__(self):
        self.wolves = []
        self.sheep = []

    def add_wolf(self, wolf):
        self.wolves.append(wolf)
    def add_sheep(self, sheep):
        self.sheep.append(sheep)

    def __repr__(self):
        return "Boat(wolves={}, sheep={})".format(self.wolves.len, self.sheep.len)


class Sheep:
    def __init__(self, sheep_number = 0):
        self.sheep_number = sheep_number

    def set_number_of_sheep(self, sheep_number):
        self.sheep_number = sheep_number

    def __repr__(self):
        return "sheep(sheep_number={})".format(self.sheep_number)


class Wolf:
    def __init__(self, wolf_number = 0):
        self.wolf_number = wolf_number

    def set_number_of_sheep(self, wolf_number):
        self.wolf_number = wolf_number

    def __repr__(self):
        return "Wolf(wolf_number={})".format(self.wolf_number)

