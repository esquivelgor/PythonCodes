# Escribir un programa que pida números al usuario, 
# mostrar los divisores de cada uno y, al finalizar, la cantidad total de números leídos en total.
# 
# Utilizar una o más funciones, según sea necesario. Se detiene al ingresar el -1.
# Considerar solamente números positivos.


def divisores(x,cta):
    divisores = []
    for i in range(1, x):
        if (x%i) == 0 :
            divisores.append(i%x)
    cta += 1
    divisores.append(x)
    print("divisor(" + str(x) + ") tenemos estos divisores: " + str(divisores))
    return cta


cta = 0
x = int(input("Ingresa un número: "))
if x > 1:
    while x > 0:
        cta = divisores(x,cta)
        x = int(input("Ingresa un número: "))
else:
    print("Numero no valido")

print("Se ingresaron " + str(cta) + " numeros validos")