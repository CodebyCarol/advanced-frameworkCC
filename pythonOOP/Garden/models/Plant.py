import abc


# in JAVA: public Class Plant{}
class Plant(object):
    __metaclass__ = abc.ABCMeta

    # ALL class members (including data members) are public in Python and all the methods are virtual.

    live = True
    number_of_plants = 0
    size = 0
    limit_of_proliferation = 0

    def __init__(self, size, limit_of_proliferation, name):
        self.size = size
        self.limit_of_proliferation = limit_of_proliferation
        self.name = name
        Plant.number_of_plants += 1

    # without annotation it is static by default
    def is_live():
        if limit_of_proliferation <= size:
            live = False

    def increase_size(change_with):
        size += change_with

    def decrease_size(change_with):
        size -= change_with

    def die():
        print("{} has been died!".format(self.name))
        self.live = False
        number_of_plants -= 1

        if number_of_plants == 0:
            print("{} was the last plant, the whole garden is dead!".format(self.name))
        else:
            pass

    @abc.abstractmethod
    def water():
        pass

    @abc.abstractmethod
    def nutritiate():
        pass

    @abc.abstractmethod
    def fertilize():
        pass