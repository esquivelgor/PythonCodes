# Crea una función que dados dos números mostrará todos los números que hay entre ellos.
#  Internamente debe reacomodarlos si el segundo es menor que el primero:

def mayor(x,y):
    if x > y:
        mayor = x; menor = y
        return mayor, menor
    elif y > x: 
        mayor = y; menor = x
        return mayor, menor
 
x = int(input("Ingresa el primer numero: "))
y = int(input("Ingresa el segundo numero: "))

M, m = mayor(x,y)
for i in range(m+1,M):
    print (i)

    