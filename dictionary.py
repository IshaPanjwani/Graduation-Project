import mysql
from mysql.connector import Error
import pandas as pd


df = pd.read_excel('dictionary/Regular and irregular verbs _ Oxford Dictionaries.xlsx')
print(df)

try:
    conn = mysql.connector.connect(host='localhost', database='stemmer', user='root', password='')
    cursor = conn.cursor()
    for r in df.values:
        r[0] = r[0].replace('to\xa0', '')
        r[1] = r[1].replace('(s)', '')
        select = "select root from dictionary where root='%s'" % (r[0])
        print(select)
        cursor.execute(select)
        row = cursor.fetchall()
        print(row)
        if row == []:
            query = "insert into dictionary(root,present,past,past_participle,continues) VALUES ('%s','%s','%s','%s','%s')" % (
            r[0], r[1], r[2], r[3], r[4])
            print(query)
            cursor.execute(query)
    conn.commit()



except Error as e:
    print(e)
finally:
    cursor.close()
    conn.close()








