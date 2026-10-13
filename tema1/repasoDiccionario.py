datos_alumnos = {
    "1": {
         "nombre":"Antonio",
         "curso":2,
         "ciclo":"DAM",
        },
    }
print(datos_alumnos)
# indexación
print(datos_alumnos["1"]["curso"])

# añadir al diccionario
datos_alumnos["2"] = {
                        "nombre":"Julia",
                        "curso":"1",
                        "ciclo":"DAW",
                    }
print(datos_alumnos)

#borrar
del(datos_alumnos["1"])
print(datos_alumnos)

# comprobar existencia
if "2" in datos_alumnos:
    print(datos_alumnos["2"]["nombre"])

#iterar diccionario
for clave in datos_alumnos:
    print(datos_alumnos[clave])
    
# lista de claves  
print(datos_alumnos.keys())

#lista de valores
print(datos_alumnos.values())

#keyError
try:
    print(datos_alumnos["1231"])
except KeyError:
    print("la clave no existe")

#none
print(datos_alumnos.get("1231"))
