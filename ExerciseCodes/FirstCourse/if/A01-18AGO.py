#Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.
#
#Ejemplo1:
#
#Entradas:  Primer número:  4 , Segundo número: 2 
#
#Salida:   "La división es exacta"
#
#Ejemplo2:
#
#Entradas:  Primer número:  4 , Segundo número: 3 
#
#Salida:   "La división no es exacta"




m = int(input("Ingresa numero uno: "))
n = int(input("Ingresa numero dos: "))
if ((m%n)==0):
    print("Residuo 0, División exacta")
else: 
    print("Este residuo es diferente a 0, Division no exacta")    