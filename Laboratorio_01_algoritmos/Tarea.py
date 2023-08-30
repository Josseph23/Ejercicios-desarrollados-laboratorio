def main():
    lista_numeros = []

    for i in range(1, 6):
        numero = float(input(f"Por favor, introduzca el número {i}: "))
        lista_numeros.append(numero)

    suma = sum(lista_numeros)
    media = suma / 5

    print("Números introducidos:", lista_numeros)
    print("La media de los números introducidos es:", media)

    if media >= 10:
        print("La media es mayor o igual a 10.")
    else:
        print("La media es menor que 10.")

if __name__ == "__main__":
    main()