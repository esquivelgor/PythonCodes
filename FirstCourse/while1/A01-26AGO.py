# Escribe un programa que realice lo siguiente:
# 
# Imprimir los números del 1 al 50.
# Imprimir los números del 50 al 75.
# Imprimir los números del -50 al -40.
# Imprimir los números del 2 al 100 pero de 2 en 2 (2,4,6,8 ....100).
# Nota: aunque tendrás 4 ciclos en el programa, para probar alguno, 
# comenta los otros 3 para que no imprima todo en la misma ejecución.

print("Para imprimir los numeros del 1 al 50 escribe: 1 ")
print("Para imprimir los numeros del 50 al 75 escribe: 2 ")
print("Para imprimir los numeros del -50 al -40 escribe: 3 ")
print("Para imprimir los numeros del 2 al 100 pero de 2 en 2 escribe: 4 ")
dec = int(input("Ingresa tu opcion: "))
if dec == 1:
    n = 1
    while (n <= 50):
        print(n)
        n += 1
elif dec == 2:
    n = 50
    while (n <= 75):
        print(n)
        n += 1
elif dec == 3:
    n = -50
    while (n <= -40):
        print(n)
        n += 1
elif dec == 4:
    n = 1
    while (n <= 100):
        if (n%2 == 0):
            print(n)
        n += 1
else: 
    print("Esa no es una opcion")

