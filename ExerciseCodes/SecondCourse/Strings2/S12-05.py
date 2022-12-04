# Diseña un programa que lea dos cadenas a y b y nos diga si b es un prefijo de a o no.
# 
# (Ejemplo: ’sub’ es un prefijo de ’subcadena’.)

p = input("Ingresa el prefijo: ")
s = input("Ingresa el texto: ")
pre = ""
for i in range(len(p)):
    pre += s[i] 
if pre == p:
    print("El texto '{}' si es prefijo de '{}'".format(p, s))
else:
    print("No tienen relacion")