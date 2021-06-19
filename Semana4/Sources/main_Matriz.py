from Matriz import matriz
import random


def rellenar(mat): #La entrada es un objeto de la clase matriz

    for i in range(1,mat.m+1):
        for j in range(1, mat.n + 1):
            valor=random.randint(0,9)
            mat.mat[i][j]=valor




mat1=matriz(m=3, n=2) #Creamos una matriz (Un objeto de la clase matriz)
mat2=matriz(m=2, n=2)

rellenar(mat1) #llamo la fucion rellanar para agregar valores
rellenar(mat2)

multi=mat1 * mat2
multi.imprimeMatrizPorColumnas() 





