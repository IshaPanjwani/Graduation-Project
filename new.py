import re

import pandas as pd
from nltk.corpus import stopwords

from version6 import mystemmer


file = open("dataset-CalheirosMoroRita-2017.csv", "r")
list = file.read()

list = re.sub('[^ a-zA-Z]', '', list).split()

filtered_list = []
stop_word = set(stopwords.words('english'))
for i in list:
    if i.lower() not in stop_word:
        filtered_list.append(i)
data = {}
data['original'] = filtered_list
data['mystemmer'] = mystemmer.stem(filtered_list)

rs = pd.DataFrame(data, columns=['original', 'mystemmer'])
print(rs)
