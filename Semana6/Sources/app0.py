from tkinter import Tk,Label

#la ventana root
ventana=Tk()
ventana.title("Hola")

#Crear etiqueta
etiqueta=Label(ventana,text="Hola mundo")
etiqueta.pack()
print(etiqueta)

ventana.mainloop()