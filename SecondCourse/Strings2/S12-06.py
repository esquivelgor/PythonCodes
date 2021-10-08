# Diseña un programa que muestre la cantidad de números que aparecen en una cadena leída de teclado. 
# Con número no queremos decir dígito, sino número propiamente dicho, es decir, secuencia de dígitos.
#  La cadena ’un 1, un 201 y 2 unos’, por ejemplo, tiene 3 números: el 1, el 201 y el 2

s = input("Ingresa una cadena de numeros: ").split(" ")
print("Aparecen un total de " + str(len(s)) + " números")

