import scrapy


class MedicaltestsSpider(scrapy.Spider):
    name = 'medicaltests'
    allowed_domains = ['medlineplus.gov/lab-tests']
    start_urls = ['http://medlineplus.gov/lab-tests/']

    def parse(self, response):
        pass
