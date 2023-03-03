# set significa grupo o conjunto
# Colección de datos que no se pueden repetir y tampoco están ordenados
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

# print(primer | segundo)  # | simbolo de union

# & intersección devuelve lo que encuentre en ambos 'sets'
# print(primer & segundo)

# '-' diferencia: muestra solamente los datos que se encuentran en el conjunto de la izq y
# le quitamos los que se encuentran a la derecha
# print(primer - segundo)

# Diferencia simetrica, Elimina los que se duplican al comparar ambas
print(primer ^ segundo)

if 5 in segundo:
    print("Hola mundo!")
