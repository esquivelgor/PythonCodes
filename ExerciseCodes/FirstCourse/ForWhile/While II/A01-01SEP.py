# Escribe un programa que escriba en pantalla los múltiplos 
# de 2 comprendidos entre 1 y 100 y muestre la siguiente salida:


a = 2
while a <= 100:
    if (a%2 == 0):
        print(a, "\t", a+2,"\t", a+4, "\t", a+6, "\t", a+8)
        a += 8
    a += 1
