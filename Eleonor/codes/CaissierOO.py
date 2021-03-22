#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 03:39:17 2021

@author: toor
"""


from tkinter import *
import psycopg2
import tkinter.messagebox




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
    
class Caissiers(Tk):
    

    def __init__(self):

        
        Tk.__init__(self)
        self.title("Gestion des ventes")
        self.geometry("910x534+140+80")
        self.resizable(False,False)
        
        
        can=Canvas(self, width=1300,heigh=600)
        self.img=PhotoImage(file="images/noirx.png")
        can.create_image(0,0,anchor=NW,image=self.img)
        can.place(x=-5,y=-1.7)
        
        #=======================zone du titre de la fenêtre===============
        
        labelNom0 = Label(can, font=('harrington', 40, 'bold'), text="INSCRIPTIONS ", fg="aqua", bg="black")
        labelNom0.place(x=60,y=2)
        
        #=======================zone de saisi d'information================
        
                
        labelNum = Label(can, font=('harrington', 20, 'bold'), text="N°: ", fg="gold", bg="black")
        labelNum.place(x=5,y=120)
        self.entryNum = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
        self.entryNum.place(x=200, y=120)
        
        labelNom = Label(can, font=('harrington', 20, 'bold'), text="Nom: ", fg="gold", bg="black")
        labelNom.place(x=5,y=160)
        self.entryNom = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
        self.entryNom.place(x=200, y=160)
                
        labelTel = Label(can, font=('harrington', 20, 'bold'), text="Téléphone  : ", fg="gold", bg="black")
        labelTel.place(x=5,y=200)
        self.entryTel = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
        self.entryTel.place(x=200,y=200)
                
        labelAdresse = Label(can, font=('harrington', 20, 'bold'), text="Adresse: ", fg="gold", bg="black")
        labelAdresse.place(x=5,y=240)
        self.entryAdresse = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
        self.entryAdresse.place(x=200,y=240)
        
        labelnum_boutique = Label(can, font=('harrington', 20, 'bold'), text="id Boutique : ", fg="gold", bg="black")
        labelnum_boutique.place(x=5,y=280)
        self.entryNum_boutique = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
        self.entryNum_boutique.place(x=200,y=280)
        
        labelpassword = Label(can, font=('harrington', 20, 'bold'), text="Mot de passe : ", fg="gold", bg="black")
        labelpassword.place(x=5,y=320)
        self.entryPassword = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
        self.entryPassword.place(x=200,y=320)
        
        
        #===============zone d'affichage des informations relatives aux inscriptions==========
        
        frameinfo=Frame(self,width=40,height=300,bd=0,cursor="hand2")
        frameinfo.place(x=555,y=118)
        
        labframeinfo = LabelFrame(frameinfo, bd=0, width=20, height=40)
        labframeinfo.pack(side=RIGHT)
        
        
        #=============================Scollbar et  Listbox================
        
        scrollbar=Scrollbar(labframeinfo)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.photocaissiers = PhotoImage(file = "images/listcaissiers1.png")
        label= Label(labframeinfo,image=self.photocaissiers)
        label.pack()   
        self.caissierslist = Listbox(labframeinfo, width=30, height=10, font=('harrington', 12, 'bold'), yscrollcommand = scrollbar.set)
        self.caissierslist.bind('<<ListboxSelect>>', self.recuperer)
        self.caissierslist.pack(side=LEFT, fill = BOTH)
        scrollbar.config(command = self.caissierslist.yview)
        
        #=====================Zone des bouttons=====================
        self.photoajouter = PhotoImage(file = "images/ajouter.png") 
        boutonAdd = Button(self, image=self.photoajouter, border = 0, bg="black",activebackground="black",cursor="hand2", command = self.ajouter)
        boutonAdd.place(x=60,y=410)
        ajouter_label = Label(self, text= "Ajouter ", bg="black", fg="gold")
        ajouter_label.place(x=90, y=510)
        
        self.photoafficher = PhotoImage(file = "images/autreafficher3.png")        
        boutonDsp = Button(self,image=self.photoafficher, border = 0, bg="black",activebackground="black",cursor="hand2", command = self.afficher)
        boutonDsp.place(x=180,y=410)
        afficher_label = Label(self, text= "Afficher ", bg="black", fg="gold")
        afficher_label.place(x=200, y=510)
        
        self.photoconnexion2 = PhotoImage(file = "images/seconnecterr2.png")
        boutonExt = Button(self,image=self.photoconnexion2, border = 0, bg="black",activebackground="black",cursor="hand2" , command = self.connecter)
        boutonExt.place(x=300,y=410)
        afficher_label = Label(self, text= "se connecter ", bg="black", fg="gold")
        afficher_label.place(x=340, y=510)
        
     #=====================FRAMES=============================
        
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Gestion des Caissiers", "confirmer la fermeture?")
        if iExit > 0:
            self.destroy()
            return
    
        
    
    def connecter(self):
        self.destroy()
        import connexion
        
    
    
    def ajouter(self):
        num = self.entryNum.get()
        nom = self.entryNom.get()
        adresse = self.entryAdresse.get()
        tel = self.entryTel.get()
        num_boutique=self.entryNum_boutique.get()
        password = self.entryPassword.get()
        if num =='' or nom =='' or adresse =='' or tel=='' or num_boutique=='' or password=='':
            messagebox.showerror("Gestion des Caissiers", "Tous les champs ne sont pas renseignés.")
        else:
            con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
            cursor = con.cursor()
            cursor.execute("INSERT INTO Caissiers (num_caissier, nom_caissier,adresse_caissier,tel_caissier, num_boutique,password) VALUES ('"+num +"','" + nom + "','" + adresse +"','" + tel + "','"+num_boutique+"','" + password + "')")
            con.commit()
            con.close()
            
            self.afficher()
            
            
    def afficher(self):
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Caissiers")
        rows = cursor.fetchall()
        con.close()
        self.caissierslist.delete(0, END)
        for row in rows:
            self.caissierslist.insert(END, row)
        self.caissierslist.select_set(0)
        
        
    def recuperer(self, event):
        line = self.caissierslist.curselection()[0]
        global item
        item = self.caissierslist.get(line)
        global selected_item
        
        selected_item = StringVar()
        selected_item.set(item)
        
        self.entryNum.delete(0, END)
        self.entryNum.insert(END, item[0])
        self.entryNom.delete(0, END)
        self.entryNom.insert(END, item[1])
        self.entryTel.delete(0,END)
        self.entryTel.insert(END, item[2])
        self.entryAdresse.delete(0, END)
        self.entryAdresse.insert(END, item[3])
        self.entryPassword.delete(0, END)
        self.entryPassword.insert(END, item[4])
        self.entryNum_boutique.delete(0, END)
        self.entryNum_boutique.insert(END, item[5])
        
        
#=======================Création de la fenêtre de travail========================

o=Caissiers()
o.mainloop()



