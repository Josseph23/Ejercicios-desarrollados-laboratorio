lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

# a. Convertir las listas en conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

# b. Encontrar el conjunto de números presentes en las tres listas
numeros_en_tres_listas = conjunto1 & conjunto2 & conjunto3

# c. Encontrar el conjunto de números presentes en al menos una de las listas
numeros_en_al_menos_una_lista = conjunto1 | conjunto2 | conjunto3

# d. Encontrar el conjunto de números presentes en la primera lista pero no en la última
numeros_solo_en_primera_lista = conjunto1 - conjunto3

# e. Convertir los conjuntos en tuplas y sumar el primer y último elemento de cada tupla
tupla_numeros_en_tres_listas = tuple(numeros_en_tres_listas)
tupla_numeros_en_al_menos_una_lista = tuple(numeros_en_al_menos_una_lista)
tupla_numeros_solo_en_primera_lista = tuple(numeros_solo_en_primera_lista)

suma_primer_ultimo_tupla1 = tupla_numeros_en_tres_listas[0] + tupla_numeros_en_tres_listas[-1]
suma_primer_ultimo_tupla2 = tupla_numeros_en_al_menos_una_lista[0] + tupla_numeros_en_al_menos_una_lista[-1]
suma_primer_ultimo_tupla3 = tupla_numeros_solo_en_primera_lista[0] + tupla_numeros_solo_en_primera_lista[-1]

print("Conjunto de números en las tres listas:", numeros_en_tres_listas)
print("Conjunto de números en al menos una lista:", numeros_en_al_menos_una_lista)
print("Conjunto de números solo en la primera lista:", numeros_solo_en_primera_lista)
print("Suma del primer y último elemento de la primera tupla:", suma_primer_ultimo_tupla1)
print("Suma del primer y último elemento de la segunda tupla:", suma_primer_ultimo_tupla2)
print("Suma del primer y último elemento de la tercera tupla:", suma_primer_ultimo_tupla3)