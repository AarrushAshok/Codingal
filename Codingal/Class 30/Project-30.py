#Inheritance Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def show_info(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def show_info(self):
        return f"EBook: {self.title} by {self.author}"

class AudioBook(Book):
    def show_info(self):
        return f"AudioBook: {self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return
    def show_all_books(self):
        for book in self.books:
            print(book.show_info())

def main():
    library = Library()
    book1 = Book("Harry Potter", "J.K. Rowling")
    ebook1 = EBook("Python 101", "John Doe")
    audiobook1 = AudioBook("The Alchemist", "Paulo Coelho")
    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(audiobook1)
    library.show_all_books()
    library.remove_book("Harry Potter")
    library.show_all_books()

if __name__ == "__main__":
    main()