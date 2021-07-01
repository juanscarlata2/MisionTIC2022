from tkinter import filedialog as fd
from tkinter import scrolledtext as sctx
from tkinter import INSERT
from tkinter import *

def buscar():
    file_name=fd.askopenfilename()
    with open(file_name) as f:
        datos=f.read()
    mostrar_hoja(datos)

def mostrar_hoja(datos):
    hoja.delete('0.0', END)
    hoja.insert(INSERT, datos)
    
def guardar():
    pass

#Se utiliza el metodo askopenfilename() de filedialog
root=Tk()
root.geometry('700x520')


B_load=Button(root, text="load file", command=buscar)
B_load.pack(expand=True, pady=20)

hoja=sctx.ScrolledText()
hoja.pack(expand=True)

B_guardar=Button(root, text="Save", command=guardar)
B_guardar.pack(pady=20)

root.mainloop()