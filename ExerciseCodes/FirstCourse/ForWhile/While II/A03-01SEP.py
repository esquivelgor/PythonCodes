# Realiza un programa que solicite al usuario un número y nos muestre como salida su tabla de multiplicar del 1 al 10

n = int(input("Desplegar la tabla del numero: "))
i = 1
while(i <= 10):
    print(str(n) + " x " + str(i) + " = " + str(n*i))
    i += 1

