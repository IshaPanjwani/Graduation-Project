import re
import nltk 
from nltk.corpus import words
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import lovins
from porter import PorterStemmer
import porter2
from paicehusk import PaiceHuskStemmer
from paicehusk import defaultrules
from pos_lemma import MyLemmatizer
from version7 import mystemmer
from NewStemmer import NewStemmer


object = defaultrules
lovins_list = []
ps = PorterStemmer()
ns = NewStemmer()
porter_list = []
phs = PaiceHuskStemmer(object)
phs_list = []
porter2_list = []
mystemmer_list = []
lemma = []
NewStemmer = []

def final():
    root = tk.Tk()
    root.title("Stemming Techniques")
    T = tk.Text(root, height=200, width=200)
    T.pack()

           
    data = {'original': [], 'lovins': [], 'porter': [], 'Paice/Husk': [], 'porter2': [], 'lemma': [], 'mystemmer': [], 'NewStemmer' : []}
        
    #For Filedialog
    filename = filedialog.askopenfilename(initialdir = "C:/Users/User/Stemmer", title = "Select file" , filetypes = [("text files","*.txt")])
    #print(filename) 
    os.path.split(filename)
    #print(os.path.split(filename)[1])
    orgname = os.path.split(filename)[1]

    stop_word = open("stopword.txt", "r").read().split()
    list = open("%s" %orgname).read() 
    output = open("stem output.txt", "w+")
        
    list = re.sub('[^ a-zA-Z]', ' ', list).split()
        
    for i in range(0,len(stop_word)):
        stop_word[i] = stop_word[i].replace("'"," ")

    filtered_list = []

    for i in list:
        if i.lower() not in stop_word:
            filtered_list.append(i)

    data['original'] = filtered_list
    for i in filtered_list:
        if i in words.words():
            for i in filtered_list:
                data['lovins'].append(lovins.stem(i))
                data['porter'].append(ps.stem(i))
                data['Paice/Husk'].append(phs.stem(i.lower()))
                data['porter2'].append(porter2.stem(i))
                data['NewStemmer'].append(ns.stem(i))
                    
            lemma_obj = MyLemmatizer()
            data['lemma'] = lemma_obj.lemma(filtered_list)
            data['mystemmer'] = mystemmer.stem(filtered_list)
                
            rs = pd.DataFrame(data, columns=['original', 'mystemmer','NewStemmer'])
            pd.set_option("display.max_rows", None) 
            rs.to_string(output)
            #print(rs)

            #TO_print_in_GUI
            root.configure(bg='red')
            T.insert(tk.END,rs)
            
            tk.mainloop()
        
        else:
            raise ValueError('Word is not true')

            #rs.to_excel(r'output.xlsx', header=['original', 'lovins', 'Paice/Husk', 'porter', 'porter2', 'mystemmer', 'lemma','NewStemmer'])



