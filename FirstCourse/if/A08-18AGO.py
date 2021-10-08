# Escribe un programa que pida que se teclee un valor entero e indique si el número es:
# 
# Par positivo
# Impar positivo
# Par negativo
# Impar negativo
# Para este ejercicio considera el valor 0 como par positivo.

n = int(input("Ingresa un valor entero: "))
if ((n >= 0) and ((n % 2) == 0)):
    print("Par positivo")
elif ((n < 0) and ((n % 2) == 0)):
    print("Par negativo")
elif ((n >= 0) and not((n % 2) == 0)):
    print("Impar positivo")
elif ((n < 0) and not((n % 2) == 0)):
    print("Impar negativo")