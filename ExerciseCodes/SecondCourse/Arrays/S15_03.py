# Determinante 3x3

from S14_00 import inicializar,solicitarData

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

m1 = inicializar(3,3)
print("Ingresa los valores para la matriz")
m1 = solicitarData(m1)

# a(ei - hf) - d(bi - hc) + g(bf - ec)
# a b c  00 01 02
# d e f  10 11 12
# g h i  20 21 22 
d1 = m1[0][0]*((m1[1][1]*m1[2][2]) - (m1[2][1]*m1[1][2])) 
d2 = m1[1][0]*((m1[0][1]*m1[2][2]) - (m1[2][1]*m1[0][2]))
d3 = m1[2][0]*((m1[0][1]*m1[1][2]) - (m1[1][1]*m1[0][2]))
dt = d1 - d2 + d3

print("La determinante de la matriz 3x3 es: {}".format(dt)) 