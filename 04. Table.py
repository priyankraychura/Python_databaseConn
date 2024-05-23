import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="", database="py_db")
db_cursonr = mydb.cursor()

db_cursonr.execute("CREATE TABLE Emp2(Roll int, Ename varchar(20))")

print("Table created!")

