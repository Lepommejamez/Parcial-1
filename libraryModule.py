class Book:
    name = ""
    def __init__(self, name: str, isAvailable: bool) -> None:
        """
        Constructor method
        Parameters: name of the book, and availability of the book.
        
        """
        self.name = name
        self.isAvailable = isAvailable

class Library():  
    def __init__(self, name: str) -> None:
        """
        Constructor method
        Parameters: name of the library
        
        """
        self.name = name
        self.books = {}

class Librarian:
    def __init__(self, name: str, library: Library) -> None:
        """
        Constructor method
        Parameters: name of the librarian, and library he belongs to
        
        """
        self.name = name
        self.library = library

    def addBook(self, book: Book) -> None:
        """
        Adds a book object to the library.
        """
        self.library.books.update({book.name: book})

    def getBook(self, name: str) -> Book:
        """
        Finds a book in the library by name and returns the object
        
        """
        return self.library.books[name]

    def _setBookStatus(self, bookName: str, status: bool) -> None:
        """
        Changes availability of a book
        
        """
        self.library[bookName].availability = status

class User:
    def __init__(self, name: str, library: Library) -> None:
        """
        Constructor method
        Parameters: name of the user, and library he belongs to
        """
        self.name = name
        self.borrowedBooks = {}
        self.library = library

    def borrow(self, bookName: str):
        """
        finds a book in the library by name, and adds it to the list of borrowed books
        """
        tempBook = self.library.books[bookName]
        self.borrowedBooks.update({bookName: tempBook})

    def returnBook(self, bookName: str):
        """
        finds a book in borrowed books by name, and removes it.
        """
        self.tempBook = self.library.books[bookName]
        self.borrowedBooks.pop(bookName)
