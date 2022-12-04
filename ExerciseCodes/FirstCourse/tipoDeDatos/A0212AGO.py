# Saca el promedio de calificaciones de tu semestre pasado.

suma = 0
# Se solicita el numero de materias
nMat = int(input("Ingresa el numero de materias a considerar: "))
# Se pide la calificacion individual de las materias y se suman
for i in range(nMat):
    m = int(input("Ingresa la materia numero " + str(i) + ": "))
    suma += m
promedio = suma/nMat
print("El promedio final fue: " + str(promedio))