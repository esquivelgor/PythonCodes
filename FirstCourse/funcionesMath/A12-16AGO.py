# Escribe un programa que reciba el ancho y largo de un rectángulo y calcule la medida de la diagonal
# . Utiliza la función de la librería math correspondiente. 

from math import hypot

print("-------------- Calcular la medida diagonal de un rectángulo ----------------")
height = int(input("Ingresa la altura: "))
width = int(input("Ingresa el ancho: "))
print("La diagonal mide: " + str(hypot(height, width)))