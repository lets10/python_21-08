import tkinter
from tkinter import *

class janela2:
    def __init__(self, master=None):
        self.widget2 = Frame(master)
        self.fontePadrao = ("Arial" , "12")
        self.widget2.pack()

        self.titulo= Label(self.widget2, text="Informe os dados")
        self.titulo["font"] = ("Verdana", "15", "italic", "bold")
        self.titulo.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idLabel = Label(self.janela2, text="IDusuario", font=self.fontePadrao)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela2)
        self.id["width"] = 30
        self.id["font"] = self.fontePadrao
        self.id.pack(side=LEFT)

        self.busca = Button(self.janela2)
        self.busca["text"] = "Buscar"
        self.busca["font"] = ("Arial", "10")
        self.busca["width"] = 10
        self.busca.pack(side=RIGHT)

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nomeLabel = Label(self.janela3, text="Nome:", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela3)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack()

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.telefoneLabel = Label(self.janela4, text="Telefone:", font=self.fontePadrao)
        self.telefoneLabel.pack(side=LEFT)
        self.telefone = Entry(self.janela4)
        self.telefone["width"] = 30
        self.telefone["font"] = self.fontePadrao
        self.telefone.pack()

        self.janela5= Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.emailLabel = Label(self.janela5, text="E-mail:", font=self.fontePadrao)
        self.emailLabel.pack(side=LEFT)
        self.email = Entry(self.janela5)
        self.email["width"] = 30
        self.email["font"] = self.fontePadrao
        self.email.pack()

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.usuarioLabel = Label(self.janela6, text="Usuario:", font=self.fontePadrao)
        self.usuarioLabel.pack(side=LEFT)
        self.usuario = Entry(self.janela6)
        self.usuario["width"] = 30
        self.usuario["font"] = self.fontePadrao
        self.usuario.pack()

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.senhaLabel = Label(self.janela7, text="Senha:", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela7)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack()

        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.inserir = Button(self.janela8)
        self.inserir["text"] = "Inserir"
        self.inserir["font"] = ("Arial", "10")
        self.inserir["width"] = 10
        self.inserir.pack(side=RIGHT)

        self.alterar = Button(self.janela8)
        self.alterar["text"] = "Alterar"
        self.alterar["font"] = ("Arial", "10")
        self.alterar["width"] = 10
        self.alterar.pack(side=RIGHT)

        self.excluir = Button(self.janela8)
        self.excluir["text"] = "Excluir"
        self.excluir["font"] = ("Arial", "10")
        self.excluir["width"] = 10
        self.excluir.pack(side=RIGHT)

root = Tk()
janela2(root)
root.mainloop()