# Escribe un programa que calcule el área y el volumen de una esfera, a partir de recibir el radio.
# A=4πr**2          Vol=4/3(πr**3)

from math import pi

r = int(input("Ingresa el radio: "))
area = 4*pi*(r**2)
volumen = ((pi*(r**3))*4)/3

print("Tus resultados son los siguientes\nArea: " + str(area) + "\nVolumen: " + str(volumen))