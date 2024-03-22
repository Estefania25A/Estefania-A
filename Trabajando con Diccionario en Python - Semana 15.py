# diccionario con información personal ficticia
informacion_personal = {
    "Nombres": "Estefania Dayanara  ",
    "Apellidos": " Anchundia Toaza " ,
    "Lugar de nacimiento ": "Los Ríos - Quevedo " ,
    "Fecha de nacimiento" : " 13 de Mayo de 1999 " ,
    "Edad":" 24 años " ,
    "Ciudad": "Cantón Joya de los Sachas - Orellana ",
    "Profesion": "Estudiante de TIC "
}

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número de teléfono ficticio
    informacion_personal["Telefono"] = "0989722274"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Información personal:")
for key in informacion_personal:
    print(f"{key}: {informacion_personal[key]}")