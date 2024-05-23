import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="", database="py_db")
db_cursonr = mydb.cursor()

db_insert = "INSERT INTO emp(Roll, Ename) VALUES(%s, %s)"
db_list = [(3, "Mohan"), (4, "Rohan"), (5, "Chaman")]
# db_cursonr.execute(db_insert, db_list)
db_cursonr.executemany(db_insert, db_list)
mydb.commit()
print(db_cursonr.rowcount, "Record Inserted!")