# Modificar el ejercicio anterior para que además de pedir el número para elaborar su tabla, 
# pida hasta que valor de la misma desea desplegar (no necesariamente 10 elementos, tu decides cuantos)


n = int(input("Desplegar la tabla del numero: "))
l = int(input("Desplegar el numero limite: "))
i = 1
while(i <= l):
    print(str(n) + " x " + str(i) + " = " + str(n*i))
    i += 1

