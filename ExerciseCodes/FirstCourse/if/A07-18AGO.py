# Para determinar si un año es bisiesto o no debe de cumplir las siguiente regla:
#  Ser divisible entre 4 y no divisible entre 100 o bien divisible entre 400.
# 
# 2017 no es bisiesto (no es divisible entre 4)
#
# 2016 es bisiesto (divisible entre 4 y no divisible entre 100)
# 
# 2100 no es bisiesto  (divisible entre 4 y divisible entre 100)
# 
# 2400 es bisiesto  (divisible entre 400)
#    Escriba un programa que pida como entrada el año e imprima si el año es bisiesto o no.

year = int(input("Ingresa el año: "))

if((((year % 4) == 0) and (not((year % 100) == 0))) or (year % 400 == 0)):
    print("Este es un año bisiesto!!")
else:
    print("No es un año bisiesto")
