# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
# rectángulo como el que se muestra. El número ingresado es el número de niveles



n = int(input("Ingresa un numero de niveles: "))
i = 0
while i <= n:
    print("*"*i)
    i += 1