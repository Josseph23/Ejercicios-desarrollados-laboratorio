def cifrado_cesar(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra.isalpha():  # Solo cifrar letras y mantener otros caracteres
            if letra.islower():
                codigo_letra = ord('a')
            else:
                codigo_letra = ord('A')
            letra_cifrada = chr((ord(letra) - codigo_letra + desplazamiento) % 26 + codigo_letra)
            mensaje_cifrado += letra_cifrada
        else:
            mensaje_cifrado += letra  # Mantener caracteres que no son letras
    return mensaje_cifrado

mensaje_original = "Hola, mi nombre es Josseph"
desplazamiento = 2

mensaje_cifrado = cifrado_cesar(mensaje_original, desplazamiento)

print("Mensaje original:", mensaje_original)    
print("Mensaje cifrado:", mensaje_cifrado)
