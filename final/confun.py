import mysql.connector

def call():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="py_test",
    )
    return conn

def select(query):
    conn = call()
    ex = conn.cursor()
    ex.execute(query)
    return ex.fetchall()

def insert(query):
    conn = call()
    ex = conn.cursor()
    ex.execute(query)
    conn.commit()


def specific( table, fields):
    conn = call()
    ex = conn.cursor()
    str_f = ",".join(fields)
    quary = f"Select {str_f} from {table}"
    ex.execute(quary)
    return ex.fetchall()
    


# hasan = select("select * from users")

# for i in hasan:
#     print(" ")
#     for j in i:
#         print(j)


mg = specific("users",["name"])

for i in mg:
    print(" ")
    for j in i:
        print(j)


