# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 40}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 36}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 35},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 39}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 40}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]

#Calcular el promedio de temperaturas para cada ciudad y semana
no_ciudad = 0
for ciudad in temperaturas:
    no_ciudad += 1
    print(f"CIUDAD No. {no_ciudad}")
    no_semana = 0
    for semana in ciudad :
        no_semana += 1
        suma = 0
        for dia in semana:
            suma += dia["temp"]
            promedio = round(suma / len(semana), 2)
            print(f"promedio semana No. {no_semana } es {promedio} ")



