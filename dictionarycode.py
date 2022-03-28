import mysql
from mysql.connector import Error

def findRoot():
    set = []
    try:
        conn = mysql.connector.connect(host='localhost', database='stemmer', user='root', password='')
        cursor = conn.cursor()

        qurey = "select root from verb"
        cursor.execute(qurey)
        row = cursor.fetchall()
        if (row):
            for i in row:
                for j in i:
                    set.append(j)
    except Error as e:
            print(e)
    finally:
        cursor.close()
        conn.close()
    return set

list = findRoot();
print(list)

dic = open("eng-dictionary-verb.txt",'w')
dic.write("\n".join(list))
dic.flush();