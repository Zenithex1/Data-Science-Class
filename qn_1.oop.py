"""
Question: Library Book Management System
Create a class named Book.
Attributes


    title (string)
    author (string)
    totalCopies (integer)
    availableCopies (integer)
Constructor
Create a constructor that initializes all attributes when a Book object is created.

Methods
Implement the following methods:

borrowBook()
    Decrease availableCopies by 1.
    If no copies are available, display an appropriate message.
returnBook()
    Increase availableCopies by 1.
    Do not allow availableCopies to exceed totalCopies.
addCopies(int copies)
    Increase both totalCopies and availableCopies by the given number.
isAvailable()
    Return true if at least one copy is available, otherwise false.
displayBookInfo()
    Display all book details in a readable format.



"""


class Book:

    def __init__(self, title, author, totalCopies, availableCopies):
        self.title = title
        self.author = author
        self.totalCopies = totalCopies
        self.availableCopies = availableCopies

    def borrowBook(self):
        if self.availableCopies <= 0:
            return "No book available"
        else:
            self.availableCopies = self.availableCopies - 1
            print(self.displayBookInfo())
            return "Book Borrow Successfully"

    def returnBook(self):
        if self.totalCopies < self.availableCopies +1:
            return "Unable to return book"
        else:q

            self.availableCopies = self.availableCopies +1
            print(self.displayBookInfo())

            return "Book Return  Successfully"

    def addCopies(self, copies):
        self.availableCopies = self.availableCopies+copies
        self.totalCopies = self.totalCopies+copies
        print(self.displayBookInfo())

        return "Successfully Added"

    def isAvailable(self):
        if not self.availableCopies<=0:
            return True
        else:
            return False

    def displayBookInfo(self):
        return (
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Total Copies: {self.totalCopies}, "
            f"Available Copies: {self.availableCopies}"
    )

obj = Book("Python", "Broadway", 1, 1)
print(obj.displayBookInfo())
print(obj.borrowBook())

# print(obj.returnBook())
# print(obj.returnBook())
# print(obj.returnBook())


print(obj.isAvailable())
print(obj.addCopies(10))
print(obj.returnBook())
