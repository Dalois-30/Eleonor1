#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:13:51 2021

@author: toor
"""

from tkinter import *
from datetime import date
import time

f1=open("factures/Facture du 03-09-2021 01:34:50.txt", "r")
donne = f1.read()
print(donne, type(donne))
val=donne.split("\n")
print(val, type(val))
root = Tk()
root.title("Gestion des ventes")
root.geometry("1010x642+140+20")
                
                
canfond=Canvas(root, width=1025,height=655)
img=PhotoImage(file="images/imeleobfact.png")
canfond.create_image(0,0,anchor=NW,image=img)
canfond.config(bg="black")
canfond.place(x=-2,y=-1.7)


                
                
                                                
                                                
                                                #==================================frames===============================
                                                            
DataFrame = Frame(root, bd=-1, width=10, height=50, bg="black")
DataFrame.place(x=160,y=140)
                
titre = Label(canfond, font=('arial', 30, 'bold'), bg="black",fg="gold", text="Informations finales de facture")
titre.place(x=210,y=40)
scrolf = Scrollbar(DataFrame, orient=VERTICAL)
txtarea = Text(DataFrame, yscrollcommand=scrolf.set)
#DataFrame.config(scrollregion=DataFrame.bbox('all'),yscrollcommand=scrolf.set)
scrolf.pack(side=RIGHT,fill=Y)
scrolf.config(command=txtarea.yview())
txtarea.pack(side=BOTTOM, fil=BOTH)
txtarea.insert(END, donne)
root.mainloop()
