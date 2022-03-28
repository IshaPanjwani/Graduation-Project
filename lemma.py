from collections import Counter

from nltk.corpus import stopwords
from nltk.corpus import wordnet
from NewStemmer import  NewStemmer

# To get words in dictionary with their parts of speech
from nltk.stem import WordNetLemmatizer
# lemmatizes word based on it's parts of speech

from nltk.tokenize import word_tokenize


stop_words = set(stopwords.words('english'))

list = open("book.txt").read()
tokens = word_tokenize(list)

punctuations = "'*?:!., ;"
for word in tokens:
    if word in punctuations:
        tokens.remove(word)

wordsList = [w for w in tokens if not w in stop_words]


def get_pos(word):
    w_synsets = wordnet.synsets(word)

    print(w_synsets)
    pos_counts = Counter()
    pos_counts["n"] = len([item for item in w_synsets if item.pos() == "n"])
    pos_counts["v"] = len([item for item in w_synsets if item.pos() == "v"])
    pos_counts["a"] = len([item for item in w_synsets if item.pos() == "a"])
    pos_counts["r"] = len([item for item in w_synsets if item.pos() == "r"])

    most_common_pos_list = pos_counts.most_common(3)
    return most_common_pos_list[0][0]
    # first indexer for getting the top POS from list,  second indexer for getting POS from tuple(POS: count)

# words = ["running", "lying", "cars", "m!spleed"]
#wnl = WordNetLemmatizer()
ns = NewStemmer()
for word in wordsList:
    print(word, end="\t")
    # print(get_pos(word),end="\t")
    # print(wnl.lemmatize(word, get_pos(word)))  # printing without newline character
    print(ns.stem(word))