import json
from pathlib import Path
from lxml import etree
import types

'''
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
'''

def recorrer_diccionario(dicc):
    for clave in dicc:
        if clave.isinstance(type.StrType):
            print(clave)
        if type(clave) == "<class 'list'>":
            recorrer_diccionario(dicc[clave])        



p = Path(file).parent / "ejemplo_json.json"


with open (p, "r", encoding = "utf-8") as f:
    contenidos = json.load(f)
print(contenidos)

recorrer_diccionario(contenidos)


print(factorial(4))
print(fib(6))