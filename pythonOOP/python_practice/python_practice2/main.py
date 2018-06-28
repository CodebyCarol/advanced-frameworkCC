from book import Book


class Main:

    def __init__(self):
        book1 = Book("Lord of the Rings", 3000)
        book2 = Book("Rings of the Lords", 2900)
        book1.read_up_itself(book1)
        book2.read_up_itself(book2)

m = Main()