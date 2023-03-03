numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort() Ordena, pero le podemos pasar un parametro también
# numeros.sort(reverse=True)
# 'sorted' crea una nueva lista sin alterar a la original
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


def ordena(elemento):  # Esto no sería la mejor manera, pero funciona y se entiende el concepto
    return elemento[1]


# usuarios.sort(key=ordena, reverse=True)  # Podemos pasarle una función
# Ordenado con función lambda -> lamda parametros:valorRetorno
usuarios.sort(key=lambda el: el[1])
print(usuarios)
