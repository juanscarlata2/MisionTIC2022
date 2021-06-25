from tkinter import Tk, Button, Entry

def imprimir(mensaje):

    mensaje=tomar_info()
    dato=texto2.insert(0,string=mensaje)
    texto1.delete(0, 'end')

def tomar_info():
    dato=texto1.get()
    return dato


root=Tk()
root.title("Boton")

texto1=Entry(root)
texto1.pack()



boton=Button(root, text="Hola",bg="blue violet", command= lambda : imprimir("Hola"))
boton.pack()

texto2=Entry(root)
texto2.pack()



root.mainloop()



