usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# transformación (map)
nombres = [usuario[0] for usuario in usuarios]  # expresion for item in items

# filtrar (filter)
# expresion for item in items para filtrar
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# Filtrar y Transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# nombres = list(map(lambda usuario:usuario[0], usuarios))
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
