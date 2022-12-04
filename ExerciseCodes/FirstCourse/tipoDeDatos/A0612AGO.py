# Crea un programa que pregunte al usuario su nombre y su edad. Debe imprimir en pantalla un mensaje indicando el año en que cumplirá 100 años

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
a = (2021-edad) + 100
print("En el año " + str(a) + " cumplirás 100 años, " + nombre + "!!" )