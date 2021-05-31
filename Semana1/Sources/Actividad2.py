import random

numero_X=random.randint(1,20) #Se genera el numero aleatorio


#Intento 1
perdiste=True

for intento in range(1,4):
    numero_usuario=int(input("Intento %s\nIngrese un numero del 1 a 20: "%(intento)))

    if (numero_usuario == numero_X): # Si son iguales
        print("Felicitaciones, ha ganado !!!")
        perdiste=False
        break

    elif (numero_usuario > numero_X): # Si el numero es mayor 
        print("El %s es mayor que el numero a adivinar"%(numero_usuario))

    else: # si no se cumple ninguna de las anteriores
        print("El %s es menor que el numero a adivinar"%(numero_usuario))

if perdiste:
    print("No eres bueno en esto")






