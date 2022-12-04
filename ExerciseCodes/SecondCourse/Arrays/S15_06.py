# Resuelve un sistema de ecuaciones lineales con tres incógnitas mediante el método de Cramer.
from S14_00 import inicializar

# Ingresamos una matriz y nos devuelve la determinante 
def determinante3x3(m):
    d1 = m[0][0]*((m[1][1]*m[2][2]) - (m[2][1]*m[1][2])) 
    d2 = m[1][0]*((m[0][1]*m[2][2]) - (m[2][1]*m[0][2]))
    d3 = m[2][0]*((m[0][1]*m[1][2]) - (m[1][1]*m[0][2]))
    dt = d1 - d2 + d3
    return dt

# Solicita la informacion en forma de ecuación, ademas del resultado
def solicitarData(m):
    e = ['x','y','z']; r = [0,0,0]
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(input("Valor {} de la ecuacion {}: ".format(e[j],i+1)))
    print("\nAhora ingresa los resultados\n")
    for i in range(len(r)):
        r[i] = int(input("Resultado de la ecuacion {}: ".format(e[i])))
    return m, r
    
# Sustituye los valores de las columnas x con el resultado para llegar a las soluciones de las determinantes
def reemplazaR(m,r,c):
    for i in range(len(m)):
        m[i][c] = r[i]
    det = determinante3x3(m)
    return det

# ----------------------- Inicializamos ----------------------------
# m = inicializar(3,3)
m = [[1,1,-1],[3,1,-1],[4,-2,1]]
r = [0,2,3]
# m,r = solicitarData(m)

# ---------------------- Proceso -----------------------------
# Calculo determinante A
detA = determinante3x3(m)
print("detA: ",detA)

# Calculo determinante A1 (x)
detA1 = reemplazaR(m, r , 0)/detA
print("detA1: ", detA1)

# Calculo determinante A2 (y)
detA2 = reemplazaR(m, r , 1)/detA
print(detA2)

# Calculo determinante A3 (z)
detA3 = reemplazaR(m, r , 2)/detA
print(detA3)

print("La solucion del problema es:\nx = {}\ny = {}\nz = {}".format(detA1,detA2,detA3))











# De S14_00 se ingresa esto:

# def inicializar(r,c):
#     m = []
#     for i in range(r):
#         a = [0]*c
#         m.append(a)
#     return m
