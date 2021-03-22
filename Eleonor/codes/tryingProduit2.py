# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:27:02 2021

@author: Paradoxe
"""
from tkinter import *
 
root = Tk()
root.config(bg="red")
root.geometry("1000x600+100+40")
can=Canvas(root, width=900,heigh=600)
can.config(bg="black")
can.place(x=95,y=20)
canvas = Canvas(can,bg="blue",width=540,height=540)#c'est ici que tu peux modifier la taille du tableau de produit

scroll_y = Scrollbar(can, orient="vertical", command=canvas.yview)

frame = Frame(canvas,width=540,height=540,bg="aqua")
# labels presents dans le frame scrollable
for i in range(200):
    Label(frame, text='label %i' % i).pack()
# insersion du frame dans le canvas
canvas.create_window(100, 100, anchor='nw', window=frame)
# on s'assure que tous sera affiché avant de définir la scrollregion
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all')#c'est cette commande qui s'assure de la presence, 
                 ,yscrollcommand=scroll_y.set)
                 
canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')

root.mainloop()