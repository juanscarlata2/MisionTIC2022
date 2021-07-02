import json

datos={1:"Hola JSON"}

with open('datos.json', 'w') as fp:
    json.dump(datos, fp)


with open('datos.json', 'r') as fp:
    datos2=json.load(fp)

print(type(datos2), datos2)
