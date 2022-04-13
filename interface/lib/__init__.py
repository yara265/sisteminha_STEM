from tkinter import*
from img import *
from interface.clicks import *

def interfacePrincipal():

    janela=Tk()
    janela.title("MENU PRINCIPAL")
    janela["bg"]="#00008B"

    lb=Label(janela,text="O QUE VOCÊ DESEJA FAZER?",font=("Georgia",10))
    lb.place(x=65,y=10)
    lb["bg"]="#00008B"


    bt1=Button(janela,width=20,text="CADASTRAR",command=cadastrar)
    bt1.place(x=80,y=70)
    bt1["bg"]="orange"
    bt1["activebackground"] = "#0000CD"



    bt2 = Button(janela, width=20, text="CONSULTAR",command=consultarCadastro)
    bt2.place(x=80, y=110)
    bt2["bg"] = "orange"
    bt2["activebackground"] = "#0000CD"

    bt3 = Button(janela, width=20, text="REGISTRAR OCORRÊNCIA",command=registrarOcorrencia)
    bt3.place(x=80, y=150)
    bt3["bg"] = "orange"
    bt3["activebackground"] = "#0000CD"

    bt4 = Button(janela, width=20, text="SAIR",command=sair)
    bt4.place(x=80, y=190)
    bt4["bg"] = "orange"
    bt4["activebackground"] = "#0000CD"


    ##.geometry("LxA+distância da tela esquerda+distância do topo")
    janela.geometry("300x300+200+200")

    janela.mainloop()

