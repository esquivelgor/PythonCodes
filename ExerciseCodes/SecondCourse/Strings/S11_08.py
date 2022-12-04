# Diseña un programa que lea una cadena y un número entero n y nos diga cuántas palabras tienen una longitud
#  de n caracteres.

s = input("Ingresa una cadena de texto: ")
x = int(input("Ingresa una longitud: "))

word = " "; lista = []; cta = 0

for i in range(len(s)):
    if s[i] != " ":
        word += s[i]
    else: 
        lista.append(word)
        word = " "
lista.append(word)

for i in lista:
    if len(i) == x+1:
        cta += 1
print("Hay ", cta, " palabra con el numero de caracteres ingresados")
