import mysql
from mysql.connector import Error
from version7 import mystemmer
class NewStemmer:
    def isCons(self, letter):
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            return False
        else:
            return True

    def isConsonant(self, word, i):
        letter = word[i]
        if self.isCons(letter):
            if letter == 'y' and self.isCons(word[i - 1]):
                return False
            else:
                return True
        else:
            return False

    def isVowel(self, word, i):
        return not (self.isConsonant(word, i))

    # *S
    def endsWith(self, stem, letter):
        if stem.endswith(letter):
            return True
        else:
            return False

    # *v*
    def containsVowel(self, stem):
        for i in stem:
            if not self.isCons(i):
                return True
        return False

    # *d
    def doubleCons(self, stem):
        if len(stem) >= 2:
            if self.isConsonant(stem, -1) and self.isConsonant(stem, -2):
                return True
            else:
                return False
        else:
            return False

    def sameDoubleCons(self, stem):
        if len(stem) >= 2:
            if self.isConsonant(stem, -1) == self.isConsonant(stem, -2):
                return True
            else:
                return False
        else:
            return False

    def doubleVowel(self, stem):
        if len(stem) >= 3:
            if self.isVowel(stem, -2) and self.isVowel(stem, -3):
                return True
            else:
                return False
        else:
            return False

    def getForm(self, word):
        form = []
        formStr = ''
        for i in range(len(word)):
            if self.isConsonant(word, i):
                if i != 0:
                    prev = form[-1]
                    if prev != 'C':
                        form.append('C')
                else:
                    form.append('C')
            else:
                if i != 0:
                    prev = form[-1]
                    if prev != 'V':
                        form.append('V')
                else:
                    form.append('V')
        for j in form:
            formStr += j
        return formStr

    def getM(self, word):
        form = self.getForm(word)
        m = form.count('VC')
        return m

    # *o
    def cvc(self, word):
        if len(word) >= 3:
            f = -3
            s = -2
            t = -1
            third = word[t]
            if self.isConsonant(word, f) and self.isVowel(word, s) and self.isConsonant(word, t):
                if third != 'w' and third != 'x' and third != 'y':
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def replace(self, orig, rem, rep):
        result = orig.rfind(rem)
        base = orig[:result]
        replaced = base + rep
        return replaced

    def replaceM0(self, orig, rem,rep):
        result = orig.rfind(rem)
        base = orig[:result]
        if self.getM(base) > 0:
            if base[-2] == 'a':
                replaced = base + 'e'
            else:
                replaced = base + rep
            return replaced
        else:
            return orig

    def replaceM1(self, orig, rem, rep):
        result = orig.rfind(rem)
        base = orig[:result]
        if self.getM(base) > 1:
            replaced = base + rep
            replaced = self.fix_ending(replaced)
            return replaced
        else:
            return orig

    def replaceM2(self, orig,rem,rep):
        result = orig.rfind(rem)
        base = orig[:result]
        if self.getM(base) > 2:
            replaced = base + rep
            replaced = self.fix_ending(replaced)
            return replaced
        else:
            return orig

    def replaceM3(self, word,rem):
        result = word.rfind(rem)
        base = word[:result]
        if base.endswith('s') | base.endswith('tr') | base.endswith('n'):
            if self.getM(base) > 1:
                word = base + 'y'
        if base.endswith('c'):
            if self.getM(base) > 1:
                word = base + 'e'
        if base.endswith('s'):
            if self.getM(base) > 3:
                word = base + ''

        if base.endswith('t'):
            if self.getM(base) > 1:
                word = base + ''
        return word

    def fix_ending(self,word):
        _doubles = frozenset(("dd", "gg", "ll", "mm", "nn", "pp", "rr", "ss", "tt","zz"))
        if word[-2:] in _doubles:
            word = word[:-1]
        return word

    def step1(self, word):
        if word.endswith('sses'):
            word = self.replace(word, 'sses', 'ss')
        elif word.endswith('ss'):
            word = self.replace(word, 'ss', 'ss')
        elif word.endswith('ies'):
            word = self.replace(word, 'ies', 'y')
        elif word.endswith('ves'):
            word = self.replace(word, 'ves', 'f')
        elif word.endswith('es'):
            base = self.replace(word, 'es', '')
            if base.endswith('o') | base.endswith('ch') | base.endswith('sh') | base.endswith('th') | base.endswith('ss') | base.endswith('gh') | base.endswith('z'):
                word = base
            else:
                word = base + 'e'
        elif word.endswith('s'):
            word = self.replace(word, 's', '')
        else:
            pass
        return word

    def step2(self, word):
        flag = False
        if word.endswith('eed'):
            result = word.rfind('eed')
            base = word[:result]
            if self.getM(base) > 0:
                word = base
                word += 'ee'
        elif word.endswith('ed'):
            result = word.rfind('ed')
            base = word[:result]
            if self.sameDoubleCons(base) | base.endswith('h') | base.endswith('w')| base.endswith('r') | base.endswith('y') | base.endswith('n')  | self.doubleVowel(base):
                word = base
            elif not self.containsVowel(base):
                word = base + 'eed'
            else:
                word = base + 'e'
            if len(word) > 2:
                word = self.fix_ending(word)
            return word

        elif word.endswith('id' ):
            result = word.rfind('id')
            base = word[:result]
            if base.endswith('a'):
                if len(base) > 1:
                    word = base + 'y'
            return word
            flag = True

        elif word.endswith('ne'):
            result = word.rfind('ined')
            base = word[:result]
            if base.endswith('o'):
                if len(base > 1):
                    word = base + ''
            return word
            flag = True


        elif word.endswith('ing'):
            result = word.rfind('ing')
            base = word[:result]
            if self.containsVowel(base):
                word = base
            flag = True

        if flag:
            if word.endswith('at') or word.endswith('bl') or word.endswith('iz') or word.endswith('az') or word.endswith('s') or word.endswith('v'):
                word += 'e'
            # elif self.doubleCons(word) and not self.endsWith(word, 'l') and not self.endsWith(word,'s') and not self.endsWith(word, 'z'):
            #     word = word[:-1]
            elif len(word) > 2:
                word = self.fix_ending(word)
            elif self.getM(word) == 1 and self.cvc(word):
                word += 'e'
            else:
                pass
        else:
            pass


        return word

    def step3(self, word):
        if word.endswith('ational'):
            word = self.replaceM0(word, 'ational', 'ate')
        elif word.endswith('tional'):
            word = self.replaceM0(word, 'tional', 'tion')
        elif word.endswith('enci'):
            word = self.replaceM0(word, 'enci', 'ence')
        elif word.endswith('anci'):
            word = self.replaceM0(word, 'anci', 'ance')
        elif word.endswith('izer'):
            word = self.replaceM0(word, 'izer', 'ize')
        elif word.endswith('abli'):
            word = self.replaceM0(word, 'abli', 'able')
        elif word.endswith('alli'):
            word = self.replaceM0(word, 'alli', 'al')
        elif word.endswith('entli'):
            word = self.replaceM0(word, 'entli', 'ent')
        elif word.endswith('eli'):
            word = self.replaceM0(word, 'eli', 'e')
        elif word.endswith('ousli'):
            word = self.replaceM0(word, 'ousli', 'ous')
        elif word.endswith('ization'):
            word = self.replaceM0(word, 'ization', 'ize')
        elif word.endswith('ation'):
            word = self.replaceM0(word, 'ation', 'ate')
        elif word.endswith('ator'):
            word = self.replaceM0(word, 'ator', 'ate')
        elif word.endswith('alism'):
            word = self.replaceM0(word, 'alism', 'al')
        elif word.endswith('iveness'):
            word = self.replaceM0(word, 'iveness', 'ive')
        elif word.endswith('fulness'):
            word = self.replaceM0(word, 'fulness', 'ful')
        elif word.endswith('ousness'):
            word = self.replaceM0(word, 'ousness', 'ous')
        elif word.endswith('aliti'):
            word = self.replaceM0(word, 'aliti', 'al')
        elif word.endswith('iviti'):
            word = self.replaceM0(word, 'iviti', 'ive')
        elif word.endswith('biliti'):
            word = self.replaceM0(word, 'biliti', 'ble')
        return word

    def step4(self, word):
        if word.endswith('icate'):
            word = self.replaceM0(word, 'icate', 'ic')
        elif word.endswith('ative'):
            word = self.replaceM0(word, 'ative', '')
        elif word.endswith('alize'):
            word = self.replaceM0(word, 'alize', 'al')
        elif word.endswith('iciti'):
            word = self.replaceM0(word, 'iciti', 'ic')
        elif word.endswith('ful'):
            word = self.replaceM0(word, 'ful', '')
        elif word.endswith('ness'):
            word = self.replaceM0(word, 'ness', '')
        return word

    def step5(self, word):
        if word.endswith('ial'):
            word = self.replaceM3(word, 'ial')
        elif word.endswith('al'):
            word = self.replaceM1(word, 'al', '')
        elif word.endswith('ance'):
            word = self.replaceM2(word, 'ance', '')
        elif word.endswith('ence'):
            word = self.replaceM1(word, 'ence', '')
        elif word.endswith('ier'):
            word = self.replace(word, 'ier', 'y')
        elif word.endswith('iest'):
            word = self.replace(word, 'iest', 'y')
        elif word.endswith('er'):
            word = self.replaceM2(word, 'er', '')
        elif word.endswith('est'):
            word = self.replaceM0(word, 'est', '')
        elif word.endswith('lly'):
            word = self.replaceM1(word, 'lly', 'l')
        elif word.endswith('ly'):
            word = self.replace(word, 'ly', '')
        elif word.endswith('ity'):
            word = self.replaceM2(word, 'ity', '')
        elif word.endswith('ic'):
            word = self.replaceM1(word, 'ic', '')
        elif word.endswith('able'):
            word = self.replaceM1(word, 'able', '')
        elif word.endswith('ible'):
            word = self.replaceM1(word, 'ible', '')
        elif word.endswith('ant'):
            word = self.replaceM1(word, 'ant', '')
        elif word.endswith('ement'):
            word = self.replaceM1(word, 'ement', '')
        elif word.endswith('ment'):
            word = self.replaceM1(word, 'ment', '')
        elif word.endswith('ent'):
            word = self.replaceM1(word, 'ent', '')
        elif word.endswith('ou'):
            word = self.replaceM1(word, 'ou', '')
        elif word.endswith('ism'):
            word = self.replaceM1(word, 'ism', '')
        elif word.endswith('ate'):
            word = self.replaceM1(word, 'ate', '')
        elif word.endswith('iti'):
            word = self.replaceM1(word, 'iti', '')
        elif word.endswith('ous'):
            word = self.replaceM1(word, 'ous', '')
        elif word.endswith('ive'):
            word = self.replaceM1(word, 'ive', '')
        elif word.endswith('ize'):
            word = self.replaceM1(word, 'ize', '')
        elif word.endswith('ion'):
            result = word.rfind('ion')
            base = word[:result]
            if self.getM(base) > 1 and (self.endsWith(base, 's') or self.endsWith(base, 't')):
                word = base
            word = self.replaceM1(word, '', '')
        return word

    def step6(self, word):
        if word.endswith('en'):
            word = word[:-1]
        if word.endswith('e'):
            base = word[:-1]
            if base.endswith('am'):
                word = base[:-2] + 'ome'
            elif base.endswith('ad'):
                word = base[:-2] + 'ake'
            elif base.endswith('ve'):
                base = base[:-2]
                if word.endswith('w') | word.endswith('h'):
                    word = base + 'eave'
                else:
                    word = base + 'ive'
        return word

    def step7(self, word):
        if word.endswith('i'):
            base = word[:-1]
            if  self.isCons(base[-1]):
                word = base + 'y'
        return word

    def stem(self, word):
        a=1
        dic = open('eng-dictionary.txt').read().split()
        if word in dic:
            return word
        elif a==1:
            list = open("book.txt").read()
            set= []
            try:
                
                for data in list:
                    data = data.strip()
                    query = "select root from exception where word = '%s' " % (data)
                    cursor.execute(query)
                    row = cursor.fetchall()
                    if (row):
                        for i in row[0]:
                            set.append(i)
                    else:
                        set.append(data)
            except Error as e:
                print(e)
            finally:
                cursor.close()
                conn.close()
        else:
           
            word = self.step1(word)
            word = self.step2(word)
            word = self.step3(word)
            word = self.step4(word)
            word = self.step5(word)
            word = self.step6(word)
            word = self.step7(word)
            return word