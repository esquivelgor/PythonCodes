# Escribe un programa que pregunte cuántos números se van a introducir, pida esos números, 
# y muestre un mensaje cada vez que un número no sea mayor que el primero.

x = int(input("Ingresa cuantos numeros deseas ingresar:  "))
a = int(input("Ingresa el numero: "))
for i in range(x):
    n = int(input("Ingresa el numero: "))
    if n < a:
        print("El numero que ingresaste es menor que el anterior!")