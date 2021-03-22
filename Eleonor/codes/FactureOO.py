#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:07:06 2021

@author: toor
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:43:50 2021

@author: Paradoxe
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

class Facture(Tk):
      
    def __init__(self, root, numBoutique, numclient, nomclient, numcaissier, produitlist, numero_produit, quantitelist, prixlist, prixtt):
        self.root = root
        self.fen=Toplevel(self.root)
        self.prixtt = prixtt
        self.produitlist = produitlist
        self.numclient=numclient
        self.num_caissier=numcaissier
        self.fen.title("Gestion des ventes")
        self.fen.geometry("1010x642+140+20")
                
                
        self.canfond=Canvas(self.fen, width=1025,height=655)
        self.img=PhotoImage(file="images/imeleobfact.png")
        self.canfond.create_image(0,0,anchor=NW,image=self.img)
        self.canfond.config(bg="black")
        self.canfond.place(x=-2,y=-1.7)
        x=random.randint(1000,9999)

        self.num_facture = x
        self.numero_produit = numero_produit
        self.quantitelist = quantitelist
        self.prixlist = prixlist        
                
                                                
                                                
                                                #==================================frames===============================
                                                            
        DataFrame = Frame(self.fen, bd=-1, width=10, height=50, bg="black")
        DataFrame.place(x=160,y=140)
                
        titre = Label(self.canfond, font=('arial', 30, 'bold'), bg="black",fg="gold", text="Informations finales de facture")
        titre.place(x=210,y=40)
        scrolf = Scrollbar(DataFrame, orient=VERTICAL)
        self.txtarea = Text(DataFrame, yscrollcommand=scrolf.set)
        scrolf.pack(side=RIGHT,fill=Y)
        scrolf.config(command=self.txtarea.yview())
        self.txtarea.pack(side=BOTTOM, fil=BOTH)
                                     
    
        self.txtarea.insert(END, "\t\t\t\t\t     "+time.strftime("%A %d %B %Y %H:%M:%S"))
        self.txtarea.insert(END, "\n\n  \t\t\t\tBoutique Numero" + str(numBoutique))
        self.txtarea.insert(END, "\n\n================================================================================")            
        self.txtarea.insert(END, "\n\n  Facture N° : "+str(self.num_facture))
        self.txtarea.insert(END, "\n  Numero du client : 000"+str(self.numclient))
        self.txtarea.insert(END, "\n  Nom du client : "+str(nomclient))
        self.txtarea.insert(END, "\n  Numero du caissiers : 000"+str(numcaissier))
        self.txtarea.insert(END, "\n\n================================================================================")
        self.txtarea.insert(END, "\n  Ref")
        self.txtarea.insert(END, "\t  Produits")
        self.txtarea.insert(END, "\t\t  Quantité")
        self.txtarea.insert(END, "\t\t  Prix Unitaire ")
        self.txtarea.insert(END, "\n================================================================================")
        i = 0
        while(i<len(produitlist)):
           
            self.txtarea.insert(END, "\n  "+str(numero_produit[i]))
            self.txtarea.insert(END, "\t "+produitlist[i])
            self.txtarea.insert(END, "\t\t\t "+str(quantitelist[i]))
            self.txtarea.insert(END, "\t\t\t "+str(prixlist[i]))
            i+=1
            
            
            
        self.txtarea.insert(END, "\n\n\n\tPrix total : "+str(prixtt)+" FCFA"  )
         
        self.butImprimer = Button(self.fen, text="Imprimer",font=('arial', 30, 'bold'), bg="black",fg="gold", command = self.imprimer)
        self.butImprimer.place(x=547, y=465)
        
    def imprimer(self):
        question = messagebox.askyesno("Enregistrement","Voulez vous enregistrer la facture?")
        if question > 0:
            self.data = self.txtarea.get("1.0","end-1c")
            if os.path.isdir('factures'):
                #pass
                print("heureux")
            else:
                os.mkdir("factures")
                print("joyeux")
                
            print("sa continu?")
            f1=open("factures/Facture du "+str(f'{datetime.now():%d-%m-%Y %H:%M:%S}')+".txt", "w")
            f1.write(self.data) 
            f1.close
            tab=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
            cursor=tab.cursor()
            cursor.execute("INSERT INTO Factures (num_facture, prix_total,date, num_client,num_caissier) VALUES ('"+str(self.num_facture)+"', '"+str(self.prixtt)+"', '"+str(datetime.now())+"', '"+str(self.numclient)+"', '"+str(self.num_caissier)+"')")
            #cursor.execute("INSERT INTO Factures (num_facture, prix_total,date, num_client,num_caissier) VALUES ('"+str(self.num_facture)+"', '"+str(self.prixtt)+"', '"+'13-03-2021'+"', '"+str(self.numclient)+"', '"+str(self.num_caissier)+"')")

            
            tab.commit()
            tab.close()
            self.fen.destroy()
            j = 0
            while (j<len(self.produitlist)):
                con=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
                cursor=con.cursor()
                cursor.execute("INSERT INTO Contenir (quantite, prix_unitaire, num_produit, num_facture) VALUES ('"+str(self.quantitelist[j])+"','"+str(self.prixlist[j])+"', '"+str(self.numero_produit[j])+"', '"+str(self.num_facture)+"')")
                j+=1
                con.commit()
                con.close()
            self.root.destroy()
                
        else:
            return
            
#if os.path.isdir('/home/wtlx/dossier1'): verifier si un dossier existe
#os.mkdir('myDirectory')        creer un dossier

"""def testC2():
    obj = Facturation(fen,1,56,"claude",89,produit,numero,qt,prixl,59350)
    #obj.remplissage(1,54,"claude",89,produit,numero,qt,prixl,59350)"""
            
"""fen = Tk() 
bouton_new = Button(fen, width=10, height=1, text="Connexion", command=testC2)
bouton_new.pack() 

produit=["tomate","pomme","orange"]
numero = [8,9,3]
qt=[10,15,7]
prixl=[800,900,750] 

#obj = Facturation(fen)
#obj.remplissage(1,54,"claude",89,produit,numero,qt,prixl,59350)

     

fen.mainloop()"""