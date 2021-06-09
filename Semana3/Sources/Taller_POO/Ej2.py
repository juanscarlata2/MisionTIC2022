from vector import vector
import random


N=int(input('Ingrese el tamagno del vector: \t'))
objeto_vector=vector(n=N) #Creamos el objeto de la clase vector

for i in range(N):
    numero_aleatorio=random.randint(a=1, b=99)
    objeto_vector.insertar(d=numero_aleatorio)

objeto_vector.imprimeVector(mensaje="mi Vector ")


