import tkinter
from tkinter import *
from tkinter import ttk
###CLICKS PRINCIPAIS###

def cadastrar():
    janelaCad = Toplevel()
    janelaCad.title("CADASTRO")
    janelaCad["bg"] = "#00008B"
    janelaCad.geometry("300x300+200+200")
    ##importando as imagens
    ##imgfundo = PhotoImage(file="CADASTRO.png")
    imgbuttonvoltar = PhotoImage(file="VOLTAR.png")
    imgbuttonsalvar = PhotoImage(file="SALVAR.png")

    back = Label(janelaCad)
    back.la = PhotoImage(file='CADASTRO.png')
    back['image'] = back.la
    back.pack()

    def salvar():
        reg_nome = caixaProp.get()
        reg_modelo = caixaModelo.get()
        reg_placa = caixaPlaca.get()
        reg_ano = caixaAno.get()
        reg_marca = caixaMarca.get()
        data = {'1': reg_nome, '2': reg_modelo, '3': reg_placa, '4': reg_ano, '5': reg_marca}

        with open("cadastro.txt", "a", encoding='utf-8') as arq:
            arq.write(" 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 \n")
            arq.write("  Proprietáio: " + data['1'] + "\n")
            arq.write("  Modelo: " + data["2"] + "\n")
            arq.write("  Placa: " + data["3"] + "\n")
            arq.write("  Ano de Modificação: " + data["4"] + "\n")
            arq.write("  Marca: " + data["5"] + "\n")
            arq.close()

        janela = Toplevel()
        janela.title("MENU PRINCIPAL")
        janela["bg"] = "#00008B"
        ##importando imagens
        btnCadastrar = PhotoImage(file="CADASTRAR (1).png")
        btnConsultar = PhotoImage(file="CONSULTAR.png")
        btnRegistrarOco = PhotoImage(file="REGISTRAROCO.png")
        btnSair = PhotoImage(file="SAIR.png")
        fundoMenu = PhotoImage(file="MENU.png")

        lb = Label(janela, image=fundoMenu)
        lb.pack()

        bt1 = Button(janela, image=btnCadastrar, command=cadastrar)
        bt1.place(width=126, height=41, x=87, y=64)
        bt1["activebackground"] = "#0000CD"

        bt2 = Button(janela, image=btnConsultar, command=consultarCadastro)
        bt2.place(width=126, height=41, x=87, y=125)
        bt2["activebackground"] = "#0000CD"

        bt3 = Button(janela, image=btnRegistrarOco, command=registrarOcorrencia)
        bt3.place(width=126, height=41, x=87, y=185)
        bt3["activebackground"] = "#0000CD"

        bt4 = Button(janela, image=btnSair, command=sair)
        bt4.place(width=126, height=41, x=87, y=245)
        bt4["activebackground"] = "#0000CD"

        ##.geometry("LxA+distância da tela esquerda+distância do topo")
        janela.geometry("300x300+200+200")

        janela.mainloop()

    ##labFundo = Label(janelaCad, image=imgfundo)
    ##labFundo.pack()

    ##caixas de texto
    caixaProp = Entry(janelaCad, bd=2, justify=CENTER)
    caixaProp.place(width=240, height=18, x=30, y=63)

    caixaModelo = Entry(janelaCad, bd=2, justify=CENTER)
    caixaModelo.place(width=240, height=18, x=30, y=100)

    caixaPlaca = Entry(janelaCad, bd=2, justify=CENTER)
    caixaPlaca.place(width=240, height=18, x=30, y=141)

    caixaAno = Entry(janelaCad, bd=2, justify=CENTER)
    caixaAno.place(width=240, height=18, x=30, y=180)

    caixaMarca = Entry(janelaCad, bd=2, justify=CENTER)
    caixaMarca.place(width=240, height=18, x=30, y=220)


    ##botões
    btnVoltar = Button(janelaCad, image=imgbuttonvoltar, width=15,command=janelaCad.destroy)
    btnVoltar.place(width=90, height=40, x=45, y=250)

    btnSalvar = Button(janelaCad, image=imgbuttonsalvar, width=15,command=salvar)
    btnSalvar.place(width=90, height=40, x=166, y=250)


    janelaCad.mainloop()




def registrarOcorrencia():

    janelaOco = Toplevel()
    janelaOco.title("REGISTRO DE OCORRÊNCIA")
    janelaOco["bg"] = "#00008B"
    janelaOco.geometry("300x300+200+200")
    ##importando as imagens
    imgfundo = PhotoImage(file="OCORRENCIA.png")
    imgbuttonregist = PhotoImage(file="REGISTRAR1.png")
    imgbuttonvoltar= PhotoImage(file="VOLTAR1.png")


    labFundo = Label(janelaOco, image=imgfundo)
    labFundo.pack()

    caixaProp = Entry(janelaOco, bd=2, justify=CENTER)
    caixaProp.place(width=240, height=18, x=30, y=74)

    caixaModelo = Entry(janelaOco, bd=2, justify=CENTER)
    caixaModelo.place(width=240, height=18, x=30, y=115)

    caixaLugar = Entry(janelaOco, bd=2, justify=CENTER)
    caixaLugar.place(width=240, height=79, x=31, y=158)
    def salvar():
        reg_nome = caixaProp.get()
        reg_modelo = caixaModelo.get()
        reg_lugar = caixaLugar.get()

        data = {'1': reg_nome, '2': reg_modelo, '3': reg_lugar}

        with open("registroOcorrencia.txt", "a", encoding='utf-8') as arq:
            arq.write(" 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 \n")
            arq.write("  Proprietáio: " + data['1'] + "\n")
            arq.write("  Modelo: " + data["2"] + "\n")
            arq.write("  Lugar do roubo: " + data["3"] + "\n")
            arq.close()

        janelaReg = Tk()
        janelaReg.title("LOCALIZADOR")
        janelaReg["bg"] = "#2a5afa"

        lbtexto = Label(janelaReg, text="A LOCALIZAÇÃO DESSE CARRO É ESTA:", font=("Georgia", 10))
        lbtexto.place(x=15, y=20)
        lbtexto["bg"] = "#2a5afa"

        lblocal = Label(janelaReg, text="Av.Silves", font=(8))
        lblocal.place(x=15, y=50)
        lblocal["bg"] = "#2a5afa"

        btnVoltar = Button(janelaReg, text="<-", font=8, command=voltar)
        btnVoltar.place(width=35, height=35, x=25, y=250)
        btnVoltar["bg"] = "#092a57"
        btnVoltar["activebackground"] = "#0000CD"

        janelaReg.geometry("300x300+200+200")
        janelaReg.mainloop()


    btnVoltar = Button(janelaOco, image=imgbuttonvoltar, width=15, command=janelaOco.destroy)
    btnVoltar.place(width=91, height=40, x=44, y=247)

    btnRegistrar = Button(janelaOco, image=imgbuttonregist, width=15,command=salvar)
    btnRegistrar.place(width=91, height=40, x=170, y=247)

    janelaOco.mainloop()



def consultarCadastro():

    janelaConsul = Toplevel()
    janelaConsul.title("Consulta de cadastros")
    janelaConsul["bg"] = "#00008B"
    janelaConsul.geometry("300x300+200+200")

    btnvoltar=PhotoImage(file="VOLTARCONSULT.png")


    back = Label(janelaConsul)
    back.la = PhotoImage(file='CONSULTA.png')
    back['image'] = back.la
    back.pack()

    def Consultar():
        with open("cadastro.txt", "r", encoding='utf-8') as arq:
            txt = arq.read()
            arq.close()
        return txt

    Consultar()
    txt2 = Consultar()



    labelNome = Label(janelaConsul, text=txt2, font=(8))
    labelNome.place(x=10, y=50)
    labelNome["bg"] = "#2a5afa"

    btnVoltar = Button(janelaConsul,  text="<-",font=8, command=janelaConsul.destroy)
    btnVoltar.place(width=35, height=35,x=25, y=250)
    btnVoltar["bg"]="#092a57"
    btnVoltar["activebackground"] = "#0000CD"


    janelaConsul.mainloop

def sair():
   print()

###CLICKS SECUNDÁRIOS###

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
    janela=Toplevel()
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

