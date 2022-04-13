from tkinter import*
from interface.lib import *

###CLICKS PRINCIPAIS###
def cadastrar():
    janelaCad = Tk()
    janelaCad.title("CADASTRO")
    janelaCad["bg"] = "#00008B"

    labelNome=Label(janelaCad,text="Propietário:",font=(8))
    labelNome.place(x=15 , y=20)
    labelNome["bg"] = "#00008B"

    caixaTexto=Entry(janelaCad,bd=2 , width=30)
    caixaTexto.pack(side=RIGHT)
    caixaTexto.place(x=100, y=20)


    labelNome1 = Label(janelaCad, text="Modelo:", font=(8))
    labelNome1.place(x=15, y=60)
    labelNome1["bg"] = "#00008B"

    caixaTexto1 = Entry(janelaCad, bd=2 , width=30)
    caixaTexto1.pack(side=RIGHT)
    caixaTexto1.place(x=100, y=60)

    labelNome2 = Label(janelaCad, text="Placa:", font=(8))
    labelNome2.place(x=15, y=100)
    labelNome2["bg"] = "#00008B"

    caixaTexto2 = Entry(janelaCad, bd=2 , width=30)
    caixaTexto2.pack(side=RIGHT)
    caixaTexto2.place(x=100, y=100)

    labelNome3 = Label(janelaCad, text="Ano Mod.:", font=(8))
    labelNome3.place(x=15, y=140)
    labelNome3["bg"] = "#00008B"

    caixaTexto3 = Entry(janelaCad, bd=2, width=30)
    caixaTexto3.pack(side=RIGHT)
    caixaTexto3.place(x=100, y=140)

    labelNome4 = Label(janelaCad, text="Marca:", font=(8))
    labelNome4.place(x=15, y=180)
    labelNome4["bg"] = "#00008B"

    caixaTexto3 = Entry(janelaCad, bd=2, width=30)
    caixaTexto3.pack(side=RIGHT)
    caixaTexto3.place(x=100, y=180)

    btnSalvar = Button(janelaCad, width=15, text="SALVAR", command=salvar)
    btnSalvar.place(x=165, y=250)
    btnSalvar["bg"] = "orange"
    btnSalvar["activebackground"] = "#0000CD"

    btnVoltar = Button(janelaCad, width=15, text="VOLTAR", command=voltar)
    btnVoltar.place(x=25, y=250)
    btnVoltar["bg"] = "orange"
    btnVoltar["activebackground"] = "#0000CD"

    janelaCad.geometry("300x300+200+200")
    janelaCad.mainloop()


def registrarOcorrencia():
    janelaOco = Tk()
    janelaOco.title("REGISTRO DE OCORRÊNCIA")
    janelaOco["bg"] = "#00008B"
    janelaOco.geometry("300x300+200+200")

    labelNome = Label(janelaOco, text="Propietário:", font=(8))
    labelNome.place(x=15, y=18)
    labelNome["bg"] = "#00008B"

    caixaTexto = Entry(janelaOco, bd=2, width=30)
    caixaTexto.pack(side=RIGHT)
    caixaTexto.place(x=100, y=20)

    labelNome1 = Label(janelaOco, text="Placa:", font=(8))
    labelNome1.place(x=15, y=60)
    labelNome1["bg"] = "#00008B"

    caixaTexto1 = Entry(janelaOco, bd=2, width=30)
    caixaTexto1.pack(side=RIGHT)
    caixaTexto1.place(x=100, y=60)

    labelNome2 = Label(janelaOco, text="Onde ocorreu o furto?:", font=(7))
    labelNome2.place(x=15, y=100)
    labelNome2["bg"] = "#00008B"

    caixaTexto2 = Entry(janelaOco, bd=2, width=45)
    caixaTexto2.place(x=15, y=130)

    btnRegistrar = Button(janelaOco, width=15, text="VOLTAR", command=voltar)
    btnRegistrar.place(x=25, y=250)
    btnRegistrar["bg"] = "orange"
    btnRegistrar["activebackground"] = "#0000CD"

    btnSalvar = Button(janelaOco, width=15, text="REGISTRAR", command=registrar)
    btnSalvar.place(x=165, y=250)
    btnSalvar["bg"] = "orange"
    btnSalvar["activebackground"] = "#0000CD"
    janelaOco.mainloop()

def consultarCadastro():
    print()

def sair():
    print()

###CLICKS SECUNDÁRIOS###
def salvar():  ##quando apertar o botão 'salvar' da tela de cadastro
    print()
def registrar():##qaundo clicar no botão 'registrar' da tela de registrar ocorrência
    janelaReg = Tk()
    janelaReg.title("LOCALIZADOR")
    janelaReg["bg"] = "#00008B"

    lbtexto = Label(janelaReg, text="A LOCALIZAÇÃO DO SEU CARRO É ESTA:", font=("Georgia",10))
    lbtexto.place(x=15, y=20)
    lbtexto["bg"] = "#00008B"

    lblocal=Label(janelaReg,text="Av.Silves",font=(8))
    lblocal.place(x=15, y=50)

    janelaReg.geometry("300x300+200+200")
    janelaReg.mainloop()

def voltar():##tentar colocar pra chamar 'interfacePrincipal()'-tava dando erro not defined
    janela = Tk()
    janela.title("MENU PRINCIPAL")
    janela["bg"] = "#00008B"

    lb = Label(janela, text="O QUE VOCÊ DESEJA FAZER?", font=("Georgia", 10))
    lb.place(x=65, y=10)
    lb["bg"] = "#00008B"

    bt1 = Button(janela, width=20, text="CADASTRAR", command=cadastrar)
    bt1.place(x=80, y=70)
    bt1["bg"] = "orange"
    bt1["activebackground"] = "#0000CD"

    bt2 = Button(janela, width=20, text="CONSULTAR", command=consultarCadastro)
    bt2.place(x=80, y=110)
    bt2["bg"] = "orange"
    bt2["activebackground"] = "#0000CD"

    bt3 = Button(janela, width=20, text="REGISTRAR OCORRÊNCIA", command=registrarOcorrencia)
    bt3.place(x=80, y=150)
    bt3["bg"] = "orange"
    bt3["activebackground"] = "#0000CD"

    bt4 = Button(janela, width=20, text="SAIR", command=sair)
    bt4.place(x=80, y=190)
    bt4["bg"] = "orange"
    bt4["activebackground"] = "#0000CD"

    ##.geometry("LxA+distância da tela esquerda+distância do topo")
    janela.geometry("300x300+200+200")

    janela.mainloop()
