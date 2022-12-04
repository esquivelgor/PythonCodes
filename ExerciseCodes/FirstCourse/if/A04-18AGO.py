# Escriba un programa que pida tres números y diga si el tercero está más cerca del primero o del segundo.  
# 
# Tip: considerar el valor absoluto de la distancia entre dos elementos.     abs(variable)
# 
# Ejemplos :
# 
# Entrada -> a=1, b=5, c=10;   Salida->c está más cerca de b que de a
# Entrada -> a=1, b=8, c=3;   Salida->c está más cerca de a que de b

print("Ingresa 3 números: ")
a = int(input("Ingresa el numero a: "))
b = int(input("Ingresa el numero b: "))
c = int(input("Ingresa el numero c: "))

disA = abs(c - a)
disB = abs(c - b)
if (disA < disB):
    print("c está más cerca de a que de b")
elif (disA > disB):
    print("c está más cerca de b que de a")
else:
    print("Estan a la misma distancia")

