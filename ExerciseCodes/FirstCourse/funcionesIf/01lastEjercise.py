# Hacer un programa que permita sumar la sucesión de los números 21+22+...+2n ,
#  siendo n un número que se ingresa por medio del teclado.


n = int(input("Ingresa un numero: "))
suma = 0
for i in range(1, n+1):
    suma += (2**i)

print(suma)