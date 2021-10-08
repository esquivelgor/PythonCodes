# Desarrolla un programa en Python que calcule la distancia entre dos puntos del plano cartesiano.
# ---------- Entradas
# El programa solicita el punto inicial (x1, y1) y el final (x2,y2). Todos enteros y en ese orden.
# ---------- Salida
#El valor de la distancia (numero flotante) que existe entre los dos puntos. Despliega el resultado con la palabra distancia ). Por ejemplo: distancia=9.90
# Ejemplo de ejecución del programa# 
from math import sqrt

print("Ingresa los siguientes valores para el primer punto")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("Ingresa los siguientes valores para el segundo punto")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distancia = sqrt((x2-x1)**2 + (y2-y1)**2)
print("Distancia: " + str(distancia))