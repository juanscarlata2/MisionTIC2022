from Matriz import matriz
import random


def rellenar(mat):

    for i in range(1,mat.m+1):
        for j in range(1, mat.n + 1):
            valor=random.randint(0,9)
            mat.mat[i][j]=valor

mat1=matriz(m=4, n=3)

rellenar(mat1)
print(mat1.mat)
mat1.imprimeMatrizPorColumnas("Matriz por Columnas")
mat1.imprimeMatrizPorFilas("Matriz por filas")