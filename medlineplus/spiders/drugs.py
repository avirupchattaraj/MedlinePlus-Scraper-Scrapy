import scrapy


class DrugsSpider(scrapy.Spider):
    name = 'drugs'
    allowed_domains = ['medlineplus.gov']
    start_urls = ['https://medlineplus.gov/druginformation.html']

    def parse(self, response):
        browse = response.xpath("//ul[@class='alpha-links']//li")
        for link in browse:
            value = link.xpath("./a/@href").get()
            yield response.follow(url=value, callback=self.parse_drugs)

    def parse_drugs(self, response):
        drugs = response.xpath("//ul[@id='index']//li")
        for drug in drugs:
            name = drug.xpath("./span/text()").get()
            drug_link = drug.xpath("./a/@href").get()
            yield response.follow(url=drug_link, callback=self.drug_info)

    def drug_info(self, response):
        pass
