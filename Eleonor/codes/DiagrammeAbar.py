# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:41:34 2021

@author: Paradoxe
"""

import tkinter.messagebox
from tkinter import *
import psycopg2

import matplotlib.pyplot as plt
import matplotlib
import random as rd

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
        

con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
cursor = con.cursor()
cursor.execute("select (sum(contenir.quantite) * sum(contenir.prix_unitaire)) as prix, factures.date from contenir inner join factures on (contenir.num_facture = factures.num_facture) where contenir.num_produit=13 group by date")
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

plt.savefig("images/grapheproduit13.png")
