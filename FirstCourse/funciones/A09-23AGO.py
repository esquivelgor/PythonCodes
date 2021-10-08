# Escribe un programa que convierta pies, pulgadas y yardas a centímetros, para lo cual debes definir 3 funciones:
# 
# Función que reciba una cantidad de pies (entero positivo) y devuelva el equivalente a centímetros.
# Función que reciba una cantidad de pulgadas (entero positivo) y devuelva el equivalente a centímetros.
# Función que reciba una cantidad de yardas (entero positivo) y devuelva el equivalente en centímetros.
# Definir un menú parecido a lo siguiente:
# 
# if opcion=1:
#     pies_a_cm()
# elif opcion==2:
#     pulg_a_cm()
# elif opcion==3:
#     yardas_a_cm()
# 
# Nota: La función puede o no regresar un valor. Tú lo decides.
# 
# Salida
# 
# La cantidad equivalente en centímetros (sólo el número).
# 
# En caso de que el número de opción sea diferente a 1, 2, o 3 se desplegará el mensaje: Error.

def piesCm(x):
    return x*30.48
def pulgadasCm(x):
    return x*2.54
def yardasCm(x):
    return x*91.44


print("----- Calculadora de conversiones a centimetros--------")
a = input("Elige alguna de las siguientes opciones \n\tPies\n\tPulgadas\n\tYardas\nIngresa el nombre de la opcion: ")
if(a == 'pies' or a == 'Pies'):
    x = int(input("Ingresa el numero de pies que quieres convertir: "))
    print(str(piesCm(x)) + " cm")
elif(a == 'pulgadas' or a == 'Pulgadas'):
    x = int(input("Ingresa el numero de pulgadas que quieres convertir: "))
    print(str(pulgadasCm(x)) + " cm")
elif(a == 'yardas' or a == 'Yardas'):
    x = int(input("Ingresa el numero de yardas que quieres convertir: "))
    print(str(yardasCm(x)) + " cm")
else:
    print("---- Error -----")
    

