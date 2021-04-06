#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:51:03 2021

@author: toor
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 22:18:00 2021

@author: Paradoxe
"""
import os
from tkinter import *
import psycopg2
import random
import time
from datetime import date
import matplotlib.pyplot as plt
import matplotlib
import random as rd
rouge="000"
vert="000"
bleu="000"

    
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
listeNumBonCmd=[]
remplirListboxAffiche=[]

class Eleonor(Tk):#Accueil

    
    
    
    def __init__(self):
        
        
        Tk.__init__(self)
        
        
        
        self.title("                                                                                     Eleonor")
        self.geometry("910x534+180+80")
        self.config(bg="blue")
        self.resizable(False, False)
        
        canfAcc=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canfAcc.create_image(0,0,anchor=NW,image=self.img)
        canfAcc.config(bg="black")
        canfAcc.place(x=-1.2,y=-1.7)
        
        self.imgClient = PhotoImage(file="images/demarrer1.png")
        boutonClient = Button(canfAcc, image=self.imgClient, cursor="hand2",bg="black",activebackground = "black",border=0,
                              command=self.menu)
        boutonClient.place(x=385, y=190)
        client_label = Label(canfAcc, text= "Commencer une nouvelle session ", font=("arial", 10,"bold"), bg="black",fg="gold")
        client_label.place(x=357, y=340)
        
    def menu(self):
        
        
        self.title("                                                                                     Eleonor")
        self.geometry("910x534+180+80")
        self.config(bg="blue")
        self.resizable(False, False)
        
        canfAcc=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canfAcc.create_image(0,0,anchor=NW,image=self.img)
        canfAcc.config(bg="black")
        canfAcc.place(x=-1.2,y=-1.7)
        
        
        self.imgClient = PhotoImage(file="images/client.png")
        boutonClient = Button(canfAcc, image=self.imgClient, cursor="hand2",bg="black",activebackground = "black",border=0,
                              command=self.client)
        boutonClient.place(x=85, y=190)
        client_label = Label(canfAcc, text= "Client ", font=("arial", 10,"bold"), bg="black",fg="gold")
        client_label.place(x=127, y=350)
        
        self.imgstat = PhotoImage(file="images/caissier.png")
        boutonCaissier = Button(canfAcc, image=self.imgstat, cursor="hand2",bg="black",activebackground = "black",border=0,
                            command=self.caissiers)
        boutonCaissier.place(x=240, y=190)
        caissier_label = Label(canfAcc, text= "Caissier ", font=("arial", 10,"bold"), bg="black",fg="gold")
        caissier_label.place(x=280, y=350)
        
        
        self.imgrespo = PhotoImage(file="images/responsable.png")
        boutonRespo = Button(canfAcc, image=self.imgrespo, cursor="hand2",bg="black",activebackground = "black",border=0,
                             command=self.responsables)
        boutonRespo.place(x=400, y=190)
        respo_label = Label(canfAcc, text= "Responsables ", font=("arial", 10,"bold"), bg="black",fg="gold")
        respo_label.place(x=425, y=350)
        
        
        self.imgParam = PhotoImage(file="images/parametres.png")
        boutonParam = Button(canfAcc, image=self.imgParam, cursor="hand2",bg="black",activebackground = "black",border=0,
                             command=self.parametres)
        boutonParam.place(x=560, y=190)
        param_label = Label(canfAcc, text= "Paramètres ", font=("arial", 10,"bold"), bg="black",fg="gold")
        param_label.place(x=590, y=350)
        
        
        
        self.imgoperateur = PhotoImage(file="images/operateur.png")
        boutonOperateur = Button(canfAcc, image=self.imgoperateur, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonOperateur.place(x=720, y=190)
        operateur_label = Label(canfAcc, text= "Operateur ", font=("arial", 10,"bold"), bg="black",fg="gold")
        operateur_label.place(x=760, y=350)
        
        
#======================ARBORESCENCE DU CLIENT =====================================
        
    def client(self):
        global rouge
        global vert 
        global bleu
        """global entryNomCl
        global entryPrenomCl
        global entryTelCl
        global entryadrCl"""
        
        global nomInsert
        global prenomInsert
        global telInsert
        global adrINsert
        
        
        self.title("Gestion des ventes")
        self.geometry("910x534+180+80")
        self.resizable(False,False)
        
        
        caninCl=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        caninCl.create_image(0,0,anchor=NW,image=self.img)
        caninCl.config(bg="black")
        
        caninCl.place(x=-2,y=-1.7)
        
        self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="black",activebackground="black",cursor="hand2",
                        command=self.menu)
        btprec.place(x=10,y=10)
        
        infoCl = Label(caninCl, font=('harrington', 35, 'bold'),bd=0, text="Informations générales", fg="aqua", bg="black")
        infoCl.place(x=210,y=52)
        
        
        nomCl = Label(self, font=('harrington', 20, 'bold'), text="Noms:", padx=1,fg="gold", bg="black")
        nomCl.place(x=165,y=160)
        entryNomCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryNomCl.place(x=320, y=162)
        
        prenomCl = Label(caninCl, font=('harrington', 20, 'bold'), text="Prenoms:", padx=1,fg="gold", bg="black")
        prenomCl.place(x=165, y=210)
        entryPrenomCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryPrenomCl.place(x=320, y=212)
                
        telCl = Label(caninCl, font=('harrington', 20, 'bold'), text="Téléphone:", padx=1,fg="gold", bg="black")
        telCl.place(x=165, y=260)
        entryTelCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryTelCl.place(x=320, y=262)
                
        adrCl = Label(caninCl, font=('harrington', 20, 'bold'), text="Addresse:", padx=1,fg="gold", bg="black")
        adrCl.place(x=165, y=310)
        entryadrCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryadrCl.place(x=320, y=312)
        
        
        
        nomInsert= entryNomCl.get()
        prenomInsert = entryPrenomCl.get()
        telInsert = entryTelCl.get()
        adrINsert = entryadrCl.get()
        
        
        self.imchSui=PhotoImage(file="images/suivant2.png")
        boutonSui= Button(self, image=self.imchSui, bd=-2,bg="black", activebackground="black",command=self.produits)
        boutonSui.place(x=360, y=350)
        
        caninCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        btprec.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        infoCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        nomCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        prenomCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        telCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        adrCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonSui.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
    """def retourAccueil(self):
        global rouge
        global vert 
        global bleu
        
        global canfAcc
        global boutonClient
        global client_label
        global boutonCaissier
        global caissier_label
        global boutonRespo
        global respo_label
        global boutonParam
        global param_label
        global boutonOperateur
        global operateur_label
        
        self.title("                                                                                     Eleonor")
        self.geometry("910x534+180+80")
        self.config(bg="blue")
        self.resizable(False, False)
        
        canfAcc=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canfAcc.create_image(0,0,anchor=NW,image=self.img)
        canfAcc.config(bg="black")
        canfAcc.place(x=-2,y=-1.7)
        
        
        self.imgClient = PhotoImage(file="images/client.png")
        boutonClient = Button(canfAcc, image=self.imgClient, cursor="hand2",bg="black",activebackground = "black",border=0,
                              command=self.client)
        boutonClient.place(x=85, y=190)
        client_label = Label(canfAcc, text= "Client ", font=("arial", 10,"bold"), bg="black",fg="gold")
        client_label.place(x=127, y=350)
        
        self.imgCaissier = PhotoImage(file="images/caissier.png")
        boutonCaissier = Button(canfAcc, image=self.imgCaissier, cursor="hand2",bg="black",activebackground = "black",border=0,
                            command=self.caissiers)
        boutonCaissier.place(x=240, y=190)
        caissier_label = Label(canfAcc, text= "Caissier ", font=("arial", 10,"bold"), bg="black",fg="gold")
        caissier_label.place(x=280, y=350)
        
        self.imgRespo = PhotoImage(file="images/responsable.png")
        boutonRespo = Button(canfAcc, image=self.imgRespo, cursor="hand2",bg="black",activebackground = "black",border=0, 
                             command=self.responsables)
        boutonRespo.place(x=400, y=190)
        respo_label = Label(canfAcc, text= "Responsables ", font=("arial", 10,"bold"), bg="black",fg="gold")
        respo_label.place(x=425, y=350)
        
        self.imgParam = PhotoImage(file="images/parametres.png")
        boutonParam = Button(canfAcc, image=self.imgParam, cursor="hand2",bg="black",activebackground = "black",border=0,
                             command=self.parametres)
        boutonParam.place(x=560, y=190)
        param_label = Label(canfAcc, text= "Paramètres ", font=("arial", 10,"bold"), bg="black",fg="gold")
        param_label.place(x=590, y=350)
        
        self.imgoperateur = PhotoImage(file="images/operateur.png")
        boutonOperateur = Button(canfAcc, image=self.imgoperateur, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonOperateur.place(x=720, y=190)
        operateur_label = Label(canfAcc, text= "Operateur ", font=("arial", 10,"bold"), bg="black",fg="gold")
        operateur_label.place(x=760, y=350)
        
        canfAcc.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonClient.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        client_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonCaissier.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        caissier_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonRespo.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        respo_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonParam.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        param_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonOperateur.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        operateur_label.config(bg="#"+rouge+""+vert+""+bleu+"")"""
        
    def produits(self):
        
        global rouge
        global vert 
        global bleu
        
        
       
        
        
        Tk.destroy(self)
        Tk.__init__(self)
        self.config(bg="black")
        self.geometry("1000x670+100+20")
        can=Canvas(self, width=900,heigh=620)
        can.config(bg="black")
        can.place(x=0,y=20)
        #can.grid()
        
        
        
        canvas = Canvas(can,bg="blue",width=540,height=640)#c'est ici que tu peux modifier la taille du tableau de produit
        
        scroll_y = Scrollbar(can, orient="vertical", command=canvas.yview)
        entête = ["Numero","Nom","Prix"]
        indice=0
        
        
        frame = Frame(canvas,width=540,height=540,bg="black")
        # labels presents dans le frame scrollable
        tab=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
        cursor=tab.cursor()
        cursor.execute("SELECT * FROM produits")
        rows=cursor.fetchall()
        tab.close()
        #print(rows)
        for i in entête:
            indice+=1   
            libelle = Label(self,text=i,bd=0.5,bg="gold",relief=RIDGE,width=26)
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
        
        self.photoValider = PhotoImage(file="images/valider1.png")
        boutonValider = Button(self,image=self.photoValider, border = 0, bg="black",activebackground="black",cursor="hand2" ,command = self.valider)
        boutonValider.place(x=700,y=320)
                
        self.photoconclure = PhotoImage(file="images/conclure3.png")
        boutonconclure = Button(self,image=self.photoconclure, border = 0, bg="black",activebackground="black",cursor="hand2" ,command = self.bonCommande )
        boutonconclure.place(x=700,y=600)
        
        self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="black",activebackground="black",cursor="hand2",
                        command=self.client)
        btprec.place(x=920,y=10)
                    
        frameValide=Frame(self,width=240,height=240,bd=-3)
        frameValide.place(x=620,y=390)
                
        scrollbar=Scrollbar(frameValide)
        scrollbar.pack(side=RIGHT, fill=Y)
                
        self.photoachat = PhotoImage(file="images/listeachat1.png")
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
        global prix_nom_affiche
        global remplirListboxAffiche
        
            
        quant= int(self.quantite.get())
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT  nom_produit, prix_produit FROM Produits WHERE num_produit=%s" %(parametre))
        rows = cursor.fetchall()
        #print(rows)
        #con.close()
        nom_affiche=str(rows[0][0])
        prixprod = rows[0][1]
        cursor.execute("SELECT prix_produit FROM produits WHERE num_produit=%s" %(parametre))
        rowprix = cursor.fetchone()
        #print(rowprix[0])
            
        prixU=rowprix[0]
        prixT=prixU*quant
        prixtt+=prixT
                    
        
        prix_affiche=str(rows[0][1])
        prix_nom_affiche=str(quant)+" "+nom_affiche+" pour "+prix_affiche+" FCFA l'unité"
        
        remplirListboxAffiche+=[prix_nom_affiche]
        self.listboxaffiche.insert(END, prix_nom_affiche)
        prix = quant*int(prix_affiche)
        print (prix)
        print(prixT)
        print(prixtt)
        print("nous avons",remplirListboxAffiche)
        
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
        
    def bonCommande(self):
        
        global numclient
        global num_facture
        
                
        numclient= random.randint(0,10000)
        x=random.randint(1000,9999)
        num_facture = x
       
        
        self.title("Gestion des ventes")
        self.geometry("1010x642+140+20")
                
                
        self.canfond=Canvas(self, width=1025,height=655)
        self.img=PhotoImage(file="images/imeleobfact.png")
        self.canfond.create_image(0,0,anchor=NW,image=self.img)
        self.canfond.config(bg="black")
        self.canfond.place(x=-2,y=-1.7)
        
        self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="black",activebackground="black",cursor="hand2",
                        command=self.retourAproduits)
        btprec.place(x=10,y=10)
        
                
                
                                                
                                                
                                                #==================================frames===============================
                                                            
        DataFrame = Frame(self, bd=-1, width=10, height=50, bg="black")
        DataFrame.place(x=160,y=140)
                
        titre = Label(self.canfond, font=('arial', 30, 'bold'), bg="black",fg="gold", text="Bon de commande final")
        titre.place(x=210,y=40)
        scrolf = Scrollbar(DataFrame, orient=VERTICAL)
        self.txtarea = Text(DataFrame, yscrollcommand=scrolf.set)
        #DataFrame.config(scrollregion=DataFrame.bbox('all'),yscrollcommand=scrolf.set)
        scrolf.pack(side=RIGHT,fill=Y)
        scrolf.config(command=self.txtarea.yview())
        self.txtarea.pack(side=BOTTOM, fil=BOTH)
                                     
    
        self.txtarea.insert(END, "\t\t\t\t\t     "+time.strftime("%A %d %B %Y %H:%M:%S"))
        #self.txtarea.insert(END, "\n\n  \t\t\t\tBoutique Numero" + str(numBoutique))
        self.txtarea.insert(END, "\n\n================================================================================")            
        self.txtarea.insert(END, "\n\n  Bon de commande N° : "+str(num_facture))
        self.txtarea.insert(END, "\n  Numero du client : "+str(numclient))
        self.txtarea.insert(END, "\n  Nom  et prenom du client : "+str(nomInsert+" "+prenomInsert))
        self.txtarea.insert(END, "\n  Coordonnées : "+str(telInsert+" "+adrINsert))
        #self.txtarea.insert(END, "\n  Numero du caissiers : 000"+str(numcaissier))
        self.txtarea.insert(END, "\n\n================================================================================")
        self.txtarea.insert(END, "\n  Ref")
        self.txtarea.insert(END, "\t  Produits")
        self.txtarea.insert(END, "\t\t  Quantité")
        self.txtarea.insert(END, "\t\t Prix Unitaire ")
        self.txtarea.insert(END, "\n================================================================================")
        i = 0
        while(i<len(produitlist)):
           
            self.txtarea.insert(END, "\n  "+str(numero_produit[i]))
            self.txtarea.insert(END, "\t  "+produitlist[i])
            self.txtarea.insert(END, "\t\t    "+str(quantitelist[i]))
            self.txtarea.insert(END, "\t\t   "+str(prixlist[i])+"FCFA")
            i+=1
            
            
            
        self.txtarea.insert(END, "\n\n\n\tPrix total : "+str(prixtt)+" FCFA"  )
        
        
        """self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="black",activebackground="black",cursor="hand2",
                        command=self.produits)"""
        btprec.place(x=10,y=10)
         
        self.butImprimer = Button(self, text="Imprimer",font=('arial', 30, 'bold'), bg="black",fg="gold", command = self.imprimer)
        self.butImprimer.place(x=547, y=540)
        
    def imprimer(self):
        
        global listeNumBonCmd
        
        question = messagebox.askyesno("Enregistrement","Voulez vous enregistrer la facture?")
        if question > 0:
            self.data = self.txtarea.get("1.0","end-1c")
            if os.path.isdir('factures'):
                f1=open("factures/Facture N°"+str(num_facture)+".txt", "w")
                f1.write(self.data)
                listeNumBonCmd+=[str(num_facture)]
                print("nombre de bon: ")
                print(listeNumBonCmd)
                f1.close()
                Eleonor.produits(self)
                #self.destroy()
            else:
                os.mkdir("factures")
                f1=open("factures/Facture N°"+str(num_facture)+".txt", "w")
                f1.write(self.data)
                listeNumBonCmd+=[str(num_facture)]
                print("nombre de bon: ")
                print(listeNumBonCmd)
                f1.close
                #tab=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
                #cursor=tab.cursor()
                #cursor.execute("INSERT INTO Factures (num_facture, prix_totale,date, num_client) VALUES ('"+num_facture+"', '"+prixtt+"', '"+f'{datetime.now():%m-%d-%Y}'+"', '"+numclient+"', '"+numcaissier+"')")
                #tab.commit()
                Eleonor.produits(self)
                #self.destroy()
                
                
    def retourAproduits(self):
        
            
            print("la listbox est:",remplirListboxAffiche)
            Eleonor.produits(self)
            for elt in remplirListboxAffiche:
                self.listboxaffiche.insert(END, elt)
            

        

        
        
        
    """def retourProduits(self):
        global rouge
        global vert 
        global bleu
        
        
        self.title("Gestion des ventes")
        self.geometry("910x534+180+80")
        self.resizable(False,False)
        
        
        caninCl=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        caninCl.create_image(0,0,anchor=NW,image=self.img)
        caninCl.config(bg="black")
        
        caninCl.place(x=-2,y=-1.7)
        
        self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="black",activebackground="black",cursor="hand2",
                        command=self.retourAccueil)
        btprec.place(x=10,y=10)
        
        infoCl = Label(caninCl, font=('harrington', 35, 'bold'),bd=0, text="Informations générales", fg="aqua", bg="black")
        infoCl.place(x=210,y=52)
        
        
        nomCl = Label(self, font=('harrington', 20, 'bold'), text="Noms:", padx=1,fg="gold", bg="black")
        nomCl.place(x=165,y=160)
        entryNomCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryNomCl.insert(END,nomInsert )
        entryNomCl.place(x=320, y=162)
        
        prenomCl = Label(caninCl, font=('harrington', 20, 'bold'), text="Prenoms:", padx=1,fg="gold", bg="black")
        prenomCl.place(x=165, y=210)
        entryPrenomCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryPrenomCl.insert(END, prenomInsert)
        entryPrenomCl.place(x=320, y=212)
                
        telCl = Label(caninCl, font=('harrington', 20, 'bold'), text="Téléphone:", padx=1,fg="gold", bg="black")
        telCl.place(x=165, y=260)
        entryTelCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryTelCl.insert(END, telInsert)
        entryTelCl.place(x=320, y=262)
                
        adrCl = Label(caninCl, font=('harrington', 20, 'bold'), text="Addresse:", padx=1,fg="gold", bg="black")
        adrCl.place(x=165, y=310)
        entryadrCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryadrCl.insert(END, adrINsert)
        entryadrCl.place(x=320, y=312)
        
        self.imchSui=PhotoImage(file="images/icsuiv1.png")
        boutonSui= Button(self, image=self.imchSui, bd=-2,bg="black", activebackground="black",command=self.produits)
        boutonSui.place(x=860, y=490)
        
        caninCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        btprec.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        infoCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        nomCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        prenomCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        telCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        adrCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonSui.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")"""
        
        
#=======================ARBORESCENCE DU CAISSIER=============================================
    def caissiers(self):
        
        self.title("Gestion des ventes")
        self.geometry("540x320+430+270")
        self.resizable(False, False)
        
        
        can=Canvas(self, width=600,heigh=400)
        self.img=PhotoImage(file="images/noirx.png")
        can.create_image(340,120,image=self.img)
        can.place(x=-5,y=-2)
        
        self.photoinscrit= PhotoImage(file="images/icprec1.png")
        boutonprecConx = Button(self,image = self.photoinscrit, bd=-2,bg="black",activebackground = "black", cursor="hand2",
                                command=self.menu)
        boutonprecConx.place(x=10,y=10)
        
        
        nom_label = Label(self, text= "Login", font=("harrington", 20), bg="black", fg="gold")
        nom_label.place(x=20, y=80)
        
        password_label = Label(self, text= "Password ", font=("harrington", 20), bg="black", fg="gold")
        password_label.place(x=20, y=150)
            
        
        nom_entry = Entry(self,bg = "white", font=("harrington", 20))
        nom_entry.place(x=150, y=80)
        
        password_entry = Entry(self, bg = "white",font=("harrington", 20),show="¤")
        password_entry.place(x=150, y=150)
        
        self.photoconnect = PhotoImage(file="images/icconex1.png")
        add_button = Button(self,image = self.photoconnect, cursor="hand2",bg="black",activebackground = "black",border=0,command=self.caissierConnect)
        add_button.place(x=134, y=210)
        
        
        
        
        
#=======================ARBORESCENCE DES RESPONSABLES=============================

    def responsables(self):
        global rouge
        global vert 
        global bleu
    
        self.title("¤¤¤¤¤¤¤¤¤¤¤¤• PRODUITS ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
        self.geometry("910x534+180+80")
        self.resizable(False,False)
        canfResp=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canfResp.create_image(0,0,anchor=NW,image=self.img)
        canfResp.config(bg="black")
        canfResp.place(x=-2,y=-1.7)
        
        self.photoPrec= PhotoImage(file="images/icprec1.png")
        boutonAcc = Button(canfResp,image = self.photoPrec, bd=-2,bg="black",activebackground = "black", cursor="hand2",
                                command=self.menu)
        boutonAcc.place(x=10,y=10)
        
        self.imgrespovente = PhotoImage(file="images/respovente1.png")
        boutonrespoventes = Button(canfResp, image=self.imgrespovente, cursor="hand2",bg="black",activebackground = "black",border=0,
                                   command=self.etatsGeneralVentes)
        boutonrespoventes.place(x=180, y=100)
        respovente_label = Label(canfResp, text= "Responsable \ndes ventes ", font=("arial", 10,"bold"), bg="black",fg="gold")
        respovente_label.place(x=210, y=250)
        
        self.imgrespoappro = PhotoImage(file="images/respoappro2.png")
        boutonrespoappro = Button(canfResp, image=self.imgrespoappro, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonrespoappro.place(x=400, y=100)
        respoappro_label = Label(canfResp, text= "Responsable \ndes approvisionement ", font=("arial", 10,"bold"), bg="black",fg="gold")
        respoappro_label.place(x=395, y=250)
        
        self.imgrespoRh = PhotoImage(file="images/resporh.png")
        boutonrespoRh = Button(canfResp, image=self.imgrespoRh, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonrespoRh.place(x=610, y=100)
        respoRh_label = Label(canfResp, text= "Responsable \ndes ressources humaines ", font=("arial", 10,"bold"), bg="black",fg="gold")
        respoRh_label.place(x=595, y=250)
        
        self.imgrespofiscal = PhotoImage(file="images/respofiscal3.png")
        boutonrespofiscal = Button(canfResp, image=self.imgrespofiscal, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonrespofiscal.place(x=280, y=320)
        respofiscal_label = Label(canfResp, text= "Responsable \nfiscal ", font=("arial", 10,"bold"), bg="black",fg="gold")
        respofiscal_label.place(x=307, y=470)
        
        self.imgComptable = PhotoImage(file="images/comptable3.png")
        boutoncomptable = Button(canfResp, image=self.imgComptable, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutoncomptable.place(x=520, y=310)
        comptable_label = Label(canfResp, text= "Responsable \ncomptabilité ", font=("arial", 10,"bold"), bg="black",fg="gold")
        comptable_label.place(x=547, y=465)
        
        canfResp.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonAcc.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonrespoventes.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        respovente_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonrespoappro.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        respoappro_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonrespoRh.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        respoRh_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonrespofiscal.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        respofiscal_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutoncomptable.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        comptable_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        
    def etatsGeneralVentes(self):
        global rouge
        global vert 
        global bleu
        
        #self.__init__()
        
        
        self.geometry("1030x600+180+80")
        canSG=Canvas(self, width=1030,height=600)
        canSG.config(bg="black")
        canSG.place(x=-2,y=-1.7)
        
        titreSG=Label(canSG, text="          Etats général des ventes",font=("harrington",30,"bold"),fg="gold",bg="black")
        titreSG.place(x=175, y=10)
        
        self.canphotoSG=Canvas(self, width=800,height=350)
        
        self.photoPrec= PhotoImage(file="images/icprec1.png")
        boutonRetRespo = Button(canSG,image = self.photoPrec, bd=-2,bg="black",activebackground = "black", cursor="hand2",
                                command=self.responsables)
        boutonRetRespo.place(x=10,y=10)
        self.imgSG= PhotoImage(file="images/grapheproduit13.png") 
        self.canphotoSG.create_image(2,2, anchor=NW, image=self.imgSG)
        self.canphotoSG.place(x=160,y=100)
        
        self.photoVparProd = PhotoImage(file="images/boutonStatprod1.png")
        btVparProd = Button(self,image=self.photoVparProd, bg="black",bd=-2,activebackground="black",cursor="hand2",
                            command=self.venteParProduit)
        btVparProd.place(x=700,y=500)
        
        canSG.config(bg="#"+rouge+""+vert+""+bleu+"")
        titreSG.config(bg="#"+rouge+""+vert+""+bleu+"")
        btVparProd.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT sum(prix_total),date FROM factures group by(date)")
        rows = cursor.fetchall()
        print(rows)
        con.close()
        
        recette=[]
        for elt in rows:
            recette+=[elt[0]]
            
        print(recette)
        
        indice=[]
        jour=[]
        for elt in rows:
            indice=str(elt[1])
            #print(str(elt[1]))
            
            #print(jour)
            
            jour+=[indice]
            
        print(jour)    
        #print(jour)
            
        
            
        taillex=len(rows)
        plt.figure(figsize=(10,4))
        
        
        
        plt.bar(jour ,height=recette,facecolor="green")
        
        plt.show()#pour fficher dans autre chose que jupiter
        
        plt.savefig('images/graphe.png')
        plt.close()
        
    def venteParProduit(self):
        
        Tk.destroy(self)
        Tk.__init__(self)
        
        self.config(bg="black")
        self.geometry("1300x695+25+0")
        can=Canvas(self, width=900,heigh=620)
        can.config(bg="black")
        can.place(x=0,y=20)
        #can.grid()
        
         
        
        
        
        canvas = Canvas(can,bg="black",width=540,height=640)#c'est ici que tu peux modifier la taille du tableau de produit
        
        scroll_y = Scrollbar(can, orient="vertical", command=canvas.yview)
        entête = ["Numero","Nom","Prix"]
        indice=0
        
        
        frame = Frame(canvas,width=540,height=540,bg="black")
        # labels presents dans le frame scrollable
        tab=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
        cursor=tab.cursor()
        cursor.execute("SELECT * FROM produits")
        rows=cursor.fetchall()
        tab.close()
        #print(rows)
        for i in entête:
            indice+=1   
            libelle = Label(self,text=i,bd=0.5,bg="gold",relief=RIDGE,width=26)
            libelle.grid(row=0,column=indice,sticky=NSEW)
        
        

        def fond(e):
            global imgp
            
            con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
            cursor = con.cursor()
            cursor.execute("select (sum(contenir.quantite) * sum(contenir.prix_unitaire)) as prix, factures.date from contenir inner join factures on (contenir.num_facture = factures.num_facture) where contenir.num_produit=%s group by date" %(e))
            rows = cursor.fetchall()
            print(rows)
            con.close()
            
            recette=[]
            for elt in rows:
                recette+=[elt[0]]
                
            print(recette)
            
            indice=[]
            jour=[]
            for elt in rows:
                indice=str(elt[1])
                #print(str(elt[1]))
                
                #print(jour)
                
                jour+=[indice]
            print("======================================================")
            print(jour)    
            #print(jour)
                
            
                
            taillex=len(rows)
            plt.figure(figsize=(10,4))
            
            
            
            plt.bar(jour ,height=recette,facecolor="green")
            
            plt.show()#pour fficher dans autre chose que jupiter
            
            plt.savefig("images/graphe"+str(e)+".png")
            plt.close()
           
            #a=int(num_produit.get())
            #self.canphoto=Canvas(obj, width=200,height=200)
            imgp=PhotoImage(file="images/graphe"+str(e)+".png")
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
        
        label_statParProd=Label(self, text= "Statistique de vente par produits", font=("arial", 15,"bold"), bg="black",fg="gold")
        label_statParProd.place(x=780, y=0)
        
        self.canphoto=Canvas(self, width=687,height=350)       
        self.imgp= PhotoImage(file="images/graphe.png") 
        self.canphoto.create_image(2,2, anchor=NW, image=self.imgp, tags="img_fond")
        self.canphoto.place(x=590,y=35)
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("select (sum(contenir.quantite) * sum(contenir.prix_unitaire)) as prix, contenir.num_produit from contenir  group by num_produit order by prix desc")
        rows = cursor.fetchall()

        
        con.close()
        print(rows)
        self.xs=[]
        self.ys=[] 
        for row in rows:
            x = row[0]
            y = row[1]
            self.xs.append(x)
            self.ys.append(y)
        print(self.xs)
        print(self.ys)
        
        
        
        label_meilleurVente=Label(self, text= "Produits les mieux vendus", font=("arial", 15,"bold"), bg="black",fg="gold")
        label_meilleurVente.place(x=780, y=420)
       
        self.meillvente=[]
        for i in (self.ys[0], self.ys[1], self.ys[2]):
            con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
            cursor = con.cursor()
            cursor.execute("select nom_produit from produits where num_produits=%s" %(i))
            rows = cursor.fetchone()
            self.meillvente.append(rows[0])
            con.close()
        print(self.meillvente)
        
        self.vente1=StringVar()
        self.vente2=StringVar()
        self.vente3=StringVar()
        
        self.vente1.set(self.meillvente[0])
        self.vente2.set(self.meillvente[1])
        self.vente3.set(self.meillvente[2])
        
        self.canphotoMeillrVente1=Canvas(self, width=200,height=200)       
        self.imgMV1= PhotoImage(file="images/prod"+str(self.ys[0])+".png") 
        self.canphotoMeillrVente1.create_image(2,2, anchor=NW, image=self.imgMV1, tags="img_fond")
        self.canphotoMeillrVente1.place(x=590,y=460)
        label_mllrVente1=Label(self, textvariable=self.vente1, font=("arial", 13,"bold"), bg="black",fg="gold")
        label_mllrVente1.place(x=590, y=665)
        
        self.canphotoMeillrVente2=Canvas(self, width=200,height=200)       
        self.imgMV2= PhotoImage(file="images/prod"+str(self.ys[1])+".png") 
        self.canphotoMeillrVente2.create_image(2,2, anchor=NW, image=self.imgMV2, tags="img_fond")
        self.canphotoMeillrVente2.place(x=830,y=460)
        label_mllrVente2=Label(self, textvariable=self.vente2, font=("arial", 13,"bold"), bg="black",fg="gold")
        label_mllrVente2.place(x=830, y=665)
        
        self.canphotoMeillrVente3=Canvas(self, width=200,height=200)       
        self.imgMV3= PhotoImage(file="images/prod"+str(self.ys[2])+".png") 
        self.canphotoMeillrVente3.create_image(2,2, anchor=NW, image=self.imgMV3, tags="img_fond")
        self.canphotoMeillrVente3.place(x=1070,y=460)
        label_mllrVente3=Label(self, textvariable=self.vente3, font=("arial", 13,"bold"), bg="black",fg="gold")
        label_mllrVente3.place(x=1070, y=665)
        
        
#===========================ARBORESCENCE DE PARAMETRES===========================

    def parametres(self):
        global rouge
        global vert 
        global bleu
        
        global varRouge
        global varVert
        global varBleu
        global canParam
        global titreParam
        global labelRouge
        global labelVert
        global labelBleu
        global boutonChangArr
        global boutonprec
        
        
        
        
        
        
        self.geometry("910x534+180+80")
        canParam=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canParam.create_image(0,0,anchor=NW,image=self.img)
        canParam.config(bg="black")
        canParam.place(x=-2,y=-1.7)
        
        self.photoPrec= PhotoImage(file="images/icprec1.png")
        boutonprec = Button(canParam,image = self.photoPrec, bd=-2,bg="black",activebackground = "black", cursor="hand2",
                                command=self.menu)
        
        boutonprec.place(x=10,y=10)
        
        
        titreParam=Label(canParam, text="Choisissez la couleur d'arrière plan \nqui vous convient",
                    font=("harrington",20,"bold"),fg="gold",bg="black")
        titreParam.place(x=175, y=10)
        
        
        
        varRouge = IntVar()
        varVert = IntVar()
        varBleu = IntVar()
        
        echelleRouge = Scale(self, variable=varRouge,from_=0 , to=255,length=200, orient="vertical" )
        echelleRouge.place(x=290,y=100)
        
        labelRouge=Label(self,text="Rouge",bg="black",fg="gold" ,font=("bold"))
        labelRouge.place(x=290,y=310)
        
        
        echelleVert = Scale(self, variable=varVert,from_=0 , to=255,length=200, orient="vertical" )
        echelleVert.place(x=400,y=100)
        
        labelVert=Label(self,text="Vert",bg="black",fg="gold",font=("bold"))
        labelVert.place(x=410,y=310)
        
        
        
        echelleBleu = Scale(self, variable=varBleu,from_=0 , to=255, length=200, orient="vertical")
        echelleBleu.place(x=530,y=100)
        
        labelBleu=Label(self,text="Bleu",bg="black",fg="gold",font=("bold"))
        labelBleu.place(x=540,y=310)
        
        
        
        
        self.imChangArr=PhotoImage(file="images/boutChang1.png")
        boutonChangArr= Button(self, image=self.imChangArr, bd=-2,bg="black", activebackground="black",
                           command=self.changeArrierePlan)
        boutonChangArr.place(x=360, y=350)
        
    def changeArrierePlan(self):
        global rouge
        global vert
        global bleu
        
        rouge=str(varRouge.get())
        vert=str(varVert.get())
        bleu=str(varBleu.get())
        
        if len(rouge)<2:
            rouge="00"+rouge
        elif len(rouge)==2:
            rouge="0"+rouge
            
            
        if len(vert)<2:
            vert="00"+vert
        if len(vert)==2:
            vert="0"+vert
            
        if len(bleu)<2:
            bleu="00"+bleu
            
        if len(bleu)==2:
            bleu="0"+bleu
        
        canParam.config(bg="#"+rouge+""+vert+""+bleu+"")
        titreParam.config(bd=-2,bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        labelRouge.config(bg="#"+rouge+""+vert+""+bleu+"")
        labelVert.config(bg="#"+rouge+""+vert+""+bleu+"")
        labelBleu.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonChangArr.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonprec.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
        
    def caissierConnect(self):
        
        
         
        self.geometry("910x534+100+40")
        canParam=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canParam.create_image(0,0,anchor=NW,image=self.img)
        canParam.config(bg="black")
        canParam.place(x=-2,y=-1.7)
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT num_caissier,nom_caissier FROM caissiers;")
        rows = cursor.fetchall()
        print(rows)
        
        for elt in rows:
            numero=elt[0]
            nom=elt[1]
        print(numero)   
        print(nom)
        
        canAff=Canvas(canParam, width=50,height=50)
        self.img2=PhotoImage(file="images/caissier2.png")
        canAff.create_image(0,0,anchor=NW,image=self.img2)
        #canAff.config(bg="black")
        canAff.place(x=25,y=5)
        
        caissier_label = Label(canParam, text=nom+""+str(numero) , font=("arial", 10,"bold"), bg="black",fg="gold")
        caissier_label.place(x=80, y=5)
        caissier_statut = Label(self, text="statut : " , font=("arial", 9,), bg="black",fg="gold")
        caissier_statut.place(x=80, y=30)
        
        caissier_statut2 = Label(self, text="Connecté... " , font=("arial", 9,"bold"), bg="black",fg="aqua")
        caissier_statut2.place(x=120, y=30)
        
        self.imbonCmd=PhotoImage(file="images/bonfactures1.png")
        boutonbonCmd= Button(self, image=self.imbonCmd, bd=-2,bg="black", activebackground="black",
                           command=self.appelBonCmd)
        boutonbonCmd.place(x=360, y=10)
        
        
   # def appelBonCmd(self):
        
        
        

        

        
        


        
        

o = Eleonor()
o.mainloop()