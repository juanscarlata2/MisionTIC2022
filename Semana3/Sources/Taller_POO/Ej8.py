"""
Clase para gestionar una maquina
"""
import random

class Maquina(object):

    def __init__(self, saldo):
        self.saldo=saldo
    
    def jugar(self):
        simbolos=['$','7','#','1','3']
        simbolos_juego=list() #Creamos una lista

        for i in range(3): #Generar los 3 simbolos del juego
            aleatorio=random.randint(0,len(simbolos)-1)
            simbolos_juego.append(simbolos[aleatorio])

        print(f"| {simbolos_juego[0]} | {simbolos_juego[1]} | {simbolos_juego[2]} |")#Muestra la jugada en la pantalla

        self.validar(jugada=simbolos_juego) #Valida si el usuario gano o perdio 

        print(f"\n Su saldo es {self.saldo}") # Muestra el saldo despues del juego

    

    def validar(self, jugada): #jugada trae los 3 simbolos generados en el juego 
        if jugada[0]==jugada[1] and jugada[0]==jugada[2]:
            print("Gano")
            self.saldo+=10
        else:
            print("Has Perdido :(")
            self.saldo-=2


