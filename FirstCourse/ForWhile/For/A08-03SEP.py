# Escribe un programa que pregunte cuántos números se van a introducir y que mediante una función
#  pida esos números, y diga al final cuántos han sido pares y cuántos impares.

def registro(n):
    par = 0; impar = 0; 
    for i in range(n):
        a = int(input("Ingresa un valor: "))
        if a % 2 == 0:
            par += 1
        else:
            impar += 1
    print("Resultado\nPares: " + str(par) + "\nImpares: " + str(impar))

x = int(input("Ingresa cuantos numeros deseas introducir: "))
registro(x)