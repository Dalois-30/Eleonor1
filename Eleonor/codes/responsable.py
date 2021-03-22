# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:05:25 2021

@author: Paradoxe
"""
from tkinter import *
import psycopg2
import tkinter.messagebox

root = Tk()
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