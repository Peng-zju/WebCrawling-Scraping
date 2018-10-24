# -*- coding: utf-8 -*-
'''
用scrapy建立爬虫脚本
'''
import scrapy 
import time 
from project_name.items import ProjectItem
from urllib.parse import urljoin
import re
#from zhejiang.money import Money 这个函数可以用来将中文大写数字转化成阿拉伯数字


class project_spider(scrapy.Spider):
    name = 'xxx'
    cur_page = 1
    page_all = 100
    raw_url = 'website'
       
    form_data={'pageID': '18',
			   'pageNum': '4'
			   ...
               }
    
    def start_requests(self):
  
        yield scrapy.FormRequest(self.raw_url, formdata=self.form_data,callback=self.parse)    

       
    def parse (self, response):

		  #网页由表格组成，对表格中每一行进行遍历，存入item,
        rows = response.xpath('//ul/li')  
            
		
        for row in rows:
            
            item = ZhejiangItem()
            item['province'] = u'xxx'
            item['city'] = u'xxx'	
            item['county'] = u'xxx'
            item['open_date'] = row.xpath('./span/text()').extract()[0].strip()
            item['punish_paper'] = row.xpath('./span[1]/@title').extract()[0]          
            half_website = row.xpath("./a/@href").extract()[0]
            item['website'] = urljoin(self.raw_url_main,half_website)
            new_website = item['website']
            time.sleep(2)
			
			#进入需要点击的新的页面,将item作为参数传进去，在yield item之前都算作一行数据
            yield scrapy.Request(new_website, callback = self.parse_item, meta={'item':item})
        
        #翻页    
        if self.cur_page < self.page_all:           
            self.cur_page += 1          
            self.form_data['pageNum'] = str(self.cur_page)
            time.sleep(2)
            yield scrapy.FormRequest(self.raw_url, formdata=self.form_data, callback=self.parse)
                		
    def parse_item (self, response):
        item = response.meta['item']
        
        content = response.xpath('//*[@id="zoomcon"]/div')
        try:
            content1 = content.xpath('string(.)').extract()[0]
		#Money.convertCNToDigit(raw_money)方法转换
        except:
            content1 = '获取失败'
        
        item['content'] = content1

        yield item 	