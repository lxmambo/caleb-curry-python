#mantain the state of an application. writin in text files
#is not a good long term solution

import sqlite3

#we pass the name of database or keep it in RAM
conn = sqlite3.connect(":memory:")
#we open the connection to the database and give
#a reference to it

#conn = sqlite3.connect("example.db")
#this would create a database in our parent directory
#the file appears in the terminal folder

#we have to create a cursor, a tool used to work
#with the database and establish a reference to it

c = conn.cursor()

#c has methods
#this creates the foundation to start working/create our first table

#execute allows to use sql directly in to the database
c.execute('''CREATE TABLE IF NOT EXISTS books 
            (title TEXT, pages INTEGER)''')
#TEXT and INTEGER are data types

#To do multiple lines we use the three '''
