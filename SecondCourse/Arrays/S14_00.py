# Codigo de elaboracion de cualquer matriz en clase

def inicializar(r,c):
    m = []
    for i in range(r):
        a = [0]*c
        m.append(a)
    return m

def solicitarData(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(input("Elemento[{}][{}]: ".format(i,j)))
    print(m)
    return m
    
def imprime(mF):
    print("---- Imprime ----")
    for i in range(len(mF)):
        for j in range(len(mF[i])):
            print(mF[i][j],"\t",end=' ')
        print()

