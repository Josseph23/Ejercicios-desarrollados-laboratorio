
import random
import string

def generar_contraseña (longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    while True:
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        if (any(c.islower() for c in contrasena) and
            any(c.isupper() for c in contrasena) and
            any(c.isdigit() for c in contrasena) and
            any(c in string.punctuation for c in contrasena)):
            return contrasena

longitud = int(input("Ingrese la longitud de la contraseña: "))
contrasena_generada = generar_contraseña(longitud)
print("Contraseña generada: " + contrasena_generada)