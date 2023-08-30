def es_palindromo(frase):
    frase = frase.lower().replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    return frase == frase[::-1]

frase_input = input("Ingrese una frase: ")
if es_palindromo(frase_input):
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")