from tkinter import Tk, Label, Button, Entry, messagebox

from random import randint

class gui:
    def __init__(self, root):
        self.texto=Entry(root, bg="white")

        self.texto.place(x=50, y=50)
        self.boton_imprimir=Button(root, width= 8, height=3, text="OK", bg="blue", command=self.click)
        self.boton_imprimir.place(x=50, y=150)
        
    def click(self):
        self.texto
        self.texto.insert(index=0, string="Hola mundo")

    def cambio(self):
        messagebox.showinfo("Se ha cambiado algo")

        



if __name__=="__main__":
    ventana_ppal=Tk()
    ventana_ppal.title("Mi primer GUI")
    calc= lambda x,y:x+y 
    print(calc(5,8))
    gui(ventana_ppal)
    ventana_ppal.mainloop()

