import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="", database="py_db")
db_cursonr = mydb.cursor()

db_update = "UPDATE emp SET Ename = %s WHERE Roll = %s"
set_value = ("Raman", 5)
db_cursonr.execute(db_update, set_value)
mydb.commit()
print(db_cursonr.rowcount, "Record Updated!")