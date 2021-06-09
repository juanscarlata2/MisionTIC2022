from Empleado import Empleado

class Empleado_hijo(Empleado):
    def __init__(self, area, horas, valor_hora, nombre):
        super().__init__(area=area, horas=horas, valor_hora=valor_hora)
        self.area=area
        self.nombre=nombre

    def pagar(self):
        pago=super().pagar()
        print(pago)
        if self.area=='ventas':
            pago+=1000000

        print(pago)



felipe=Empleado_hijo(area='ti', horas=160, valor_hora=30000, nombre='Felipe')
felipe.pagar()
