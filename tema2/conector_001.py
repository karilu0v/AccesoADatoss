import sqlite3

conn = sqlite3.connect("prueba.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL DEFAULT 18
);
""")

sql = "INSERT INTO usuarios (nombre, edad) VALUES (?, ?)"
cur.execute(sql, ["Ragdoll", 20])
conn.commit()
conn.close()