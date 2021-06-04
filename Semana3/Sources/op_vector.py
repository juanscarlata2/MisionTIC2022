from vector import vector #Importamos nuestra clase vector, debe estar en la misma carpeta que este archivo
import random #importa random para generar numeros aleatorios 
N=5 #Deifine la longitud que va a tener nuestro vector
mi_vector=vector(n=N) #Crea un objeto de la clase vector

for i in range(N): #Ciclo para rellenar el vector con numeros aletorios del 1 al 20
    mi_vector.agregarDato(random.randint(1, 20)) #Usa el metodo agregarDatos para rellenar el vector

mi_vector.imprimeVector(mensaje='mi_vector') #imprime el contenido del vector creado


