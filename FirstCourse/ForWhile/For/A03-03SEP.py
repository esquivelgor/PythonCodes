# Escribe un programa que pida dos números enteros y que mediante una función escriba la suma de todos 
# los enteros desde el primer número hasta el segundo.
# Los dos números entran como argumentos a la función. 

def suma(x,y):
    suma = 0 
    for i in range(x,y+1):
        suma += i
        print(suma)
    return suma

a = int(input("Ingresa el numero a: "))
b = int(input("Ingresa el numero b: "))

print("La suma es: " + str(suma(a,b)))
