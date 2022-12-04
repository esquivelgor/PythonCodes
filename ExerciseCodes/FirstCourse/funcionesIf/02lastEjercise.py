# Hacer un programa que pida por teclado dos números, 
# muestre la suma en pantalla y pregunte al usuario si quiere realizar otra suma.
# 
# *Modificarlo para que la petición se haga solamente dentro del ciclo, es decir,
#  los números se deben pedir dentro del ciclo incluso la primera vez.

# Reutilicé este codigo de mi examen
def validacion():
    sn = input("¿Desea repetir el programa? \n(Escriba Si o No)\n")
    # Mediante la entrada del usuario se cambia el valor común y se regresa al codigo principal
    if (sn == "Si") or (sn == "si") or (sn == "SI"):
        repetir = True
        return repetir
    elif(sn == "No") or (sn == "no") or (sn == "NO"):
        print("Gracias por usar esta app!") # (Nombre random haha)
        repetir = False
        return repetir
    else:
        print("Hubo un error en la entrada de los datos!")      


repetir = True
while repetir == True:
    x = int(input("Ingresa el primer numero: "))
    y = int(input("Ingresa el segundo numero: "))
    print("Tu resultado es: " + str(x+y) + "\n")
    repetir = validacion()
