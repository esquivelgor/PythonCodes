# Un texto está bien parentizado si por cada paréntesis abierto hay otro más adelante que lo cierra.
# 
# Por ejemplo, la cadena ’Esto (es (un) (ejemplo (de) ((cadena) bien)) parentizada
# )' está bien parentizada, pero no lo están estas otras:
# 
# ’una cadena)’
# ’(una cadena’
# ’(una (cadena)’
# ’)una( cadena’
# Realiza un programa que detecte si una cadena está bien parentizada

s = input("Ingresa un texto parantizado: ")
oL = ["("]; cL = [")"]; l = []

for i in s:
    if i in oL:
        l.append(i)
    elif i in cL:
        pos = cL.index(i)
        if (len(l) > 0) and (oL[pos] == l[len(l)-1]):
            l.pop()
        else:
            print("Esta mal parantizado")
if len(l) == 0:
    print("Esta bien parantizado")
else:
    print("Esta mal parantizado")


# Otro algoritmo que no me funciono del todo bien    
# ls = list(s)
# for i in range(len(s)):
#     for j in ls:
#         if j == "(":
#             for k in ls:
#                 if k == ")":
#                     ls.remove(k)
#                     ls.remove(j)
#             
# if "(" in ls or ")" in ls:
#     print("Esta mal parantizada")
# else:
#     print("Esta bien parantizado")


    
