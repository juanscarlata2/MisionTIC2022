filas_triangulo=input("Ingrese el numero de filas del trinagulo:\t")

for i in range(1,int(filas_triangulo)+1):
    fila=''
    for j in range(i):
        fila+='@'
    print(fila)

print('\n||')