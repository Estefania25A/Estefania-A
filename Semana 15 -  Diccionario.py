#Pizarra (Whiteboard)

# Diccionario

informacion_personal = {
    'nombres':'Estefania Dayanara ',
    'apellidos':'Anchundia Toaza ' ,
    'edad':" 24 años",
    'ciudad':'La Joya de los Sachas',
    'provincia':'Orellana',
}
print('----------------------')
print('Diccionario Original')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')

# Clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['ciudad'] = 'Quevedo'
informacion_personal['provincia'] = 'Los Ríos '

# Nueva clave-valor al diccionario "profesion"
informacion_personal['profesion'] = 'Estudiante'

# Verifica si la clave "telefono" existe
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0989722274'

# Elimina la clave "edad" del diccionario
# del informacion_personal['edad']
informacion_personal.pop('edad')

print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')