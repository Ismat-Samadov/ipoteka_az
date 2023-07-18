import scrapy


class PropertySpider(scrapy.Spider):
    name = "link_extractor"
    allowed_domains = ["ipoteka.az"]
    start_urls = ["https://ipoteka.az/"]

    urls = ["https://ipoteka.az/search?ad_type=0&page=1",  # 18405
            "https://ipoteka.az/search?kompleks=1",  # 8
            "https://ipoteka.az/search?ad_type=0&credit_type=1&only=ads&search_type=1",  # 676
            "https://ipoteka.az/search?premium=1&only=ads",  # 4
            "https://ipoteka.az/search?ad_type=0&credit_type=3&only=ads&search_type=1&page=7"  # 269
            ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        # Extract the href values of the links on the current page
        hrefs = response.xpath('//*[@id="search_page"]/div[2]/div[2]/div[1]/div/a/@href').getall()

        for href in hrefs:
            yield response.follow(url=href, callback=self.parse_property)

        next_page_href = response.xpath('//ul[@class="pagination"]/li/a[@class="next"]/@href').get()

        if next_page_href:
            next_page_url = response.urljoin(next_page_href)
            yield response.follow(url=next_page_url, callback=self.parse_page)

    def parse_property(self, response):
        user_name = response.xpath('//div[@class="user"]/text()').get()
        phone_number = response.xpath('//div[@class="showNumber active"]/text()').get()
        announcement_id = response.xpath(
            '//div[@class="stats"]//div[contains(text(), "Elan İD")]/following-sibling::div[1]/text()').get()
        update_date = response.xpath(
            '//div[@class="stats"]//div[contains(text(), "Yeniləndi")]/following-sibling::div[1]/text()').get()
        baxis_sayi = response.xpath(
            '//div[@class="stats"]//div[contains(text(), "Baxış sayı")]/following-sibling::div[1]/text()').get()
        area = response.xpath(
            '//div[@class="params_block"]//div[@class="rw"]/div[contains(text(), "Ümumi sahə")]/following-sibling::div[1]/text()').get()
        flat = response.xpath(
            '//div[@class="params_block"]//div[@class="rw"]/div[contains(text(), "Mərtəbə")]/following-sibling::div[1]/text()').get()
        room_count = response.xpath(
            '//div[@class="params_block"]//div[@class="rw"]/div[contains(text(), "Otaq sayı")]/following-sibling::div[1]/text()').get()
        document_type = response.xpath(
            '//div[@class="params_block"]//div[@class="rw"]/div[contains(text(), "Sənədin tipi")]/following-sibling::div[1]/text()').get()
        repair_type = response.xpath(
            '//div[@class="params_block"]//div[@class="rw"]/div[contains(text(), "Təmir")]/following-sibling::div[1]/text()').get()

        yield {
            "user_name": user_name,
            "phone_number": phone_number,
            "announcement_id": announcement_id,
            "update_date": update_date,
            "baxis_sayi": baxis_sayi,
            "area": area,
            "flat": flat,
            "room_count": room_count,
            "document_type": document_type,
            "repair_type": repair_type
        }
