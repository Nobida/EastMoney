# -*- coding: utf-8 -*-
from eastMoney.items import EastmoneyItem
from bs4 import BeautifulSoup
import scrapy
import re
import datetime


from ..settings import RANKING_DICT

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
        item['fcode'] = int(response.xpath("//span[@class='fix_fcode']/text()").extract_first())
        item['name'] = response.xpath("//span[@class='fix_fname']/text()").extract_first()
        item['value'] = response.xpath("//dl[@class='dataItem01']//dd[@class='dataNums']/span/text()").extract_first()
        item['annualized_rate_7'] = response.xpath("//dl[@class='dataItem02']//dd[@class='dataNums']/span/text()").extract_first()
        item['annualized_rate_14'] = response.xpath("//dl[@class='dataItem03']//dd[@class='dataNums']/span/text()").extract_first()
        item['annualized_rate_28'] = response.xpath("//dl[@class='dataItem04']//dd[@class='dataNums']/span/text()").extract_first()
        item['starting_amount'] = int(response.xpath("//div[@class='moneyAmount']/input/@data-minsg").extract_first())
        #item['rank'] = response.xpath("//tr//div[@class='Rdata']/text()").extract()[0:4] 
        item['rank_evaluate'] = response.xpath("//tr/td/h3/text()").extract()[0:4] 
        item['score'] = self.rank_computing(item['rank_evaluate'])
        item['record_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')   
        yield item      

    
    #对货币型基金的rank进行打分
    def rank_computing(self,rank_evaluate):
        score = 0
        for rank in rank_evaluate:
            score += RANKING_DICT[rank]
        return score    
            
        

 

        
