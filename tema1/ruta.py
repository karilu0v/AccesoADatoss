from pathlib import Path

p = Path("texto.txt") #True
p = Path("textos.txt") #false
p = Path("texto.txt")

print(p.exists())
print(p.name)
print(p.suffix)
p = Path(".")
print(p.exists())
print(list(p.glob("*.py"))[0].suffix)

# concatenar rutas

p = Path(".")
print(p.is_file()) #directorio actual = false

p_completa = p / "texto.txt"
print(p_completa.is_file()) #archivo = True


#creación carpetas
arbol = Path("logs")
print(arbol.exists())
try:
    Path.mkdir(arbol, parents=True)
except FileExistsError:
    print("subcarpetas ya existen, abortando operación")
finally:
    with open ("logs/log.txt", "a",  encoding="utf-8") as log:
        log.write("come on angel don't you cry\n")
