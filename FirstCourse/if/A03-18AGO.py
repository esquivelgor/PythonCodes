# Escribir un programa que convierta grados a radianes o viceversa,
#  dependiendo de la opción que elija el usuario.
# 
# Ejemplo:
# 
# Selecciona 1 si deseas convertir grados a radianes o selecciona 2 si deseas convertir radianes a grados. 
# (En lugar de 1 o 2 puede ser "a" o "b" o alguna palabra, pero hay que especificarla al usuario)

# Escribe un programa que reciba una cantidad de grados y los convierta a radianes.
from math import radians, degrees


print("Selecciona alguna de las opciones \nGrados a Radianes - 1\nRadianes a Grados - 2")
opt = int(input("Ingresa tu opción: "))
if(opt == 1):
    x = int(input("Ingresa los grados que quieres convertir a radianes: "))
    print("Son: " + str(radians(x)) + " radianes" )
elif( opt == 2):
    x = int(input("Ingresa los radianes que quieres convertir a grados: "))
    print("Son: " + str(degrees(x)) + " degrees" )
else:
    print("Debes ingresar un numero entre 1 y 2")
