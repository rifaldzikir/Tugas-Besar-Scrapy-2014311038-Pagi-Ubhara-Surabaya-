import scrapy


class QuotesSpider(scrapy.Spider):
    name = "novel5"
    
    def start_requests(self):
        urls = [
               'https://www.worldnovel.online/novel-legendary-armament-canon/chapter-1/',
               'https://www.worldnovel.online/novel-legendary-armament-canon/chapter-2/',
               'https://www.worldnovel.online/novel-legendary-armament-canon/chapter-3/',
               'https://www.worldnovel.online/novel-legendary-armament-canon/chapter-4/',
               'https://www.worldnovel.online/novel-legendary-armament-canon/chapter-5/',
               'https://www.worldnovel.online/novel-legendary-armament-canon/chapter-6/',
               'https://www.worldnovel.online/novel-legendary-armament-canon/chapter-7/',
               'https://www.worldnovel.online/novel-legendary-armament-canon/chapter-8/',
               'https://www.worldnovel.online/novel-legendary-armament-canon/chapter-9/',
               'https://www.worldnovel.online/novel-legendary-armament-canon/chapter-10/',


        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):

        yield {
        'novel5': response.css('#soop > p ::text').extract(),
        
    }