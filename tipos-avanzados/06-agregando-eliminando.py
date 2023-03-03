mascotas = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito feliz"
]
mascotas.insert(1, "Melvin")  # Primero el indice, luego el elemento
mascotas.append("Chanchito triste")  # Directamente lo agrega al final

# Va directamente el elemento y solo elemina el primer elemento que se encuentra
mascotas.remove("Pulga")
# Remueve el ultimo elemento de la lista por default, pero también se le puede pasar el indice
mascotas.pop(1)
del mascotas[0] # Le podemos pasar el indice la lista
mascotas.clear() # Elimina su contenido por completo
print(mascotas)
