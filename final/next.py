import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="py_test",
)

ex = conn.cursor()

ex.execute("insert into users (name, age, address) values ('John', 30,'Tripoli'), ('Jane', 25,'Benghazi') ,('Doe', 22,'Misrata'), ('Alice', 28,'Sirt'), ('Bob', 35,'Derna')")
conn.commit()
print("Data inserted successfully")