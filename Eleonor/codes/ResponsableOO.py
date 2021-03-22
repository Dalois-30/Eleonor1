#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:46:26 2021

@author: toor
"""

"""Codes réecrits en utilisant les concepts orienté objet
"""

from tkinter import *
import psycopg2
import tkinter.messagebox

class Responsable(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Eleonor")
        self.geometry("870x580+260+40")
        self.canfond=Canvas(self, width=1300,height=600)
        self.img=PhotoImage(file="images/noirmotif1.png")
        self.canfond.create_image(0,0,anchor=NW,image=self.img)
        self.canfond.place(x=-2,y=-1.7)
        
        self.imgrespovente = PhotoImage(file="images/respovente1.png")
        self.boutonrespoventes = Button(self, image=self.imgrespovente, cursor="hand2",bg="black",activebackground = "black",border=0)
        self.boutonrespoventes.place(x=130, y=100)
        self.respovente_label = Label(self, text= "Responsable \ndes ventes ", font=("arial", 10,"bold"), bg="black",fg="gold")
        self.respovente_label.place(x=160, y=250)
        
        self.imgrespoappro = PhotoImage(file="images/respoappro2.png")
        self.boutonrespoappro = Button(self, image=self.imgrespoappro, cursor="hand2",bg="black",activebackground = "black",border=0)
        self.boutonrespoappro.place(x=350, y=100)
        self.respoappro_label = Label(self, text= "Responsable \ndes approvisionement ", font=("arial", 10,"bold"), bg="black",fg="gold")
        self.respoappro_label.place(x=345, y=250)
        
        self.imgrespoRh = PhotoImage(file="images/resporh.png")
        self.boutonrespoRh = Button(self, image=self.imgrespoRh, cursor="hand2",bg="black",activebackground = "black",border=0)
        self.boutonrespoRh.place(x=560, y=100)
        self.respoRh_label = Label(self, text= "Responsable \ndes ressources humaines ", font=("arial", 10,"bold"), bg="black",fg="gold")
        self.respoRh_label.place(x=545, y=250)
        
        self.imgrespofiscal = PhotoImage(file="images/respofiscal3.png")
        self.boutonrespofiscal = Button(self, image=self.imgrespofiscal, cursor="hand2",bg="black",activebackground = "black",border=0)
        self.boutonrespofiscal.place(x=230, y=320)
        self.respofiscal_label = Label(self, text= "Responsable \nfiscal ", font=("arial", 10,"bold"), bg="black",fg="gold")
        self.respofiscal_label.place(x=257, y=470)
        
        self.imgComptable = PhotoImage(file="images/comptable3.png")
        self.boutoncomptable = Button(self, image=self.imgComptable, cursor="hand2",bg="black",activebackground = "black",border=0)
        self.boutoncomptable.place(x=460, y=310)
        self.comptable_label = Label(self, text= "Responsable \ncomptabilité ", font=("arial", 10,"bold"), bg="black",fg="gold")
        self.comptable_label.place(x=490, y=465)
        

        
#obj = Responsable()
#obj.mainloop()

        