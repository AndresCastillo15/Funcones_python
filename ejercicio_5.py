# construir una funcion que reciba como parametro una lista de datos numericos y retorne el promedio de los daots pares.
import random
def promedio_pares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    if len(pares) == 0:
        return 0
    return sum(pares) / len(pares)

print
lista_numeros = []
#tamaño de la lista
n = int(input("digite el tamaño de la lista: "))
for i in range(n):
    num = random.randint(1,100)
    lista_numeros.append(num) 

resultado = promedio_pares(lista_numeros)
print("El promedio de los números pares es:", resultado)