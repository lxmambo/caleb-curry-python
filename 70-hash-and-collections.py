#when we override the __eq__ method is best
#pratice to deal with the __hash__ method
#we can have our one implementation or just not having it
#__hash__ = none is the default when we override __eq__ (book is not hashable)
#hash method is used for any of the hashing data structures which includes sets 
#and dictionaries
# if we try to do a set with objects, they are not hashable
#everytime we put something in a set, it get's hashed

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
    
    #__hash__ = None #in this case our data structure is not hashed
    #this class is not suppposed to be used for hashing
    #we want to do this for mutable types, we shouldn't hash mutable data
    #the hash is derived from the data we are storing, so if we updata
    #the data, we change the hash. We can use mutable data for hashing
    #but we cannot change it

book = Book("are you my mother", 72)
book2 = Book("the digging-est Dog", 102)

#we create a set and pass book and book2
#data = {book,book2}
#it says unhashable type: 'Book'
#everytime we put something in a set it gets hashed
#strings and keys of dictionaries are hashable
#-> a dictionary with key:string is hashable
#data = {"hell":book}
#it ok because the value is not hashed, only the key
#a list is not hashable too

#if we don't want our data structure to be hashable __hash__ = None
#this is telling that this class is not supposed to be used for hashing
#we may want to do that for mutable types, for example, in we want
#to change books titles, pages, etc because the hash is computed from
#the stored data, if the data changes, the hash can change...


books = {book, book2} # -> after overriding the hash method
#we can build this set of objects

print(hash(book)) #prints the hash of the book object
book.title = "something else"
print(hash(book)) #ater we changed the title, we get a diferent hash value
#we don't want the hash to change...because the hash is used to derive 
#an index location for this data structures

#another thing: if 2 objects are consired equal accordingly to the the
#equal override definition, they should have the same hash

book2.title = "something else"
book2.pages = 72

print(book == book2)
print(hash(book) == hash(book2))