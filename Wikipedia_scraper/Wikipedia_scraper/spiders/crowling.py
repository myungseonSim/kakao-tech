import scrapy
import json

class WolfSpider(scrapy.Spider):
    name = "Wolf"
    start_urls = ["https://ko.wikipedia.org/wiki/늑대"]
    
    def parse(self, response):
        title = response.css('#content > firstHeading > span.mw-page-title-main').get()
        description = response.css('#mw-content-text > div.mw-content-ltr.mw-parser-output').get()
        yield{
            'title' : title,
            'description' : description,
        }
        
