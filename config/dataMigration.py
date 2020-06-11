# -*- coding: utf-8 -*-

import pymysql

ORIGIN_DBNAME = 'MoneyFund'
DESTINATION_DBNAME = 'Monetary_monetary'

def conne2db():
    client = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',  #使用自己的用户名
        passwd='qzwkx333530',  # 使用自己的密码
        db='restframework',  # 数据库名
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )
    cursor = client.cursor()
    return client, cursor


def update_db(client,cursor):
    search_query = 'SELECT * FROM %s WHERE to_days(record_time) = to_days(now())'%(ORIGIN_DBNAME) 
    cursor.execute(search_query)
    datas = cursor.fetchall()
    for item in datas:
        values = (
            item['primary_key'], 
            item['fcode'], 
            item['name'], 
            item['value'], 
            item['score'],
            item['record_time'],
            item['tendency']
        )
        insert_query = "INSERT INTO Monetary_monetary VALUES (%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(insert_query, values)
            client.commit()
        except Exception as e:
            print(e)    


    

if __name__ == "__main__":
    client,cursor = conne2db()
    update_db(client,cursor)

