def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        raise ValueError("No se puede dividir entre cero.")
    return num1 / num2

def calculadora():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

        if operacion == '+':
            resultado = suma(num1, num2)
        elif operacion == '-':
            resultado = resta(num1, num2)
        elif operacion == '*':
            resultado = multiplicacion(num1, num2)
        elif operacion == '/':
            resultado = division(num1, num2)
        else:
            print("Operación no válida. Por favor ingrese +, -, *, o /.")
            return

        print("El resultado de la operación es:", resultado)
    except ValueError:
        print("Error de entrada. Por favor ingrese números válidos.")

try:
    calculadora()
except ValueError as e:
    print(e)