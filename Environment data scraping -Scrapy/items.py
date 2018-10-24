# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ProjectItem(Item):
    punish_paper = Field()      
    name = Field()              
    behavior = Field()          
    law = Field()               
    punish_ground = Field()     
    punish_measure = Field()    
    money = Field()             
    punish_date = Field()      
    province = Field()          
    city = Field()              
    county = Field()            
    punisher = Field()          
    website = Field()           
    content = Field()           
    open_date = Field()         
    is_full_paper = Field()       
    num_org = Field()           
    num_zhizhao = Field()       
    num_xinyong = Field()      
    content = Field()
    behavior22 = Field()


