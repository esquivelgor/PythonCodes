# Escriba un programa que permita crear una lista de palabras y que, a continuación,
#  pida una palabra y elimine esa palabra de la lista.


x = int(input("Ingresa el numero de valores que tendrá la lista: "))
l = []
for i in range(x):
    l.append(input("Valor [{}]: ".format(i+1)))


s1 = input("Eliminar la palabra: ")
if s1 in l:
    l.remove(s1)
else:
    print("Tal palabra no se encuentra en la lista")
print("La lista actualizada es: {}".format(l))
