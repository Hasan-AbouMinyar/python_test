import mysql.connector


def connection():
    conn = mysql.connector.connect(
        host="localhost",
        user= "root",
        password="",
        database="py_test",
    )
    return conn

def insert(fields):
    conn = connection()
    ex = conn.cursor()
    sql = "insert into users (name,age,address) values (%s, %s, %s)"
    ex.execute(sql, fields)
    conn.commit()
    print("Data inserted successfully")
    conn.close()


    
conn = connection()


ex = conn.cursor()
ex.execute("delete from users where age = 25")
conn.commit()
print("Rows deleted:", ex.rowcount)
ex.execute("select * from users")

amg = ex.fetchone()

for  a in amg:
    print(a)