import json
import uuid
from pathlib import Path

lista = []
ruta = Path("datos_personas.json")

if ruta.exists():
        with open (ruta, "r", encoding="utf-8") as f:
            lista = json.load(f)
        for d in lista:
            nombre = d["nombre"]
            ciudad = d["ciudad"]
            print(f"{nombre} vive en {ciudad}")
            