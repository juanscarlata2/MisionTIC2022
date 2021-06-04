class Aves(object):
    def __init__(self, especie, pais):#Constructor
        self.especie=especie
        self.pais=pais

    def volar(self):
        return True
    
    def poner_huevos(self, cantidad):
        print(f"l@s {self.especie} ponen {cantidad} huevos a la vez")

        

class Peces(object):
    def __init__(self, tipo_agua, especie):
        self.tipo=tipo_agua
        self.especie=especie

    def nadar(self, velocidad):
        print(f"Los {self.especie} nadan a una velocidad de {velocidad} k/h")

    def obtener_habitat(self):
        if self.tipo == 'salada':
            return 'agua salada'
        else:
            return 'agua dulce'


