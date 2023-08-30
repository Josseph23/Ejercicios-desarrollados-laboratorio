def calcular_factorial(n):
    factorial = 1

    if n == 0 or n == 1:
        return 1

    while n > 1:
        factorial *= n
        n -= 1

    return factorial

numero = int(input("Ingrese un número para calcular su factorial: "))
resultado = calcular_factorial(numero)
print("El factorial de", numero, "es", resultado)