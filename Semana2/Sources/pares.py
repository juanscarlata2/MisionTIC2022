"""
Programa para calcular los numeros pares
El usuario ingresa el limete superior para encontrar los pares
"""

numero=int(input("Ingrese un numero entero: "))

#modulo=numero % 2

numero_a_mostrar=1

while numero_a_mostrar <= numero:
    modulo=numero_a_mostrar % 2
    
    if modulo == 0:
        print (numero_a_mostrar)

    numero_a_mostrar+=1






