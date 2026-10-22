from lxml import etree
from pathlib import Path
import os

filepath = Path(_file_).parent / "personas.xml"
if not filepath.exists():
    print("la ruta es incorrecta")
    os._exit(-1)

root = etree.parse(filepath).getroot()
print(root)
primeras_personas = root.findall("persona")
print(primeras_personas)

primer_nombre = primeras_personas[0].find("nombre")
print(primer_nombre.text)

nombres = []
for p in primeras_personas:
    nombres.append(p.find("nombre").text)
print(nombres)

persona_Atributo = root.find("persona[@id='2']")
print(persona_atributo.find("nombre").text)