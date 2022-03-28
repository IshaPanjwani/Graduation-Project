import mysql
from mysql.connector import Error

# engine = create_engine("mysql+pymysql://root:@localhost:3306/stemmer")
#with engine.connect() as conn, conn.begin():
#file.to_sql('lemmatization', conn, if_exists='append')

try:
    conn = mysql.connector.connect(host='localhost', database='stemmer', user='root', password='')
    cursor = conn.cursor()
    qurey = "select verb,headword from lemmatization "
    print(qurey)
    cursor.execute(qurey)
    row = cursor.fetchall()
    for r in row:
        print(r)
        if r[0] is not None:
            query = "update lemmatization set verb = '%s' and headword = '%s' where headword = '%s'" % (
            r[1], r[0], r[1])
            print(query)
            cursor.execute(query)
    conn.commit()


except Error as e:
    print(e)
finally:
    cursor.close()
    conn.close()


