import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="", database="py_db")
db_cursor = mydb.cursor()

db_cursor.execute("SELECT * FROM emp")

# db_select = db_cursor.fetchall()
# db_select = db_cursor.fetchone()
# print(db_select)

for db_data in db_cursor.fetchall():
    print(db_data)

