from plant import Plant


class Garden:
    '''this is the place where gardeners working'''

    def __init__(self, name):
        self.name = name
        print(" New Garden opened")

    def gardening(self):
        plant1 = Plant("noveny")
        plant1.tell_my_name
        print(plant1.name, "has been planted")

garden = Garden("New Garden")

garden.gardening()
