# calcular la moda de una lista de n números
import random

random.seed(0)
lista_aleatoria = [random.randint(0,10) for x in range(10)]

def moda_1(lista):
    num_mas_rep=None
    num_max_rep=0
    for num in lista:        
        num_rep_actual=0
        for numero in lista:
            if numero==num:
                num_rep_actual+=1
        if num_rep_actual>num_max_rep:
            num_mas_rep = num
            num_max_rep= num_rep_actual
    return num_mas_rep

def moda_2(lista):
    repeticiones={}
    num_max_rep=0
    num_mas_rep=None
    for i in lista:
        if i in repeticiones:
            repeticiones[i]+=1
        else:
            repeticiones[i]=1
        if repeticiones[i] > num_max_rep:
            num_max_rep=repeticiones[i]
            num_mas_rep=i
    return num_mas_rep
        
def moda_3(lista):
    num_max_rep=0
    num_mas_rep=None
    for i in lista:
        rep = lista.count(i)
        if rep>num_max_rep:
            num_max_rep = rep
            num_mas_rep = i
    return num_mas_rep

print(lista_aleatoria)
print()
print(f"El número más repetido es: {moda_1(lista_aleatoria)}")
print()
print(f"El número más repetido es: {moda_2(lista_aleatoria)}")
print()
print(f"El número más repetido es: {moda_3(lista_aleatoria)}")