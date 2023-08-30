import random
import string

def generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_caracteres_especiales):
    try:
        caracteres = ''
        if incluir_mayusculas:
            caracteres += string.ascii_uppercase
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_caracteres_especiales:
            caracteres += string.punctuation

        if not caracteres:
            raise ValueError("Debe seleccionar al menos un tipo de caracter.")

        password = ''.join(random.choice(caracteres) for _ in range(longitud))
        return password
    except ValueError as e:
        return str(e)
