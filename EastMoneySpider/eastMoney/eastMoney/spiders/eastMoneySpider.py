# -*- coding: utf-8 -*-
from eastMoney.items import EastmoneyItem
from bs4 import BeautifulSoup
import scrapy
import re
import datetime
import time


from ..settings import RANKING_DICT
import statsmodels.api as sm

class eastMoneySpider(scrapy.Spider):
    name = 'eastMoneySpider'
    allowed_domains = ['fund.eastmoney.com']
    start_urls = ['http://fund.eastmoney.com/HBJJ_dwsy.html']


    def start_requests(self):
        url = 'http://fund.eastmoney.com/HBJJ_dwsy.html'
        yield scrapy.Request(url=url, callback=self.parse)


    #从首页抓取货币性基金的list    
    def parse(self, response):
        fund_detail_urls_lst = response.xpath("//td[@class='jc']//a/@href").extract()
        for url in fund_detail_urls_lst:
            yield scrapy.Request(url=url, callback=self.parse_detail)

    #抓去货币性基金的详细内容        
    def parse_detail(self, response):
        item = EastmoneyItem()
        item['fcode'] = self._fill_fcode(response.xpath("//span[@class='fix_fcode']/text()").extract_first())
        item['primary_key'] = item['fcode'] + '_' + str(time.time())[0:8]
        item['name'] = response.xpath("//span[@class='fix_fname']/text()").extract_first()
        item['value'] = response.xpath("//dl[@class='dataItem01']//dd[@class='dataNums']/span/text()").extract_first()
        item['annualized_rate_7'] = response.xpath("//dl[@class='dataItem02']//dd[@class='dataNums']/span/text()").extract_first()
        item['annualized_rate_14'] = response.xpath("//dl[@class='dataItem03']//dd[@class='dataNums']/span/text()").extract_first()
        item['annualized_rate_28'] = response.xpath("//dl[@class='dataItem04']//dd[@class='dataNums']/span/text()").extract_first()
        item['starting_amount'] = str(response.xpath("//div[@class='moneyAmount']/input/@data-minsg").extract_first())
        item['rank'] = self._rank2num(response.xpath("//tr//div[@class='Rdata']/text()").extract()[0:4]) 
        item['rank_evaluate'] = response.xpath("//tr/td/h3/text()").extract()[0:4] 
        item['score'] = self._rank_computing(item['rank_evaluate'])
        item['record_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        item['tendency'] = str(self._tendency_classfication(item['rank']))
        #print(item)
        yield item      

    
    #对货币型基金的rank进行打分
    def _rank_computing(self,rank_evaluate):
        score = 0
        for rank in rank_evaluate:
            score += RANKING_DICT[rank]
        return str(score)    
            
    #补足fcode
    def _fill_fcode(self,fcode):
        if len(fcode) == 6:
            return fcode
        else:
            while len(fcode) != 6:
                fcode = '0' + fcode
            return fcode        
                
    
    def _rank2num(self, rank):
        rank_num_list = []
        pattern = re.compile(r'\d+|\d+')
        for item in rank:
            result = pattern.findall(item)
            num = int(result[0])/int(result[1])
            rank_num_list.append(num)
        return rank_num_list


    def _tendency_classfication(self, rank_lst):
        X = sm.add_constant([0.1,0.2,0.3,0.4])
        y = rank_lst
        est = sm.OLS(y,X)
        est = est.fit()
        return est.params[1]


                               
        

 

        
