# Realizar un programa que lea el número de millas y mediante una función las convierta a kilómetros.

def change(miles):
    km = miles * 1.60934
    return km


miles = float(input("Ingresa las millas que quieres convertir: "))
print(str(miles) + " millas son equivalentes a: " + str(change(miles))+ " kilometros")