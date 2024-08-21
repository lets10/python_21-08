import tkinter
from tkinter import *

class Janela1:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.msg = Label(self.widget1, text="Pagina de Botões")
        self.msg["font"] = ("Verdana", "15", "italic", "bold")
        self.msg.pack()

        self.fechar= Button(self.widget1)
        self.fechar["text"] = "Fechar"
        self.fechar["font"] = ("Arial", "15")
        self.fechar["width"] = 20
        self.fechar["command"] = self.widget1.quit
        self.fechar.pack(side=RIGHT)

        self.usuarios = Button(self.widget1)
        self.usuarios["text"] = "Usuarios"
        self.usuarios["font"] = ("Arial", "15")
        self.usuarios["width"] = 20
        self.usuarios.pack(side=RIGHT)

        self.cidades = Button(self.widget1)
        self.cidades["text"] = "Cidades"
        self.cidades["font"] = ("Arial", "15")
        self.cidades["width"] = 20
        self.cidades.pack(side=RIGHT)

        self.clientes = Button(self.widget1)
        self.clientes["text"] = "Clientes"
        self.clientes["font"] = ("Arial", "15")
        self.clientes["width"] = 20
        self.clientes.pack(side=RIGHT)

root = Tk()
Janela1(root)
root.mainloop()