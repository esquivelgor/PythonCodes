# Realizar un programa que reciba el cateto adyacente y el ángulo α (en grados) , 
# y entregue como salida el cateto opuesto.

# *Ten en cuenta que la función cos () de Python trabaja con radianes, 
# así que el ángulo que recibes en grados deberás convertirlo a radianes.
from math import radians, tan

ca = int(input("Ingresa la longitud del cateto adyacente: "))
angle = radians(int(input("Ingresa el valor del ángulo: ")))
res = tan(angle)*ca
print("El resultado es: " + str(res))