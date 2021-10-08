# Escriba un programa que permita crear una lista de palabras y que, a continuación,
#  cree una segunda lista igual a la primera, pero al revés 
# (no se trata de escribir la lista al revés, sino de crear una lista distinta).

x = int(input("Ingresa el numero de valores que tendrá la lista: "))
l = []
for i in range(x):
    l.append(input("Valor [{}]: ".format(i+1)))

print("La lista actualizada es: {}".format(l[::-1]))
