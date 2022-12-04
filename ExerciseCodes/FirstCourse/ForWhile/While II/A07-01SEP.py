# Escribe un programa que lea un número entero positivo n y 
# muestre una lista de números que empieza en 1 e incrementa de uno en uno hasta llegar a n
#  y después decrementa de uno en uno hasta llegar a 1:
# 1, 2, ... n, n-1, n-2 ... 1
# 
# Por ejemplo:
# 
# Si n = 5 el programa debe mostrar:
# 1, 2, 3, 4, 5, 4, 3, 2, 1
# 
# Primero lograr la secuencia pedida en forma vertical, un elemento por renglón. Posteriormente modificarla para que se muestre en el mismo renglón y separado por comas
# 
# Nota que los números deben estar separados por una coma y después un espacio. Y nota que después del último número no hay coma.
# 
tot = []
i = 1
n = int(input("Ingresa un numero: "))

while i <= n:
    tot.append(i)
    i += 1
i = n-1
while i <= n and i > 0:
    tot.append(i)
    i-=1
    
print(*tot, sep = ", " ) 