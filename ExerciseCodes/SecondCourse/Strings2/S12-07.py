# Escribir un programa en Python que lea un string y muestre como salida el string recibido escrito en reversa, 
# comenzando con el último carácter y terminando con el primer carácter del string original, y completamente en
# mayúsculas.

s = input("Ingresa un texto: ")
si = " "
for i in range((len(s)-1),-1,-1):
    si += s[i]

print(si.upper())

