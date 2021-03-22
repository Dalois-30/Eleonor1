#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 08:51:36 2021

@author: toor
"""

tab = [1,2,0,5,8]
print(tab, type(tab))
def defilement(x):
    for i in x:
        print(i)
defilement(tab)


class test():
    def __init__(self, a, b, c, e):

        i=0
        while i<len(self.nom):
            print("l'etudiant "+str(a[i])+" "+str(b[i])+" est agée de "+str(c[i])+" et habite "+str(e[i]))
            i+=1
            
a = ["aime"," paule","george"]
b = ["saoul", "gregoire", "tamo"]
c = [14, 19, 8]
d = ["Maroua", "Dla", "ynd"]

obj = test(a, b, c, d)
#obj.ecrire()