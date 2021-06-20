from ListasLigadas import LSL

class cola(LSL):
    def __init__(self):
        LSL.__init__(self)

    def encolar(self, d):
        self.agregarDato(d)

    def desencolar(self):
        if self.esVacia():
            print("\nCola vacía no hay datos para desencolar")
            return None
        d = self.primero.retornarDato()
        p = self.primerNodo()
        self.borrar(p)
        return d

    def siguiente(self):
        if self.esVacia():
            print("\nCola vacía no hay siguiente")
            return None
        d = self.primero.retornarDato()
        return d
