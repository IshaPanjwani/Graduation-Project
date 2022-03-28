import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

list = open("file.txt").read()
tokens = word_tokenize(list)
lem = WordNetLemmatizer()

punctuations = "'*?:!.,;"
for word in tokens:
    if word in punctuations:
        tokens.remove(word)

wordsList = [w for w in tokens if not w in stop_words]
tagged = nltk.pos_tag(wordsList)
for word in tagged:
    print(word[0] + ":", word[1], end='\t')
    print()
    # print(lem.lemmatize(word[0],word[1]))






#
# tokens_pos = pos_tag(list)
# print(tokens_pos)
