from tkinter import *

def telaReg():
    janelaOco = Tk()
    janelaOco.title("REGISTRO DE OCORRÊNCIA")
    janelaOco["bg"] = "#00008B"
    janelaOco.geometry("300x300+200+200")
    ##importando as imagens
    imgfundo = PhotoImage(file="sist/OCORRENCIA.png")
    imgbuttonregist = PhotoImage(file="sist/REGISTRAR.png")


    labFundo = Label(janelaOco, image=imgfundo)
    labFundo.pack()

    caixaProp = Entry(janelaOco, bd=2, justify=CENTER)
    caixaProp.place(width=240, height=18, x=30, y=63)

    caixaModelo = Entry(janelaOco, bd=2, justify=CENTER)
    caixaModelo.place(width=240, height=18, x=30, y=100)

    caixaLugar = Entry(janelaOco, bd=2, justify=CENTER)
    caixaLugar.place(width=240, height=99, x=30, y=141)

    btnSalvar = Button(janelaOco, image=imgbuttonregist, width=15)
    btnSalvar.place(width=122, height=40, x=88, y=250)

    janelaOco.mainloop()

