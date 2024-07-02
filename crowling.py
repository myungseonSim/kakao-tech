import scrapy
import json

class WolfSpider(scrapy.Spider):
    name = "Wolf"
    start_urls = ["https://ko.wikipedia.org/wiki/늑대"]
    
    def parse(self, response):
        title = response.css('mw-page-title-main')
        yield{
            'title' : title,
        }
        
class WolfPipeline:
    def open_spider(self, spider):
        self.file = open('Wolf_data.json','w',encoding='UTF-8')
        
    def close_spider(self, spider):
        self.file.close()
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
    
    
settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'ITEM_PIPELINES': {
        '__main__.WolfPipeline': 300,
    }
}
    
if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess(settings)
    process.crawl(WolfSpider)
    process.start()