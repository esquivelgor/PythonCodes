# Requerir al usuario que ingrese un número entero e informar si es primo o no,
#  utilizando una función booleana que lo decida.


def primo(x):
    if x > 1:
        for i in range(2, x):
            if (x%i) == 0:
                return False
        return True
    else: 
        print("Por favor, ingresa un numero mayor a 1") 


x = int(input("Ingresa un numero para saber si es primo: "))
if primo(x):
     print ("Es primo")
else:
    print("No es primo")