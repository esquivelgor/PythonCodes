#Escribe un programa que pregunte al usuario la cantidad de
# números a sumar, posteriormente ir pidiendo cada uno de los números e irlos sumando dentro del ciclo,
#  solamente si el número que va ingresando es positivo.
#
#Al final desplegar el valor de la suma (fuera del ciclo)



print("Suma varios numeros")
suma = 0; i = 0
n = int(input("Ingresa los numeros a sumar: "))
while (i != n):
    a = int(input("Ingresa el numero a sumar: "))
    if a > 0:
        suma += a
    i += 1
print("La suma fue: " + str(suma))
