import sqlite3

#consulta sobre usuarios
conn = sqlite3.connect("prueba.db")
cur = conn.cursor()

sql = "SELECT * from usuarios WHERE edad > 18"
cur.execute(sql)
'''
#iterar tal cual
for r in cur:
    print(r)
'''
#fetch
'''
res = cur.fetchone()
print(res)
res = cur.fetchone()
print(res)
'''
#fetchall
'''
res = cur.fetchall()
print(res)
'''
#fetchmany
res = cur.fetchmany(20) #--> enseña las que hay guardadas incluso si el número es superior
print(res)

conn.close()