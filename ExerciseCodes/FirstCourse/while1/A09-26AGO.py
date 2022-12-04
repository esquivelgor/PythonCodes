# Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar 
# y luego ingrese la longitud de cada perfil, sabiendo que la pieza cuya longitud esté comprendida 
# en el rango de 1.20 y 1.30 son aptas.
# 
# Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.
suma = 0
n = float(input("Ingresa las piezas a contemplar: "))
a = n
while n != 0:
    p = float(input("Ingresa la longitud de la pieza: "))
    if (p <= 1.20) or (p >= 1.30):
        a -= 1
    n -= 1 
print("Tenemos " + str(a) + " piezas ")