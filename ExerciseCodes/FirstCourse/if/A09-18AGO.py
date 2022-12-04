# El índice de masa corporal (IMC) se utiliza para determinar si la proporción de peso y altura de una persona es adecuada.
#  El IMC se puede calcular utilizando la siguiente fórmula:   IMC=pesoaltura2
# 
# Donde el peso debe darse en kilogramos y la altura en metros ambas entradas son datos de punto flotante.
# 
# La siguiente tabla muestra cómo se clasifican los diferentes rangos de índice:
# 
# 
# Rango de índice Descripción
# 
# 
# índice < 20    'PESO BAJO'
# 20 <= índice < 25    'NORMAL'
# 25 <= índice < 30    'SOBRE PESO'
# 30 <= índice < 40    'OBESIDAD'
# 40 <= índice    'OBESIDAD MORBIDA'
# 
# Escribe el programa ll que determina el IMC correspondiente a partir del peso
#  (en kilogramos y la altura (en metros) que se dan como entrada uno en cada reglón. 
# La salida será un String indicando el índice correspondiente, 
# la descripción del índice de masa corporal se mostrará en mayúsculas.
#
# Entrada
# 
# Dos números flotantes (peso y altura) uno en cada renglón.
# 
# Salida
# 
# Descripción del índice corporal..

peso = float(input("Ingresa tu peso en kilogramos: "))
alt = float(input("Ingresa tu altura en metros: "))
IMC = peso/(alt**2)
if IMC < 20:
    print("Tu IMC es: BAJO ")
elif IMC >= 20 and IMC < 25:
    print("Tu IMC es: NORMAL ")
elif IMC >= 25 and IMC < 30:
    print("Tu IMC es: SOBREPESO ")
elif IMC >= 30 and IMC < 40:
    print("Tu IMC es: OBESIDAD ")
elif IMC >= 40:
    print("Tu IMC es: OBESIDAD MORBIDA ")
        