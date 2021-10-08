# Diseña un programa que lea una cadena y muestre el número de espacios en blanco que contiene.

cta = 0
s = input("Ingresa un texto: ")
for i in s:
    if i == " ":
        cta += 1
print("Hay " + str(cta) + " espacios en el texto") 