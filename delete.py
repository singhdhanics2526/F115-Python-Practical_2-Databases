from sqlite3 import *

conn = connect("Studentinfo.db")
cur = conn.cursor()

cur.execute("DELETE FROM Studentdata WHERE rollno = ?", (3,))

conn.commit()
print("Record deleted!")
conn.close()
