#Create table
from sqlite3 import *
conn = connect("Studentinfo.db")
cur = conn.cursor()
cur.execute('CREATE TABLE Studentdata (sname varchar, rollno int, course varchar, email varchar, contact int)')
print("Table Created!")