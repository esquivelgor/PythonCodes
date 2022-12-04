# Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).


x = int(input("Ingresa el numero de valores que tendrá la lista: "))
l = []; nl = []
for i in range(x):
    l.append(input("Valor [{}]: ".format(i+1)))
# for i in l:
#     if l.count(i) > 1:
#         for j in range(l.count(i)-1):
#             l.remove(i)
#             
# print(l)

for i in l:
    if i not in nl:
        nl.append(i)
print(nl)

