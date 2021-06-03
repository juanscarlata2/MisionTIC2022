def ordenar(lista):
    elementos_ordenados=[]
   
    while True:
        if len(lista)==0:
            break
        menor, posicion =buscar_menor(lista)
        elementos_ordenados.append(menor)
        lista.pop(posicion)
    return elementos_ordenados


def buscar_menor(lista):
    menor=lista[0] # va guardar el nnumero mayor
    posicion=0
    contador=0
    for i in lista:
        if i < menor:
            menor=i
            posicion=contador

        contador+=1

    return menor,posicion



print(ordenar(lista=[5,2,0,-1,-10,2]))

