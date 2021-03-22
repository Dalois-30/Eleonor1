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
        obj = Produits(self)
        

        
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
        self = Toplevel(root)
        
        self.title("Gestion des ventes")
        self.geometry("910x534+100+40")
        self.resizable(False,False)
        
        
        caninCl=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        caninCl.create_image(0,0,anchor=NW,image=self.img)
        caninCl.config(bg="black")
        
        caninCl.place(x=-2,y=-1.7)
        
        self.photoprecedent = PhotoImage(file="images/precedent.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="black",activebackground="black",cursor="hand2" )
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
        self = Toplevel(root)

        self.title("¤¤¤¤¤¤¤¤¤¤¤¤• PRODUITS ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
        self.geometry("910x534+100+40")
        self.resizable(False,False)
        canfResp=Canvas(self, width=915,height=540)
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
        
        self=Toplevel(root)
        
        self.title("                                                                                     Eleonor")
        self.geometry("910x534+180+80")
        self.config(bg="black")
        self.resizable(False, False)
        
        canfAcc=Canvas(self, width=915,height=540)
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
        
        
        
        
class Facturation(Tk):
    
    global rouge
    global vert 
    global bleu
    def __init__(self,root):
        self=Toplevel(root)
        
        
        self.title("Gestion des ventes")
        self.geometry("1010x642+140+20")
                
                
        canfond=Canvas(self, width=1025,height=655)
        self.img=PhotoImage(file="images/imeleobfact.png")
        canfond.create_image(0,0,anchor=NW,image=self.img)
        canfond.config(bg="black")
        canfond.place(x=-2,y=-1.7)
        
                
                
                                                
                                                
                                                #==================================frames===============================
                                                            
        DataFrame = Frame(self, bd=-1, width=10, height=50, bg="black")
        DataFrame.place(x=160,y=140)
                
        titre = Label(canfond, font=('arial', 30, 'bold'), bg="black",fg="gold", text="Informations finales de facture")
        titre.place(x=210,y=40)
        scrolf = Scrollbar(DataFrame, orient=VERTICAL)
        txtarea = Text(DataFrame, yscrollcommand=scrolf.set)
        scrolf.pack(side=RIGHT,fill=Y)
        scrolf.config(command=txtarea.yview())
        txtarea.pack()
                                             
        txtarea.insert(END, "\t\t\t\t\t     "+time.strftime("%A %d %B %Y %H:%M:%S"))
        txtarea.insert(END, "\n\n\t\t\t\tBoutique Numero 5698")
        txtarea.insert(END, "\n\n================================================================================")            
        txtarea.insert(END, "\n\nNumero du client : 000+str(numclient))")
        txtarea.insert(END, "\nNom du client : +nomclient)")
        txtarea.insert(END, "\nNumero du caissiers : 000+str(numcaissier))")
        txtarea.insert(END, "\n\n================================================================================")
        txtarea.insert(END, "\n\nRef")
        txtarea.insert(END, "\tProduits")
        txtarea.insert(END, "\t\t\tQuantité")
        txtarea.insert(END, "\t\t\tPrix Unitaire \n")
        i = 0
        """while(i<len(produitlist)):
                    
                    txtarea.insert(END, "\n"+str(numero_produit[i]))
                    txtarea.insert(END, "\t"+produitlist[i])
                    txtarea.insert(END, "\t\t\t"+str(quantitelist[i]))
                    txtarea.insert(END, "\t\t\t"+str(prixlist[i]))
                    i+=1
                    
                    
                    
                    txtarea.insert(END, "\n\n\n\tPrix total : "+str(prixtt)+" FCFA"  )"""
                    
                    
        canfond.config(bg="#"+rouge+""+vert+""+bleu+"")
        titre.config(bg="#"+rouge+""+vert+""+bleu+"")
        
        
        
 
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

   


        #print(parametre)       
class Produits(Tk):
    
    global rouge
    global vert 
    global bleu
    def __init__(self,root):
        self=Toplevel(root)
        """def __init__(self):
            Tk.__init__(self)"""
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
        fen=Facturation(obj,532,39,"kevin",29,produitlist,numero_produit,quantitelist,prixlist,prixtt)
     
           
        
        
        
        


    
    

    
    
    
obj=Parametres()

obj.mainloop()






