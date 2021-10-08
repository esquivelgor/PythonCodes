# Escriba un programa que pida el número de mes (del 1 al 12 ) e imprima el número de días que tiene el mes, donde: 
# 
#  El mes 2 tiene 28 dias
#  Los meses 4,6,9 y 11 tienen 30 días
#  Los meses 1,3,5,7,8,10 y 12 tienen 31 días
#    Si da un mes diferente a los anteriores deberá imprimir el mensaje “MES ERRONEO”

num = int(input("Ingresa un número entre el 1 y el  12: "))

if (num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12):
    print("El mes " + str(num) + "tiene 31 dias")
elif (num == 4 or num == 6 or num == 9 or num == 11):
    print("El mes " + str(num) + "tiene 30 dias")
elif (num == 2):
    print("El mes " + str(num) + "tiene 28 dias")
else:
    print("MES ERRONEO")