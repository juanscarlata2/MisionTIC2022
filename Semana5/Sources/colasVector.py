from Vector.vector import vector


class cola(vector):
    def __init__(self, n):
        vector.__init__(self, n)
        self.primero = 0
        self.ultimo = 0

    def esLlena(self):
        return self.primero == self.ultimo

    def esVacia(self):
        return self.primero == self.ultimo

    def encolar(self, d):
        self.ultimo = (self.ultimo + 1) % self.n
        if self.esLlena():
            print("cola llena, no se puede encolar\n")
            self.ultimo = (self.ultimo - 1 + self.n) % self.n
            return
        self.V[self.ultimo] = d

    def desencolar(self):
        if self.esVacia():
            print("cola vacía, no se puede desencolar\n")
            return None
        self.primero = (self.primero + 1) % self.n
        return self.V[self.primero]

    def siguiente(self):
        if self.esVacia():
            print("cola vacía, no hay siguiente\n")
            return None
        aux = (self.primero + 1) % self.n
        return self.V[aux]

    def muestraCola(self):
        print("La cola es:",end=' ')
        for i in range(self.primero+1,self.ultimo+1):
            print(self.V[i],end=', ')



qu = cola(10)

qu.encolar("a")
qu.encolar("b")
qu.encolar(316)

qu.muestraCola()

d = qu.desencolar()
print("\nDato desencolado:", d)
print(f"El siguiente es: {qu.siguiente()}")
qu.encolar("Juan")
qu.muestraCola()

