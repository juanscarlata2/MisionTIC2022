from ListasLigadas import LSL


class pila(LSL):
    def __init__(self):
        LSL.__init__(self)

    def apilar(self, d):
        if self.esVacia():
            self.agregarDato(d)
        else:  
            self.insertar(d,None) #Se le agrega el parametro None para que funcione insertar

    def muestraPila(self):
        self.recorrerLista()

    def desapilar(self):
        p = self.primerNodo()
        d = p.retornarDato()
        

        self.borrar(p)
        return d
