# Diseña un programa que indique si una cadena leída de teclado está bien formada como número entero.
#  El programa escribirá "Es entero" en caso afirmativo y "No es entero" en caso contrario.
# 
# Por ejemplo, para ’12’ mostrará "Es entero", pero para ’1   2’ o ’a12' mostrará  "No es entero". 


s = input("Ingresa una cadena de texto: ")
if s.isdigit():
    print("Es entero")
else: print("No es entero")
