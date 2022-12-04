#Escribir un programa que, mediante una función,
#  verifique si un caracter introducido es una vocal o no.

# Tip: comparar el caracter ingresado con cada una de las vocale

a = input("Ingresa un caracter: " )

def verif(n):
    if(n[0] == 'a' or n[0] == 'e' or n[0] == 'i' or n[0] == 'o' or n[0] == 'u'):
        print("La primer letra es una vocal!")
    else:
        print(str(n[0]) + " no es una vocal!!")

verif(a)

