# Escribir un programa en Python que lea un string y muestre fragmentos de este.

s = input("Ingresa el texto: ")
print(len(s))
print(s[0])
print(s[-1])
a = ""
for i in range(1,len(s), 2):
    a += s[i]
print(a)
