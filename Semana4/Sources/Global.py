
id=0
datos={}

class persona(object):
    def __init__(self, nombre, edad):
       self.nombre=nombre
       self.edad=edad
       
    
    def guardar_datos(self):
        global id # Declaramos a id como una variable global

        datos[id]={"nombre":self.nombre, "edad":self.edad}
        id+=1 #id=id+1
        
        return datos

    
obj_persona=persona(nombre="Alba", edad=29)
datos=obj_persona.guardar_datos()

obj_persona2=persona(nombre="Milena", edad=45)
datos=obj_persona2.guardar_datos()

print(datos)


