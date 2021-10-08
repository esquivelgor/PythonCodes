
# Realiza un programa que sume y reste dos matrices del mismo tamaño. Tú decides el tamaño

from S14_00 import inicializar,solicitarData,imprime

# De S14_00 se ingresa esto: 
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

r = int(input("Ingresa los valores para inicializar tus arrays\nLineas: "))
c = int(input("Columnas: "))

m1 = inicializar(r,c)
print("Ingresa los valores para la primer matriz")
m1 = solicitarData(m1)

m2 = inicializar(r,c)
print("Ingresa los valores para la segunda matriz")
m2 = solicitarData(m2)

# Suma
m3 = inicializar(r,c)
for i in range(r):
    for j in range(c):
        m3[i][j] = m1[i][j] + m2[i][j]
# Resta
m4 = inicializar(r,c)
for i in range(r):
    for j in range(c):
        m4[i][j] = m1[i][j] - m2[i][j]

print("\nSuma")
imprime(m3) 
print("\n Resta")
imprime(m4)
