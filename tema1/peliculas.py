#menú donde se pida si se quiere añadir datos de película o leer una

import json
import uuid
from pathlib import Path
import os

preguntar = True
diccionario={}
ruta = Path("pelicula_rating.json")

def respuesta_valida(respuesta):
    try:
        numero = int(respuesta)
        return numero in [1, 2, 3]
    except ValueError:
        return False
    
def num_valido(respuesta):
    try:
        numero = float(respuesta)
        return numero >= 0 and numero <= 5
    except ValueError:
        return False

def insertar_pelicula(): #hay que leer archivo antes de añadir una pelicula para ver si existe
    global diccionario, ruta
    titulo = input("Introduce el título de la película: ")
    clave = str(uuid.uuid4())
    if ruta.exists():
        print("la ruta existte")
        with open (ruta, "r", encoding="utf-8") as f:
            diccionario = json.load(f)
            for c,valor in diccionario.items():
                if titulo.lower() in valor.get("titulo").lower():
                    print("El titulo ya existe")
                    return                  
        diccionario[clave] = {}
        diccionario[clave]["titulo"] = titulo
        diccionario[clave]["puntuacion"] = input("Introduce la puntuación de la película (0-5): ")
        while not num_valido(diccionario[clave]["puntuacion"]):
            diccionario[clave]["puntuacion"] = input("Introduce una puntuación válida (0-5): ")
        diccionario[clave]["cita"] = input("Introduce la cita de la película: ")
        with open (ruta, "w", encoding="utf-8") as f:
            f.write(json.dumps(diccionario))
            print("Se ha añadido la película")        
    else: 
        with open (ruta, "w", encoding="utf-8") as f:
            f.write(json.dumps(diccionario))
            print("Se ha creado el archivo")

def mostrar_pelicula(nombre_pelicula):
    global diccionario, ruta
    existe = False
    if ruta.exists():
        with open (ruta, "r", encoding="utf-8") as f:
            diccionario = json.load(f)
            for c,valor in diccionario.items():
                if nombre_pelicula.lower() in valor.get("titulo").lower():
                    print(valor)
                    existe = True
        if not existe:
            print("La película no existe")
    else:
        print("No hay películas guardadas")
    
while(preguntar):
    respuesta = input("¿Quieres añadir una película(1) o mirarla(2) o salir del prgrama(3)?: ")
    while not respuesta_valida(respuesta):
        respuesta = input("Introduce un término válido (1 o 2 o 3): ")
    if int(respuesta) == 1:
        insertar_pelicula()
    elif int(respuesta) == 2:
        nombre_pelicula = input("Introduce el nombre de la película que quieres ver: ")
        mostrar_pelicula(nombre_pelicula)
    else:
        print("sales del pograma")
        preguntar = False
    
    