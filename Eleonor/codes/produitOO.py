#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 03:20:29 2021

@author: toor
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:39:23 2021

@author: toor
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 07:56:18 2021

@author: Paradoxe
"""

from FactureOO import Facture
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


   


 
class ScrollableCanvas(Frame):
     def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        #parent = Produits() 
        canvas=Canvas(self,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,10,10))
  
        vbar=Scrollbar(self,orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canvas.yview)
         
        canvas.config(width=200,height=680)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(pady=20,expand=True,fill=BOTH)
        
        can2=Canvas(obj,width=550, height=20,bg="green")
        can2.place(x=-1.7,y=-2)
        
        entête = ["Numero","Nom","Prix"]
        indice=0
        for i in entête:
            indice+=1   
            libelle = Label(can2,text=i,bd=3,bg="gold",relief=RIDGE,width=25)
            libelle.grid(row=0,column=indice,sticky=NSEW)
         
        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(-2.5, 0, window=interior, anchor=NW )
 
        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)
 
        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)
 
 
 
class Main_frame(Frame):
    # Init
    def __init__(self, fenetre_principale=None):
        Frame.__init__(self, fenetre_principale)
        self.grid()
        self.scrollable_canvas = ScrollableCanvas(self)
        self.scrollable_canvas.grid(row=1,column=1)
        
                
        tab=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
        cursor=tab.cursor()
        cursor.execute("SELECT * FROM produits")
        rows=cursor.fetchall()
        tab.close()
        #print(rows)
        
   

        def fond(e):
            
            #a=int(num_produit.get())
            #canphoto=Canvas(obj, width=200,height=200)
            obj.imgp=PhotoImage(file="images/prod"+str(e)+".png")
            obj.canphoto.itemconfigure("img_fond",image=obj.imgp)
            global parametre
            parametre = e
            #print(parametre)
   
        
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
        
            numero[i] = Button(self.scrollable_canvas.interior,text=listeNumero[i],bg="black",fg="gold",cursor="hand2",bd=0.5,width=25)
            numero[i].grid(row=i,column=1,sticky=NSEW)
            
            i+=1
            

         
        #for indice in range(len(listeNom)):
           # for element in listeNom
 

        nom=dict()  
        i=0
        while(i<len(listeNom)):
                nom[i] = Button(self.scrollable_canvas.interior,text=listeNom[i],bg="black",fg="gold", cursor="hand2",bd=0.5,width=25)
                nom[i].grid(row=i,column=2,sticky=NSEW)
                i+=1
                
        itemList=[]        
        for item in listeNumero:
            numero[listeNumero.index(item)].config(command = lambda z=item: fond(z)) 
            itemList.append(item)
            nom[listeNumero.index(item)].config(command = lambda z=item: fond(z))                
        
        #print(numero[listeNumero.index(item)])    
        i=0
        while(i<len(listePrix)):
                prix = Label(self.scrollable_canvas.interior,text=str(listePrix[i])+" FCFA",bg="black",fg="gold", relief=RAISED,bd=0.5,width=25)
                prix.grid(row=i,column=3,sticky=NSEW)
                i+=1

   


        #print(parametre)       
class Produits(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("¤¤¤¤¤¤¤¤¤¤¤¤• PRODUITS ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
        self.geometry("930x700+140+40")
        self.config(bg="black")
        self.resizable(False,False)
        
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
        fen=Facture(obj,532,20,"kevin",1,produitlist,numero_produit,quantitelist,prixlist,prixtt)
        
     
    
obj = Produits()

 


    
interface = Main_frame(fenetre_principale=obj)
interface.mainloop()
                



obj.mainloop()          
            
      
    
    
    
    
            
            


