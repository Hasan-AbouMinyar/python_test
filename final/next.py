import mysql.connector

ssqqll = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)


db_name = ssqqll.cursor()

db_name.execute("create database if not exists py_test")