from tkinter import ttk
from tkinter import *
from app_filtros import filtro


def filtrar():
    opcion=opciones_filtro.selection_get()
    valor=E_valor.get()
    print(opcion)
    try:
        opcion=opciones_filtro.selection_get()
        valor=E_valor.get()
    except:
        print("Error")
        return False
    else:
        mi_filtro=filtro(file_name='Productos.csv')
        tabla_filtrada=mi_filtro.filtrar_por(registro=opcion, valor=valor)
        print(tabla_filtrada)

        mostrar_tabla(filas=len(tabla_filtrada), tabla_datos=tabla_filtrada)


def mostrar_tabla(filas, tabla_datos):
    eliminar_tabla() #Elimina la tabla anterior

    for f in range(filas):
        for c in range(4):
            registro=Entry(tabla)
            registro.grid(row=f, column=c)
            registro.insert(0, tabla_datos[f][keys[c]])

def eliminar_tabla():
    hijos=tabla.winfo_children()
    for w in hijos:
        w.destroy()
    tabla.pack_forget()

root=Tk()
root.title("FilterAPP")
root.geometry('550x300')


keys=['id', 'nombre', 'cantidad', 'precio']

opciones_filtro=ttk.Combobox(root, state='readonly')
opciones_filtro.grid(row=0, column=0,padx=5)
opciones_filtro['values']=keys

B_filtar=Button(root, text="Filtrar", command=filtrar)
B_filtar.grid(row=0, column=1, padx=5)

L_valor=Label(root, text="Valor a filtrar")
L_valor.grid(row=0, column=2)

E_valor=Entry(root)
E_valor.grid(row=0, column=3)

tabla=Frame(root)
tabla.grid(row=1, column=0, columnspan=4, pady=10, padx=5)




root.mainloop()
