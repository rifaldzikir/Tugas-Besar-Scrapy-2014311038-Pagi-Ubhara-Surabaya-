import scrapy


class QuotesSpider(scrapy.Spider):
    name = "novel4"
    
    def start_requests(self):
        urls = [
                'https://www.worldnovel.online/losing-money-to-be-a-tycoon/chapter-1/',
                'https://www.worldnovel.online/losing-money-to-be-a-tycoon/chapter-2/',
                'https://www.worldnovel.online/losing-money-to-be-a-tycoon/chapter-3/',
                'https://www.worldnovel.online/losing-money-to-be-a-tycoon/chapter-4/',
                'https://www.worldnovel.online/losing-money-to-be-a-tycoon/chapter-5/',
                'https://www.worldnovel.online/losing-money-to-be-a-tycoon/chapter-6/',
                'https://www.worldnovel.online/losing-money-to-be-a-tycoon/chapter-7/',
                'https://www.worldnovel.online/losing-money-to-be-a-tycoon/chapter-8/',
                'https://www.worldnovel.online/losing-money-to-be-a-tycoon/chapter-9/',
                'https://www.worldnovel.online/losing-money-to-be-a-tycoon/chapter-10/'



        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):

        yield {
        'novel4': response.css('#soop > p ::text').extract(),
        
    }