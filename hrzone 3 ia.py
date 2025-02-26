# Función para calcular la frecuencia cardíaca máxima
def maxHR(edad):
    return 208 - (0.7 * edad)

# Función para determinar la zona de trabajo
def obtener_zona(frec, frec_max):
    zonas = [
        (0.5, 0.6, "Z1 (Reposo)"),
        (0.6, 0.7, "Z2 (Resistencia Aeróbica)"),
        (0.7, 0.8, "Z3 (Umbral Aeróbico)"),
        (0.8, 0.9, "Z4 (Umbral Anaeróbico)"),
        (0.9, 1.0, "Z5 (Esfuerzo Máximo)")
    ]
    
    for min_ratio, max_ratio, zona in zonas:
        if min_ratio * frec_max <= frec < max_ratio * frec_max:
            return zona
    return "Fuera de rango"

# Solicitar datos
edad = int(input("Ingrese su edad: "))
frecuencia_maxima = maxHR(edad)
num_entrenamientos = int(input("Número de entrenamientos: "))

# Listas para almacenar resultados
frecuencias = []
zonas = []

# Recoger datos
for i in range(num_entrenamientos):
    frec = int(input(f"Ingrese la frecuencia cardíaca promedio del entrenamiento {i+1}: "))
    zona = obtener_zona(frec, frecuencia_maxima)
    
    frecuencias.append(frec)
    zonas.append(zona)
    
    print(f"Entrenamiento {i+1}: {zona}")

# Contar porcentajes
zonas_unicas = set(zonas)
print("\nResumen de entrenamientos:")
for zona in sorted(zonas_unicas):
    porcentaje = (zonas.count(zona) / num_entrenamientos) * 100
    print(f"{zona}: {porcentaje:.2f}%")

