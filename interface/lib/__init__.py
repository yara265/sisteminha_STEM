from tkinter import*
from img import *
from interface.clicks import *
from img import *

def interface_Principal():
    janela=Tk()
    janela.title("MENU PRINCIPAL")
    janela["bg"]="blue"

    lb=Label(janela,text="O que você deseja fazer?")
    lb.place(x=80,y=10)
    lb["bg"]="blue"


    bt1=Button(janela,width=20,text="CADASTRAR",command=cadastrar)
    bt1.place(x=80,y=70)
    bt1["bg"]="orange"
    bt1["activebackground"] = "cyan"
    bt1["activeforeground"] = "black"

    bt2 = Button(janela, width=20, text="CONSULTAR",command=consultarCadastro)
    bt2.place(x=80, y=110)
    bt2["bg"] = "orange"
    bt2["activebackground"] = "cyan"

    bt3 = Button(janela, width=20, text="REGISTRAR OCORRÊNCIA",command=registrarOcorrencia)
    bt3.place(x=80, y=150)
    bt3["bg"] = "orange"
    bt3["activebackground"] = "cyan"

    bt4 = Button(janela, width=20, text="SAIR",command=sair)
    bt4.place(x=80, y=190)
    bt4["bg"] = "orange"
    bt4["activebackground"] = "cyan"


    ##.geometry("LxA+distância da tela esquerda+distância do topo")
    janela.geometry("300x300+200+200")

    janela.mainloop()