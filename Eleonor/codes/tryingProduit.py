# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:27:02 2021

@author: Paradoxe
"""
from tkinter import *
 
root = Tk()
root.config(bg="red")
root.geometry("910x534+100+40")
can=Canvas(root, width=1300,heigh=600)
root.img=PhotoImage(file="noirx.png")
can.create_image(0,0,anchor=NW,image=root.img)
can.place(x=-5,y=-1.7)
canvas = Canvas(can,bg="blue")

scroll_y = Scrollbar(can, orient="vertical", command=canvas.yview)

frame = Frame(canvas)
# group of widgets
for i in range(20):
    Label(frame, text='label %i' % i).pack()
# put the frame in the canvas
canvas.create_window(100, 100, anchor='nw', window=frame)
# make sure everything is displayed before configuring the scrollregion
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'), 
                 yscrollcommand=scroll_y.set)
                 
canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')

root.mainloop()