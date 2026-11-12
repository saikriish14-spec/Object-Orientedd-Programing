class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(f"{self.title} by {self.author} has been borrowed")


    def return_book(self):
        self.is_borrowed = False
        print(f"{self.title} by. {self.author} has been returned")

book1 = Book("Harry Potter", "J.K Rowling")
book2 = Book("The Lion King", "Disney")
book3 = Book("The power of your subconcious mind", "Joseph murphy")

book1.borrow()
book2.borrow()
book1.return_book()
book3.borrow()
book2.return_book