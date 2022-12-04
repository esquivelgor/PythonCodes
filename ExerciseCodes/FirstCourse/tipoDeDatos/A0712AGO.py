# Una compañía de telefonía celular cobra $0.80 por mensaje, por mega o por minuto.
# Realiza un programa que calcule el costo total mensual de un usuario según estos datos 
# (que son ingresados por el usuario).

print("Procede a ingresar los datos mensuales que se te indican")
msj = int(input("Mensajes enviados: "))
mega = int(input("Megas o minutos gastados: "))
pago = (0.80*msj) + (0.80*mega)
print("El usuario deberá pagar: $" + str(pago))