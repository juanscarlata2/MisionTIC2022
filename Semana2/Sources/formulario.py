
datos_usuarios={}
id=0
opcion=1


while opcion != '5':
    opcion=input("1. Inresar Usuario\n2. Ver Usuario por id\n3. Ver todos los usuarios\n5. Salir\n\n")
   
    if opcion=='1':
        nombre=input("\n\nIngresar Nombre: ")
        edad=input("\nIngresar edad: ")

        datos_usuarios[id]={"nombre":nombre, "edad":edad}
        id+=1
        print (datos_usuarios)

    elif opcion =="2":
        id_a_buscar=int(input("\nIngrese el id que desea buscar: "))

        if id_a_buscar in datos_usuarios: #alida si el id a a buscar esta en el diccionario
            usuario_buscado=datos_usuarios[id_a_buscar]
            input("Nombre: "+usuario_buscado['nombre']+" y su edad es "+usuario_buscado['edad']+"\n\nPresione ENTER para continuar")
        else:
            input("id no encontrado por favor precione ENTER para volver al menu inicial")
            

    elif opcion =='3':
        if datos_usuarios:
            for usuario in datos_usuarios:
                datos_de_usuario=datos_usuarios[usuario]
                nombre=datos_de_usuario["nombre"]
                edad=datos_de_usuario["edad"]
                print(f"\nid:{usuario} Nombre: {nombre} con edad {edad} \n")
        else:
            input("No hay usuarios registrados. Presione ENTER para ir al menu principal")
        
    
    elif opcion=='5':
        pass
    else:
        input("Opcion no valida presione ENTER para continuar")


print("Hasta Pronto")

    

    