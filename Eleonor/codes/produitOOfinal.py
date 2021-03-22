#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 08:52:10 2021

@author: toor
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:27:02 2021

@author: Paradoxe
"""
from FactureOO import Facture
from tkinter import *
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
    
prixtt=0
parametre =1
produitlist = []
quantitelist = []
prixlist = []
numero_produit=[]


class Produits(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.config(bg="white")
        self.geometry("1000x600+100+40")
        can=Canvas(self, width=900,heigh=600)
        can.config(bg="black")
        can.place(x=0,y=20)
        #can.grid()
        canvas = Canvas(can,bg="blue",width=540,height=540)#c'est ici que tu peux modifier la taille du tableau de produit
        
        scroll_y = Scrollbar(can, orient="vertical", command=canvas.yview)
        entête = ["Numero","Nom","Prix"]
        indice=0
        
        
        frame = Frame(canvas,width=540,height=540,bg="aqua")
        # labels presents dans le frame scrollable
        tab=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
        cursor=tab.cursor()
        cursor.execute("SELECT * FROM produits")
        rows=cursor.fetchall()
        tab.close()
        #print(rows)
        for i in entête:
            indice+=1   
            libelle = Label(self,text=i,bd=0.5,bg="gold",relief=RIDGE,width=25)
            libelle.grid(row=0,column=indice,sticky=NSEW)
        
        

        def fond(e):
            global imgp
           
            #a=int(num_produit.get())
            #self.canphoto=Canvas(obj, width=200,height=200)
            imgp=PhotoImage(file="images/prod"+str(e)+".png")
            self.canphoto.itemconfigure("img_fond",image=imgp)
            global parametre
            parametre = e
            print(parametre)
        
            
        listeNumero=[]
        for groupe in rows:
            listeNumero+=[groupe[0]]
                
            #print(listeNumero)
                
        listeNom=[]
        for groupe in rows:
            listeNom+=[groupe[1]]
            #print(listeNom)
            
        listePrix=[]
        for groupe in rows:
            listePrix+=[groupe[2]]
                #print(listePrix)
                    
        numero=dict()
        i=0
        while(i<len(listeNumero)): 
                
            numero[i] = Button(frame,text=listeNumero[i],bg="black",fg="gold",cursor="hand2",bd=0.5,width=25)
            numero[i].grid(row=i+1,column=1,sticky=NSEW)
                    
            i+=1
                    
        
                 
                #for indice in range(len(listeNom)):
                   # for element in listeNom
         
        
        nom=dict()  
        i=0
        while(i<len(listeNom)):
            nom[i] = Button(frame,text=listeNom[i],bg="black",fg="gold", cursor="hand2",bd=0.5,width=25)
            nom[i].grid(row=i+1,column=2,sticky=NSEW)
            i+=1
                        
        itemList=[]        
        for item in listeNumero:
            numero[listeNumero.index(item)].config(command = lambda z=item: fond(z)) 
            itemList.append(item)
            nom[listeNumero.index(item)].config(command = lambda z=item: fond(z))                
                
                #print(numero[listeNumero.index(item)])    
        i=0
        while(i<len(listePrix)):
            prix = Label(frame,text=str(listePrix[i])+" FCFA",bg="black",fg="gold", relief=RAISED,bd=0.5,width=25)
            prix.grid(row=i+1,column=3,sticky=NSEW)
            i+=1
    
       # insersion du frame dans le canvas
        canvas.create_window(100, 100, anchor='nw', window=frame)
        # on s'assure que tous sera affiché avant de définir la scrollregion
        canvas.update_idletasks()
        
        canvas.configure(scrollregion=canvas.bbox('all')#c'est cette commande qui s'assure de la presence, 
                         ,yscrollcommand=scroll_y.set)
                         
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')
        
        self.canphoto=Canvas(self, width=200,height=200)
               
        self.imgp= PhotoImage(file="images/nature.png") 
        self.canphoto.create_image(2,2, anchor=NW, image=self.imgp, tags="img_fond")
        self.canphoto.place(x=660,y=20)
                
        labelquantite = Label(self, font=('arial', 12, 'bold'), text="Quantité: ", fg="gold", bg="black")
        labelquantite .place(x=680,y=250)
        self.quantite = Entry(self, font=('arial', 14, 'bold'), width=3,bd=5)
        self.quantite.place(x=790,y=245)
            
        labelquantite = Label(self, font=('arial', 7, 'bold'), text="Indiquer \nla quantité achetée \navant de valider ", fg="green", bg="black")
        labelquantite .place(x=710,y=280)
        
        self.photoValider = PhotoImage(file = "images/valider1.png")
        boutonValider = Button(self,image=self.photoValider, border = 0, bg="black",activebackground="black",cursor="hand2" ,command = self.valider)
        boutonValider.place(x=700,y=320)
                
        self.photoconclure = PhotoImage(file = "images/conclure3.png")
        boutonconclure = Button(self,image=self.photoconclure, border = 0, bg="black",activebackground="black",cursor="hand2" ,command = self.ecrire )
        boutonconclure.place(x=700,y=600)
                    
        frameValide=Frame(self,width=240,height=240,bd=-3)
        frameValide.place(x=620,y=390)
                
        scrollbar=Scrollbar(frameValide)
        scrollbar.pack(side=RIGHT, fill=Y)
                
        self.photoachat = PhotoImage(file = "images/listeachat1.png")
        label= Label(frameValide,image=self.photoachat)
        label.pack()
                
        self.listboxaffiche=Listbox(frameValide,width=40,height=11,yscrollcommand=scrollbar.set)
        self.listboxaffiche.pack(side=LEFT, fill = BOTH)
        scrollbar.config(command=self.listboxaffiche.yview)   
        
            
    def valider(self):
        global prixtt
        global produitlist
        global quantitelist
        global prixlist
        global numero_produit
            
        quant= int(self.quantite.get())
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT  nom_produit, prix_produit FROM Produits WHERE num_produits=%s" %(parametre))
        rows = cursor.fetchall()
        #print(rows)
        #con.close()
        nom_affiche=str(rows[0][0])
        prixprod = rows[0][1]
        cursor.execute("SELECT prix_produit FROM produits WHERE num_produits=%s" %(parametre))
        rowprix = cursor.fetchone()
        #print(rowprix[0])
            
        prixU=rowprix[0]
        prixT=prixU*quant
        prixtt+=prixT
                    
        
        prix_affiche=str(rows[0][1])
        prix_nom_affiche=str(quant)+" "+nom_affiche+" pour "+prix_affiche+" FCFA l'unité"
        self.listboxaffiche.insert(END, prix_nom_affiche)
        prix = quant*int(prix_affiche)
        print (prix)
        print(prixT)
        print(prixtt)
        
        produitlist.append(nom_affiche)
        quantitelist.append(quant)
        prixlist.append(prixprod)
        numero_produit.append(parametre)
                    
        print(produitlist)
        print(quantitelist)
        print(prixlist)
        print(numero_produit)
        self.quantite.delete(0,END)              
                    
        """tupl=listboxaffiche.get('@1,0', END)
        #print (tupl, tupl[0])
        liste=list(tupl) 
        divis = liste[0].split(" ")
        #print(divis, divis[0], divis[1], divis[2]  )"""
        
    def ecrire(self):
        fen=Facture(self,532,20,"kevin",1,produitlist,numero_produit,quantitelist,prixlist,prixtt)
            
         
 
            
    
obj = Produits()
obj.mainloop()