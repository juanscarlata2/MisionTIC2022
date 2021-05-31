limite=int(input("Ingrese la cantidad de numeros que desa ingresar: "))

todos_los_numeros=list()

for i in range(limite):

    numero_ingresado=int(input("Ingrese el numero %s:\t"%(i+1))) #Lee el numero i del usario

    if i==0: #Solo para la primera iteracion haga esto
        todos_los_numeros.append(numero_ingresado)
        numero_anterior=numero_ingresado

    elif numero_ingresado > numero_anterior: #Validacion si el numero ingresado es mayor al anterior
        todos_los_numeros.append(numero_ingresado) # agregamos  el nuemro valido a la lista
    
    numero_anterior=numero_ingresado #Actualiza el numero acterior para comparar en el siguiente ciclo 

print (todos_los_numeros)


