import scrapy
import json

class KaggleSpider(scrapy.Spider):
    name = "kaggle"
    start_urls = [
        'https://www.kaggle.com/datasets/jguerreiro/running',
    ]

    def parse(self, response):
        # 메타 태그에서 제목과 설명 추출
        title = response.css('meta[property="og:title"]::attr(content)').get(default='No title found')
        description = response.css('meta[property="og:description"]::attr(content)').get(default='No description found')
        
        yield {
            'title': title,
            'description': description,
        }

class KaggleCrawlerPipeline:
    def open_spider(self, spider):
        self.file = open('running_data.json', 'w', encoding='utf-8')
        self.file.write('[')

    def close_spider(self, spider):
        self.file.seek(self.file.tell() - 2, 0)
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

# Scrapy 설정
# USER_AGENT: 웹사이트들은 스크래핑 요청을 차단하거나 제한함, USER_AGENT를 설정하여 스크래핑 요청을 실제 브라우저에서 오는 요청처럼 보이게함
# ITEM_PIPELINES: 이는 데이터 처리 파이프라인을 지정함, 파이프라인은 크롤링된 데이터를 JSON 파일로 저장하는 역할함. 이 설정이 없으면, 데이터가 파이프라인을 거쳐 파일로 저장되지 않습니다.
settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'ITEM_PIPELINES': {
        '__main__.KaggleCrawlerPipeline': 300,
    }
}

# 크롤러 실행
if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess(settings)
    process.crawl(KaggleSpider)
    process.start()