from random import randint
def numeroAleatorio():
    ra = randint(1, 10)
    numero = 0
    intento = 0
    try:
        numero = int(input("Elige un numero del 1 al 10: "))
    except:
        print("Debe ser numero rey")

    if numero > ra:
        print("El numero es menor, vuelve a probar un numero menor que " + str(numero))
        numero = int(input())
        if numero > ra:
            print("El numero es menor, vuelve a probar un numero menor que " + str(numero))
            intento += 1
            if numero > ra:
                print("El numero es menor, vuelve a probar un numero menor que " + str(numero))
                intento += 1
                numero = int(input())
            elif numero < ra:
                print("El numero es mayor, vuelve a probar")
                intento += 1
                numero = int(input())
            else:
                print("Le diste! \nEl numero es: " + str(ra))
                print("Tardaste " + str(intento) + " intentos!")
        elif numero < ra:
            print("El numero es mayor, vuelve a probar")
            intento += 1
        else:
            print("Le diste! \nEl numero es: " + str(ra))
            print("Tardaste " + str(intento) + " intentos!")
    elif numero < ra:
        print("El numero es mayor, vuelve a probar")
        intento += 1
        numero = int(input("Elige un numero del " + str(numero) + " hasta el 10: "))
        if numero > ra:
            print("El numero es menor, vuelve a probar un numero menor que " + str(numero))
            intento += 1
        elif numero < ra:
            print("El numero es mayor, vuelve a probar: ")
            intento += 1
            numero = int(input())
            if numero > ra:
                print("El numero es menor, vuelve a probar un numero menor que " + str(numero))
                intento += 1
            elif numero < ra:
                print("El numero es mayor, vuelve a probar")
                intento += 1
                if numero > ra:
                    print("El numero es menor, vuelve a probar un numero menor que " + str(numero))
                    intento += 1
                elif numero < ra:
                    print("El numero es mayor, vuelve a probar")
                    intento += 1
                else:
                    print("Le diste! \nEl numero es: " + str(ra))
                    print("Tardaste " + str(intento) + " intentos!")
            else:
                print("Le diste! \nEl numero es: " + str(ra))
                print("Tardaste " + str(intento) + " intentos!")
        else:
            print("Le diste! \nEl numero es: " + str(ra))
            print("Tardaste " + str(intento) + " intentos!")
    else:
        print("Le diste! \nEl numero es: " + str(ra))
        print("Tardaste " + str(intento) + " intentos!")
numeroAleatorio()

