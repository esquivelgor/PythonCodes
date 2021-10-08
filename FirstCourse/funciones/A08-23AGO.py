# Escribe una función que reciba como parámetro 2 números enteros y una clave que es una letra.
# 
# La clave representa una operación aritmética de acuerdo con la siguiente tabla:
# 
# Clave Significado
# 
# s        Suma
# r        Resta
# m       Multiplicación
# d        División
# 
# La función debe aplicar la operación aritmética a los 2 valores recibidos y 
# regresar como valor de retorno el resultado de dicha operación.
# 
# Nota que dentro de la función no mostrarás nada, solo regresarás el valor usando return.
# 
#  
# 
# Escribe ahora una función main en la que pidas al usuario teclear 2 valores numéricos 
# y una clave (s, r, m, d), después llama la función con los parámetros correspondientes 
# y luego muestra el resultado de la operación que regresó la función

def operacionMat(x,y,a):
    if(a == 's'):
        r = x+y
        return r
    elif(a == 'r'):
        r = x-y
        return r
    elif(a == 'm'):
        r = x*y
        return r
    elif(a == 'd'):
        r = x/y
        return r
    else:
        print("Esta no es una operacion valida")

def solEImpr():
    a = input("-----Operaciones-----\nTeclear para las siguientes operaciones: \nSuma = s\nResta = r\nMultiplicación = m\nDivision = d\nIngresa el tipo de operacion: ")
    n1 = int(input("Ingresa el primer numero: "))
    n2 = int(input("Ingresa el segundo numero: "))
    r = operacionMat(n1,n2,a)
    if(r != None):
        print("\nEl resultado de su operacion es: " + str(r) )
    else:
        print("\nSucedió un error")
    


solEImpr()