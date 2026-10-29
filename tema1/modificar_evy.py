from lxml import etree
from pathlib import Path


p = Path(_file_).parent / "everything.xml"
p_out = Path(_file_).parent / "everything_mod.xml"
tree = etre.parse(p)

def elemento: 
    xml = etree.tostring(elemento, pretty_print=True)
    print(xml.decode(), end ="")
    
root = tree.getroot()

if etree.iselement(root):
    pretty_print(root)
    
print(root.tag) #referencia a añadir nuevo elemento

nueva_temporada = etree.SubElement(root, "temporada", id="3")
nuevo_nombre = etree.SubElement(nueva_temporada, "nombre")
nuevo_nombre.text= "Mask"
nuevo_personaje = etree.SubElement(nueva_temporada, "personaje")
nuevo_personaje.text= "Fadia"
pretty_print(root)

tree.write(p_out, encoding="UTF-8", pretty_print=True, xml_declaration=True)