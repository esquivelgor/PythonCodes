# Escribe un programa que mediante una función pida dos números enteros y escriba qué números son pares
#  y cuáles impares desde el primero hasta el segundo.
# 
# Valida que el segundo es mayor que el primero. Los dos números entran como argumentos a la función. 

def impar(x,y):
    for i in range(x, y+1):
        if(i % 2 == 0):
            print("El valor " + str(i) + " es par")
        else:
            print("El valor " + str(i) + " es impar")


x = int(input("Ingresa el primer numero: "))
y = int(input("Ingresa el segundo numero: "))
impar(x,y)