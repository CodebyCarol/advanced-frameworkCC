# in JAVA: public Class Cactus extends Plant {}
# can have multiple parent class (check how solved the diamond problem in python)
# there is no abstract class, no interface
class Cactus(Plant):

    def __init__(self, size, name):
        # Python does not automatically call the constructor of the base class Plant, you have to explicitly call it yourself.
        Plant.__init__(self)
        self.size = size
        self.limit_of_proliferation = 4
        self.name = name

    def water():
        Plant.decrease_size(1)
        
    def nutritiate():
        Plant.increase_size(1)

    def fertilize():
        Plant.increase_size(1)
