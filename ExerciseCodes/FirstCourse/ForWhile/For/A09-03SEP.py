# Escribe un programa que pida un número entero mayor que 1 y 
# que mediante una función escriba si el número es un número primo o no.
# 
# Un número primo es aquel que solo es divisible entre 1 y el mismo número.
#  Ejemplo: 1, 3, 5, 7, 11, 13    ( 6 aunque es divisible entre 1 y 6, también es divisible entre 
#  2 al menos, por lo tanto no es primo)

def primo(n):
    noti = False
    if n > 1:
        for i in range(2,n):
            if (n%i) == 0:
                noti = True
                break
    if noti == True:
        print("El numero no es primo")
    else:
        print("El numero es primo")


x = int(input("Ingresa un número mayor que 1: "))
primo(x)