from book import Book


book1 = Book("Lord of the Rings", 3000)
book2 = Book("Rings of the Lords", 2900)
book1.read_up_itself()
book2.read_up_itself()
book1.list_all_books()
#when you calling a static method, you should whrite the instances to replace "self"
book1.say_hello_to_librarian(book1)
book1.gross_price()
