# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 06:26:28 2021

@author: Paradoxe
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
produitlist = []
quantitelist = []
prixlist = []
    
global numero 
    
class Contenir():
    #cette classe servira a gerer les achats d'un client
    def __init__(self,num_caissier,  num_produit,nom_produit,quantite,prix,
                 nom_client, tel_client,tel_caissier):
        
        self.num_caissier=num_caissier.get()
        
        
        
        
        self.quantite=quantite.get()
     
        
        self.nom_client=nom_client.get()
        
        
        self.tel_client=tel_client.get()
        self.tel_caissier=tel_caissier.get() 
        
        
    def ecrire():
        
        #numfacture=num_facture.get()
        
        
        nomclient=nom_client.get()
        telclient=Tel_client.get()
        numcaissier=num_caissier.get()
        
        
        if nomclient=="" or numcaissier=="":
            messagebox.showerror("Facture", "Toutes les informations du client ne sont pas renseignés.")
        else:
            con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
            cursor = con.cursor()
            cursor.execute("INSERT INTO Clients (num_client, nom_client, tel_client) VALUES (nextval('client_seq'),'" + nomclient + "', '" + telclient +"')")
            con.commit()
            
            cursor.execute("SELECT num_client FROM Clients WHERE nom_client = '%s' AND tel_client = '%s'" %(nomclient, telclient))
            rows = cursor.fetchall()
            numclient=rows[0][0]
            print(numclient, type(numclient))
            cursor.execute("INSERT INTO Factures (num_facture, prix_total, date, num_client, num_caissier) VALUES (nextval('fact_seq'),'%s', '%s','%s','%s')"%(prixtt,date.today().isoformat(),numclient,numcaissier))
            con.commit()
            
            con.close()
        
        root.destroy()
        #txtarea.insert(END, "\t\t\t\t\t     "+date.today().isoformat()
        txtarea.insert(END, "\t\t\t\t\t     "+time.strftime("%A %d %B %Y %H:%M:%S"))
        txtarea.insert(END, "\n\n\t\t\t\tBoutique Numero 5698")
        #txtarea.insert(END, "\nFacture numéro : "+numfacture)
        txtarea.insert(END, "\n\n================================================================================")
        
        txtarea.insert(END, "\n\nNumero du client : 000"+str(numclient))
        txtarea.insert(END, "\nNom du client : "+nomclient)
        txtarea.insert(END, "\nNumero du caissiers : 000"+str(numcaissier))
        #txtarea.insert(END, "\nNom du caissiers : "+nomcaissier)
        txtarea.insert(END, "\n\n================================================================================")
        txtarea.insert(END, "\n\nProduits")
        txtarea.insert(END, "\t\t\t\tQuantité")
        txtarea.insert(END, "\t\t\t\tPrix Unitaire \n")
        i = 0
        while(i<len(produitlist)):
            
               txtarea.insert(END, "\n"+produitlist[i])
               txtarea.insert(END, "\t\t\t\t"+str(quantitelist[i]))
               txtarea.insert(END, "\t\t\t\t"+str(prixlist[i]))
               i+=1
                    
                    
                  
        txtarea.insert(END, "\n\n\n\tPrix total : "+str(prixtt)+" FCFA"  )
    
    def annuler():
        
        
        num_produit.delete(0,END)
        quantite.delete(0,END)
        listboxNumProd.delete(0,END)
        listboxNomProd.delete(0,END)
        listboxPrixProd.delete(0,END)
        
        
    def valider():
        """canphoto.create_image(2,2, anchor=NW, image=imgp )
        canphoto.place(x=60,y=380)"""
        global prixtt
        global produitlist
        global quantitelist
        global prixlist
        
        nomclient=nom_client.get()
        telclient=Tel_client.get()
        numcaissier=num_caissier.get()
        #nomcaissier=nom_caissier.get()
        
        numprod=num_produit.get()
        quant= int(quantite.get())
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT  nom_produit, prix_produit FROM Produits WHERE num_produit=%s" %(numprod))
        rows = cursor.fetchall()
        print(rows)
        #con.close()
        nom_affiche=str(rows[0][0])
        prixprod = rows[0][1]
        cursor.execute("SELECT prix_produit FROM produits WHERE num_produit=%s" %(numprod))
        rowprix = cursor.fetchone()
        print(rowprix[0])
        
        prixU=rowprix[0]
        prixT=prixU*quant
        prixtt+=prixT
        
        
        prix_affiche=str(rows[0][1])
        prix_nom_affiche=str(quant)+" "+nom_affiche+" pour "+prix_affiche+" FCFA l'unité"
        listboxaffiche.insert(END, prix_nom_affiche)
        prix = quant*int(prix_affiche)
        print (prix)
        print(prixT)
        print(prixtt)
        
        produitlist.append(nom_affiche)
        quantitelist.append(quant)
        prixlist.append(prixprod)
        
        print(produitlist)
        print(quantitelist)
        print(prixlist)
        
        num_produit.delete(0,END)
        quantite.delete(0,END)
        listboxNumProd.delete(0,END)
        listboxNomProd.delete(0,END)
        listboxPrixProd.delete(0,END)
        
        
      
        
        
        
        
        """if nomclient=="" or numclient=="":
            messagebox.showerror("Facture", "Toutes les informations du client ne sont pas renseignés.")
        else:
            con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
            cursor = con.cursor()
            cursor.execute("INSERT INTO Clients (num_client, nom_client, tel_client) VALUES (nextval('client_seq'),'" + nomclient + "', '" + telclient +"')")
            con.commit()
            
        cursor.execute("SELECT num_client FROM Clients WHERE nom_client = '%s' AND tel_client = '%s'" %(nomclient, telclient))
        rows1 = cursor.fetchall()
        numclient=rows1[0][0]
        cursor.execute("INSERT INTO Factures (num_facture, prix_total, date, num_client, num_caissier) VALUES (nextval('fact_seq'),'"+prixTotal+"', '"+date.today().isoformat()+"','"+num_client+"','"+num_caissier+"')")
        
        cursor.execute("SELECT currval('fact_seq')")
        row2=cursor.fetchall()
        numfacture=row2[0][0]
        con.close()
    
        #root.destroy()
        #txtarea.insert(END, "\t\t\t\t\t     "+date.today().isoformat()
        txtarea.insert(END, "\t\t\t\t\t     "+time.strftime("%A %d %B %Y %H:%M:%S"))
        txtarea.insert(END, "\n\n\t\t\t\tBoutique Numero 5698")
        txtarea.insert(END, "\nFacture numéro : "+numfacture)
        txtarea.insert(END, "\n\n================================================================================")
        
        txtarea.insert(END, "\n\nNumero du client : 000%s"(numclient))
        txtarea.insert(END, "\nNom du client : "+nomclient)
        txtarea.insert(END, "\nNumero du caissiers : 000"+numcaissier)
        txtarea.insert(END, "\nNom du caissiers : "+nomcaissier)
        txtarea.insert(END, "\n\n================================================================================")
        txtarea.insert(END, "\n\nProduits")
        txtarea.insert(END, "\t\t\t\tQuantité")
        txtarea.insert(END, "\t\t\t\tPrix ")
        txtarea.insert(END, "\n\n")
        txtarea.insert(END, "\t\t\t\t")
        txtarea.insert(END, "\t\t\t\t")
        
        
        txtarea.insert(END, "\n\n\n\tPrix total : "+prixtt  )"""
    
        
            
    def conclure():
        valeurs=listboxaffiche.get('@1,0',END)    
        print(valeur[0], type(valeur[0]))
        
    
    def tes():
        global canphoto,imgp,a
    def fond():
        global imgp,a

        a=int(num_produit.get())
        imgp=PhotoImage(file="images/prod"+str(a)+".png")
        canphoto.itemconfigure("img_fond",image=imgp)

        
        listboxNumProd.delete(0,END)
        listboxNomProd.delete(0,END)
        listboxPrixProd.delete(0,END)
        
            
        num = num_produit.get()
        numProduit = int(num)
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT num_produit, nom_produit, prix_produit FROM Produits WHERE num_produit=%s" %(numProduit))
        #cursor.execute("SELECT num_produits, nom_produit, prix_produit FROM Produits WHERE num_produits=1")
        rows = cursor.fetchall()
        numProd = rows[0][0]
        #print(numProd)
        nomProd = rows[0][1]
        #print(nomProd)
        prixProd = rows[0][2]
        #print(prixProd)
        numero = numProd
        listboxNumProd.insert(END,numProd)
        listboxNomProd.insert(END, nomProd)
        listboxPrixProd.insert(END, prixProd)
        
    
        

        
        
        

 
        
        
 
    def creation():
        import fenetre




#=======================Création de la fenêtre de travail========================


root = Tk()
root.title("Gestion des ventes")
root.geometry("1195x600+100+40")
root.resizable(False,False)


can=Canvas(root, width=1300,height=600)
img=PhotoImage(file="images/noirx3.png")
can.create_image(0,0,anchor=NW,image=img)
can.place(x=-5,y=-1.7)

#=======================zone du titre de la fenêtre===============

labelNom = Label(can, font=('harrington', 40, 'bold'), text="FACTURATIONS ", fg="aqua", bg="black")
labelNom.place(x=10,y=2)

#=======================informations sur la facture=========================
labelnom_client = Label(root, font=('arial', 12, 'bold'), text="Nom Client : ", fg="gold", bg="black")
labelnom_client.place(x=60,y=80)
nom_client = Entry(root, font=('arial', 14, 'bold'), width=25)
nom_client.place(x=210,y=80)

labelTel_client = Label(root, font=('arial', 12, 'bold'), text="Téléphone Client: ", fg="gold", bg="black")
labelTel_client.place(x=60,y=120)
Tel_client = Entry(root, font=('arial', 14, 'bold'), width=10)
Tel_client.place(x=210,y=120)

labelnum_caissier = Label(root, font=('arial', 12, 'bold'), text="N° Caissier: ", fg="gold", bg="black")
labelnum_caissier.place(x=60,y=160)
num_caissier = Entry(root, font=('arial', 14, 'bold'), width=10)
num_caissier.place(x=210,y=160)

labelnum_produit = Label(root, font=('arial', 12, 'bold'), text="Ref produit: ", fg="gold", bg="black")
labelnum_produit.place(x=60,y=200)
num_produit = Entry(root, font=('arial', 14, 'bold'), width=10)
num_produit.place(x=210,y=200)

#=================bouton sous info préliminaires ==============================
photoGénerer = PhotoImage(file = "images/générer1.png")
boutonGénerer = Button(root,image=photoGénerer, border = 0, bg="black",activebackground="black",cursor="hand2" , command = Contenir.fond)
boutonGénerer.place(x=160,y=240)

#===============================canvas d'information après génération================

canphoto=Canvas(root, width=200,height=200)
#a=1
imgp= PhotoImage(file="images/nature.png") 
canphoto.create_image(2,2, anchor=NW, image=imgp, tags="img_fond")
canphoto.place(x=60,y=380)

#====================listbox===========================
#canafficher=Canvas(root,width=260,height=250,bg="black",bd=-2)
#canafficher.place(x=280,y=380)

con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
cursor=con.cursor()
#cursor.execute("SELECT nom_produit, prix_produit    ")
labelnum_produitaff = Label(root, font=('arial', 12, 'bold'), text="N° Produit: ", fg="gold", bg="black")
labelnum_produitaff.place(x=300,y=380)
listboxNumProd=Listbox(root,width=22, height=1,bd=0,cursor="hand2") #,yscrollcommand=scrollbar.set)
a='bonjour'
#listboxNumProd.insert(END,a)
listboxNumProd.place(x=410,y=383)

labelnom_produitaff = Label(root, font=('arial', 12, 'bold'), text="Nom Produit: ", fg="gold", bg="black")
labelnom_produitaff.place(x=300,y=420)
listboxNomProd=Listbox(root,width=22, height=1,bd=0,cursor="hand2") #,yscrollcommand=scrollbar.set)
a=5
#listboxNomProd.insert(1,a)
listboxNomProd.place(x=410,y=423)

labelprix_produitaff = Label(root, font=('arial', 12, 'bold'), text="Prix produit: ", fg="gold", bg="black")
labelprix_produitaff.place(x=300,y=460)
listboxPrixProd=Listbox(root,width=22, height=1,bd=0,cursor="hand2") #,yscrollcommand=scrollbar.set)
a=5

#listboxPriProd.insert(1,a)
listboxPrixProd.place(x=410,y=463)

#========================Entry de la quantité====================
labelquantite = Label(root, font=('arial', 12, 'bold'), text="Quantité: ", fg="gold", bg="black")
labelquantite .place(x=300,y=500)
quantite = Entry(root, font=('arial', 14, 'bold'), width=3,bd=5)
quantite.place(x=380,y=500)

labelquantite = Label(root, font=('arial', 7, 'bold'), text="Indiquer \nla quantité achetée \navant de valider ", fg="green", bg="black")
labelquantite .place(x=435,y=500)


#=================bouton sous info générées ==============================
photoValider = PhotoImage(file = "images/valider1.png")
boutonValider = Button(root,image=photoValider, border = 0, bg="black",activebackground="black",cursor="hand2" , command = Contenir.valider)
boutonValider.place(x=420,y=540)

photoAnnuler = PhotoImage(file = "images/annuler1.png")
boutonAnnuler = Button(root,image=photoAnnuler, border = 0, bg="black",activebackground="black",cursor="hand2" , command = Contenir.annuler)
boutonAnnuler.place(x=280,y=540)

#============================zone d'affichage des produit validés================

frameValide=Frame(root,width=240,height=240,bd=-3)
frameValide.place(x=600,y=388)

scrollbar=Scrollbar(frameValide)
scrollbar.pack(side=RIGHT, fill=Y)

photoachat = PhotoImage(file = "images/listeachat1.png")
label= Label(frameValide,image=photoachat)
label.pack()

listboxaffiche=Listbox(frameValide,width=40,height=11,yscrollcommand=scrollbar.set)
listboxaffiche.pack(side=LEFT, fill = BOTH)
scrollbar.config(command=listboxaffiche.yview)


photoconclure = PhotoImage(file = "images/conclure3.png")
boutonconclure = Button(root,image=photoconclure, border = 0, bg="black",activebackground="black",cursor="hand2" , command = Contenir.ecrire)
boutonconclure.place(x=1022,y=520)


window = Tk()
window.title("Gestion des ventes")
window.geometry("1300x600+0+0")
window.config(bg="#255000255")
window.minsize(width=1300, height=600)


MainFrame = Frame(window, bg="#049232247")
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
#boutonExt = Button(window, text="Imprimer", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
#boutonExt.place(x=500,y=505)

Contenir.tes()
       
window.mainloop()        
 

root.mainloop()
