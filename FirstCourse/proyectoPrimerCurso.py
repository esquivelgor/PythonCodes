# Ejercicio medio termino - Hotel


# Interfaz principal
def menu():
    # Obtención de datos principales
    print(">>>>>>>>>>>>>>>> Bienvenido a nuestra pantalla principal <<<<<<<<<<<<<<<<<<<<\n")
    # Tipo de habitación
    hab = input("Por favor, ingresa el tipo de habitación\n >>>>>>>>> Habitación estandar (a) <<<<<<<<<<\n >>>>>>>>> Master Suite (b) <<<<<<<<<<\nValor: ")
    
    if hab == "a":
        habA(hab)
    elif hab == "b":
        habB(hab)
    else:
        repetir = True
        return repetir
    return validacion()

# Habitación estándar 
def habA(h):
    print("\n-------------- Habitación estandar --------------\n(1) Habitacíon sencilla - $700\n(2) Habitación doble - $1000\n")
    # Seleccion del tipo de habitación 
    cant = int(input("¿Que tipo de habitación desea seleccionar? "))
    if cant == 1:
        print("\nEl cliente deberá pagar $700 por una habitación estandar sencilla\n\n")
    elif cant == 2:
        print("\nEl cliente deberá pagar $1000 por una habitación estandar doble\n\n")
    else:
        print("\nIngreso de forma erronea los datos!\n\n")

# Habitación master suite
def habB(h):
    print("-------------- Habitación Master Suite --------------\n(1) Habitacíon sencilla - $1500\n(2) Habitación doble - $2000\n(3) Habitación cuádruple - $3000")
    cant = int(input("¿Que tipo de habitación desea seleccionar? "))
    if cant == 1:
        print("\nEl cliente deberá pagar $1500 por una habitación Master Suite sencilla\n\n")
    elif cant == 2:
        print("\nEl cliente deberá pagar $2000 por una habitación Master Suite doble\n\n")
    elif cant == 3:
        mar = int(input("\n¿Desea que tenga vista al mar?\nIngrese 1 para confirmar o 2 para negar\n"))
        if mar == 1:
            print("\nEl cliente deberá pagar $3000 por una habitación Master Suite cuádruple con vista al mar\n\n")
        elif mar == 2:
            print("\nEl cliente deberá pagar $3000 por una habitación Master Suite cuádruple\n\n")
        else:
            print("\nIngreso de forma erronea los datos!\n\n")       
    else:
        print("\nIngreso de forma erronea los datos!\n\n")
 
# Función para la validacion de repeticion del codigo
def validacion():
    sn = input("¿Desea repetir el programa? \n(Escriba Si o No)\n")
    # Mediante la entrada del usuario se cambia el valor común y se regresa al codigo principal
    if (sn == "Si") or (sn == "si") or (sn == "SI"):
        repetir = True
        return repetir
    elif(sn == "No") or (sn == "no") or (sn == "NO"):
        print("Gracias por usar Escenotelapp!") # (Nombre random haha)
        repetir = False
        return repetir
    else:
        print("Hubo un error en la entrada de los datos!")      



print("-------------------------------------------------------------------\n")
print("----------------------- Hotel Escenario ---------------------------\n")
print("-------------------------------------------------------------------\n")

# Ciclo para repetir si lo desea el usuario
repetir = True
while repetir == True:
    # Mostramos nuestra interfaz principal
    repetir = menu()
