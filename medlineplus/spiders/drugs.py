import scrapy


class DrugsSpider(scrapy.Spider):
    name = 'drugs'
    allowed_domains = ['medlineplus.gov/druginformation.html']
    start_urls = ['https://medlineplus.gov/druginformation.html']

    def parse(self, response):
        browse = response.xpath(".//ul[@class='alpha-links']//li")
        for link in browse:
            value = link.xpath("./a/@href").get()
            yield response.follow(url=value, callback=self.parse_drugs)

    def parse_drugs(self, response):
        pass
