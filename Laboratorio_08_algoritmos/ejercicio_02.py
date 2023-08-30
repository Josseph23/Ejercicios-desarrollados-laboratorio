# El módulo sys es un módulo incorporado en Python que proporciona acceso a variables y funciones relacionadas 
# con la configuración y funcionalidad del intérprete de Python. Aquí hay una explicación de algunas de las 
# funcionalidades más comunes del módulo sys y ejemplos de cómo se pueden usar:
import sys


# Nos permite acceder a los argumentos de línea de comandos que se pasan al script Python cuando se ejecuta desde la línea de comandos:
script_name = sys.argv[0]
arguments = sys.argv[1:]

print("Nombre del script:", script_name)
print("Argumentos:", arguments)


# Permite la salida estándar y error estándar:
# Redirigimos la salida estándar a un archivo
sys.stdout = open('salida.txt', 'w')
print("Este mensaje se escribirá en salida.txt")
sys.stdout = sys.__stdout__


# Proporciona información sobre la versión de Python y el sistema operativo en el que se está ejecutando el script:
print("Versión de Python:", sys.version)
print("Plataforma:", sys.platform)


#proporciona el valor de la profundidad máxima de recursión permitida en el intérprete de Python:
print("Profundidad máxima de recursión:", sys.getrecursionlimit())

# Nos permite salir del programa: Usando el método sys.exit() se utiliza para salir del programa y puede recibir un código de estado como argumento:

#def main():
    #print("Ejecución del programa")
    #sys.exit(0)  
#if __name__ == "__main__":
    #main()
