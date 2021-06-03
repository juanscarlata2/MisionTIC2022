"""
Fuencion para obtener el promedio de una lista numerica
Mision TIC
"""
#[3,4,5]

def promedio (datos):
    contador=0 #Contar el numero de elementos en la lista
    suma=0 #Acomula los valores de la lista

    for valor in datos:
        suma+=valor
        contador+=1
    
    calc_promedio=suma/contador
    
    return calc_promedio


resultado=promedio(datos=[3,5,1,2,3,2])