import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="")
db_cursor = mydb.cursor()
db_cursor.execute("SHOW DATABASES")
for i in db_cursor:
    print(i)


