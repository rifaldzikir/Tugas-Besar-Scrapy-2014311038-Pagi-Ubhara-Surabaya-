import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/the-earth-is-my-dantian/chapter-1-young-master-twelve-ye-sheng/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):

        yield {
        'ch': response.css('#soop > p:nth-child(4)::text').extract()
    }