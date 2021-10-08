# Escribe un programa que que mediante una función pida un número entero mayor que cero y 
# que escriba sus divisores. El número entra como argumento a la función. 
# 
# Un numero es divisor de otro si al hacer la división el residuo es cero
# 
# Valida que el numero pedido sea mayor que cero.

def div(x):
    if x > 0:
        for i in range(x,0,-1):
            if (i%2==0):
                print("El numero " + str(i) + " es divisor")
    else:
        print("Se necesita un numero mayor que 0")


x = int(input("Ingresa un numero entero mayor que cero: "))
div(x)