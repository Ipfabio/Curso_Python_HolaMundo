saludo = 25 # Esto generaria un error
# saludo = "Hola global"


def saludar():
    global saludo # Así decimos que nos referimos a la variable global y es la que vamos a afectar (No se recomienda esto)
    saludo = "Hola Mundo"


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)

resultasdo1 = saludo + 3
print(resultasdo1)
saludar()
resultasdo2 = saludo + 3
print(resultasdo2)
