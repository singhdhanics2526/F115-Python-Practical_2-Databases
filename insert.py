#Insert records
from sqlite3 import *
conn = connect("Studentinfo.db")
cur = conn. cursor()
cur.execute('INSERT INTO Studentdata values("Jaya", 1, "CS", "jaya123@gmail.com", 9087546742)')
cur.execute('INSERT INTO Studentdata values("Aarna", 2, "IT", "aarna123@gmail.com", 9087546742)')
cur.execute('INSERT INTO Studentdata values("Shreya", 3, "CS", "shreya123@gmail.com", 9087546742)')
cur.execute('INSERT INTO Studentdata values("Aditi", 3, "IT", "aditi123@gmail.com", 9087546742)')
cur.execute('INSERT INTO Studentdata values("Riya", 4, "CS", "riya123@gmail.com", 9087546742)')
cur.execute('INSERT INTO Studentdata values("Bindu", 5, "IT", "bindu123@gmail.com", 9087546742)')
print("Data inserted into Studentdata table!")
conn.commit()
conn.close()