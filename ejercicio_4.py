# Construir una funcion que reciba como paramatro una lista de daots numericos y que retorne el promedio de dichos datos
print("="*35)
print("DPROMEDIO DE UNA LISTA")
print("="*35)

def promedio_lista(numeros):
    suma = 0
    for i in lista:
        suma = suma + 1
        promedio_lista = suma / len(lista)
        return promedio_lista

import random
# creamos una lista vacia
lista = []
#tamaño de la lista
n = int(input("digite el tamaño de la lista: "))
for i in range(n):
    num = random.randint(14,18)
    lista.append(num) 

print("lista de numeros: ", lista)
resultado = promedio_lista(lista)
print("El promedio de los números es:", resultado)