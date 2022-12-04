# Escriba un programa que pida dos números enteros.
# 
# El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero.
# 
# El programa terminará escribiendo los dos números.
b = -1000000000000000000
a = int(input("Ingresa el numero a: "))
while b < a:
    b = int(input("Ingresa el numero b: "))
print("Numbers: " + str(a) + "\t" + str(b)) 
