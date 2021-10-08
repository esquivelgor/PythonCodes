# Diseña un programa que lea una cadena y muestre el número de letras mayúsculas que contiene.
#    Ord regresa el valor ASCII de un caracter


s = input("Ingresa el texto: ")
upperCase = 0
for i in s:
    if i.isupper():
        upperCase += 1
print("Esta palabra tiene " + str(upperCase) + " letras en mayuscula")
