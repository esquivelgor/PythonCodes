# Escribe un programa en el cual definas la función llamada calcula_grado. 
# Esta función debe recibir un número flotante entre 0 y 1, y debe regresar 
# una nota alfabética de acuerdo con la tabla.

# Entrada
# Un número flotante entre 0 y 1.
# 
# Salida
# La letra correspondiente al score asignado de acuerdo con la tabla de arriba.
# 
# Si la entrada no está dentro del rango de 0 a 1 (inclusive), 
# la función debe regresar la leyenda "score incorrecto" (sin las comillas).
# 
# Ejemplos de ejecución del programa
# 
# >>> 0.95
#
# A
# >>> 10.0
# 
# score incorrecto 
# >>> 0.5
# F


def calcula_grado(x):
    a = ""
    if(x >= 0 and x <= 1):
        if(x>0.9):
            a = "A"
            return a
        elif(x>0.8):
            a = "B"
            return a
        elif(x>0.7):
            a = "C"
            return a
        elif(x>0.6):
            a = "D"
            return a
        elif(x<=0.6):
            a = "F"
            return a
    else:
        print("Invalid number")

n = float(input("Ingresa un numero entre el 0 y 1: "))
print(calcula_grado(n))
