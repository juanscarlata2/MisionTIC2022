from tkinter import Tk, Label, Button
from random import randint


def click():
    etiqueta.configure(text=str(randint(a=0, b=1000)), bg="blue")



ventana=Tk()
ventana.title("Ejemplo")
ventana.iconbitmap("images/planet.ico")



etiqueta=Label(ventana, bg="white")
etiqueta.pack()


boton=Button(ventana, text="Imprimir", bg="coral3", height=5, width=15, command=click)
boton.pack(pady=20)

ventana.mainloop()






