
#boiler plate code
import sqlite3
#memory database
conn = sqlite3.connect(":memory:")
c = conn.cursor()

#create a table
c.execute('''CREATE TABLE IF NOT EXISTS books 
            (title TEXT, pages INTEGER)''')

#working with the cursor object
c.execute('INSERT INTO books VALUES("Are You My Mother",72)')
#working with the connection. Use commit everytime you want
#to insert data in the table
conn.commit()

#if we don't want to specify a field...
c.execute('INSERT INTO books (title) VALUES("Silence of the Lambs")')