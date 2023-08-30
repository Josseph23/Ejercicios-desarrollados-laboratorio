def invertir_frase(frase):
    palabras = frase.split()
    # Invertir el orden de las palabras
    palabras_invertidas = palabras[::-1]  
    frase_invertida = ' '.join(palabras_invertidas)
    return frase_invertida

frase_original = "Aprendiendo Python con Edem"
frase_invertida = invertir_frase(frase_original)

print("Frase invertida:", frase_invertida)