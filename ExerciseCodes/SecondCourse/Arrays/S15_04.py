# Escribe un programa que permita multiplicar dos matrices de 3x3

from S14_00 import inicializar, solicitarData, imprime

# De S14_00 se ingresa lo siguiente : 
# 
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

def multo3x3(m1,m2,mR):
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                mR[i][j] += m1[i][k] * m2[k][j]
    for r in mR:
       print(r)

    print(mR)
    return mR
            


m1 = inicializar(3,3); m2 = m1; mR = m2

print("Ingresa la informacion para la primer matriz")
m1 = solicitarData(m1) 
print("Ingresa la informacion para la segunda matriz")
m2 = solicitarData(m2)
imprime(multo3x3(m1,m2,mR))

