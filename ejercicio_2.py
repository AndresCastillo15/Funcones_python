# construir una funcion que reciba una cadena digitada (como parametro) por el usuario que lo muestre n veces en la pantalla. EL valor de n tambien digitado por el usuario
def Nombre(nombre, veces):
    return nombre * veces

print("="*35)
print("DIGITE SU NOMBRE")
print("="*35)

nombre = input("Escriba su nombre aqui: ")
veces = int(input("Escriba cuantas veces quiere que se repita: "))

for i in range(1,veces +1):
    print(f"{i}. {nombre}")