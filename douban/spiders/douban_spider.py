# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    #爬虫名字
    name = 'douban_spider'
    #允许到域名
    allowed_domains = ['movie.douban.com']
    #入口url，人到调度器里面
    start_urls = ['https://movie.douban.com/top250']

    #解析器
    def parse(self, response):
        movie_list = response.xpath("//*[@id='content']/div/div[1]/ol/li")
        for i_item in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_number'] = i_item.xpath("./div/div[1]/em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath("./div/div[2]/div[1]/a/span[1]/text()").extract_first()
            # douban_item['introduce'] = i_item.xpath("./div/div[2]/div[2]/p[1]/text()").extract_first()
            content = i_item.xpath("./div/div[2]/div[2]/p[1]/text()").extract_first()
            content_s = ""
            for i_content in content:
                content_s = content_s + "".join(i_content.split())
            douban_item['introduce'] = content_s
            douban_item['star'] = i_item.xpath("./div/div[2]/div[2]/div/span[2]/text()").extract_first()
            #评价
            douban_item['evaluate'] = i_item.xpath("./div/div[2]/div[2]/div/span[4]/text()").extract_first()
            douban_item['describe'] = i_item.xpath("./div/div[2]/div[2]/p[2]/span/text()").extract_first()
            # print(douban_item)
            # 将数据yield到pipelines里面，进行数据清洗、存储
            yield douban_item
        print("-------------------------")
        #解析下一页xpath
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        # 判断是否存在下一页连接，到未页就没有了
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback= self.parse)


