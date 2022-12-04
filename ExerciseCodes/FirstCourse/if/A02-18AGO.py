# Escribe un programa que reciba la calificación del examen y la del proyecto. 
# Si la calificación del examen es mayor o igual a 70 Y la del proyecto es mayor a 50 despliega la palabra APROBADO,
#  en caso contrario la palabra mostrada es REPROBADO.

ex = int(input("Ingresa la calificación del examen: "))
proy = int(input("Ingresa la calificación del proyecto: "))

if ((ex > 70) and (proy > 50)):
    print("APROBADO")
else:
    print("REPROBADO")