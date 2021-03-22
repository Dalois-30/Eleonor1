# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:43:50 2021

@author: Paradoxe
"""


#import django
from tkinter import *
import tkinter.messagebox
from tkinter import *
import psycopg2
import tkinter.messagebox
import tkinter.messagebox #conclure
from datetime import date
import time
#print(django.get_version())


windowFact = Tk()
windowFact.title("Gestion des ventes")
windowFact.geometry("1140x660+140+20")
windowFact.config(bg="black")

canfond=Canvas(windowFact, width=1160,height=660)
img=PhotoImage(file="images/noirmotifC.png")
canfond.create_image(0,0,anchor=NW,image=img)
canfond.place(x=-2,y=-1.7)


                                
                                
                                #==================================frames===============================
                                            
DataFrame = Frame(windowFact, bd=-1, width=1040, height=500, bg="black")
DataFrame.place(x=140,y=100)

titre = Label(DataFrame, font=('arial', 30, 'bold'), bg="black",fg="gold", text="Informations générale de la facturation").pack()
scrolf = Scrollbar(DataFrame, orient=VERTICAL)
txtarea = Text(DataFrame, yscrollcommand=scrolf.set)
scrolf.pack(side=RIGHT)
scrolf.config(command=txtarea.yview())
txtarea.pack()
                             
txtarea.insert(END, "\t\t\t\t\t     "+time.strftime("%A %d %B %Y %H:%M:%S"))
txtarea.insert(END, "\n\n\t\t\t\tBoutique Numero 5698")
txtarea.insert(END, "\n\n================================================================================")            
txtarea.insert(END, "\n\nNumero du client : 000+str(numclient))")
txtarea.insert(END, "\nNom du client : +nomclient)")
txtarea.insert(END, "\nNumero du caissiers : 000+str(numcaissier))")
txtarea.insert(END, "\n\n================================================================================")
txtarea.insert(END, "\n\nRef")
txtarea.insert(END, "\tProduits")
txtarea.insert(END, "\t\t\tQuantité")
txtarea.insert(END, "\t\t\tPrix Unitaire \n")
i = 0
"""while(i<len(produitlist)):
    
    txtarea.insert(END, "\n"+str(numero_produit[i]))
    txtarea.insert(END, "\t"+produitlist[i])
    txtarea.insert(END, "\t\t\t"+str(quantitelist[i]))
    txtarea.insert(END, "\t\t\t"+str(prixlist[i]))
    i+=1
    
    
    
    txtarea.insert(END, "\n\n\n\tPrix total : "+str(prixtt)+" FCFA"  )"""
    
windowFact.mainloop() 
