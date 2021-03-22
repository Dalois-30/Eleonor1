# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 22:18:00 2021

@author: Paradoxe
"""

from tkinter import *
import psycopg2
import tkinter.messagebox

def responsable():

    
    root = Toplevel(window)
    root.title("¤¤¤¤¤¤¤¤¤¤¤¤• PRODUITS ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    root.geometry("870x580+260+40")
    canfond=Canvas(root, width=1300,height=600)
    img=PhotoImage(file="images/noirmotif1.png")
    canfond.create_image(0,0,anchor=NW,image=img)
    canfond.place(x=-2,y=-1.7)
    
    imgrespovente = PhotoImage(file="images/respovente1.png")
    boutonrespoventes = Button(root, image=imgrespovente, cursor="hand2",bg="black",activebackground = "black",border=0)
    boutonrespoventes.place(x=130, y=100)
    respovente_label = Label(root, text= "Responsable \ndes ventes ", font=("arial", 10,"bold"), bg="black",fg="gold")
    respovente_label.place(x=160, y=250)
    
    imgrespoappro = PhotoImage(file="images/respoappro2.png")
    boutonrespoappro = Button(root, image=imgrespoappro, cursor="hand2",bg="black",activebackground = "black",border=0)
    boutonrespoappro.place(x=350, y=100)
    respoappro_label = Label(root, text= "Responsable \ndes approvisionement ", font=("arial", 10,"bold"), bg="black",fg="gold")
    respoappro_label.place(x=345, y=250)
    
    imgrespoRh = PhotoImage(file="images/resporh.png")
    boutonrespoRh = Button(root, image=imgrespoRh, cursor="hand2",bg="black",activebackground = "black",border=0)
    boutonrespoRh.place(x=560, y=100)
    respoRh_label = Label(root, text= "Responsable \ndes ressources humaines ", font=("arial", 10,"bold"), bg="black",fg="gold")
    respoRh_label.place(x=545, y=250)
    
    imgrespofiscal = PhotoImage(file="images/respofiscal3.png")
    boutonrespofiscal = Button(root, image=imgrespofiscal, cursor="hand2",bg="black",activebackground = "black",border=0)
    boutonrespofiscal.place(x=230, y=320)
    respofiscal_label = Label(root, text= "Responsable \nfiscal ", font=("arial", 10,"bold"), bg="black",fg="gold")
    respofiscal_label.place(x=257, y=470)
    
    imgComptable = PhotoImage(file="images/comptable3.png")
    boutoncomptable = Button(root, image=imgComptable, cursor="hand2",bg="black",activebackground = "black",border=0)
    boutoncomptable.place(x=460, y=310)
    comptable_label = Label(root, text= "Responsable \ncomptabilité ", font=("arial", 10,"bold"), bg="black",fg="gold")
    comptable_label.place(x=490, y=465)
    
    root.mainloop()




window = Tk()
window.title("Eleonor")
window.geometry("660x400+360+150")
window.config(bg="black")
window.resizable(False, False)

canfondC=Canvas(window, width=665,height=405)
img=PhotoImage(file="images/noirmotifC.png")
canfondC.create_image(0,0,anchor=NW,image=img)
canfondC.place(x=-2,y=-1.7)


imgcaisse = PhotoImage(file="images/client.png")
boutonCaisse = Button(window, image=imgcaisse, cursor="hand2",bg="black",activebackground = "black",border=0)
boutonCaisse.place(x=80, y=150)
caisse_label = Label(window, text= "Client ", font=("arial", 10,"bold"), bg="black",fg="gold")
caisse_label.place(x=92, y=230)

imgstat = PhotoImage(file="images/caissier.png")
boutonStat = Button(window, image=imgstat, cursor="hand2",bg="black",activebackground = "black",border=0)
boutonStat.place(x=180, y=150)
stat_label = Label(window, text= "Caissier ", font=("arial", 10,"bold"), bg="black",fg="gold")
stat_label.place(x=195, y=230)

imgparam = PhotoImage(file="images/responsable.png")
boutonParam = Button(window, image=imgparam, cursor="hand2",bg="black",activebackground = "black",border=0, command=lambda:respoonsable())
boutonParam.place(x=280, y=150)
param_label = Label(window, text= "Responsables ", font=("arial", 10,"bold"), bg="black",fg="gold")
param_label.place(x=275, y=230)

imgadmin = PhotoImage(file="images/parametres.png")
boutonAdmin = Button(window, image=imgadmin, cursor="hand2",bg="black",activebackground = "black",border=0)
boutonAdmin.place(x=390, y=150)
admin_label = Label(window, text= "Paramètres ", font=("arial", 10,"bold"), bg="black",fg="gold")
admin_label.place(x=380, y=230)

imgoperateur = PhotoImage(file="images/operateur.png")
boutonOperateur = Button(window, image=imgoperateur, cursor="hand2",bg="black",activebackground = "black",border=0)
boutonOperateur.place(x=490, y=150)
operateur_label = Label(window, text= "Operateur ", font=("arial", 10,"bold"), bg="black",fg="gold")
operateur_label.place(x=490, y=230)

window.mainloop()