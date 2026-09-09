# Paso 1: Ejemplos positivos
positivos = [
  {"Edad": 25, "Frecuencia de Asistencia": "Frecuente", "Plan Contratado": "Premium"},
  {"Edad": 32, "Frecuencia de Asistencia": "Frecuente", "Plan Contratado": "Premium"},
  {"Edad": 45, "Frecuencia de Asistencia": "Frecuente", "Plan Contratado": "Premium"}
]

# Paso 2: Ejemplos negativos
negativos = [
  {"Edad": 25, "Frecuencia de Asistencia": "Ocacional", "Plan Contratado": "Basico"},
  {"Edad": 32, "Frecuencia de Asistencia": "Ocacional", "Plan Contratado": "Estandar"},
  {"Edad": 32, "Frecuencia de Asistencia": "Rara", "Plan Contratado": "Basico"}
]

# Paso 3: Inducción de reglas 
regla = {} # DICCIONARIO VACIO

# Obtener los nombres de los atributos
atributos = [] 
ejemplo = positivos[0] 
for clave in ejemplo:
    print("Clave: ", clave)
    atributos.append(clave)

# Para cada atributo, comparar valores únicos en positivos y negativos
for atributo in atributos:
    valores_pos = []
    valores_neg = []

    # Extraer valores de positivos
    for ej in positivos:
        valor = ej[atributo]
        if valor not in valores_pos:
            valores_pos.append(valor)

    # Extraer valores de negativos
    for ej in negativos:
        valor = ej[atributo]
        if valor not in valores_neg:
            valores_neg.append(valor)

   #Compara y guarda los valores que estan en positivo pero no en negativo
   
    valores_validos = []
    for valor in valores_pos:
        encontrado = False
        for v in valores_neg:
            if valor == v:
                encontrado = True
                break
        if not encontrado:
            valores_validos.append(valor)

    # Agrega valores validos a la lista en caso de haberlos
    if len(valores_validos) > 0:
        regla[atributo] = valores_validos

# Paso 4: Mostrar la regla inducida
print("Regla inducida para identificar si se trata de un socio activo:")
for atributo in regla:
    print("-", atributo, "debe ser igual a :", regla[atributo])
    
