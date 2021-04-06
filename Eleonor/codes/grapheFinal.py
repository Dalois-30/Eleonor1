#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 00:20:34 2021

@author: toor
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:48:22 2021

@author: Paradoxe
"""

from tkinter import *
import psycopg2
import tkinter.messagebox
import time
import matplotlib.pyplot as plt
import numpy as np 
    
    
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
cursor.execute("SELECT (date, sum(prix_total)) FROM factures GROUP BY date ORDER BY date")
rows = cursor.fetchall()
print(rows)
con.close()

xs=[]
ys=[]
for row in rows:
    lst = row[0]
    print(lst)
    x, y = lst.split(',')

    x=x[len(x)-8:len(x)]
    y=y[0:len(y)-1]
    y=int(y)
    
    xs.append(x)
    ys.append(y)
print(xs)
print(ys)


#col=[f"jour{i}" for i in range(1,len(rows)+1) ]
#print(col)

taillex=len(rows)
plt.figure(figsize=(taillex,5))
plt.plot(xs,ys)
plt.show()#pour fficher dans autre chose que jupiter

#root.mainloop()
