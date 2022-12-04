# Desarrolla un programa que solicite un número entero, 
# entre 0 y 360 que representa los grados del plano cartesiano y
# que muestre como resultado el número de cuadrante en donde se encuentra. 
# En caso de que el grado caiga en un eje, tu programa debe mostrar la palabra "eje".
# En caso de que el grado sea menor a cero o mayor a 360,  tu programa debe mostrar la palabra "excede".

x = int(input("Ingresa un número entero entre 0 y 360: "))
if (x >= 0 and x <= 360):
    if (x > 0 and x < 90):
        print("Está en el segundo cuadrante")
    elif(x > 90 and x < 180):
        print("Está en el primer cuadrante")
    elif(x > 180 and x < 270):
        print("Está en el tercer cuadrante")
    elif(x > 270 and x < 360):
        print("Está en el cuarto cuadrante")
    else:
        print("Eje")
else:
    print("Debe ser un numero entre 0 y 360, este excede")