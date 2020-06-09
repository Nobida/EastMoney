# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class EastmoneyPipeline(object):


    def __init__(self):
        self.client = pymysql.connect(
            host='59.110.243.182',
            port=3306,
            user='root',  #使用自己的用户名
            passwd='qzwkx333530',  # 使用自己的密码
            db='restframework',  # 数据库名
            charset='utf8'
        )
        self.db_cur = self.client.cursor()

    def process_item(self,item,spider):
        insert_sql = '''
                      INSERT INTO MoneyFund(`fcode`,`name`,`value`,`annualized_rate_7`,`annualized_rate_14`,
                      `annualized_rate_28`,`starting_amount`,`record_time`,`score`) VALUES ('%d','%s','%s','%s','%s','%s','%d','%s','%d')
                     '''%(item['fcode'],item['name'],item['value'],
                        item['annualized_rate_7'],item['annualized_rate_14'],item['annualized_rate_28'],
                        item['starting_amount'],item['record_time'],item['score'])
        #print(insert_sql)
        try:
            self.db_cur.execute(insert_sql)
            self.client.commit()
            print("获取%d最新信息成功"%(item['fcode']))
        except Exception as e:
            print(e)



