lista=[-3,0,-100,50,89,9,1,4,45]

mayor=lista[0]

for numero in lista:

    if numero > mayor:
        mayor=numero

print(f"El mayor es {mayor}")
