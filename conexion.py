import sys
import pyodbc
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\cuc\Documents\Database")
cursor=conn.cursor()
cursor.execute("SELECT * FROM persona")
for row in cursor.fetchall():
    print()
cursor.close
conn.close