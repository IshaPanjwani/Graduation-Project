#for selcting option b/w file & word
import os
import version5
from version5 import final
from version5_data import get
import version5_data
import tkinter as tk
from tkinter import * 


root = tk.Tk()
#root['bg'] = '#0059b3'
image1=tk.PhotoImage(file="download.pgm")
Label1=Label(root,image=image1)
Label1.pack()
global user_ip
v = tk.IntVar()
root.title("STEMMING TECHNIQUES")

tk.Label(root,text="Choose one option",justify = tk.LEFT,padx = 20).pack()
rf=tk.Radiobutton(root, 
              text="FILE",
              padx = 20, 
              variable=v, 
              value=1,command=final).pack(anchor=tk.CENTER)
rf=tk.Radiobutton(root, 
              text="WORD",
              padx = 20, 
              variable=v, 
              value=2,command=get).pack(anchor=tk.CENTER)


tk.mainloop()
