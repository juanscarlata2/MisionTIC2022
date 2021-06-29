from tkinter import messagebox
from tkinter import *
#variables globales


class app:
    def __init__(self, root):

        L_nombre=Label(root, text="Name")
        L_nombre.grid(row=0, column=0, padx=5)

        #Campos para el nombre 
        self.E_nombre=Entry(root)
        self.E_nombre.grid( row=0, column=1, pady=15, padx=10)

        L_space=Label(root)
        L_space.grid(row=0, column=2, padx=20)

        #Cmpos para la edad
        L_age=Label(root, text="Age")
        L_age.grid(row=0, column=3, padx=5)
        self.E_age=Entry(root)
        self.E_age.grid( row=0, column=4, pady=15, padx=10)

        #Boton guardar
        B_guardar=Button(root, text="Guardar", command=self.guardar)
        B_guardar.grid(row=1, column=2, pady=20)

        #Para buscar 
        L_buscar=Label(text="ID")
        L_buscar.grid(row=2, column=0)
        self.E_buscar=Entry(root)
        self.E_buscar.grid(row=2, column=1, padx=5, pady=20)

        B_buscar=Button(text="Buscar", command=self.buscar)
        B_buscar.grid(row=2, column=2)

        self.tabla=Frame(root)
        self.tabla.grid(row=3, column=2, pady=10)

    def guardar(self):
        global id

        nombre=self.E_nombre.get()
        age=self.E_age.get()
        datos[id]={"nombre":nombre, "edad":age}
        id+=1 #id=id+1
       
    def buscar(self):
        id=self.E_buscar.get()
        if id=='*':
            self.crear_tabla(fila=len(datos))
        else:
            try:
                id=int(id)
            except:
                messagebox.showerror("Not int", "Debe ingresar un id en entero")
            else:    
                if id in datos:
                    self.crear_tabla(fila=1, unico=datos[id])
                else:
                    messagebox.showinfo("Not Found", "Ese ID no esta en los datos")
            

    def crear_tabla(self, fila, unico=False):

        registros=self.tabla.winfo_children() #Obtenemos los elementos de la tabla
        for widget in registros:
            widget.destroy()

        if unico:
            for c in range(0,2):
                fila=Entry(self.tabla)
                fila.grid(row=0, column=c)
                key=self.detectar_registro(columna=c)
                fila.insert(index=0, string=unico[key])

        else:
            for f in range(0, fila):
                for c in range(0,2):
                    fila=Entry(self.tabla)
                    fila.grid(row=f, column=c)
                    key=self.detectar_registro(columna=c)
                    fila.insert(index=0, string=datos[f][key])



    def detectar_registro(self, columna):
        if columna==0:
            key='nombre'
        elif columna==1:
            key='edad'
        
        return key





#Metodo  main
if __name__=="__main__":
    datos={}
    id=0

    ventana=Tk()
    #Crear un instancia de la clase app
    app(ventana)

    ventana.mainloop()





