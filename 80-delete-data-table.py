import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS books 
            (title TEXT, pages INTEGER)''')

c.execute('INSERT INTO books VALUES("Are You My Mother?",72)')
conn.commit()
c.execute('INSERT INTO books (title) VALUES("Silence of the Lambs")')
conn.commit()

books = [
    ("Are You My Mother? 2",72),
    ("The Digging-Est Dog",72),
    ("The Giving Tree",66)
]
c.executemany('INSERT INTO books VALUES (?,?)',books)
conn.commit()

c.execute('SELECT rowid, title FROM books')
data3 = c.fetchall()
print(data3)

c.execute('SELECT * FROM books WHERE title = "Are You My Mother?"')
data4 = c.fetchall()
print(data4)

c.execute('DELETE FROM books WHERE title="Are You My Mother?"')
conn.commit()
c.execute('SELECT * FROM books')
data5 = c.fetchall()
print(data5)