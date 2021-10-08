# Los divisores propios de un número n son aquellos divisores positivos menores que n.
# 
# Un número entero positivo n se dice que es perfecto si la suma de sus divisores propios es igual a n.
# 
# Realiza un programa que lea un número y muestre un mensaje indicando si es perfecto o no.
# 
# Por ejemplo:
# 
# Si se teclea 6
# 
# El programa mostrará el mensaje :  “El número es perfecto”
# 
# Nota: 6 es perfecto porque sus factores son 1,2,3 y 6. En este caso no se considera a él mismo y la suma de 1+2+3=6

# -------------------- Honestamente, no estoy seguro que este bien, lo dejaré hasta el final para revisarlo con mas tiempo -------------------------

n = int(input("Ingresa un numero: "))
d = n; suma = 0
while d % 2 == 0:
    suma += d
    d -= 1
d-=1
if suma == n:
    print("El numero es perfecto.")
else:  
    print("El numero no es perfecto")

