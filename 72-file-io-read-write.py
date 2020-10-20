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

file = open("input.txt",'w') #w overwrites, a appends if the file exists
file.write("are you my mother?\t72\n")
file.write("humman bondage\t108")
file.close()
file = open('input.txt','r')
#data = file.read()
data = file.read().split('\n') #this way creates a list
file.close()
print(data)

book1_data = data[0].split('\t')
print(len(data))
print(len(book1_data))
print(book1_data)
book1 = Book(book1_data[0], book1_data[1])
book2 = Book(data[1].split('\t')[0],data[1].split('\t')[1])
print(book1)
print(book2)