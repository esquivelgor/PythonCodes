# Leer números enteros mediante el teclado, hasta que el usuario ingrese el 0.

# Finalmente, mostrar la sumatoria de todos los números ingresados.

a = 1; suma = 0
while a != 0:
    a = int(input("Ingresa un numero: "))
    suma += a
a -= 1
print("El total fue: " + str(suma))