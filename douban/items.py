# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #序号
    serial_number = scrapy.Field()
    #电影名称
    movie_name = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    #评价人数
    evaluate = scrapy.Field()
    describe = scrapy.Field()
