# Escribe una función llamada equivalente que reciba como parámetro una cantidad de 
# horas, minutos y segundos y regrese como valor de retorno el tiempo equivalente en segundos.
# 
# Por ejemplo:
# 
# Si la función recibe los valores horas = 2, minutos = 20 y segundos = 8, regresará el valor 8408.
# 
# Nota que la función no mostrará nada, solo regresa como valor de retorno la cantidad de segundos equivalente.

def sec(s,m,h):
    t = 0
    t += s + (m*60) + (h*3600) 
    return t


print("--------- Equivalente de tiempo en segundos ----------")
s = int(input("Ingresa los segundos: "))
m = int(input("Ingresa los minutos: "))
h = int(input("Ingresa las horas: "))
t = sec(s,m,h)
print(t)
