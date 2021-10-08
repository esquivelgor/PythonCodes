# Escribe un programa que lea los valores a y b
#  y muestre todos los números pares que van
#  desde a hasta b incluyendo los límites.
# 
# *Supón que siempre a < b.
# 
# Para este ejercicio considera el valor 0
#  como par

a = 0
a = int(input("Ingresa a: "))
b = int(input("Ingresa b: "))
while a <= b:
    if (a%2 == 0):
        print(a)
    a += 1
