def no_space(texto):  # Quitamos espacios
    nuevo_texto = ""
    for caract in texto:
        if caract != " ":
            nuevo_texto += caract
    return nuevo_texto


def reverse(texto):  # Damos vuelta el texto
    texto_al_reves = ""
    for char in texto:
        # Si hicieramos 'texto_al_reves +='  nos devolveria mal el resultado porque 'añadiria' de der a izq, en lugar de izq a der
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):  # Verificamos si es Palindromo
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
print("Somos o no somos", es_palindromo("Somos o no somos"))
