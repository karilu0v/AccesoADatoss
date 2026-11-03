import json
from pathlib import Path

p = Path(__file__).parent / "inventario.json"

def printMenu():
    print("----MENÚ TIENDA----")
    print("1 - completo")
    print("2 - crear")
    print("3 - reponer")
    print("4 - vender")
    print("5 - borrar")
    print("6 - salir")
    
if not p.exists():
    with open (p, "w", encoding="utf-8") as f:
        f.write("{}") #--> primera forma
        #dicc= {}
        #json.dump(dicc, f) --> segunda forma
        #f.write(json.dumps(dicc))  --> tercera forma
        
finished = False
while not finished:
    printMenu();
    entrada = input("Elige opción:\t")
    try:
        entrada = int(entrada)
    except:
        continue
    match entrada:
        case 1:
            with open (p, "r", encoding="utf-8") as f:
                #dicc = json.loads(f.read())
                dicc = json.load(f)
            for item in dicc.items():
                print(item[0], "-->", item[1])
        case 2:
            dicc = {}
            with open(p, "r", encoding="utf-8") as f:
                dicc = json.load(f)
            producto = input("Inserte nombre del nuevo producto - ")
            while producto.strip()=="":
                producto = input("Inserte nombre del nuevo producto - ")
            if producto not in dicc: #no existe aún el producto
                dicc[producto] = 0
            else:
                print(f"El producto '{producto}' ya existe y hay {dicc[producto]} unidades")
            with open (p, "w", encoding="utf-8") as f:
                json.dump(dicc, f)
            print(f"Producto '{producto}' creado")
        case 3:
            dicc = {}
            with open(p, "r", encoding="utf-8") as f:
                dicc = json.load(f)
            producto = input("Inserte nombre del producto a reponer - ")
            while producto.strip()=="":
                producto = input("Inserte nombre del producto a reponer - ")
            if producto not in dicc: #no existe aún el producto
                print(f"El producto '{producto}' no existe, crealo antes")
            else:                
                cantidad_valida = False
                cantidad = 0
                while not cantidad_valida:
                    cantidad = input("Ingrese cantidad a reponer - ")
                    try:
                        cantidad = int(cantidad)
                        if cantidad >0:
                            cantidad_valida = True
                        else:
                          print("La cantidad debe ser un entero positivo")  
                    except:
                         print("La cantidad debe ser un entero positivo")
                       
                dicc[producto] += cantidad
                with open (p, "w", encoding="utf-8") as f:
                    json.dump(dicc, f)
                print(f"Reposición de '{cantidad}' '{producto}'/s completa")
        case 4:
            dicc = {}
            with open(p, "r", encoding="utf-8") as f:
                dicc = json.load(f)
            producto = input("Inserte nombre del producto a vender - ")
            while producto.strip()=="":
                producto = input("Inserte nombre del producto a vender - ")
            if producto not in dicc: #no existe aún el producto
                print(f"El producto '{producto}' no existe, consulte inventario")
            else:
                cantidad = 0
                while cantidad <= 1 or cantidad > dicc[producto]:
                    cantidad = input("Ingrese cantidad a vender - ")
                    try:
                        cantidad = int(cantidad)
                        if cantidad <= 1 or cantidad > dicc[producto]:
                            print("La cantidad no puede ser mayor al stock o menor de 1")
                    except:
                        print("La cantidad tiene que ser un número menor al stock o 1 o más")
                        cantidad= 0
                print(cantidad)
                dicc[producto] = dicc[producto] - cantidad
                with open (p, "w", encoding="utf-8") as f:
                    json.dump(dicc, f)
                print(f"Venta de '{cantidad}' '{producto}'/s completa")
                    
        case 5:
            dicc = {}
            with open(p, "r", encoding="utf-8") as f:
                dicc = json.load(f)
            producto = input("Inserte nombre del producto a borrar - ")
            while producto.strip()=="":
                producto = input("Inserte nombre del producto a borrar - ")
            if producto not in dicc: #no existe aún el producto
                print(f"El producto '{producto}' no existe")
            else:
                del(dicc[producto]) 
                with open (p, "w", encoding="utf-8") as f:
                    json.dump(dicc, f)
                print(f"Producto '{producto}' eliminado del inventario")
        case _:
            finished = True
            print("saleees")
print("Bye")
            