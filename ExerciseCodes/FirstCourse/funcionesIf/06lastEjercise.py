# Hacer un programa que lea n números y determine cuál es el mayor, 
# el menor y la media de los números leídos.
# 
# Tip: Solo la primera vez, el primer número ingresado es asignado tanto a la variable mayor como a la menor.
#  Posteriormente empieza la comparación.

def promedio(ordenados, x):    
    s = 0
    for n in ordenados:
        print (n)
        s += n
    s /= x
    return s


ordenados = []; ordenadosM = []

# Ingreso de datos
n = int(input("Ingresa el numero de datos: "))
for i in range(1, n+1):
    x = int(input("Ingresa el numero " + str(i) + ": "))
    ordenados.append(x)

M = 0; m = 100000000
# Mayor
for i in range(n):
    if ordenados[i] > M:
        M = ordenados[i]
# Menor
for i in range(n):
    if ordenados[i] < m:
        m = ordenados[i]

ordenadosM.append(M)
ordenadosM.append(m)
ordenadosM.append(promedio(ordenados, n))

print("El numero mayor es: " + str(ordenadosM[0]) + "\nEl numero menor es: " + str(ordenadosM[1]) + "\nEl promedio es: " + str(ordenadosM[2]))
