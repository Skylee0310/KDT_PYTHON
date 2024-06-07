import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='root',
                      password='5387',
                      db = 'sakila', charset='utf8')
cur = conn.cursor() #cursor 객체 생성
cur.execute('select * from language')
rows = cur.fetchall() #모든 데이터를 가져옴

print(rows)
language_df = pd.DataFrame(rows) #DataFrame 형태로 변환
print(language_df)

cur.close()
conn.close() #데이터베이스 연결 종료.
