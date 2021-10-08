# Realizar un programa que multiplique una matriz por un escalar
from S14_00 import inicializar,solicitarData,imprime

# De S14_Ejemplo01 se ingresa esto: 
# def inicializar(r,c):
#     m = []
#     for i in range(r):
#         a = [0]*c
#         m.append(a)
#     return m
# 
# def solicitarData(m):
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             m[i][j] = int(input(("Elemento[{}][{}]: ".format(i,j))))
#     print(m)
#     return m
#     
# def imprime(mF):
#     print("---- Imprime ----")
#     for i in range(len(mF)):
#         for j in range(len(mF[i])):
#             print(mF[i][j],"\t",end=' ')
#         print()



r = int(input("Ingresa los valores para inicializar tu matriz\nLineas: "))
c = int(input("Columnas: "))

m1 = inicializar(r,c); mR = inicializar(r,c)
print("Ingresa los valores para la matriz")
m1 = solicitarData(m1)
n = int(input("Ahora ingresa un escalar para multiplicar a la matriz: "))

for i in range(r):
    for j in range(c):
        mR[i][j] = m1[i][j] * n

imprime(mR) 
