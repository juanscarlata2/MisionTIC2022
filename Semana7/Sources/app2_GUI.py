from tkinter import ttk
from tkinter import *
from random import randint

def mostrar():
    filas=randint(0,10)
    registros=tabla.winfo_children()

    for widget in registros:
            widget.destroy()

    for f in range(2,filas):
        for c in range(3):
            L=Entry(tabla)
            L.grid(row=f, column=c)
            L.insert(0, str(f))
            
def filtrar():
    Seleccion=filtros.selection_get()
    print(Seleccion)

root=Tk()
root.title("InventApp")
root.geometry("500x300")

pestagnas=ttk.Notebook(root) # Se crea un objeto para manejar las pestañas


F_buscar=Frame(pestagnas)
F_buscar.pack()

L_id=Label(F_buscar, text="id a bucar")
L_id.grid(row=0, column=1)

E_id=Entry(F_buscar)
E_id.grid(row=0, column=2)

B_buscar=Button(F_buscar, text="Buscar", command=mostrar)
B_buscar.grid(row=1, column=2)

tabla=Frame(F_buscar) #Frame para manejar la tabla
tabla.grid(row=2, column=2)


F_ingresar=Frame(pestagnas)
F_ingresar.pack()
filtros=ttk.Combobox(F_ingresar, state="readonly")
filtros.grid(row=0, column=1)
items = ["1","2","3"]
filtros['values']=items        


B_filtrar=Button(F_ingresar, text="Filtrar", command=filtrar)
B_filtrar.grid(row=0, column=2)




pestagnas.add(F_buscar, text="Buscar")
pestagnas.add(F_ingresar, text="Ingresar")

pestagnas.pack()

root.mainloop()