import mysql.connector

me = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

print(me)