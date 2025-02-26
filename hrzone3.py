def maxHR(age):
  return 208 - 0.7 * age


# Preguntar por la edad, frecuencia cardíaca
age = int(input('Ingrese su edad: '))


num_entrenamientos = int(input("Ingrese el número de entrenamientos realizados: "))
frecuencia_maxima = maxHR(age)

zona_entrenamientos = []
for i in range(num_entrenamientos):
  frecuencia_reposo = int(input(f"Ingrese su frecuencia cardíaca del entrenamiento {i + 1}: "))
  if frecuencia_reposo >= 0.5 * frecuencia_maxima and frecuencia_reposo <= 0.6 * frecuencia_maxima:
    print("Se encuentra en la zona de trabajo Z1 (reposo)")
    zona_entrenamientos.append("Z1")
  elif frecuencia_reposo >= 0.6 * frecuencia_maxima and frecuencia_reposo <= 0.7 * frecuencia_maxima:
    print("Se encuentra en la zona de trabajo Z2 (resistencia aeróbica)")
    zona_entrenamientos.append("Z2")
  elif frecuencia_reposo >= 0.7 * frecuencia_maxima and frecuencia_reposo <= 0.8 * frecuencia_maxima:
    print("Se encuentra en la zona de trabajo Z3 (umbral aeróbico)")
    zona_entrenamientos.append("Z3")
  elif frecuencia_reposo >= 0.8 * frecuencia_maxima and frecuencia_reposo <= 0.9 * frecuencia_maxima:
    print("Se encuentra en la zona de trabajo Z4 (umbral anaeróbico)")
    zona_entrenamientos.append("Z4")
  elif frecuencia_reposo >= 0.9 * frecuencia_maxima and frecuencia_reposo <= frecuencia_maxima:
    print("Se encuentra en la zona de trabajo Z5 (esfuerzo máximo)")
    zona_entrenamientos.append("Z5")
  else:
    print("Fuera del rango")
    zona_entrenamientos.append("Fuera del rango")

# Imprimir estimación de la frecuencia cardíaca máxima basada en la edad
print(f'Su frecuencia cardíaca máxima es: {maxHR(age)} bpm')

contador_zona = {"Z1": 0, "Z2": 0, "Z3": 0, "Z4": 0, "Z5": 0, "Fuera del rango": 0}
for zona in zona_entrenamientos:
  contador_zona[zona] += 1
print("\nPorcentaje de entrenamientos en cada zona:")

for zona, contador in contador_zona.items():
    if num_entrenamientos > 0:
        porcentaje = (contador / num_entrenamientos) * 100
    else:
        porcentaje = 0
    print(f"{zona}: {porcentaje:.2f}%")