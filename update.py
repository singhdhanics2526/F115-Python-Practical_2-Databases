from sqlite3 import *

conn = connect("Studentinfo.db")
cur = conn.cursor()

cur.execute("""
    UPDATE Studentdata
    SET rollno = ?
    WHERE rollno = ?
""", (6, 1))
cur.execute("""
    UPDATE Studentdata
    SET rollno = ?
    WHERE rollno = ?
""", (7, 2))
conn.commit()
print("Roll number updated!")
conn.close()

