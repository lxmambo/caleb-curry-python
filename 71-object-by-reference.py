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
    #override of hash method
    def __hash__(self):
        #hash the individual components of the object and exclusive or them
        return hash(self.title) ^ hash(self.pages)
    
book = Book("are you my mother?",72)
book2 = Book("are you my mother?",72)

print(id(book))
#id is unique between objects in existence
#it uses the object memory address