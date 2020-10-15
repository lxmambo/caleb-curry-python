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

book = Book("are you my mother", 72)
book2 = Book("the digging-est Dog", 103)

Book.favorites.append(book)
Book.favorites.append(book2)
print(Book.favorites)

for b in Book.favorites:
    print(b.title)