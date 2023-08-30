def contar_caracteres_y_palabras(frase):
    # Contar caracteres (incluyendo espacios y signos de puntuación)
    num_caracteres = len(frase)
    
    # Contar palabras
    palabras = frase.split()
    num_palabras = len(palabras)
    
    return num_caracteres, num_palabras

frase = "Estoy aprendiendo Python y me está gustando mucho. ¡Es genial!"
caracteres, palabras = contar_caracteres_y_palabras(frase)

print("Número de caracteres:", caracteres)
print("Número de palabras:", palabras)