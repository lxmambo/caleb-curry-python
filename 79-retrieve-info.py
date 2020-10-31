
#boiler plate code
import sqlite3
#memory database
conn = sqlite3.connect(":memory:")
c = conn.cursor()

#create a table
c.execute('''CREATE TABLE IF NOT EXISTS books 
            (title TEXT, pages INTEGER)''')

#working with the cursor object
c.execute('INSERT INTO books VALUES("Are You My Mother?",72)')
#working with the connection. Use commit everytime you want
#to insert data in the table
conn.commit()

#if we don't want to specify a field...
c.execute('INSERT INTO books (title) VALUES("Silence of the Lambs")')

#to retrieve info we use 'SELECT'. to grab everything we use *

c.execute('SELECT * FROM books') #here we select everything, and now ->
data = c.fetchone() #we have more two options, fetchmany and fetchall
#fetch all gives a list of tuples
print(data)
data2 = c.fetchall()
print(data2)

#let's create a list of tuples
books = [
    ("Are You My Mother? 2",72),
    ("The Digging-Est Dog",72),
    ("The Giving Tree",66)
]

c.executemany('INSERT INTO books VALUES (?,?)',books)
conn.commit()
c.execute('SELECT * FROM books')
data3 = c.fetchall()
print(data3)

c.execute('SELECT * FROM books WHERE title = "Are You My Mother?"')
data4 = c.fetchall()
print(data4)