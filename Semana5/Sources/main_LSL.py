from ListasLigadas import LSL

lista1=LSL() #Creamos una lista ligada

for i in range(1,2):
     d = int(input("Entre dato: "))
     y = lista1.buscarDondeInsertar(d=d)
     lista1.insertar(d=d, y=y)

for i in range(2):
    d = int(input("Entre dato: "))
    lista1.agregarDato(d=d)
    
lista1.recorrerLista()




