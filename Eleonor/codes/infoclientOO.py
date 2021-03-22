#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:31:11 2021

@author: toor
"""
from tkinter import *
import tkinter.messagebox
from tkinter import *
import psycopg2
import tkinter.messagebox
import tkinter.messagebox
from datetime import date
import time
    
DATABASE = "kali_db2"   #nom de la base de donnée
USER = "kali"          #propriétaire de la bd
PASSWORD = "kali"         # mot de passe d'accès
HOST = "localhost"       #adresse ip du serveur, ici on est en local
          
    
            #Établissement de la connexion . Création du curseur"
try:
    con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
           
except Exception as err:
    print('La connexion a la base de donnée a échoué : \n'\
              'Erreur détecté :\n%s' % err)
    echec =1
else:
    cursor = con.cursor()  #création du curseur
    echec =0
                
if echec:
    sys.exit()
        
    
    
fen_client = Tk()
fen_client.title("Gestion des ventes")
fen_client.geometry("910x534+100+40")
fen_client.resizable(False,False)


can=Canvas(fen_client, width=915,height=540)
img=PhotoImage(file="images/noirx3.png")
can.create_image(0,0,anchor=NW,image=img)
can.place(x=-5,y=-1.7)

photoprecedent = PhotoImage(file = "images/precedent.png")
boutonprecedent = Button(fen_client,image=photoprecedent, bd=-5, bg="black",activebackground="black",cursor="hand2" )
boutonprecedent.place(x=10,y=10)

labelNom = Label(can, font=('harrington', 35, 'bold'),bd=0, text="Informations générales", fg="aqua", bg="black")
labelNom.place(x=50,y=52)


labelNom = Label(fen_client, font=('harrington', 20, 'bold'), text="Noms:", padx=1,fg="gold", bg="black")
labelNom.place(x=5,y=160)
entryNom = Entry(can, font=('harrington', 20, 'bold'), width=20)
entryNom.place(x=160, y=162)

labelNom = Label(can, font=('harrington', 20, 'bold'), text="Prenoms:", padx=1,fg="gold", bg="black")
labelNom.place(x=5, y=210)
entryNom = Entry(can, font=('harrington', 20, 'bold'), width=20)
entryNom.place(x=160, y=212)
        
labelAdresse = Label(can, font=('harrington', 20, 'bold'), text="Téléphone:", padx=1,fg="gold", bg="black")
labelAdresse.place(x=5, y=260)
entryAdresse = Entry(can, font=('harrington', 20, 'bold'), width=20)
entryAdresse.place(x=160, y=262)
        
labelTel = Label(can, font=('harrington', 20, 'bold'), text="Addresse:", padx=1,fg="gold", bg="black")
labelTel.place(x=5, y=310)
entryTel = Entry(can, font=('harrington', 20, 'bold'), width=20)
entryTel.place(x=160, y=312)

photosuivant = PhotoImage(file = "images/suivant2.png")
boutonsuivant = Button(fen_client,image=photosuivant, bg="black",bd=-2,activebackground="black",cursor="hand2", command=suivant)
boutonsuivant.place(x=240,y=400)
