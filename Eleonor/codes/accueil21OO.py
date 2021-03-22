# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 22:18:00 2021

@author: Paradoxe
"""

from tkinter import *
import psycopg2
import tkinter.messagebox

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
        
   
        def tes():
            global canphoto
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

class Accueil(Tk):
    
    global rouge
    global vert 
    global bleu
    def __init__(self):
        
        Tk.__init__(self)
        
        self.title("Eleonor")
        self.geometry("930x700+140+40")
        self.config(bg="blue")
        self.resizable(False, False)
        canfAcc=Canvas(self, width=930,height=700)
        self.img=PhotoImage(file="images/imeleob.png")
        canfAcc.create_image(0,0,anchor=NW,image=self.img)
        canfAcc.config(bg="black")
        canfAcc.place(x=-1.2,y=-1.7) 
        self.imgparam = PhotoImage(file="images/responsable.png")
        boutonParam = Button(canfAcc, image=self.imgparam, cursor="hand2",bg="black",activebackground = "black",border=0, command=self.commencer)
        boutonParam.place(x=400, y=190)
        param_label = Label(canfAcc, text= "Commencer ", font=("arial", 10,"bold"), bg="black",fg="gold")
        param_label.place(x=425, y=350)
        

    def commencer(self):
        self.title("Eleonor")
        self.geometry("910x534+180+80")
        self.config(bg="blue")
        self.resizable(False, False)        
        canfAcc=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canfAcc.create_image(0,0,anchor=NW,image=self.img)
        canfAcc.config(bg="black")
        canfAcc.place(x=-1.2,y=-1.7)
    
            
        self.imgcaisse = PhotoImage(file="images/client.png")
        boutonCaisse = Button(canfAcc, image=self.imgcaisse, cursor="hand2",bg="black",activebackground = "black",border=0,
                                  command=self.client)
        boutonCaisse.place(x=85, y=190)
        caisse_label = Label(canfAcc, text= "Client ", font=("arial", 10,"bold"), bg="black",fg="gold")
        caisse_label.place(x=127, y=350)
            
        self.imgstat = PhotoImage(file="images/caissier.png")
        boutonStat = Button(canfAcc, image=self.imgstat, cursor="hand2",bg="black",activebackground = "black",border=0, command=self.produit)
        boutonStat.place(x=240, y=190)
        stat_label = Label(canfAcc, text= "Caissier ", font=("arial", 10,"bold"), bg="black",fg="gold")
        stat_label.place(x=280, y=350)
            
        self.imgparam = PhotoImage(file="images/responsable.png")
        boutonParam = Button(canfAcc, image=self.imgparam, cursor="hand2",bg="black",activebackground = "black",border=0, command=lambda:responsable())
        boutonParam.place(x=400, y=190)
        param_label = Label(canfAcc, text= "Responsables ", font=("arial", 10,"bold"), bg="black",fg="gold")
        param_label.place(x=425, y=350)
            
        self.imgadmin = PhotoImage(file="images/parametres.png")
        boutonAdmin = Button(canfAcc, image=self.imgadmin, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonAdmin.place(x=560, y=190)
        admin_label = Label(canfAcc, text= "Paramètres ", font=("arial", 10,"bold"), bg="black",fg="gold")
        admin_label.place(x=590, y=350)
            
        self.imgoperateur = PhotoImage(file="images/operateur.png")
        boutonOperateur = Button(canfAcc, image=self.imgoperateur, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonOperateur.place(x=720, y=190)
        operateur_label = Label(canfAcc, text= "Operateur ", font=("arial", 10,"bold"), bg="black",fg="gold")
        operateur_label.place(x=760, y=350)
        
              
        
    def client(self):
        self.title("Gestion des ventes")
        self.geometry("910x534+100+40")
        self.resizable(False,False)
        
        
        caninCl=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        caninCl.create_image(0,0,anchor=NW,image=self.img)
        caninCl.config(bg="black")
        
        caninCl.place(x=-2,y=-1.7)
        
        self.photoprecedent = PhotoImage(file = "images/precedent.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="black",activebackground="black",cursor="hand2",
                        command=self.retourclient)
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
        
    def retourclient(self):
        self.title("                                                                                     Eleonor")
        self.title("Eleonor")
        self.geometry("910x534+180+80")
        self.config(bg="blue")
        self.resizable(False, False)        
        canfAcc=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canfAcc.create_image(0,0,anchor=NW,image=self.img)
        canfAcc.config(bg="black")
        canfAcc.place(x=-1.2,y=-1.7)
    
            
        self.imgcaisse = PhotoImage(file="images/client.png")
        boutonCaisse = Button(canfAcc, image=self.imgcaisse, cursor="hand2",bg="black",activebackground = "black",border=0,
                                  command=self.client)
        boutonCaisse.place(x=85, y=190)
        caisse_label = Label(canfAcc, text= "Client ", font=("arial", 10,"bold"), bg="black",fg="gold")
        caisse_label.place(x=127, y=350)
            
        self.imgstat = PhotoImage(file="images/caissier.png")
        boutonStat = Button(canfAcc, image=self.imgstat, cursor="hand2",bg="black",activebackground = "black",border=0, command=self.produit)
        boutonStat.place(x=240, y=190)
        stat_label = Label(canfAcc, text= "Caissier ", font=("arial", 10,"bold"), bg="black",fg="gold")
        stat_label.place(x=280, y=350)
            
        self.imgparam = PhotoImage(file="images/responsable.png")
        boutonParam = Button(canfAcc, image=self.imgparam, cursor="hand2",bg="black",activebackground = "black",border=0, command=lambda:responsable())
        boutonParam.place(x=400, y=190)
        param_label = Label(canfAcc, text= "Responsables ", font=("arial", 10,"bold"), bg="black",fg="gold")
        param_label.place(x=425, y=350)
            
        self.imgadmin = PhotoImage(file="images/parametres.png")
        boutonAdmin = Button(canfAcc, image=self.imgadmin, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonAdmin.place(x=560, y=190)
        admin_label = Label(canfAcc, text= "Paramètres ", font=("arial", 10,"bold"), bg="black",fg="gold")
        admin_label.place(x=590, y=350)
            
        self.imgoperateur = PhotoImage(file="images/operateur.png")
        boutonOperateur = Button(canfAcc, image=self.imgoperateur, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonOperateur.place(x=720, y=190)
        operateur_label = Label(canfAcc, text= "Operateur ", font=("arial", 10,"bold"), bg="black",fg="gold")
        operateur_label.place(x=760, y=350)
        
    def produit(self):
        self.destroy()
        self.__init__()
        
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
        boutonValider = Button(self,image=self.photoValider, border = 0, bg="black",activebackground="black",cursor="hand2" )
        boutonValider.place(x=700,y=320)
        
        self.photoconclure = PhotoImage(file = "images/conclure3.png")
        boutonconclure = Button(self,image=self.photoconclure, border = 0, bg="black",activebackground="black",cursor="hand2" )
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
        
        interface = Main_frame(fenetre_principale=self)
        interface.mainloop()
  
        

obj = Accueil()
obj.mainloop()