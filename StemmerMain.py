import re
import pandas as pd
from NewStemmer import NewStemmer


list = open("dataset-CalheirosMoroRita-2017.csv", "r").read()
# list = "experienced friends spend"
stop_word = open("stopword.txt", "r").read().split()
#list = open("book.txt", "r").read()
output = open("New Stemmer Output.txt", "w")

list = re.sub('[^ a-zA-Z]', '', list).split()

filtered_list = []
ns = NewStemmer()
for i in range(0,len(stop_word)):
    stop_word[i] = stop_word[i].replace("'","")

for i in list:
    if i.lower() not in stop_word:
        filtered_list.append(i)
data = {}
data = {'original': [], 'NewStemmer' : []}
NewStemmer = []
data['original'] = filtered_list


for i in filtered_list:
    data['NewStemmer'].append(ns.stem(i))

rs = pd.DataFrame(data, columns=['original', 'NewStemmer'])
rs.to_string(output)
print(rs)

rs.to_excel(r'New Stemmer Output.xlsx', header=['original','NewStemmer'])
