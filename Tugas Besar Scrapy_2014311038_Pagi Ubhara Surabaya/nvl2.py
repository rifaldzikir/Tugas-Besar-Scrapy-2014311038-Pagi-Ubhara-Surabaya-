import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = [
                'https://www.worldnovel.online/the-princess-consort-has-a-lethal-destiny/chapter-1/',
                'https://www.worldnovel.online/the-princess-consort-has-a-lethal-destiny/chapter-2/',
                'https://www.worldnovel.online/the-princess-consort-has-a-lethal-destiny/chapter-3/',
                'https://www.worldnovel.online/the-princess-consort-has-a-lethal-destiny/chapter-4/',
                'https://www.worldnovel.online/the-princess-consort-has-a-lethal-destiny/chapter-5/',
                'https://www.worldnovel.online/the-princess-consort-has-a-lethal-destiny/chapter-6/',
                'https://www.worldnovel.online/the-princess-consort-has-a-lethal-destiny/chapter-7/',
                'https://www.worldnovel.online/the-princess-consort-has-a-lethal-destiny/chapter-8/',
                'https://www.worldnovel.online/the-princess-consort-has-a-lethal-destiny/chapter-9/',
                'https://www.worldnovel.online/the-princess-consort-has-a-lethal-destiny/chapter-10/'


        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):

        yield {
        'novel2': response.css('#soop > p ::text').extract(),
        
    }