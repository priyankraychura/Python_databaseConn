import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="", database="py_db")
db_cursor = mydb.cursor()

roll = int(input("Enter roll number: "))
name = input("Enter name: ")
db_insert = "INSERT INTO emp(Roll, Ename) VALUES(%s, %s)"
db_list = (roll, name)
db_cursor.execute(db_insert, db_list)
mydb.commit()
print(db_cursor.rowcount, "Record Inserted!", db_cursor.lastrowid)

mydb.close()