import math 
# Programa que pida el radio de un círculo y calcule su área y su perimetro

radio = int(input("Ingresa el radio: "))
area = math.pi * (radio**2)
perimetro = math.pi * radio * 2

print("El area: " + str(area))
print("El perimetro: " + str(perimetro))
