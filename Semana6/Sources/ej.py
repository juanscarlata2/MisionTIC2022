import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box
def getInputBoxValue():
    userInput = texto.get()
    return userInput


# this is the function called when the button is clicked
def btnClickFunction():
    dato=texto.get()
    print(dato)


root = Tk()

# This is the section of code which creates the main window
root.geometry('470x240')
root.configure(background='#F0F8FF')
root.title('Imprimir')


# This is the section of code which creates a text input box
texto=Entry(root)
texto.place(x=118, y=100)


# This is the section of code which creates a button
Button(root, text='Button text!', bg='#6495ED', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=130, y=134)


root.mainloop()
