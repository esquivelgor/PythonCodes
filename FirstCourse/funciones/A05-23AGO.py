# Realizar un programa que pida el radio de una esfera y mediante dos funciones calcule su área y su volúmen.
from math import pi 

def area(r):
    a = (4*pi*(r**2))
    print("El area es: " + str(a))
def volumen(r):
    v = (4*pi*(r**3))/3
    print("El volumen es: " + str(v))


r = int(input("Ingresa el radio de la esfera: "))

area(r)
volumen(r)