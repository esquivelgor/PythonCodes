# Programa que dada una lista de números, cambia dichos números por su cuadrado.
from math import pow

x = int(input("Ingresa el numero de valores que tendrá la lista: "))
l = []; l2 = []
for i in range(x):
    l.append(input("Valor [{}]: ".format(i+1)))

for i in l:
    l2.append(int(pow(int(i),2)))
print(l2)