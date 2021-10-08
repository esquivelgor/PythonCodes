from S14_00 import inicializar, solicitarData

# Escribe un programa despliegue una matriz de 3x3, así como sus correspondientes sumas por renglón y por columna:

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
def imprime(mF):
    # Suma de numeros
    r = [0,0,0]; c = [0,0,0]
    for i in range(len(mF)):
        for j in range(len(mF[i])):
            r[i] += mF[i][j]
            c[i] += mF[j][i]    
    print("-------- Imprime --------")
    for i in range(len(mF)):
        for j in range(len(mF[i])):
            print(mF[i][j],"\t",end=' ')
        print("|", r[i])
    print("-------------------------")
    for i in range(len(c)):
        print(c[i],"\t",end=' ')



# Matriz de prueba
#m = [[1,2,3],[4,5,6],[7,8,9]]

m = inicializar(3,3)
print("Ingresa los valores para la matriz")
m = solicitarData(m)
imprime(m)