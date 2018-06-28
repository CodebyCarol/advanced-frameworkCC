from plant import Plant


class Cactus(Plant):

    def __init__(self, name, size, max_size):
        self.name = name
        self.size = size
        self.max_size = max_size
        Plant.plants.append(self)