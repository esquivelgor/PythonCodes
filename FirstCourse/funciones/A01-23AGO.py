# Un programa que permita elevar un numero a cualquier potencia dada
def potencia(x,y): 
    r = x**y
    return r    



n = int(input("Ingresa el numero a elevar: "))
x = int(input("Ingresa la potencia: "))
r= potencia(n,x)
print("El resultado es: " + str(r))

    