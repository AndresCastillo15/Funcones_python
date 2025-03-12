# Construir una funcion que reciba como parametro una lista de datos numericos y retome la suma de dichos datos.
print("="*30)
print("Suma en una lista")
print("="*30)
import random
def sumar_lista(numeros):
    sumar_lista = 0
    for i in lista:
        sumar_lista = sumar_lista + 1
    return sum(numeros)

# creamos una lista vacia
lista = []
#tamaño de la lista
n = int(input("digite el tamaño de la lista: "))
for i in range(n):
    num = random.randint(1,9)
    lista.append(num) 
print("lista: ", lista)

resultado = sumar_lista(lista)
print("La suma de los números es:", resultado)


