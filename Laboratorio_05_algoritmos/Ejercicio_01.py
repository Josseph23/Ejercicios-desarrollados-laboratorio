edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a. Ordenar la lista y encontrar edad mínima y máxima
edades.sort()
edad_minima = edades[0]
edad_maxima = edades[-1]

# b. Añadir la edad mínima y máxima de nuevo a la lista
edades.append(edad_minima)
edades.append(edad_maxima)

# c. Encontrar la edad mediana
n = len(edades)
if n % 2 == 1:
    edad_mediana = edades[n // 2]
else:
    medio1 = edades[(n - 1) // 2]
    medio2 = edades[n // 2]
    edad_mediana = (medio1 + medio2) / 2

# d. Encontrar la edad promedio
edad_promedio = sum(edades) / len(edades)

# e. Calcular el rango de edades
rango_edades = edad_maxima - edad_minima

# f. Comparar el valor absoluto de (mínimo - promedio) y (máximo - promedio)
diferencia_min_promedio = abs(edad_minima - edad_promedio)
diferencia_max_promedio = abs(edad_maxima - edad_promedio)

# Imprimir los resultados
print("Edades ordenadas:", edades)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)
print("Edad mediana:", edad_mediana)
print("Edad promedio:", edad_promedio)
print("Rango de edades:", rango_edades)
print("Diferencia entre mínimo y promedio:", diferencia_min_promedio)
print("Diferencia entre máximo y promedio:", diferencia_max_promedio)