import sqlite3

with sqlite3.connect("prueba.db") as conn:
    cur = conn.cursor()
    SELECT = "SELECT * FROM personajes;"
    cur.execute(SELECT)
    for r in cur:
        print(r[:2])