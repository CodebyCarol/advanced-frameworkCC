class Book:

    instances = []

    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.__class__.instances.append(self)

    @classmethod
    def list_all_books(cls):
        for instance in cls.instances:
            print(cls.title)

    @staticmethod
    def read_up_itself(self):
        print(self.title)        
