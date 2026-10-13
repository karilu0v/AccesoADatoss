import json

videojuegos = {
    "Dark Souls": 40,
    "Minecraft": 4,
    "GTAV": 15,
    }


with open ("tiempos_juegos.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(videojuegos))