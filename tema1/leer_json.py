import json
from pathlib import Path
import os

ruta = Path("tiempos_juegos.json")
videojuegos = None

#que no exista
if not ruta.exists():
    print("El fichero no existe")
    os._exit(1) #permite hacer llamadas al sistema
    
#que no sea un ficero
if not ruta.is_file():
    print("La ruta no condunce a un fichero")
    os._exit(1)
    
clave = input("Ingresa el juego del que quieres ver su duración:\t")


with open (ruta, "r", encoding="utf-8") as f:
    try:
        videojuegos = json.loads(f.read())
        print(type(videojuegos))
        print("El archivo ha sido cargado correctamente")
        
        '''if clave in videojuegos:
            print(videojuegos[clave])
        else:
            print(f"No existe la clave '{clave}'")'''
            
        
        duracion = videojuegos.get(clave)
        if duracion:
           print(duracion)
        else:
            print("No existe la clave '{clave}'")
           
    except json.JSONDecodeError:
        print("El archivo no se puede decodificar")
    