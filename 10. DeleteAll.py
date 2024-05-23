import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="", database="py_db")
db_cursor = mydb.cursor()

db_deleteData = "TRUNCATE table emp"
db_cursor.execute(db_deleteData)
mydb.commit()
print("Whole table deleted!")