# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 09:30:23 2021

@author: Paradoxe
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
    
class Caissiers:
    """classe pour gerer les personnes enregistrées dans notre base de donnée"""
    def __init__(self, num, nom,tel, adresse, num_boutique, password):

        self.num = entryNum.get()
        self.nom = entryNom.get()
        self.tel = entryTel.get()
        self.adresse = entryAdresse.get()
        self.num_boutique = entryNum_boutique.get()
        self.password = entryPassword.get()
        
     #=====================FRAMES=============================
        
    def iExit():
        iExit = tkinter.messagebox.askyesno("Gestion des Caissiers", "confirmer la fermeture?")
        if iExit > 0:
            root.destroy()
            return
    
    def connecter():
        root.destroy()
        import connexion
        
    
    
    def ajouter():
        num = entryNum.get()
        nom = entryNom.get()
        adresse = entryAdresse.get()
        tel = entryTel.get()
        num_boutique=entryNum_boutique.get()
        password = entryPassword.get()
        if num =='' or nom =='' or adresse =='' or tel=='' or num_boutique=='' or password=='':
            messagebox.showerror("Gestion des Caissiers", "Tous les champs ne sont pas renseignés.")
        else:
            con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
            cursor = con.cursor()
            cursor.execute("INSERT INTO Caissiers (num_caissier, nom_caissier,adresse_caissier,tel_caissier, num_boutique,password) VALUES ('"+num +"','" + nom + "','" + adresse +"','" + tel + "','"+num_boutique+"','" + password + "')")
            con.commit()
            con.close()
            
            Caissiers.afficher()
            
            
    def afficher():
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Caissiers")
        rows = cursor.fetchall()
        con.close()
        caissierslist.delete(0, END)
        for row in rows:
            caissierslist.insert(END, row)
        caissierslist.select_set(0)
        
        
    def recuperer(event):
        line = caissierslist.curselection()[0]
        global item
        item = caissierslist.get(line)
        global selected_item
        
        selected_item = StringVar()
        selected_item.set(item)
        
        entryNum.delete(0, END)
        entryNum.insert(END, item[1])
        entryNom.delete(0, END)
        entryNom.insert(END, item[0])
        entryTel.delete(0,END)
        entryTel.insert(END, item[3])
        entryAdresse.delete(0, END)
        entryAdresse.insert(END, item[2])
        entryPassword.delete(0, END)
        entryPassword.insert(END, item[4])
        entryNum_boutique.delete(0, END)
        entryNum_boutique.insert(END, item[5])
        
        
#=======================Création de la fenêtre de travail========================


root = Tk()
root.title("Gestion des ventes")
root.geometry("910x534+140+80")
root.resizable(False,False)


can=Canvas(root, width=1300,heigh=600)
img=PhotoImage(file="images/noirx.png")
can.create_image(0,0,anchor=NW,image=img)
can.place(x=-5,y=-1.7)

#=======================zone du titre de la fenêtre===============

labelNom = Label(can, font=('harrington', 40, 'bold'), text="INSCRIPTIONS ", fg="aqua", bg="black")
labelNom.place(x=60,y=2)

#=======================zone de saisi d'information================

        
labelNom = Label(can, font=('harrington', 20, 'bold'), text="N°: ", fg="gold", bg="black")
labelNom.place(x=5,y=120)
entryNom = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
entryNom.place(x=200, y=120)

labelNum = Label(can, font=('harrington', 20, 'bold'), text="Nom: ", fg="gold", bg="black")
labelNum.place(x=5,y=160)
entryNum = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
entryNum.place(x=200, y=160)
        
labelAdresse = Label(can, font=('harrington', 20, 'bold'), text="Téléphone  : ", fg="gold", bg="black")
labelAdresse.place(x=5,y=200)
entryAdresse = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
entryAdresse.place(x=200,y=200)
        
labelTel = Label(can, font=('harrington', 20, 'bold'), text="Adresse: ", fg="gold", bg="black")
labelTel.place(x=5,y=240)
entryTel = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
entryTel.place(x=200,y=240)

labelnum_boutique = Label(can, font=('harrington', 20, 'bold'), text="id Boutique : ", fg="gold", bg="black")
labelnum_boutique.place(x=5,y=280)
entryNum_boutique = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
entryNum_boutique.place(x=200,y=280)

labelpassword = Label(can, font=('harrington', 20, 'bold'), text="Mot de passe : ", fg="gold", bg="black")
labelpassword.place(x=5,y=320)
entryPassword = Entry(can, font=('harrington', 20, 'bold'), width=20,bd=2)
entryPassword.place(x=200,y=320)


#===============zone d'affichage des informations relatives aux inscriptions==========

frameinfo=Frame(root,width=40,height=300,bd=0,cursor="hand2")
frameinfo.place(x=555,y=118)

labframeinfo = LabelFrame(frameinfo, bd=0, width=20, height=40)
labframeinfo.pack(side=RIGHT)


#=============================Scollbar et  Listbox================

scrollbar=Scrollbar(labframeinfo)
scrollbar.pack(side=RIGHT, fill=Y)

photocaissiers = PhotoImage(file = "images/listcaissiers1.png")
label= Label(labframeinfo,image=photocaissiers)
label.pack()   
caissierslist = Listbox(labframeinfo, width=30, height=10, font=('harrington', 12, 'bold'), yscrollcommand = scrollbar.set)
caissierslist.bind('<<ListboxSelect>>', Caissiers.recuperer)
caissierslist.pack(side=LEFT, fill = BOTH)
scrollbar.config(command = caissierslist.yview)

#=====================Zone des bouttons=====================
photoajouter = PhotoImage(file = "images/ajouter.png") 
boutonAdd = Button(root, image=photoajouter, border = 0, bg="black",activebackground="black",cursor="hand2", command = Caissiers.ajouter)
boutonAdd.place(x=60,y=410)
ajouter_label = Label(root, text= "Ajouter ", bg="black", fg="gold")
ajouter_label.place(x=90, y=510)

photoafficher = PhotoImage(file = "images/autreafficher3.png")        
boutonDsp = Button(root,image=photoafficher, border = 0, bg="black",activebackground="black",cursor="hand2", command = Caissiers.afficher)
boutonDsp.place(x=180,y=410)
afficher_label = Label(root, text= "Afficher ", bg="black", fg="gold")
afficher_label.place(x=200, y=510)

photoconnexion2 = PhotoImage(file = "images/seconnecterr2.png")
boutonExt = Button(root,image=photoconnexion2, border = 0, bg="black",activebackground="black",cursor="hand2" , command = Caissiers.connecter)
boutonExt.place(x=300,y=410)
afficher_label = Label(root, text= "se connecter ", bg="black", fg="gold")
afficher_label.place(x=340, y=510)

root.mainloop()
