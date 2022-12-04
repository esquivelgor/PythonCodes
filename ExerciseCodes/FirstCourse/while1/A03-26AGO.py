# Escriba un algoritmo que lea del teclado un 
# número entero y que compruebe si el número es menor que 10.
# 
# Si no lo es, debe volver a leer el número repitiendo la operación
#  hasta que el usuario escriba un valor correcto.
# 
# Finalmente, debe escribir en pantalla el valor leído
#  cuando este sea correcto.

n = 11
while (n > 10):
    n = int(input("Ingresa n: "))
print(n)
