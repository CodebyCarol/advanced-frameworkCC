from plant import Plant
from cactus import Cactus


class Garden:
    '''this is the place where gardeners working'''

    def __init__(self, name):
        self.name = name
        print(" New Garden opened")

    def gardening(self):
        plant1 = Plant("noveny")
        print(plant1.name, "has been planted")

        cactus1 = Cactus("karacsonyi kaktusz", 5, 7)
#        cactus1.tell_my_name()
        print(cactus1.name, "has been planted")
        print("There is", len(Plant.plants), "plant in the Garden")

        cactus1.die()
        print("There is", len(Plant.plants), "plant in the Garden")

        plant1.die()
        print("There is", len(Plant.plants), "plant in the Garden")


garden = Garden("New Garden")

garden.gardening()
