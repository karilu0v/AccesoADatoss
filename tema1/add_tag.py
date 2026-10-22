from lxml import etree
from pathlib import Path

ruta = Path(_file_).parent / "everything.xml"

print(ruta)

tree = etree.parse(ruta)
root = tree.getroot()

first_season = root.find("temporada")

chapters = etree.Element("capitulos")
chapters.text = "3"

firdt_season.append(chapters)

chapters_search = firdt_seaosn.find("capitulos")
print(adress_search.text)

#recorrer hijos
for sub in first_season:
    print(sub.tag, "-->", sub.text)
    
#cantidad de personas
seasons = root.findall("temporada")
print(len(seasons))
print(len(root))

#creacion de etiqueta estado
state = etree.SubElement(first_season, "estado", tipo="activo")
state.text = "en produccion"
for sub in first_season:
    if sub.attrib.items():
        print(sub.tag, "-->", sub.text, "atributos:", sub.attrib.items())
    else:
         print(sub.tag, "-->", sub.text)