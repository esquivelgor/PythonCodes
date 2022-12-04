# Escribe un programa que pida el número de datos a recibir, 
# posteriormente pida cada uno de ellos de la forma 
# indicada y proporcione como salida la suma de todos los números y el promedio.
i = 1; total = 0
n = int(input("Ingresa el numero de valores a ingresar: "))

while i <= n:
    data = int(input("Ingresa el dato numero " + str(i) + ": "))
    total += data
    i += 1

print("Suma total: " + str(total))
print("Promedio: " + str(total/n))