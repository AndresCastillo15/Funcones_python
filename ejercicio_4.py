# Construir una funcion que reciba como paramatro una lista de daots numericos y que retorne el promedio de dichos datos
def promedio_lista(numeros):
    if len(numeros) == 0:
        return 0  
    return sum(numeros) / len(numeros)

lista_numeros = [10, 20, 30, 40, 50]
resultado = promedio_lista(lista_numeros)
print("El promedio de los números es:", resultado)