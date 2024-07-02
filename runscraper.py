from scrapy.crawler import CrawlerProcess
from Wikipedia_scraper.Wikipedia_scraper.spiders.crowling import WolfSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'FEEDS': {
        'output.json': {
            'format': 'json',
            'encoding': 'utf8',
            'store_empty': False,
            'fields': None,
            'indent': 4,
        },
    },
})
process.crawl(WolfSpider)
process.start()