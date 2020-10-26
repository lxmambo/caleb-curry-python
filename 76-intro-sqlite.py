#mantain the state of an application. writin in text files
#is not a good long term solution

import sqlite3

#we pass the name of database or keep it in RAM
conn = sqlite3.connect(":memory:")
#we open the connection to the database and give
#a reference to it
