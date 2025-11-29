# Insert records using executemany
from sqlite3 import *

conn = connect("Studentinfo.db")
cur = conn.cursor()

data = [("Muskan",   1, "CS", "muskan123@gmail.com",   9087546742),
    ("Zainab",  2, "CS", "zainab123@gmail.com",  9087546742)]

cur.executemany( "INSERT INTO Studentdata VALUES (?, ?, ?, ?, ?)",data)

conn.commit()
print("Data inserted into Studentdata table!")
conn.close()
