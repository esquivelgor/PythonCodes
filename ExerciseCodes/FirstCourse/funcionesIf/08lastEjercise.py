# Hacer un programa que lea un numero y entregue la suma de sus dígitos. Considerar solo números con dos dígitos.

n = int(input("Ingresa un numero de dos digitos: "))
s = str(n)
x, y = s[0], s[1]
t = int(x)+int(y)
print(t) 