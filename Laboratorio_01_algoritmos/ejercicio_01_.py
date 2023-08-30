import math

 # Pedir al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

if numero < 2:
    print("El número no es primo.")
else:
    es_primo = True
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")