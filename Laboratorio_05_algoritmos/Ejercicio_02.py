frase = "Soy profesor y me encanta inspirar y enseñar a la gente"
# Dividir la frase en palabras utilizando el espacio como separador
palabras = frase.split() 
# Crear un conjunto de palabras únicas
palabras_unicas = set(palabras) 

 # Obtener la cantidad de palabras únicas
cantidad_palabras_unicas = len(palabras_unicas) 

print("Cantidad de palabras únicas:", cantidad_palabras_unicas)