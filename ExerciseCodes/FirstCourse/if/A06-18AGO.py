# Crea un programa que, dado el valor de x, 
# te despliegue su correspondiente valor de y de acuerdo a la siguiente función por intervalos:
# si x= -2  la salida es y=-1
# si x=0 la salida es y=0
# si x= 3 la salida es y=4

x = int(input("Ingresa el valor de x: "))

if x == 0:
    y = 0
    print("x = " + str(x) + ",y = " + str(y))
elif x > 0:
    y = x + 1
    print("x = " + str(x) + ",y = " + str(y))
elif x < 0:  
    y = -1
    print("x = " + str(x) + ",y = " + str(y))