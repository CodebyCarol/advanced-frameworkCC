import Plant
# in JAVA: public Class Cactus extends Plant {}
# can have multiple parent class (check how solved the diamond problem in python)
# there is no abstract class, no interface


class Cactus(Plant):

    size = 2

    def __init__(self, size, limit_of_proliferation, name):
        # Python does not automatically call the constructor of the base class Plant, you have to explicitly call it yourself.
        Plant.__init__(self)
        self.size = super
        self.limit_of_proliferation = limit_of_proliferation
        self.name = name
        cactus1 = Cactus(4, "tesztkaktusz")
        print(self)

    def water():
        Plant.decrease_size(1)

    def nutritiate():
        Plant.increase_size(1)

    def fertilize():
        Plant.increase_size(1)
