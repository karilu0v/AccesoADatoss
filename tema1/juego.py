import json

estado = [4567, 3, 200, 75, {
                             "0":"fennekin",
                             "1":"pykumuku",
                             "2":"mawile"
                             }
          ]

with open("guardado.save", "w", encoding="utf-8") as save:
    for item in estado[:-1]:
        save.write(str(item) + ";")
    save.write(json.dumps(estado[-1]))
    print("partida guardada")
    
with open("guardado.save", "r", encoding="utf-8") as save:
    linea = save.read()
    items_saved = linea.split(";")
    estado = [int(item) for item in items_saved[:-1]]
pokemons = json.loads(items_saved[-1])
estado.append(pokemons)
print(estado)
