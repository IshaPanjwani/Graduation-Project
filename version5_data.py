import re
import nltk 
from nltk.corpus import words
import pandas as pd
from version8 import mystemmer
from NewStemmer import NewStemmer
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def get():
    
    #root=tk.Tk()
    temp=simpledialog.askstring("Input","enter string")
    var5_data(temp)
   
                         

def var5_data(user_ip):
    
    #for stemming
    ns = NewStemmer()        
    data = {'original': [], 'mystemmer': [], 'NewStemmer' : []}
    output = open("stem output.txt", "w+")

    #str1= re.compile("[a-zA-Z]")
    if user_ip.isalpha() == False:
        
       # raise ValueError("INPUT SHOULD BE STRING")
        messagebox.showerror("ERROR","INVALID STRING")
    else:
        if user_ip in words.words():
            raise ValueError('Word is not true')
        #Calling_Functions
        data['original'] = user_ip
        data['NewStemmer'].append(ns.stem(user_ip))
        data['mystemmer'] = mystemmer.stem(user_ip)

        #COnvert_rs_into_tabular_form
        rs = pd.DataFrame(data, columns=['original','mystemmer','NewStemmer'])
        rs.to_string(output)
        #print(rs)

        root=tk.Tk()
        T = tk.Text(root, height=200, width=200)
        T.pack()
        T.insert(tk.END,rs)
        tk.mainloop()






