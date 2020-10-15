class Book():
    def __init__(self, title,pages):
        print("creating book")
        self.title = title
        self.pages = pages
    def upup(self):
        #uppercase method
        return self.title.upper()
    def is_long(self):
        if self.pages > 100:
            return True
        return False

book = Book("are you my mother?",72)

print(book.title)
print(book.upup())
print(book.is_long())

book2 = Book("another book",101)
print(book2.is_long())
#methods are functions attached to objects
