class matriz:

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.mat = [] * (m + 1)

        for i in range(m + 1):
            a = [0]*(n + 1)
            self.mat.append(a)

    
    def numeroFilas(self):
        return self.m


    def numeroColumnas(self):
        return self.n


    def imprimeMatrizPorFilas(self, mensaje="Matriz sin nombre: "):
        print("\n", mensaje)
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                print(self.mat[i][j], "\t", end="")
            print()


    def imprimeMatrizPorColumnas(self, mensaje="Matriz sin nombre: "):
        print("\n", mensaje)
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                print(self.mat[j][i], "\t", end="")
            print()


    def intercambiarFilas(self, i, j):
        for k in range(1, self.n):
            aux = self.mat[i][k]
            self.mat[i][k] = self.mat[j][k]
            self.mat[j][k] = aux


    def intercambiarColumnas(self, i, j):
        for k in range(1, self.m):
            aux = self.mat[k][i]
            self.mat[k][j] = self.mat[k][i]
            self.mat[k][i] = aux

        

    def sumarFilas(self):
        v = vector(self.m)
        for i in range(1, self.m + 1):
            s = 0
            for j in range(1, self.n + 1):
                s = s + self.mat[i][j]
            v.agregarDato(s)
        return v


    def sumarColumnas(self):
        v = vector(self.n)
        for i in range(1, self.n + 1):
            s = 0
            for j in range(1, self.m + 1):
                s = s + self.mat[j][i]
            v.agregarDato(s)
        return v

    def traspuesta(self):
        c = matriz(self.n, self.m)
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                c.mat[j][i] = self.mat[i][j]
        return c
