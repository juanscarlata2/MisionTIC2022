from tkinter import messagebox
from tkinter import *
#variables globales


class app:
    def __init__(self, root):
        L_nombre=Label(root, text="Name")
        L_nombre.grid(row=0, column=0, padx=5)
        self.E_nombre=Entry(root)
        self.E_nombre.grid( row=0, column=1, pady=15, padx=10)

        L_space=Label(root)
        L_space.grid(row=0, column=2, padx=20)

        L_age=Label(root, text="Age")
        L_age.grid(row=0, column=3, padx=5)
        self.E_age=Entry(root)
        self.E_age.grid( row=0, column=4, pady=15, padx=10)

        B_guardar=Button(root, text="Guardar", command=self.guardar)
        B_guardar.grid(row=1, column=2, pady=20)

        

    def guardar(self):
        global id

        nombre=self.E_nombre.get()
        age=self.E_age.get()
        datos[id]={"nombre":nombre, "edad":age}
        id+=1 #id=id+1
        print(datos)




#Metodo  main
if __name__=="__main__":
    datos={}
    id=0

    ventana=Tk()
    app(ventana)

    ventana.mainloop()





