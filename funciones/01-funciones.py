def hola(nombre, apellido="Feliz"):  # Las parametros que indicamos acá, son obligatorias
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")
# Dentro de la función = parametro
# Al llamar a la función = argumento

hola("Fabio", "Stone")  # Acá nos referimos a lo que le pasamos como argumento
hola("Chanchito")

hola(apellido="Schurman", nombre="Wolfbang")