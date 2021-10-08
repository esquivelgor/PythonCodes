# Escribe un programa que reciba un texto y detecte cuantas palabras lo conforman.
s = input("Ingresa un texto: ")

space = 0; rep = 0; word = False

for i in s:
    if (i != " "):
        rep = 0
        word = True
    if (i == " ") and (rep == 0):
        space += 1
        rep += 1
if (rep == 1):
    space -= 1

if (word == False):
    print("No hay ninguna palabra en tu texto")
else:
    print("Hay un total de " + str(space+1) + " palabras ")
    
