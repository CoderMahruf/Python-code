class Library:
    def __init__(self):
        self.noBook = 0
        self.books = []
    def addbook(self,book):
        self.books.append(book)
        self.noBook = len(self.books)
    def showInfo(self):
        print(f"The library has {self.noBook} Books.The books are")
        for book in self.books:
            print(book)
obj = Library()
obj.addbook("Fluent Python")
obj.addbook("Python Programming language")
obj.addbook("Learn Python coding")
obj.addbook("Black Hat Python")
obj.showInfo()
