# construir una funcion que reciba como parametro una lista de datos numericos y retorne el promedio de los daots pares.
def promedio_pares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    if len(pares) == 0:
        return 0
    return sum(pares) / len(pares)


lista_numeros = [10, 15, 20, 25, 30]
resultado = promedio_pares(lista_numeros)
print("El promedio de los números pares es:", resultado)