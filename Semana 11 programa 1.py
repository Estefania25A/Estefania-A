# Pizarra (Whiteboard)

matriz=[
    [2, 4, 6],
    [8, 10,12],
    [14,16,18]

]

no_fila = 0
busqueda = int(input("ingrese el valor de busqueda: "))

for fila in matriz:
    no_columna = 0
    for columna in fila:
        if (columna == busqueda):
            print(f"No. {busqueda} , posision es : [{no_fila}][{no_columna}]")
            no_columna += 1
        no_fila += 1