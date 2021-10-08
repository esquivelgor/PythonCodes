# En una universidad cada estudiante cursa 4 materias en el semestre.
# Preguntar el nombre y semestre del alumno.

# Desarrolla un programa que pregunte la calificación de cada materia, 
# calcula el promedio de las 4 materias y muestra el resultado, 
# así como los datos del alumno en formato agradable al usuario.


suma = 0; nMat = 4 
# Se solicitan los datos 
nombre = input("Ingresa el nombre: ")
semestre = int(input("Ingresa el semestre: "))

# Se pide la calificacion individual de las materias y se suman
for i in range(nMat):
    m = int(input("Ingresa la materia numero " + str(i) + ": "))
    suma += m
promedio = suma/nMat
print("\nAlumno: " + nombre + "\nSemestre: " + str(semestre) + "\nEl promedio final fue: " + str(promedio))