import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Hola mundo')

ventana.iconbitmap('icono.ico')
ventana.config(background='#CA57C8')
boton1 = ttk.Button(ventana, text='Puto el que lee')
boton1.pack()
#ultimo metodo
ventana.mainloop()