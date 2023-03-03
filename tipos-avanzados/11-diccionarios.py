# Coleccion de datos que se encuentra agrupados por "llave valor"
# Solamente acepta Strings como 'llave'
punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45  # Creamos una nueva llave en el dict
# print(punto, punto['lala'])
if "lala" in punto:
    print("Encontre lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]  # Elimina su valor
del (punto["y"])  # Elimina la llave asociada al dict
print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]
for usuario in usuarios:
    print(usuario["nombre"])
