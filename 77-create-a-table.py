
#boiler plate code
import sqlite3
#memory database
conn = sqlite3.connect(":memory:")
c = conn.cursor()

#create a table
c.execute('''CREATE TABLE IF NOT EXISTS books 
            (title TEXT, pages INTEGER)''')

