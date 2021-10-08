# Realizar un programa que lea dos números de entrada y mediante una función despliegue su suma, 
# su resta, su multiplicación, su división y su residuo.  Ejecutar todo dentro de una sola función.
def operaciones(x,y):
    print("El resultado de la suma es: " + str(x+y))
    print("El resultado de la resta es: " + str(x-y))
    print("El resultado de la multiplicacion es: " + str(x*y))
    print("El resultado de la division es: " + str(x/y))
    print("El residuo de la division es: " + str(x%y))

n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))
operaciones(n1,n2)