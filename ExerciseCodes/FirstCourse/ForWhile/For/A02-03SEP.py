# Escribe un programa que pregunte cuantos números se van a introducir, 
# pida esos números (que puedan ser decimales) y calcule su suma.

n = int(input("Introduce los numeros que se van a ingresar: "))
suma = 0
for i in range(n):
    suma += float(input("Ingresa el numero: " + str(i) + ": "))
print("Suma: " + str(suma))