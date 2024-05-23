import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="", database="py_db")
db_cursor = mydb.cursor()

db_deleteData = "DELETE FROM emp WHERE Roll = %s"
set_value = (5,)
db_cursor.execute(db_deleteData, set_value)
mydb.commit()
print(db_cursor.rowcount, "Record Deleted!")