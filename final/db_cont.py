import mysql.connector

call = mysql.connector.connect(
    host="localhost",
    user="roor",
    password="",
)

print(call)

call.close()