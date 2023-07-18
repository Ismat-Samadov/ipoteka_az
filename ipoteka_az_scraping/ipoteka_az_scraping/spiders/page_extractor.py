import scrapy


class PageExtractorSpider(scrapy.Spider):
    name = "page_extractor"
    allowed_domains = ["ipoteka.az"]
    start_urls = ["https://ipoteka.az/search?ad_type=0&credit_type=1&only=ads&search_type=1"]

    def parse(self, response):
        # Extract the href values of the links on the current page
        hrefs = response.xpath('//*[@id="search_page"]/div[2]/div[2]/div[1]/div/a/@href').getall()
        # Process the href values for further scraping operations
        for href in hrefs:
            # Perform your scraping operations using the extracted href values
            yield {
                'href': href
            }
        next_page_hrefs = response.xpath('//ul[@class="pagination"]/li/a[contains(@href, "page=")]/@href').getall()
        # If "Next" page links are found, follow each link and continue parsing
        for next_page_href in next_page_hrefs:
            next_page_url = response.urljoin(next_page_href)
            yield scrapy.Request(next_page_url, callback=self.parse)
