from sqlite3 import *

conn = connect("Studentinfo.db")
cur = conn.cursor()

cur.execute("SELECT * FROM Studentdata")
rows = cur.fetchall()

for row in rows:
    print(row)
    
conn.close()
