# Realiza un programa que indique el número de lustros que ha vivido una persona por medio de su año de nacimiento
#  y el año actual.

from datetime import date
# Se solicita el año de nacimiento del usuario
nacimiento = int(input("Ingresa tu año de nacimiento: "))
# Se obtiene el año actual basado en el sistema
actual = (date.today()).year 
# Obtenemos el numero de lustros 
lustros = (actual-nacimiento)//5
# Mostramos el resultado
print("El usuario tiene un total de " + str(lustros) + " lustros")