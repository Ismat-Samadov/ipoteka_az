import scrapy


class LinkExtractorSpider(scrapy.Spider):
    name = "link_extractor"
    allowed_domains = ["ipoteka.az"]
    start_urls = ["https://ipoteka.az/"]

    def parse(self, response):
        href = response.xpath('//div[@class="link"]/a[contains(text(), "Hamısını göstər")]/@href').getall()
        yield {
            "href" : href
        }