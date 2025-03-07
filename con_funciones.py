print("=" * 35)
print(" Buscar un numero en conjunto")
print("=" * 35)

# definicio de la funcion
def buscarDatoEnLista(datoABuscar, lista):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return  r
    
# entrada
dato = int(input("Numero a buscar: "))

# procesing
lista = [1,2,3,4,5]
if buscarDatoEnLista(dato, lista):
    print("Lo encontre")
else:
    print("no lo encontre")

    # salida
print ("\nEso era...")    