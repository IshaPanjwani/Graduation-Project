import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


class MyLemmatizer:
    def get_wordnet_pos(self, word):
        """Map POS tag to first character lemmatize() accepts"""
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)

    def lemma(self, list):
        lemmatizer = WordNetLemmatizer()
        lemma = []
        for word in list:
            lemma.append(lemmatizer.lemmatize(word, self.get_wordnet_pos(word)))
        return lemma





        #
        # # 3. Lemmatize a Sentence with the appropriate POS tag
        # # sentence = "The striped bats are hanging on their feet for best"
        # list = open("file.txt").read()
        #
        # list = re.sub('[^ a-zA-Z]', '', list).split()
        #
        # filtered_list = []
        # stop_word = set(stopwords.words('english'))
        #
        # for i in list:
        # if i.lower() not in stop_word:
        #         filtered_list.append(i)