import Book 


my_book = book.Book("Egri csillagok", 10)
# my_book.read_up()

my_book2 = book.Book("Könyv2", 20)
my_book2.read_up()
#print(my_book2.__gross_price())

book.Book.list_all_books()
book.Book.say_hello_to_librarian()
