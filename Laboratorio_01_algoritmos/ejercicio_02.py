import math
n = int(input("Ingrese un número n: "))
for i in range(2, n):
    es_primo = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(i, "es un número primo menor que", n)