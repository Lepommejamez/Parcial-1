from libraryModule import Library
from libraryModule import User
from libraryModule import Librarian
from libraryModule import Book

#Creates new Library and Librarian.
libraryName = "Biblioteca KCP"
librarianName = "Daniel"
MyLibrary = Library(libraryName)
librarian1 = Librarian(librarianName, MyLibrary)

book1 = Book("Percy Jackson", True)
book2 = Book("Harry Potter", True)
librarian1.addBook(book1)
librarian1.addBook(book2)

user1 = User("Jimbo", MyLibrary)
user1.borrow("Percy Jackson")
user1.returnBook("Percy Jackson")
