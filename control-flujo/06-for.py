# for numero in range(5):
#     print(numero, numero*'Hola mundo ')
buscar = 10
for numero in range(5):  # iterable
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontré el número buscado")

for char in "Ultimate python":
    print(char)
