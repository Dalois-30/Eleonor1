#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:31:21 2021

@author: toor
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:40:34 2021

@author: Paradoxe
"""

from tkinter import *
from datetime import date
import time


rouge="000"
vert="000"
bleu="000"

class Parametres(Tk):
    def __init__(self):
        
        global varRouge
        global varVert
        global varBleu
        global canParam
        global boutonch
        global titreParam
        global labelRouge
        global labelVert
        global labelBleu
        global caninCl
        
        
        Tk.__init__(self)
        
        
        self.geometry("910x534+100+40")
        canParam=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canParam.create_image(0,0,anchor=NW,image=self.img)
        canParam.config(bg="black")
        canParam.place(x=-2,y=-1.7)
        
        
        
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
        
        
        
        
        self.imch=PhotoImage(file="images/boutChang1.png")
        boutonch= Button(self, image=self.imch, bd=-2,bg="black", activebackground="black",command=self.changement)
        boutonch.place(x=360, y=350)
        
        self.imch1=PhotoImage(file="images/boutChang1.png")
        bouton= Button(self, image=self.imch1, bd=-2,bg="black", activebackground="black",command=self.appel)
        bouton.place(x=520, y=350)
        
        self.photosuivant = PhotoImage(file="images/btsuivCl.png")
        btsuivCl = Button(self,image=self.photosuivant, bg="black",bd=-2,activebackground="black",cursor="hand2",command=self.appel2)
        btsuivCl.place(x=400,y=440)
        
        self.photosuivant1 = PhotoImage(file="images/btsuivCl.png")
        btsuivAcc = Button(self,image=self.photosuivant1, bg="black",bd=-2,activebackground="black",cursor="hand2",command=self.appel3)
        btsuivAcc.place(x=500,y=440)
        
        self.photosuivant2 = PhotoImage(file="images/btsuivCl.png")
        btsuivAcc = Button(self,image=self.photosuivant2, bg="black",bd=-2,activebackground="black",cursor="hand2",command=self.appel4)
        btsuivAcc.place(x=500,y=40)
        
    def appel(self):
        obj = InfoClient(self)
        
    def appel2(self):
        obj = Responsable(self)
    
        
    def appel3(self):
        obj = Accueil(self)
        
    def appel4(self):
        from FactureOO import Facture
        obj = Facture(self,1,70,"claude",89,produit,numero,qt,prixl,59350)
        obj.canfond.config(bg="#"+rouge+""+vert+""+bleu+"")

        
    def changement(self):
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
        boutonch.config(bd=-2,bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        titreParam.config(bd=-2,bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        labelRouge.config(bg="#"+rouge+""+vert+""+bleu+"")
        labelVert.config(bg="#"+rouge+""+vert+""+bleu+"")
        labelBleu.config(bg="#"+rouge+""+vert+""+bleu+"")
       
        
        
        
        return rouge,vert,bleu
    
class InfoClient(Tk):
    
    global rouge
    global vert 
    global bleu
    
    
    def __init__(self, root):
        self.fen = Toplevel(root)
        
        self.fen.title("Gestion des ventes")
        self.fen.geometry("910x534+100+40")
        self.fen.resizable(False,False)
        
        
        caninCl=Canvas(self.fen, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        caninCl.create_image(0,0,anchor=NW,image=self.img)
        caninCl.config(bg="black")
        
        caninCl.place(x=-2,y=-1.7)
        
        self.photoprecedent = PhotoImage(file="images/precedent.png")
        btprec = Button(self.fen,image=self.photoprecedent, bd=-5, bg="black",activebackground="black",cursor="hand2" )
        btprec.place(x=10,y=10)
        
        infoCl = Label(caninCl, font=('harrington', 35, 'bold'),bd=0, text="Informations générales", fg="aqua", bg="black")
        infoCl.place(x=210,y=52)
        
        
        nomCl = Label(self.fen, font=('harrington', 20, 'bold'), text="Noms:", padx=1,fg="gold", bg="black")
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
                
        print(rouge)
        
        caninCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        btprec.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        infoCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        nomCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        prenomCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        telCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        adrCl.config(bg="#"+rouge+""+vert+""+bleu+"")
        #btsuivCl.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
class Responsable(Tk):
    
    global rouge
    global vert 
    global bleu
    def __init__(self,root):
        self.fen = Toplevel(root)

        self.fen.title("¤¤¤¤¤¤¤¤¤¤¤¤• PRODUITS ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
        self.fen.geometry("910x534+100+40")
        self.fen.resizable(False,False)
        canfResp=Canvas(self.fen, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canfResp.create_image(0,0,anchor=NW,image=self.img)
        canfResp.place(x=-2,y=-1.7)
        
        self.imgrespovente = PhotoImage(file="images/respovente1.png")
        boutonrespoventes = Button(canfResp, image=self.imgrespovente, cursor="hand2",bg="black",activebackground = "black",border=0)
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
        
        respovente_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        comptable_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        respoappro_label.config(bg="#"+rouge+""+vert+""+bleu+"")        
        respoRh_label.config(bg="#"+rouge+""+vert+""+bleu+"")        
        respofiscal_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        boutonrespoventes.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutoncomptable.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonrespoappro.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonrespofiscal.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonrespoRh.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
        
class Accueil(Tk):
    
    global rouge
    global vert 
    global bleu
    def __init__(self,root):
        
        self.fen=Toplevel(root)
        
        self.fen.title("                                                                                     Eleonor")
        self.fen.geometry("910x534+180+80")
        self.fen.config(bg="black")
        self.fen.resizable(False, False)
        
        canfAcc=Canvas(self.fen, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canfAcc.create_image(0,0,anchor=NW,image=self.img)
        canfAcc.config(bg="black")
        canfAcc.place(x=-1.2,y=-1.7)
        
        
        self.imgclient = PhotoImage(file="images/client.png")
        boutonClient = Button(canfAcc, image=self.imgclient, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonClient.place(x=85, y=190)
        client_label = Label(canfAcc, text= "Client ", font=("arial", 10,"bold"), bg="black",fg="gold")
        client_label.place(x=127, y=350)
        
        self.imgcaissier = PhotoImage(file="images/caissier.png")
        boutonCaissier = Button(canfAcc, image=self.imgcaissier, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonCaissier.place(x=242, y=190)
        caissier_label = Label(canfAcc, text= "Caissier ", font=("arial", 10,"bold"), bg="black",fg="gold")
        caissier_label.place(x=280, y=350)
        
        self.imgrespo = PhotoImage(file="images/responsable.png")
        boutonRespo = Button(canfAcc, image=self.imgrespo, cursor="hand2",bg="black",activebackground = "black",border=0, command=lambda:responsable())
        boutonRespo.place(x=400, y=190)
        respo_label = Label(canfAcc, text= "Responsables ", font=("arial", 10,"bold"), bg="black",fg="gold")
        respo_label.place(x=425, y=350)
        
        self.imgParam = PhotoImage(file="images/parametres.png")
        boutonParam = Button(canfAcc, image=self.imgParam, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonParam.place(x=560, y=190)
        param_label = Label(canfAcc, text= "Paramètres ", font=("arial", 10,"bold"), bg="black",fg="gold")
        param_label.place(x=590, y=350)
        
        self.imgoperateur = PhotoImage(file="images/operateur.png")
        boutonOperateur = Button(canfAcc, image=self.imgoperateur, cursor="hand2",bg="black",activebackground = "black",border=0)
        boutonOperateur.place(x=720, y=190)
        operateur_label = Label(canfAcc, text= "Operateur ", font=("arial", 10,"bold"), bg="black",fg="gold")
        operateur_label.place(x=760, y=350)
        
        canfAcc.config(bg="#"+rouge+""+vert+""+bleu+"")
        client_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        caissier_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        respo_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        param_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        operateur_label.config(bg="#"+rouge+""+vert+""+bleu+"")
        
        boutonClient.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonCaissier.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonRespo.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonParam.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonOperateur.config(bg="#"+rouge+""+vert+""+bleu+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
        
produit=["tomate","pomme","orange","jus", "banane","coco", "igname", "avocat","ananas", "peche"]
numero = [8,9,3,9,9,2,7,65,1,25]
qt=[10,15,7,8,3,9,41,20,12,50]
prixl=[800,900,750,950,1590,2350,1450,9500,3500,7525]         
        
class Facturation(Tk):
    
    global rouge
    global vert 
    global bleu
    def __init__(self, root, numBoutique, numclient, nomclient, numcaissier, produitlist, numero_produit, quantitelist, prixlist, prixtt):
        self.fen=Toplevel(root)
        
        
        self.fen.title("Gestion des ventes")
        self.fen.geometry("1010x642+140+20")
                
                
        canfond=Canvas(self.fen, width=1025,height=655)
        self.img=PhotoImage(file="images/imeleobfact.png")
        canfond.create_image(0,0,anchor=NW,image=self.img)
        canfond.config(bg="black")
        canfond.place(x=-2,y=-1.7)
        
                
                
                                                
                                                
                                                #==================================frames===============================
                                                            
        DataFrame = Frame(self.fen, bd=-1, width=10, height=50, bg="black")
        DataFrame.place(x=160,y=140)
                
        titre = Label(canfond, font=('arial', 30, 'bold'), bg="black",fg="gold", text="Informations finales de facture")
        titre.place(x=210,y=40)
        scrolf = Scrollbar(DataFrame, orient=VERTICAL)
        self.txtarea = Text(DataFrame, yscrollcommand=scrolf.set)
        scrolf.pack(side=RIGHT,fill=Y)
        scrolf.config(command=self.txtarea.yview())
        self.txtarea.pack(side=BOTTOM, fil=BOTH)
                                     
    
        self.txtarea.insert(END, "\t\t\t\t\t     "+time.strftime("%A %d %B %Y %H:%M:%S"))
        self.txtarea.insert(END, "\n\n\t\t\t\tBoutique Numero" + str(numBoutique))
        self.txtarea.insert(END, "\n\n================================================================================")            
        self.txtarea.insert(END, "\n\nNumero du client : 000"+str(numclient))
        self.txtarea.insert(END, "\nNom du client : "+str(nomclient))
        self.txtarea.insert(END, "\nNumero du caissiers : 000"+str(numcaissier))
        self.txtarea.insert(END, "\n\n================================================================================")
        self.txtarea.insert(END, "\n\nRef")
        self.txtarea.insert(END, "\tProduits")
        self.txtarea.insert(END, "\t\t\tQuantité")
        self.txtarea.insert(END, "\t\t\tPrix Unitaire \n")
        i = 0
        while(i<len(produitlist)):
           
            self.txtarea.insert(END, "\n"+str(numero_produit[i]))
            self.txtarea.insert(END, "\t"+produitlist[i])
            self.txtarea.insert(END, "\t\t\t"+str(quantitelist[i]))
            self.txtarea.insert(END, "\t\t\t"+str(prixlist[i]))
            i+=1
            
            
            
        self.txtarea.insert(END, "\n\n\n\tPrix total : "+str(prixtt)+" FCFA"  )
        data = self.txtarea.get(self)
        print(data)                    
        canfond.config(bg="#"+rouge+""+vert+""+bleu+"")
        titre.config(bg="#"+rouge+""+vert+""+bleu+"")
        
        
        
        
        
        
        
        


    
    

    
    
    
obj=Parametres()

obj.mainloop()






