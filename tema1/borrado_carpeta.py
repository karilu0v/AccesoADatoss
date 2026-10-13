from pathlib import Path
import time

p = Path("logs")

#creación de carpeta
if not p.exists():
    Path.mkdir(p)
    #creación de archivos
    for i in range(5):
        with open(f"logs/f{i}.txt", "a") as f:
            f.writelines("hola")    

time.sleep(5)

if p.exists():
    #borrar ficheros
    ficheros = list(p.glob("*"))
    for f in ficheros:
        if f.exists() and f.is_file():
            f.unlink()
    #borrar carpeta
    Path.rmdir(p)