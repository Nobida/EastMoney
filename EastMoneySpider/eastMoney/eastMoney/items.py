# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class EastmoneyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    primary_key = Field()
    fcode = Field()
    name = Field()
    value = Field()
    annualized_rate_7 = Field()
    annualized_rate_14 = Field()
    annualized_rate_28 = Field()
    starting_amount = Field()
    rank = Field()
    rank_evaluate = Field()
    record_time = Field()
    score = Field()
    tendency = Field()

