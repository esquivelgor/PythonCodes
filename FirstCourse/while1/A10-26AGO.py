# Escriba un programa que pida la cantidad de números positivos que se tienen que escribir 
# y a continuación pida números
#  hasta que se haya escrito la cantidad de números positivos indicada.


n = int(input("Ingresa la cantidad de numeros a ingresar: "))
p = 0; t = 0
while (n != 0):
    nu = int(input("Ingresa un numero: "))
    if nu > 0:
        p += 1
        n -= 1
    t += 1
print("Se han escrito un total de " + str(t) + " numeros y " + str(p) + " de estos son positivos")