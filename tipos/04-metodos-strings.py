animal = "  chanCHito feliz   "
print(animal.upper())
print(animal.lower())
# antes de usarlo, podríamos necesitar hacer uso de Strip()
print(animal.strip().capitalize())  # print(animal.capitalize())
print(animal.title())
# Elimina espacios vacíos que se encuentran a la izq. y der.
print(animal.strip())
print(animal.lstrip())  # Quita espacios izq
print(animal.rstrip())  # Quita espacios der
print(animal.find("CH"))
print(animal.replace("nCH","j"))
print("nCH" in animal)
print("nCH" not in animal)
