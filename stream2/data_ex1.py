import pymysql
conn = pymysql.connect(host='localhost',user='root',password='root',db='bank')
a = conn.cursor()
sql = " SELECT * from 'customer'"
a.execute(sql)
countrow = a.execute(sql)
print ("number of row",countrow)
data = a.fetchone()
print(data)

