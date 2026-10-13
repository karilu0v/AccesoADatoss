#menú donde se pida si se quiere añadir datos de película o leer una

import json
import uuid
from pathlib import Path
import os

preguntar = True
diccionario={}
ruta = Path("pelicula_rating.json")

def respuesta_valida(respuesta):
    if int(respuesta) == 1 or int(respuesta) == 2 or int(respuesta) == 3:
        return True
    return False

def insertar_pelicula(): #hay que leer archivo antes de añadir una pelicula para ver si existe
    global diccionario, ruta
    titulo = "The heart killers"
    clave = str(uuid.uuid1())
    diccionario[clave] = {}
    if ruta.exists():
        print("la ruta existte")
        with open (ruta, "r", encoding="utf-8") as f:
            diccionario = json.loads(f.read())
            for clave,valor in diccionario.items():
                if titulo in valor.values():
                    print("El titulo ya existe")
                    
        diccionario[clave]["titulo"] = "The heart killers"
        diccionario[clave]["puntuacion"] = 4.5
        diccionario[clave]["cita"] = "Fadel, they are the snitches"
    else: 
        with open (ruta, "w", encoding="utf-8") as f:
            f.write(json.dumps(diccionario))
    
    
while(preguntar):
    respuesta = input("¿Quieres añadir una película(1) o mirarla(2) o salir del prgrama(3)?: ")
    while not respuesta_valida(respuesta):
        respuesta = input("Introduce un término válido (1 o 2 o 3): ")
    if int(respuesta) == 1:
        insertar_pelicula()
    elif int(respuesta) == 2:
        print(si)
    else:
        print("sales del pograma")
        preguntar = False
    
    