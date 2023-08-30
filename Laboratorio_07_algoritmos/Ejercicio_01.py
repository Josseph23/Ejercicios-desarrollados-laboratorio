persona = {
 'first_name': 'Josseph',
 'last_name': 'Castillo',
 'age': 19,
 'country': 'Peru',
 'is_married': False,
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}

# a) Comprobamos si el diccionario de la persona tiene la clave de habilidades
if 'skills' in persona:
    habilidades = persona['skills']
    cantidad_habilidades = len(habilidades)
    if cantidad_habilidades > 0:
        habilidad_del_medio = habilidades[cantidad_habilidades // 2]
        print(f"Habilidad del medio: {habilidad_del_medio}")

# b) Comprobamos si el diccionario de la persona tiene la habilidad 'Python'
if 'skills' in persona and 'Python' in persona['skills']:
    print("La persona tiene la habilidad 'Python'.")

# c) Determinamos el título basado en las habilidades
habilidades = persona.get('skills', [])
if habilidades == ['JavaScript', 'React']:
    print("Él es un desarrollador frontend.")
elif set(['Node', 'Python', 'MongoDB']).issubset(habilidades):
    print("Él es un desarrollador backend.")
elif set(['React', 'Node', 'MongoDB']).issubset(habilidades):
    print("Él es un desarrollador fullstack.")
else:
    print("Título desconocido.")
