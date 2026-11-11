from pathlib import Path
from lxml import etree

#tree = etree.parse(Path(__file__).parent / "biblioteca_videojuegos.xml")

def numValido(respuesta):
    try:
        numero = int(respuesta)
        return numero >= 0 and numero <= 10
    except ValueError:
        return False
def anoValido(respuesta):
    try:
        numero = int(respuesta)
        return numero >= 1900 and numero <= 2024
    except ValueError:
        return False
def precioValido(respuesta):
    try:
        numero = float(respuesta)
        return numero >= 0
    except ValueError:
        return False


def crearBiblioteca():
    titulo = input("Introduce el título: ")
    plataforma = input("Introduce la plataforma: ")
    anoLanzamiento = input("Introduce el año de lanzamiento¡: ")
    genero = input("Introduce el género: ")
    precio = input("Introduce el precio: ")
    puntuacion = input("Introduce la puntuación: ")
    
    while not numValido(puntuacion) and not precioValido(precio) and not anoValido(anoLanzamiento):
        print("Introduce una puntuación válida (0-10), un precio válido (>=0), y un año de lanzamiento válido (1900-2024): ")
        puntuacion = input("Introduce la puntuación: ")
        precio = input("Introduce el precio: ")
        anoLanzamiento = input("Introduce el año de lanzamiento: ")

    biblioteca = etree.Element("biblioteca")
    videojuego = etree.SubElement(biblioteca, "videojuego")
    videojuego.set("plataforma", plataforma)
    titulo_elem = etree.SubElement(videojuego, "titulo")
    titulo_elem.text = titulo
    anoLanzamiento_elem = etree.SubElement(videojuego, "anoLanzamiento")
    anoLanzamiento_elem.text = anoLanzamiento
    genero_elem = etree.SubElement(videojuego, "genero")
    genero_elem.text = genero
    precio_elem = etree.SubElement(videojuego, "precio")
    precio_elem.text = precio
    puntuacion_elem = etree.SubElement(videojuego, "puntuacion")
    puntuacion_elem.text = puntuacion
    tree = etree.ElementTree(biblioteca)
    tree.write(Path(__file__).parent / "biblioteca_videojuegos.xml", pretty_print=True, xml_declaration=True, encoding="UTF-8")

def listarGeneros(tree, root):
    generos = []
    videojuegos = root.findall("videojuego")
    for videojuego in videojuegos:
        genero = videojuego.find("genero").text
        generos.append(genero)
    print("Géneros disponibles:")
    for genero in generos:
        print(genero)
        
def videojuegoMejorPuntuado(tree, root):
    videojuegos = root.findall("videojuego")
    mejor_puntuacion = -1
    for v in videojuegos:
        puntuacion = v.find("puntuacion").text
        try:
            puntuacion = float(puntuacion)
            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
                mejor_videojuego = v
        except ValueError:
            continue
    if mejor_puntuacion != -1:
        print("El videojuego con mejor puntuación es:", mejor_videojuego.find("titulo").text)
    
def agregarVideojuego(tree, root):
    titulo = input("Introduce el título: ")
    plataforma = input("Introduce la plataforma: ")
    anoLanzamiento = input("Introduce el año de lanzamiento¡: ")
    genero = input("Introduce el género: ")
    precio = input("Introduce el precio: ")
    puntuacion = input("Introduce la puntuación: ")
    
    while not numValido(puntuacion) and not precioValido(precio) and not anoValido(anoLanzamiento):
        print("Introduce una puntuación válida (0-10), un precio válido (>=0), y un año de lanzamiento válido (1900-2024): ")
        puntuacion = input("Introduce la puntuación: ")
        precio = input("Introduce el precio: ")
        anoLanzamiento = input("Introduce el año de lanzamiento: ")

    videojuego = etree.SubElement(root, "videojuego")
    videojuego.set("plataforma", plataforma)
    titulo_elem = etree.SubElement(videojuego, "titulo")
    titulo_elem.text = titulo
    anoLanzamiento_elem = etree.SubElement(videojuego, "anoLanzamiento")
    anoLanzamiento_elem.text = anoLanzamiento
    genero_elem = etree.SubElement(videojuego, "genero")
    genero_elem.text = genero
    precio_elem = etree.SubElement(videojuego, "precio")
    precio_elem.text = precio
    puntuacion_elem = etree.SubElement(videojuego, "puntuacion")
    puntuacion_elem.text = puntuacion
    tree.write(Path(__file__).parent / "biblioteca_videojuegos_actualizada.xml", pretty_print=True, xml_declaration=True, encoding="UTF-8")
   

tree = etree.parse(Path(__file__).parent / "biblioteca_videojuegos.xml")
root = tree.getroot()
agregarVideojuego(tree, root)    
listarGeneros(tree, root)
videojuegoMejorPuntuado(tree, root)
    