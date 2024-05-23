import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="")
db_cursonr = mydb.cursor()

db_cursonr.execute("CREATE DATABASE py_db")

print("Databse created!")