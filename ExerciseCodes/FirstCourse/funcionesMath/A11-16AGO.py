# Realiza un programa que reciba las coordenadas de dos puntos 
# y que calcule la pendiente de la recta que une esos dos puntos.
# ------------ El mismo que el anterior??? -------------------

print("---------- Pendiente de una recta ----------")
print("Ingresa los siguientes valores para el primer punto")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("Ingresa los siguientes valores para el segundo punto")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

m = (y2 - y1) / (x2 - x1)
print("La pendiente es aproximadamente igual a: " + str(m))
