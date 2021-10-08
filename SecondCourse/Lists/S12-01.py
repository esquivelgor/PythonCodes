#  Escriba un programa que permita crear una lista de palabras.
#  Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista.
#  Por último, el programa tiene que escribir la lista.

x = int(input("Ingresa el numero de valores que tendrá la lista: "))
l = []
for i in range(x):
    l.append(input("Valor [{}]: ".format(i+1)))

print("Tu lista es {}".format(l))