#mirar para tres tablas que el default ponga la fecha del sistema, validación tipo check
import sqlite3

conn = sqlite3.connect("prueba.db")
cur = conn.cursor()
# Cambia cur.execute por cur.executescript para que te permita crear ambas tablas a la vez

cur.executescript("""

CREATE TABLE IF NOT EXISTS temporadas (
    numero INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    fecha_creacion TEXT DEFAULT (datetime('now', 'localtime')),
    UNIQUE(nombre)
);

CREATE TABLE IF NOT EXISTS personajes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    es_gay TEXT NOT NULL CHECK(es_gay IN('si', 'no')),
    temporada TEXT NOT NULL REFERENCES temporadas(nombre) ON DELETE CASCADE,
    UNIQUE(nombre)
);

""")


sql = "INSERT INTO temporadas (nombre) VALUES (?)"
#cur.execute(sql,["Ragdoll&Crew"])
sql = "INSERT INTO personajes (nombre, es_gay, temporada) VALUES (?, ?, ?)"
cur.execute(sql,["Mia", "si", "Ragdoll&Crew"])

conn.commit()
conn.close()