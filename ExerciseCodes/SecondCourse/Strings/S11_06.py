# Diseña un programa que lea una cadena y muestra en pantalla el mensaje ((Contiene dígito)) 
# si contiene algún dígito y ((No contiene dígito)) en caso contrario.

s = input("Ingresa un texto: ")
di = False
for i in s:
    if i.isdigit():
        di = True
if di == True:
    print("Contiene dígito")
else: print("No contiene dígito")

