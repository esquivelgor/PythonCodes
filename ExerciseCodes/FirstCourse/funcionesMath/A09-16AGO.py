# Escribe un programa que calcule la población de una especie en un determinado número de años. 
# Utiliza la fórmula Ni(e^rt), donde Ni es la población inicial, r es la tasa de crecimiento, 
# la cual siempre es un número entre 0 y 1, t es el tiempo en años y e la constante de Euler. 

# Entrada :Tres números, correspondientes a: población inicial (entero positivo), tiempo en años (entero positivo) 
# y tasa de crecimiento (flotante entre 0 y 1).

# Salida : Un número entero, resultado del cálculo de la población final. IMPORTANTE: 
# Trunca los decimales del número resultante,
# para que el resultado sea entero (¿Cuál es la función de la librería math de
#  Python que te puede ayudar a truncar los decimales?).

#Ejemplo:
#>>> 100   
#>>> 1 
#>>> 0.5 
#164
from math import e, trunc

print("------------ Poblaciones ---------------")
ni = int(input("Ingresa la población inicial: "))
if ni >= 0:
    r = float(input("Ingresa la tasa de crecimiento (valor entre 0-1): "))
    if (r >= 0) and (r <= 1):
        t = float(input("Ingresa el tiempo en años: "))
        if t <= 0:
            print("Debe ser un valor mayor que 0")             
    else: print("Debe ser un valor mayor que 0 y menor o igual que 1")
else: print("Debe ser un valor mayor que 0")

pobFin = ni*(e**(r*t))
print("La población final es: " + str(trunc(pobFin)))