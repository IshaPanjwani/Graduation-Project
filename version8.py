import mysql
from mysql.connector import Error

class mystemmer:
    def stem(data):
        set = []
        try:
            conn = mysql.connector.connect(host='localhost', database='stemmer', user='root', password='')
            cursor = conn.cursor()
            data = data.strip()
            qurey = "select singular from plural where plural = '%s' " % (data)
            cursor.execute(qurey)
            row = cursor.fetchall()
            if (row):
                for i in row[0]:
                    set.append(i)
            else:
                qurey = "select root from dictionary where past = '%s' OR past_participle = '%s' OR present = '%s' OR continues = '%s' " % (
                data, data, data, data)
                cursor.execute(qurey)
                row = cursor.fetchall()
                if (row):
                    for i in row[0]:
                        set.append(i)
                else:
                    qurey = "select headword from lemmatization where verb = '%s' OR noun = '%s' OR adjective = '%s' OR adverb = '%s' " % (
                    data, data, data, data)
                    cursor.execute(qurey)
                    row = cursor.fetchall()
                    if (row):
                        for i in row[0]:
                            set.append(i)
                    else:
                        qurey = "select root from exception where word = '%s' " % (data)
                        cursor.execute(qurey)
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
        return set





