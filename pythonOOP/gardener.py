# in JAVA: public Class Plant{}
class Plant:

    #ALL class members (including data members) are public in Python and all the methods are virtul.

    live = True
    number_of_plants = 0

    def __init__(self, size, limit_of_proliferation, name):
        self.size = size
        self.limit_of_proliferation = limit_of_proliferation
        self.name = name
        Plant.number_of_plants += 1

    def is_live():
        pass

    def increase_size(change_with):
        pass

    def decrease_size(change_with):
        pass

    def die():
        print("{} has been died!".format(self.name))
        self.live = False
        number_of_plants -= 1

        if number_of_plants == 0:
            print("{} was the last plant, the whole garden is dead!".format(self.name))
        else:
            pass

    def water():
        pass

    def nutritiate():
        pass

    def fertilize():
        pass                 

# in JAVA: public Class Cactus extends Plant {}
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


