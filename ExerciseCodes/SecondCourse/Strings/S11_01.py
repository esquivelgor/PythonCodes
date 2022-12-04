# Escribe un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable.
# 
# A continuación, mostrar en pantalla la primera letra del texto ingresado.
# 
# Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad
#  de caracteres que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, 
#  tendrá que ser un número entre 0 y 3) y almacenar este número en una variable llamada índice.
# 
# Mostrar en pantalla el carácter del texto ubicado en la posición dada por índice.


s = input("Ingresa un texto: ")
print("La primer palabra del texto es: " + s[0])

nm = int(input("Ingrese un numero positivo menor a la cantidad de caracteres que tiene el texto anterior: "))
if nm < len(s):
    print(s[nm-1])
