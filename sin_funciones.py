print("=" * 35)
print("Buscar un numero en conjunto")
print("=" * 35)
# entrada

b =int(input("numero a buscar: "))

# proccesing

a = [1,2,3,4,5]
r = False

for i in a:
    if i==b:
        print("Lo encontre")
    r = True
if r ==False:
    print ("no lo encontre")

# salida

print("\nEso era...")