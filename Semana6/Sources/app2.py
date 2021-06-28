from tkinter import messagebox
from tkinter import *

def calcular():
    
    A=float(numeroA.get())
    B=float(numeroB.get())

    resultado=A+B

    E_resultado.delete(0, 'end') #Borrar

    E_resultado.insert(0, str(resultado)) #Muestra en resultado en pantall
    
    

#Ventana principal
ventana=Tk()


#Numero A 
L_numeroA=Label(ventana, text="number A")
numeroA=Entry(ventana)
L_numeroA.grid(row=0, column=0)
numeroA.grid(row=0, column=3, pady=10, padx=5)


#Numero B
L_numeroB=Label(ventana, text="number B")
numeroB=Entry(ventana)
L_numeroB.grid(row=1, column=0)
numeroB.grid(row=1, column=3, pady=10, padx=5)


B_resultado=Button(ventana, text="CALCULAR", bg="blue", command=calcular)
B_resultado.grid(row=2, column=3)


L_resultado=Label(ventana, text="Resultado")
E_resultado=Entry(ventana)

L_resultado.grid(row=3, column=0)
E_resultado.grid(row=3, column=3, pady=10, padx=5)

ventana.mainloop()


