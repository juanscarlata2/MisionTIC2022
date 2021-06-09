from vector import vector


N=int(input('Ingrese el tamagno del vector: \t'))

if N > 0 and N <= 5:
    objeto_vector=vector(n=N) #Creamos el objeto de la clase vector

    for i in range(N): 
       elemento=int(input(f'Ingrese el valor {i}: '))
       objeto_vector.insertar(d=elemento)
    
    mayor=objeto_vector.mayor()

    print(f"El mayor es {objeto_vector.V[mayor]}")


else:
    print("El valor debe estar entre 1 y 5")
