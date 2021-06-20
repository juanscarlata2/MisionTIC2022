import random

class palabras(object):
    def __init__(self):
        fichero = open('data', 'r')
        self.cantidad_palabras=len(fichero.readlines())
        fichero.close()

    def get_palabra(self):
        n_palabra=random.randint(0, self.cantidad_palabras - 1)
        fichero = open('data', 'r')
        i=0
        while (True):
            palabra=fichero.readline()
            if i==n_palabra:
                return palabra

            i+=1

            if not palabra: #Rompe el while
                break

        fichero.close()



class grafico(object):
    def __init__(self):
        self.dibujo = ['''
                        +---+
                        |   |
                            |
                            |
                            |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                            |
                            |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                        |   |
                            |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                        /|  |
                            |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                        /|\ |
                            |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                        /|\ |
                        /   |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                        /|\ |
                        / \ |
                            |
                        =========''']

        self.oportunidades=len(self.dibujo)

    def get_grafico(self, N):
        if N < self.oportunidades:
            return self.dibujo[N]
        else:
            return False

