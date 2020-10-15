#override of __str__ method

class Book():

    favorites = [] #class level atribute. all objects

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
    def __str__(self):
        #define string representation of the objecs
        #we are gonna use string formatting with fstring
        return f"{self.title} is {self.pages} pages long."
    def __eq__(self,book):
        print("self:",self)
        print("book:",book) #printing books using __str__override
        if(self.title == book.title and self.pages == book.pages):
            return "books are equal"
        return "books are diferent"

book = Book("are you my mother", 72)
book2 = Book("the digging-est Dog", 102)

Book.favorites.append(book)
Book.favorites.append(book2)
print(Book.favorites)

for b in Book.favorites:
    print(b)
    print(b.title)

print(book == book2)
#the default object comparison is comparing 
#memory address if book2 = book, then book2 == book 
#would return true