num1 = 8
num2 = 6

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
modulo = num1 % num2
division_entera = num1 // num2
potencia = num1 ** num2

resultado = f"{num1} + {num2} = {suma}\n" \
            f"{num1} - {num2} = {resta}\n" \
            f"{num1} * {num2} = {multiplicacion}\n" \
            f"{num1} / {num2} = {division:.2f}\n" \
            f"{num1} % {num2} = {modulo}\n" \
            f"{num1} // {num2} = {division_entera}\n" \
            f"{num1} ** {num2} = {potencia}"

print(resultado)