class Book():

    instances = []
    title

    @classmethod
    def list_all_books(cls):
        print("These are the books in the library:")
        for instance in cls.instances:
            print(instance.title)

    @staticmethod
    def say_hello_to_librarian():
        print("Hello librarian")

    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.__class__.instances.append(self)

    def read_up(self):
        print(self.title)

    def __gross_price(self):
        return 1.27 * self.price

print("bases: ", Book.__bases__)
print("module: ", Book.__module__)

