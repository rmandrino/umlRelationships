# Part class
class Book:
    def display(self):
        print("This is a book")


# Whole class
class Library:
    def __init__(self, book):
        self.book = book

    def show_book(self):
        self.book.display()


# Main program
book = Book()  # Created independently
library = Library(book)

library.show_book()
