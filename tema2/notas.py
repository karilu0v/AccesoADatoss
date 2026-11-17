import sqlite3

SCHEMA = """
        CREATE TABLE IF NOT EXISTS notas(
            id INTEGER PRIMARY KEY,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            tittle TEXT NOT NULL CHECK (LENGTH(tittle)<=50),
            description TEXT NOT NULL CHECK (LENGTH(description)>5)
        );
        """

with sqlite3.connect("prueba.db") as conn:
    cur = conn.cursor()
    cur.executescript(SCHEMA)
    print("Esquema creado")

def borrar_nota():
    id_borrar= input("ingrese el id de la nota a borrar:\n")
    try:
        ind_borrar = int(id_borrar)
        with sqlite3.connect("prueba.db") as conn:
            cur = conn.cursor()
            SQL_D = "DELETE FROM notas WHERE id=?;"
            SQL_S= "SELECT id FROM notas WHERE id=?;"
            cur.execute(SQL_S, (id_borrar,))
            registro = cur.fetchall()
            if len(registro) != 1:
                print(f"La nota con id {id_borrar} no existe")
                raise sqlite3.IntegrityError("id no existe")
            cur.execute(SQL_D, (id_borrar,))
            print(cur.rowcount)
    except ValueError:
        print("El id a borrar debe ser un entero")
    except:
        print("no existe")
        return
    
        
def crear_nota():
    titulo = input("Ingrese el título de la nota: \n")
    descripcion = input("Ingrese la descripción de la nota: \n")
    SQL = "INSERT INTO notas (tittle, description) VALUES (?,?);"
    with sqlite3.connect("prueba.db") as conn:
        cur = conn.cursor()
        cur.execute(SQL, (titulo, descripcion))
    print(cur.rowcount)

def imprimir_notas():
    SQL = "SELECT * FROM notas;"
    print("id, \tcreated at, \ttittle ,\tdescription")
    print("-"*100)
    with sqlite3.connect("prueba.db") as conn:
        cur = conn.cursor()
        cur.execute(SQL)
        for f in cur:
            print(f)
            print("-"*100)

def menu():
    fin = False
    while not fin:
        print("Gestor de notas:")
        print("1.- Crear Nota")
        print("2.- Imprimir Nota")
        print("3.- Borrar Nota")
        
        print("5.-FIN")
        opcion = input("Elige la opción que quieras realizar: ")
        try:
            opcion = int(opcion)
        except:
            print("la entrada debe ser entera")
            continue
        match opcion:
            case 1:
                print("CREAR NOTA")
                crear_nota()
            case 3:
                print("BORRAR NOTA")
                borrar_nota()
            case 2:
                print("IMPRIMIR NOTA")
                imprimir_notas()
            case 5:
                fin = True
                print("bye :D")
            case _:
                print("La entrada debe estar entre 1y5")
#main
menu()