# Es igual a una lista, excpeto por la diferencia de que es inmutable (no se puede agregar, quitar o modificar elementos)
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)
menosNumeros = numeros[:2]  # Crea una nueva tupla sin afectar 'numeros'
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)

# creamos una nueva lista de elementos, pero no modifcamos a la tupla
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito Feliz"
print(listaNumeros)
