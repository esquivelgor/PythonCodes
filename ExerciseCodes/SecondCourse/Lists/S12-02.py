# Escriba un programa que permita crear una lista de palabras y que, a continuación,
#  pida una palabra y diga cuántas veces aparece esa palabra en la lista.


x = int(input("Ingresa el numero de valores que tendrá la lista: "))
l = []
for i in range(x):
    l.append(input("Valor [{}]: ".format(i+1)))

s = input("Ingresa la palabra que deseas buscar: ")
if s in l:
    print("Tu palabra esta un total de {} veces".format(l.count(s)))