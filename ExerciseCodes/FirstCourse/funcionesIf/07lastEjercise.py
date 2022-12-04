# Los padres de un niño le regalarán $10 cuando cumpla n años,
#  y cada cumpleaños doblarán la cantidad que le darán hasta que el obsequio exceda $1000.
# 
# Escribe un programa que lea el valor n, es decir, la edad en la que iniciará el regalo de $10 y muestre 
# como salida la edad que tendrá el niño cuando reciba el último obsequio y la cantidad de dinero quewhile cant < 1000:  recibirá en ese año

n = int(input("Ingresa la edad del niño: "))
cant = 0
for i in range(n):
    cant += 10*i
if cant > 1000:
    print("El regalo ya excedio los $1000 ya que tiene " + str(n) + " años\n")        
else:
    print("El niño recibirá " + str(cant) + " por su compleaños numero " + str(n))
