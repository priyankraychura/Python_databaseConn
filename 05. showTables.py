import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="", database="py_db")
db_cursor = mydb.cursor()
db_cursor.execute("SHOW TABLES")
for i in db_cursor:
    print(i)


