class Circulo(object):
    def __init__(self, radio):
        self.r=radio
        self.pi=3.141516

    def obtener_area(self):
        area=self.pi*self.r**2 #Calcula el area del circulo
        return area
        print("Hola sigo aqui")


    def obtener_perimetro(self):
        perimetro=2*self.pi*self.r
        return perimetro

    def obtener_ecuacion(self):
        ecuacion=f'x²+y²={self.r}²'
        return ecuacion
