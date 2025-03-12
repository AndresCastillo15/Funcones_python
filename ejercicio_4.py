# Construir una funcion que reciba como paramatro una lista de daots numericos y que retorne el promedio de dichos datos
def promedio_lista(numeros):
    if len(numeros) == 0:
        return 0  
    return sum(numeros) / len(numeros)

import random
# creamos una lista vacia
lista = []
#tamaño de la lista
n = int(input("digite el tamaño de la lista: "))
for i in range(n):
    num = random.randint(1,100)
    lista.append(num) 
print("lista: ", lista)

lista_numeros = [10, 20, 30, 40, 50]
print("lista de numeros: ", lista)
resultado = promedio_lista(lista)
print("El promedio de los números es:", resultado)