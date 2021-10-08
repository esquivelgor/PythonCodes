# El programa deberá pedir la edad y el nombre y hacer los cálculos necesarios.


edad = int(input("Introduce tu edad: "))
nombre = input("Introduce tu nombre: ")
tiempo = edad*365
print("\nEdad: " + str(edad) + "\tNombre: " + str(nombre) + "\nHas vivido mas de " + str(tiempo) + " dias.")