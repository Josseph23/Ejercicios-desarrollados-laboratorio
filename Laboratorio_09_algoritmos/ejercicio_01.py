def celsius_a_fahrenheit(temp):
    return temp * 9/5 + 32

def fahrenheit_a_celsius(temp):
    return (temp - 32) * 5/9

def conversion_temperatura():
    temp = float(input("Ingrese la temperatura: "))
    unidad = input("Ingrese la unidad de temperatura (C o F): ")

    if unidad.upper() == 'C':
        temp_convertida = celsius_a_fahrenheit(temp)
        print("La temperatura convertida a Fahrenheit es:", temp_convertida)
    elif unidad.upper() == 'F':
        temp_convertida = fahrenheit_a_celsius(temp)
        print("La temperatura convertida a Celsius es:", temp_convertida)
    else:
        print("Unidad de temperatura no válida. Por favor ingrese C o F.")

try:
    conversion_temperatura()
except ValueError:
    print("Valor de temperatura no válido. Por favor ingrese un número.")