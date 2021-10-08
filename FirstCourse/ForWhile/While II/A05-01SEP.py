# Escribe un programa que lea del teclado números enteros y los vaya contando y sumando.
#  El programa se debe detener cuando la suma de los números leídos sea 1000 o más.
# 
# Cuando la suma sea 1000 o más, el programa debe mostrar el total de la suma, 
# y la cantidad de números que se sumaron.
suma = 0; d = 0
while suma < 1000:
    n = int(input("Ingresa un numero a sumar: "))
    suma += n
    d += 1
print("La suma llegó a su limite!! \nEl total llegó a un total de: " + str(suma) + "\nY hubo un total de " + str(d) + " numeros ingresados")