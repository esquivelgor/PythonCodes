# Escribe un programa, el cual recibe un string y nos despliegue como salida un nuevo string pero
#  con todas las vocales en mayúsculas. Si la palabra no tiene vocales o las vocales ya están en mayúsculas, 
#  la salida será un String idéntico al recibido por el usuario.

a = ""
l = ["a","e","i","o","u","A","E","I","O","U"]
s = input("Ingresa un texto: ")
for i in s:
    if i in l:
        a += i.upper()
    else:
        a += i
print(a)