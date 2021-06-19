import numpy as np

def ver_valores(matriz):
    m,n=matriz.shape
    for fila in range(m):
        for columna in range(n):
            print(matriz[fila, columna])


C=np.array([[1,-3,6],[5,0,-2]])
print(C)
n=2
print(C[0:,-1])



