# Realizar un programa que lea el ancho y largo de un rectángulo y
#  mediante dos funciones calcule su área y su perímetro.
def area(b,h):
    r = b*h
    return r
def perimetro(b,h):
    r = (2*b)+(2*h)
    return r

x = int(input("Ingresa el ancho del rectangulo: "))
y = int(input("Ingresa el alto del rectangulo: "))

print("El area es: " + str(area(x,y)))
print("El perimetro es: " + str(perimetro(x,y)))