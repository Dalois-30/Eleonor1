#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 09:00:19 2021

@author: toor
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:15:21 2021

@author: toor
"""
from string import punctuation
from tkinter import *
import psycopg2
import tkinter.messagebox
from datetime import date
import time




    #"""connexion a la base de données"""
    
    
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
    
global numero 

from tkinter import *

def donothing():
    filewin = Toplevel(rootMenu)
    button = Button(filewin, text="do nothing button")
    button.pack()
    
    

def nouvelleVente():
    def suivant():
        class ScrollableCanvas(Frame):
             def __init__(self, parent, *args, **kw):
                Frame.__init__(self, parent, *args, **kw)
                 
                canvas=Canvas(self,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,10,10))
          
                vbar=Scrollbar(self,orient=VERTICAL)
                vbar.pack(side=RIGHT, fill=Y)
                vbar.config(command=canvas.yview)
                 
                canvas.config(width=200,height=680)
                canvas.config(yscrollcommand=vbar.set)
                canvas.pack(pady=20,expand=True,fill=BOTH)
                
                can2=Canvas(root,width=550, height=20,bg="green")
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
                    global canphoto,imgp,a
                def fond(e):
                    global imgp,a
        
                    #a=int(num_produit.get())
                    imgp=PhotoImage(file="images/prod"+str(e)+".png")
                    canphoto.itemconfigure("img_fond",image=imgp)
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
        def valider():
            global prixtt
            global produitlist
            global quantitelist
            global prixlist
            global numero_produit
            
            quant= int(quantite.get())
                    
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
            listboxaffiche.insert(END, prix_nom_affiche)
            prix = quant*int(prix_affiche)
            #print (prix)
            #print(prixT)
            #print(prixtt)
                    
            produitlist.append(nom_affiche)
            quantitelist.append(quant)
            prixlist.append(prixprod)
            numero_produit.append(parametre)
                    
            #print(produitlist)
            #print(quantitelist)
            #print(prixlist)
            #print(numero_produit)
            quantite.delete(0,END)              
                    
            tupl=listboxaffiche.get('@1,0', END)
            #print (tupl, tupl[0])
            liste=list(tupl) 
            divis = liste[0].split(" ")
            #print(divis, divis[0], divis[1], divis[2]  )
            
            
        def ecrire():
                        
            #numfacture=num_facture.get()
                        
        
                        
            #root.destroy()
                        
                        
            windowFact = Toplevel(rootMenu)
            windowFact.title("Gestion des ventes")
            windowFact.geometry("1300x600+0+0")
            windowFact.config(bg="#255000255")
            windowFact.minsize(width=1300, height=600)
                        
            
            MainFrame = Frame(windowFact, bg="#049232247")
            MainFrame.pack()
                            
            TitFrame = Frame(MainFrame, bg="#049232247",padx=54, pady=8, relief=RIDGE)
            TitFrame.pack(side=TOP)
            labelTitre = Label(TitFrame, font=('arial', 35, 'bold'),text="Gestion des Ventes", bg="#049232247",fg="gold")
            labelTitre.grid()
                        
            #==================================frames===============================
                        
            DataFrame = Frame(MainFrame, relief = GROOVE, bd=1, width=1300, height=600, padx=20, pady=20, bg="blue")
            DataFrame.pack(side=BOTTOM)
                        
            titre = Label(DataFrame, font=('arial', 30, 'bold'), bg="blue",fg="gold", text="Informations générale sur la vente").pack()
            scrolf = Scrollbar(DataFrame, orient=VERTICAL)
            txtarea = Text(DataFrame, yscrollcommand=scrolf.set)
            scrolf.pack(side=RIGHT)
            scrolf.config(command=txtarea.yview())
            txtarea.pack()
            #boutonExt = Button(windowFact, text="Imprimer", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
            #boutonExt.place(x=500,y=505)
                        
            #Contenir.tes()
                               
                               
                                
                        
            #txtarea.insert(END, "\t\t\t\t\t     "+date.today().isoformat()
            txtarea.insert(END, "\t\t\t\t\t     "+time.strftime("%A %d %B %Y %H:%M:%S"))
            txtarea.insert(END, "\n\n\t\t\t\tBoutique Numero 5698")
            #txtarea.insert(END, "\nFacture numéro : "+numfacture)
            txtarea.insert(END, "\n\n================================================================================")
                        
            txtarea.insert(END, "\n\nNumero du client : 000+str(numclient))")
            txtarea.insert(END, "\nNom du client : +nomclient)")
            txtarea.insert(END, "\nNumero du caissiers : 000+str(numcaissier))")
            #txtarea.insert(END, "\nNom du caissiers : "+nomcaissier)
            txtarea.insert(END, "\n\n================================================================================")
            txtarea.insert(END, "\n\nRef")
            txtarea.insert(END, "\tProduits")
            txtarea.insert(END, "\t\t\tQuantité")
            txtarea.insert(END, "\t\t\tPrix Unitaire \n")
            i = 0
            while(i<len(produitlist)):
                            
                txtarea.insert(END, "\n"+str(numero_produit[i]))
                txtarea.insert(END, "\t"+produitlist[i])
                txtarea.insert(END, "\t\t\t"+str(quantitelist[i]))
                txtarea.insert(END, "\t\t\t"+str(prixlist[i]))
                i+=1
                                    
                                    
                                  
                txtarea.insert(END, "\n\n\n\tPrix total : "+str(prixtt)+" FCFA"  )
                        
            windowFact.mainloop() 
        
                    
                    
              
            
            
            
            
                    
                    
        
        if __name__ == "__main__":
            root = Toplevel(rootMenu)
            root.title("¤¤¤¤¤¤¤¤¤¤¤¤• PRODUITS ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
            root.geometry("930x700+140+40")
            root.config(bg="black")
            root.resizable(False,False)
            
            canphoto=Canvas(root, width=200,height=200)
        
            imgp= PhotoImage(file="images/nature.png") 
            canphoto.create_image(2,2, anchor=NW, image=imgp, tags="img_fond")
            canphoto.place(x=660,y=20)
            
            labelquantite = Label(root, font=('arial', 12, 'bold'), text="Quantité: ", fg="gold", bg="black")
            labelquantite .place(x=680,y=250)
            quantite = Entry(root, font=('arial', 14, 'bold'), width=3,bd=5)
            quantite.place(x=790,y=245)
        
            labelquantite = Label(root, font=('arial', 7, 'bold'), text="Indiquer \nla quantité achetée \navant de valider ", fg="green", bg="black")
            labelquantite .place(x=710,y=280)
            
            photoValider = PhotoImage(file = "images/valider1.png")
            boutonValider = Button(root,image=photoValider, border = 0, bg="black",activebackground="black",cursor="hand2" ,command=valider)
            boutonValider.place(x=700,y=320)
            
            photoconclure = PhotoImage(file = "images/conclure3.png")
            boutonconclure = Button(root,image=photoconclure, border = 0, bg="black",activebackground="black",cursor="hand2" ,command=ecrire )
            boutonconclure.place(x=700,y=600)
                
            frameValide=Frame(root,width=240,height=240,bd=-3)
            frameValide.place(x=620,y=390)
            
            scrollbar=Scrollbar(frameValide)
            scrollbar.pack(side=RIGHT, fill=Y)
            
            photoachat = PhotoImage(file = "images/listeachat1.png")
            label= Label(frameValide,image=photoachat)
            label.pack()
            
            listboxaffiche=Listbox(frameValide,width=40,height=11,yscrollcommand=scrollbar.set)
            listboxaffiche.pack(side=LEFT, fill = BOTH)
            scrollbar.config(command=listboxaffiche.yview)
        
            
            interface = Main_frame(fenetre_principale=root)
            interface.mainloop()
    
    
    fen_client = Toplevel(rootMenu)
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
    
    fen_client.mainloop()

 
    
rootMenu = Tk()
menubar = Menu(rootMenu)

ventemenu = Menu(menubar, tearoff=0)
ventemenu.add_command(label="Nouvelle", command=nouvelleVente)
ventemenu.add_command(label="Statistiques", command=donothing)
ventemenu.add_command(label="Exit", command=rootMenu.destroy)
ventemenu.add_separator()
menubar.add_cascade(label="Ventes", menu=ventemenu)


clientmenu = Menu(menubar, tearoff=0)
clientmenu.add_command(label="Nouveau", command=donothing)
clientmenu.add_command(label="Afficher", command=donothing)
clientmenu.add_command(label="Exit", command=rootMenu.destroy)
clientmenu.add_separator()
menubar.add_cascade(label="Clients", menu=clientmenu)


produitmenu = Menu(menubar, tearoff=0)
produitmenu.add_command(label="Nouveau", command=donothing)
produitmenu.add_command(label="Lister", command=donothing)
produitmenu.add_command(label="Exit", command=rootMenu.destroy)
produitmenu.add_separator()
menubar.add_cascade(label="Produits", menu=produitmenu)


factmenu = Menu(menubar, tearoff=0)
factmenu.add_command(label="Nouvelle", command=donothing)
factmenu.add_command(label="Lister", command=donothing)
factmenu.add_command(label="Exit", command=rootMenu.destroy)
factmenu.add_separator()
menubar.add_cascade(label="Factures", menu=factmenu)



rootMenu.config(menu=menubar)
rootMenu.mainloop()


