# Function to compute maximum heart rate
def maxHR(age):
    return 208-0.7*age

2


# Ask user for age
age=int(input('ingrese su edad : '))

frecuencia_maxima=maxHR(age)
frecuencia_reposo= int(input(f"Ingrese su frecuencia cardiaca:  "))


if frecuencia_reposo>=0.5*frecuencia_maxima and frecuencia_reposo<=0.6*frecuencia_maxima:
   print("se encuentra en la zona de trabajo z1(reposo)")
   
elif frecuencia_reposo>=0.6*frecuencia_maxima and frecuencia_reposo<=0.7*frecuencia_maxima:
    print("se encuentra en la zona de trabajo z2(resistecia aerobica)")
    
elif frecuencia_reposo>=0.7*frecuencia_maxima and frecuencia_reposo<=0.8*frecuencia_maxima: 
    print("se encuentra en la zona de trabajo z3(umbral aerobico)")
    
elif frecuencia_reposo>=0.8*frecuencia_maxima and frecuencia_reposo<=0.9*frecuencia_maxima:
   print(" se encuentra en la zona de trabajo z4(umbral anaerobico)")
   
elif frecuencia_reposo>=0.9*frecuencia_maxima and frecuencia_reposo<=frecuencia_maxima:
    print("se encuentra en la zona de trabajo z5(esfuerzo maximo)")
    
else:
    print("fuera del rango")

# Print estimation of maximum heart rate based on age
print(f'su frecuencia cardiaca maxima es: {maxHR(age)} bpm')