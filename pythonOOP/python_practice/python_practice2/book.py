class Book:

    instances = []

    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.__class__.instances.append(self)

    @classmethod
    def list_all_books(cls):
        for instance in cls.instances:
            print(instance.title)

    def read_up_itself(self):
        print(self.title)    

    @staticmethod
    def say_hello_to_librarian(self):
        print("Hello Librarian!")
