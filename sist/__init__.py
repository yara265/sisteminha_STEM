from tkinter import*
from sist.clickss import *

def interfacePrincipal():

    janela=Tk()
    janela.title("MENU PRINCIPAL")
    janela["bg"]="#00008B"
    ##importando imagens
    btnCadastrar=PhotoImage(file="CADASTRAR (1).png")
    btnConsultar=PhotoImage(file="CONSULTAR.png")
    btnRegistrarOco=PhotoImage(file="REGISTRAROCO.png")
    btnSair=PhotoImage(file="SAIR.png")
    fundoMenu=PhotoImage(file="MENU.png")


    lb=Label(janela,image=fundoMenu)
    lb.pack()


    bt1=Button(janela,image=btnCadastrar,command=cadastrar)
    bt1.place(width=126,height=41,x=87,y=64)
    bt1["activebackground"] = "#0000CD"



    bt2 = Button(janela,image=btnConsultar,command=consultarCadastro)
    bt2.place(width=126,height=41,x=87,y=125)
    bt2["activebackground"] = "#0000CD"

    bt3 = Button(janela,image=btnRegistrarOco,command=registrarOcorrencia)
    bt3.place(width=126,height=41,x=87,y=185)
    bt3["activebackground"] = "#0000CD"

    bt4 = Button(janela,image=btnSair,command=sair)
    bt4.place(width=126,height=41,x=87,y=245)
    bt4["activebackground"] = "#0000CD"


    ##.geometry("LxA+distância da tela esquerda+distância do topo")
    janela.geometry("300x300+200+200")

    janela.mainloop()

