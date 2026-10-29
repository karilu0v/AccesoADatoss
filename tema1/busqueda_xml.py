from lxml import etree
from pathlib import Path

def pretty_print(element):
    xml = etree,tostring(element, pretty_print = True, encoding="utf-8")
    print(xml.decode, end="")
    
    
p = Path(_file_).parent / "menu.xml"

tree = etree.parse(p)
root = tree.getroot()

pretty_print(root)

foods = root.findall("food")

productos_baratos = []

if len(foods) != 0:
    for f in foods:
        price = f.find("price")
        if etree.ieselement(price):
            precio_raw = price.text
            precio_limpio = precio_raw.replace("$", "").strip()[1:]
            try:
                precio_limpio = float(precio_limpio)
                if precio_limpio <= 5.0:
                    f.set("barato", "true")
                    productos_baratos.append(f)
            except:
                continue
for e in productos_baratos:
    pretty_print(e)
    