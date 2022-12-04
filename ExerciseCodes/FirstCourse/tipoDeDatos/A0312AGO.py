# Calcula la propina que debe dejar una persona de acuerdo con un monto de consumo. El porcentaje de propina es una entrada.

# Obten el porcentaje de la propina
pp = int(input("Ingresa el porcentaje considerado de las propinas (Escala 1-100):  "))
pp /= 100
# Calcula y muestra la propina a otorgar
consumo = int(input("Ingresa el monto total: "))
print("La propina que se debe dejar es de: " + str(consumo*pp))
