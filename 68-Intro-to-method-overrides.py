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

book = Book("are you my mother", 72)
book2 = Book("the digging-est Dog", 103)

Book.favorites.append(book)
Book.favorites.append(book2)
print(Book.favorites)

for b in Book.favorites:
    print(b)
    print(b.title)