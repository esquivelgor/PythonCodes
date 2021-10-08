# Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# pida dos palabras y sustituya la primera por la segunda en la lista.

x = int(input("Ingresa el numero de valores que tendrá la lista: "))
l = []
for i in range(x):
    l.append(input("Valor [{}]: ".format(i+1)))


s1 = input("Sustituir la palabra: ")
s2 = input("Por la palabra: ")
if s1 in l:
    l[l.index(s1)] = s2
else:
    print("Tal palabra no se encuentra en la lista")

print("La lista actualizada es: {}".format(l))
