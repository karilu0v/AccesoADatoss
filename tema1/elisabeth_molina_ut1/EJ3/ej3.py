from pathlib import Path
from lxml import etree

tree = etree.parse(Path(__file__).parent / "books.xml")
root = tree.getroot() 
p = Path(__file__).parent / "books.xml"
    
def listaGeneros(root): #muestra los géneros sin repetirlos
    generos = []
    libros = root.findall("book")
    for l in libros:
        genero = l.find("genre").text
        if (genero not in generos):
            generos.append(genero)
    return generos
            
def addFavorito(root,id,): #añade la etiqueta de favorito a el libro con el id introducido por el usuario
    libros= root.findall("book")
    for l in libros:
        if l.get("id") == str(id):
            l.set("favorito", "true")
            tree.write(p, encoding = "utf-8", xml_declaration = True)
            return id
    return None

def listaOferta(root, precio): #lista los libros más baratos que un precio establecido por el usuario
    lista = []
    libros = root.findall("book")
    libro = None
    for l in libros:
        try:
            price = float(l.find("price").text)
        except:
            continue
        if precio >= price:
            libro = l.get("id"), l.find("title").text, l.find("price").text
            lista.append(libro)
    return lista

print("lista de géneros: ")    
print(listaGeneros(root))
id = input("Escribe el id: ")
print(addFavorito(root, id))

valido = False
while not valido:
    precio = input("Escribe el precio: ")
    try:
        precio = float(precio)
        valido = True
    except:
        print("introduce un numero válido")
print("libros más baratos que ", precio)
print(listaOferta(root, precio))



