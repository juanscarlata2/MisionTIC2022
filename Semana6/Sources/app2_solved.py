from tkinter import Tk, Button, Entry

operacion=[]

def click_boton(valor):
    if valor:
        operacion.append(str(valor))
        print(operacion)
        texto=crear_string(operacion)
        mostrar_pantalla(texto)
    else:
        resultado=calcular(operacion)
        mostrar_pantalla(valor=resultado)

def calcular(operacion):
    if operacion[-1] in ['+','-']:
        operacion.pop()

    operacion=crear_string(operacion)
    resultado=str(eval(operacion))
    return resultado

def mostrar_pantalla(valor):
    pantalla.delete(0, 'end')
    pantalla.insert(index=0, string=valor)

def crear_string(operacion):
    return ''.join(operacion)



root=Tk()
#Pantalla
pantalla=Entry(bg="white")
pantalla.grid(row=0, column=0, pady=10, padx=3, columnspan=3)

#Botones
b_1=Button(root, bg='grey', text="1", width=3, command=lambda:click_boton(1))
b_2=Button(root, bg='grey', text="2", width=3, command=lambda:click_boton(2))
b_3=Button(root, bg='grey', text="3", width=3, command=lambda:click_boton(3))
b_4=Button(root, bg='grey', text="4", width=3, command=lambda:click_boton(4))
b_5=Button(root, bg='grey', text="5", width=3, command=lambda:click_boton(5))
b_6=Button(root, bg='grey', text="6", width=3, command=lambda:click_boton(6))
b_7=Button(root, bg='grey', text="7", width=3, command=lambda:click_boton(7))
b_8=Button(root, bg='grey', text="8", width=3, command=lambda:click_boton(8))
b_9=Button(root, bg='grey', text="9", width=3, command=lambda:click_boton(9))
b_0=Button(root, bg='grey', text="0", width=3, command=lambda:click_boton(0))

b_suma=Button(root, bg='grey', text="+", width=3, command=lambda:click_boton('+'))
b_resta=Button(root, bg='grey', text="-", width=3, command=lambda:click_boton('-'))
b_igual=Button(root, bg='grey', text="=", command=lambda:click_boton(False), width=5)


numeros=[b_0, b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9]


conta_botones=1
for x in range(1,4):
    for y in range(0,3):
        numeros[conta_botones].grid(row=x,column=y, pady=5, padx=5)
        conta_botones+=1

b_0.grid(row=4,column=1, pady=5, padx=5)
b_suma.grid(row=4,column=0, pady=5, padx=5)
b_resta.grid(row=4,column=2, pady=5, padx=5)
b_igual.grid(row=5, column=1, pady=5)
root.mainloop()



