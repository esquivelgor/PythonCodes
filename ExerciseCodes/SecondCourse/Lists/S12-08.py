# Programa que recibe del usuario una cadena (string) y nos indica cuántas vocales tiene.
# 
# Usar la lista   vocales= ['a','e','i','o','u','A','E', 'I', 'O', 'U']

vocales = ['a','e','i','o','u','A','E', 'I', 'O', 'U']

s = input("Ingresa un texto: ")
v = 0
for i in s:
    if i in vocales:
        v += 1

print("Hay un total de {} vocales".format(v))
