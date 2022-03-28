import re

import pandas as pd
import tkinter as tk
import lovins
from porter import PorterStemmer
import porter2
from paicehusk import PaiceHuskStemmer
from paicehusk import defaultrules
from pos_lemma import MyLemmatizer
from version7 import mystemmer
from NewStemmer import NewStemmer

root = tk.Tk()
T = tk.Text(root, height=200, width=200)
T.pack()

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
        
        
data = {'original': [], 'lovins': [], 'porter': [], 'Paice/Husk': [], 'porter2': [], 'lemma': [], 'mystemmer': [], 'NewStemmer' : []}
        
        
stop_word = open("stopword.txt", "r").read().split()
list = open("book.txt").read()
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
    data['lovins'].append(lovins.stem(i))
    data['porter'].append(ps.stem(i))
    data['Paice/Husk'].append(phs.stem(i.lower()))
    data['porter2'].append(porter2.stem(i))
    data['NewStemmer'].append(ns.stem(i))
            
lemma_obj = MyLemmatizer()
data['lemma'] = lemma_obj.lemma(filtered_list)
data['mystemmer'] = mystemmer.stem(filtered_list)
        
rs = pd.DataFrame(data, columns=['original', 'lovins', 'porter', 'Paice/Husk', 'porter2','lemma',  'mystemmer','NewStemmer'])
rs.to_string(output)
print(rs)

#TO_print_in_GUI
T.insert(tk.END,rs)
tk.mainloop()

#rs.to_excel(r'output.xlsx', header=['original', 'lovins', 'Paice/Husk', 'porter', 'porter2', 'mystemmer', 'lemma','NewStemmer'])