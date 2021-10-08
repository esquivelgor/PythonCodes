# Crea un programa que pueda aceptar dos cadenas como entrada e imprima la cadena con la longitud máxima
#  en la consola. Si dos cadenas tienen la misma longitud, la función debe imprimir ambas cadenas línea por línea.

s1 = input("Ingresa el texto 1: ")
s2 = input("Ingresa el texto 2: ")

if len(s1) > len(s2):
    print(s1)
elif len(s2) > len(s1):
    print(s2)
else: 
    print(s1 + "\n" + s2)