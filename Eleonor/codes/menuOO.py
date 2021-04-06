#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 23:37:52 2021

@author: toor
"""
import os

#import django
from tkinter import *
import psycopg2
import tkinter.messagebox #conclure
from datetime import date, datetime
import time
import math, random

#print(django.get_version())

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

class Menu(Tk):
    def __init__(self):
        self.fen = Tk()
        self.fen.title("Gestion des ventes")
        self.fen.geometry("1010x642+140+20")        
        menubar = Menu(self.fen)
        
        ventemenu = Menu(menubar, tearoff=0)
        ventemenu.add_command(label="Nouvelle")
        ventemenu.add_command(label="Statistiques")
        ventemenu.add_command(label="Exit", command=self.fen.destroy)
        ventemenu.add_separator()
        menubar.add_cascade(label="Ventes", menu=ventemenu)
        
        
        clientmenu = Menu(menubar, tearoff=0)
        clientmenu.add_command(label="Nouveau")
        clientmenu.add_command(label="Afficher")
        clientmenu.add_command(label="Exit", command=self.fen.destroy)
        clientmenu.add_separator()
        menubar.add_cascade(label="Clients", menu=clientmenu)
        
        
        produitmenu = Menu(menubar, tearoff=0)
        produitmenu.add_command(label="Nouveau")
        produitmenu.add_command(label="Lister")
        produitmenu.add_command(label="Exit", command=self.fen.destroy)
        produitmenu.add_separator()
        menubar.add_cascade(label="Produits", menu=produitmenu)
        
        
        factmenu = Menu(menubar, tearoff=0)
        factmenu.add_command(label="Nouvelle")
        factmenu.add_command(label="Lister")
        factmenu.add_command(label="Exit", command=self.fen.destroy)
        factmenu.add_separator()
        menubar.add_cascade(label="Factures", menu=factmenu)
        
        
        
        self.fen.config(menu=menubar)
        

obj = Menu()
    #obj.remplissage(1,54,"claude",89,produit,numero,qt,prixl,59350)
            
 



#obj = Facturation(fen)
#obj.remplissage(1,54,"claude",89,produit,numero,qt,prixl,59350)

     

obj.mainloop()
