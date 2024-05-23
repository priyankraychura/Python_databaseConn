import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="root", password="")

print(mydb, "Connection Established...")


