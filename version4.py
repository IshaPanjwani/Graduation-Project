import mysql
from mysql.connector import Error


def rreplace(data, old, new):
    li = data.rsplit(old, 1)
    return new.join(li)


list = input("please enter the String:   ").split(" ")
conn = mysql.connector.connect(host='localhost', database='stemmer', user='root', password='')
cursor = conn.cursor()

for j in range(len(list)):
    data = list[j]
    i = 2
    while (i < len(data)):
        query = "select ending from endings WHERE ending = '%s'" % data[i:]
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            data = rreplace(data, data[i:], "")
            i = 1
        i = i + 1
    list[j] = data

print(' '.join(list))