# Paso 1: Ejemplos positivos
positivos = [
  {"edad": "Joven", "ingreso": "Alto", "tiene_garaje": "Si", "distancia_trabajo": "Corta" },
  { "edad": "Adulto", "ingreso": "Medio", "tiene_garaje": "Si", "distancia_trabajo": "Media"},
  {"edad": "Mayor", "ingreso": "Alto", "tiene_garaje": "Si", "distancia_trabajo": "Larga"}
]

# Paso 2: Ejemplos negativos
negativos = [
{"edad": "Joven", "ingreso": "Alto", "tiene_garaje": "No", "distancia_trabajo": "Corta" },
{"edad": "Adulto", "ingreso": "Medio", "tiene_garaje": "No", "distancia_trabajo": "Media"},
{"edad": "Mayor", "ingreso": "Bajo", "tiene_garaje": "No", "distancia_trabajo": "Larga"}
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
print("Regla inducida para identificar si la persona puede comprar un automovil electrico:")
for atributo in regla:
    print("-", atributo, "debe ser igual a :", regla[atributo])
