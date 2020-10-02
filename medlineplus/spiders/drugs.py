import scrapy


class DrugsSpider(scrapy.Spider):
    name = 'drugs'
    allowed_domains = ['medlineplus.gov/druginformation.html']
    start_urls = ['http://medlineplus.gov/druginformation.html/']

    def parse(self, response):
        pass
