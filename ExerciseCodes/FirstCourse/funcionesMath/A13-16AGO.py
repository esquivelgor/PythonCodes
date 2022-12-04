# Escribe un programa para calcular la cantidad de litros de pintura necesarios para pintar una superficie.

# El programa debe leer el área de la superficie a pintar en metros cuadrados y 
# la cantidad de metros cuadrados que se pueden cubrir con un litro de pintura.

# El programa debe mostrar la cantidad de litros de pintura que se deben comprar para cubrir esa superficie.
# Considera que sólo se pueden comprar litros completos de pintura.
# 
# Por ejemplo:
# Si se va a pintar una superficie de 857 metros cuadrados
# Y se sabe que se puede cubrir 10 metros cuadrados de superficie con un litro de pintura.

from math import ceil

print("---------------- Cantidad de litros de pintura necesarios para pintar una superficie ---------------")
area = int(input("Ingresa la superficie a pintar (en metros cuadrados): "))
mtsCub = int(input("Ingresa la superficie que se pueden cubrir por cada litro de pintura: "))
print
print("La cantidad de m2/l es: " + str(ceil(area/mtsCub)))