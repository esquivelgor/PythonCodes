# El área de un triángulo se puede calcular a partir de valor de dos de sus lados mediante  la fórmula 
#                A=12absin(θ) 

# Realiza un programa que pida el valor de los lados y el ángulo (en grados) y muestre el valor del área.

from math import radians, sin 

ca = int(input("Ingresa la longitud del cateto adyacente: "))
hi = int(input("Ingresa la longitud de la hipotenusa: "))
angle = radians(int(input("Ingresa el valor del ángulo: "))) 
res = (ca*hi*sin(angle))/2
print("El resultado es: " + str(res)) 