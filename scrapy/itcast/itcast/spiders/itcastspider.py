# -*- coding: utf-8 -*-
import scrapy
from itcast.items import ItcastItem


class ItcastspiderSpider(scrapy.Spider):
    """
        :param 默认生成的爬虫类，继承于scrapy.Spider
    """
    name = 'itcastspider'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#a']

    def parse(self, response):
        """
            response 就是请求之后返回的源码
        """
        items = []
        # 在srapy中可以直接用xpah对返回文件处理，不需要etree
        node_list = response.xpath('//div[@class="li_txt"]')
        for each in node_list:
            # 实例化一个item对象，用于给管道文件处理 item可以看成是一个字典类型
            item = ItcastItem()
            # each.xpath('.//h3/text()')返回的是xpath匹配对象
            # obj.extract() 把对象按照Unicode编码
            item['teach_name'] = each.xpath('.//h3/text()').extract()[0]
            item['teach_title'] = each.xpath('.//h4/text()').extract()[0]
            item['teach_info'] = each.xpath('.//p/text()').extract()[0]
            items.append(item)
        
        with open('teach.csv', 'w', encoding='gbk') as f:
            f.write(str(items))

