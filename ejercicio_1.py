# construir una funcion que reciba su nombre como parametro y que lo muestre 5 veces en la pantalla
def Nombre(nombre):
    return nombre * 5

print("="*35)
print("DIGITE SU NOMBRE")
print("="*35)

nombre = input("Escriba su nombre aqui: ")

for i in range(1,6):
    print(f"{i}. {nombre}")

