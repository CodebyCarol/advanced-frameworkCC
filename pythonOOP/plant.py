# in JAVA: public Class Plant{}
class Plant:

    #ALL class members (including data members) are public in Python and all the methods are virtual.

    live = True
    number_of_plants = 0

    def __init__(self, size, limit_of_proliferation, name):
        self.size = size
        self.limit_of_proliferation = limit_of_proliferation
        self.name = name
        Plant.number_of_plants += 1

    #without annotation it is static by default
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

