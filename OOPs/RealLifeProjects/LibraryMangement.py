"""
Implement a library management system which will handle the following tasks using OOP concepts:
1. Customer should be able to display all the books available in the library.
2. Handle the process when a customer requests to borrow a book.
3. Update the library collection when the customer returns a book.

Solution approach:
Nouns-> Customer, book
Adjectives->
Verbs-> borrow, return
"""

#Class -> Library
#Layers of abstractions -> to display the available books, to lend a book, add a book

#Class -> Customer
#Layers of abstractions -> request for a book, return a book

class Library:
    def __init__(self, availableBooks):
        self.availableBooks = availableBooks
        
    def displayAvailableBooks(self):
        print()
        print("Available Books:-")
        print()
        for book in self.availableBooks:
            print(book)
    
    def lendBook(self, requestedBook):
        if (requestedBook in self.availableBooks):
            print("You have now borrowed the book from the library")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry! The book is not available...")
    
    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have successfully returned the book. Thank you! Keep Learning")
    
class Customer:
    def requestBook(self):
        print("Enter the book name you want to borrow")
        self.requestBook = input()
        return self.requestBook
    
    def returnBook(self):
        print("Enter the book name you want to return")
        self.returnBook = input()
        return self.returnBook

availableBooks = ['Think and Grow Rich', 'Who will Cry when you die', 'The Monk who sold his Ferrari']
library = Library(availableBooks)
customer1 = Customer()
library.displayAvailableBooks()

while(True):
    print()
    print("Enter 1 to display available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit.")
    print()
    userChoice = int(input())
    if userChoice == 1:
        library.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = customer1.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnBook = customer1.returnBook()
        library.addBook(returnBook)
    elif userChoice == 4:
        quit()
        
